from dataclasses import dataclass
from typing import List
import numpy as np
import ollama
from flask import Flask, render_template, request, jsonify
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class Document:
    id: str
    text: str
    index: int
    source: str = ""


def load_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    chunks = [c.strip() for c in content.split("\n\n") if len(c.strip()) > 30]

    docs = []
    for i, chunk in enumerate(chunks):
        docs.append(Document(
            id=f"text_chunk_{i}",
            text=chunk,
            index=i,
            source=os.path.basename(filepath)
        ))

    return docs


class SimpleTfidfRAG:
    def __init__(self, docs: List[Document]):
        self.docs = docs
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2)
        )
        self.doc_matrix = self.vectorizer.fit_transform([d.text for d in docs])

    def retrieve(self, query, top_k=3, expand_neighbors=True):
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.doc_matrix).flatten()

        top_indices = np.argsort(sims)[::-1][:top_k]

        selected_indices = set()

        for idx in top_indices:
            if sims[idx] > 0:
                selected_indices.add(idx)

                if expand_neighbors:
                    if idx - 1 >= 0:
                        selected_indices.add(idx - 1)

                    if idx + 1 < len(self.docs):
                        selected_indices.add(idx + 1)

        ordered_indices = sorted(selected_indices)

        return [(self.docs[i], float(sims[i])) for i in ordered_indices]


def ask_ollama(model_name, query, context):
    prompt = f"""
You are a technical documentation assistant.

Strictly answer using the provided context.
If the context does not contain enough information, clearly say:
"The documentation does not specify this."

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.generate(
        model=model_name,
        prompt=prompt,
        stream=False
    )

    return response["response"]


app = Flask(__name__, template_folder='templates')

rag_system = None
model_name = "phi3"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/search', methods=['POST'])
def api_search():
    try:
        data = request.json
        query = data.get('query', '').strip()

        if not query:
            return jsonify({'error': 'Query cannot be empty'}), 400

        results = rag_system.retrieve(query, top_k=3, expand_neighbors=True)

        if not results:
            return jsonify({
                'answer': 'No matching content found in the documentation.',
                'sources': []
            })

        context = "\n\n".join([doc.text for doc, _ in results])

        final_answer = ask_ollama(model_name, query, context)

        sources = [
            {
                'chunk_id': doc.id,
                'score': round(score, 4),
                'text': doc.text
            }
            for doc, score in results
        ]

        return jsonify({
            'answer': final_answer,
            'sources': sources
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def main():
    global rag_system

    docs = load_text_file("Tech_data.txt")

    rag_system = SimpleTfidfRAG(docs)

    app.run(debug=False, host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()