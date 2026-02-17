🧠 Enterprise Knowledge Assistant using RAG
📌 Project Overview

This project implements an Enterprise Knowledge Assistant using Retrieval-Augmented Generation (RAG).
The system retrieves relevant information from structured text documents and generates context-grounded answers using a Large Language Model (LLM).

Instead of relying only on the LLM’s internal knowledge, the system injects retrieved document context before generating responses, significantly reducing hallucinations and improving answer reliability.

🎯 Objectives

The primary objectives of this project are to:

Improve contextual accuracy in AI-generated responses

Reduce hallucinations using document-grounded retrieval

Avoid expensive model fine-tuning

Enable multi-domain question answering

Provide confidence-aware responses

Demonstrate multiple real-world RAG use cases

🏗 System Architecture

The system follows a standard RAG pipeline:

Load domain-specific text documents

Split documents into manageable text chunks

Convert chunks into vectors using TF-IDF

Accept a user query

Compute cosine similarity between query and document vectors

Retrieve Top-K relevant chunks

Apply a confidence threshold

Inject retrieved context into the LLM

Generate a grounded response

Display answer with confidence awareness

📂 Use Cases Implemented
1️⃣ Internal Employee Knowledge Base (RAG)

Policies, remote work rules, leave policy, IT support, code of conduct

2️⃣ Customer Support Ticket Autocomplete (RAG)

Past support tickets, issue resolution, SLA handling

3️⃣ Legal & Compliance Document Audit (RAG)

Contracts, compliance clauses, termination terms, data protection

4️⃣ General Knowledge Retrieval (RAG)

Landmarks, monuments, engineering achievements (Ondiputhur dataset)

5️⃣ Technical Documentation Support (RAG)

API documentation, authentication flows, security guidelines

🛠 Technologies Used

Python

Scikit-learn

TF-IDF Vectorizer

Cosine Similarity

NumPy

Flask (for web interface)

Ollama

LLM Model: Llama3

Retrieval-Augmented Generation (RAG)

📁 Project Structure
RAG_Use_Cases/
│
├── Emp_Knowledge/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── employee_data.txt
│   ├── README.txt
│   └── requirements.txt
│
├── Ticket_Autocomplete/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── Customer_Ticket_Data.txt
│   ├── README.txt
│   └── requirements.txt
│
├── Compliance_Audit/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── legal.txt
│   ├── README.txt
│   └── requirements.txt
│
├── rag_phi3_textfile_project/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── ondiputhur.txt
│   ├── README.txt
│   └── requirements.txt
│
├── Docs_Assist/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── Tech_data.txt
│   ├── README.txt
│   └── requirements.txt
│
├── Working_Screens/
│   ├── 01_Employee_KB/
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── 3.png
│   │
│   ├── 02_Ticket_RAG/
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── 3.png
│   │
│   ├── 03_Legal_Audit/
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── 3.png
│   │
│   ├── 04_Ondiputhur_RAG/
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── 3.png
│   │
│   └── 05_Tech_Docs/
│       ├── 1.png
│       ├── 2.png
│       └── 3.png
│
├── .gitignore
└── README.md


▶ How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Ensure Ollama is Running
ollama run llama3

3️⃣ Run Any Use Case

Navigate to the required use case folder:

cd Compliance_Audit
python app.py


Open your browser and visit:

http://localhost:5000


Repeat the same steps for other use cases.

🔍 Key Features

Domain-specific document retrieval

Top-K chunk retrieval (K = 3)

Confidence-aware answer generation

Context-grounded LLM responses

Reduced hallucination

Modular architecture (one app per use case)

Screenshot-based result validation

🔢 Confidence Handling

The system evaluates the similarity score of retrieved chunks:

If similarity ≥ threshold → Answer is generated

If similarity < threshold → System avoids unreliable output

This ensures safe and trustworthy responses.

🚀 Future Enhancements

Replace TF-IDF with semantic embeddings

Integrate FAISS for scalable vector storage

Add PDF and DOCX ingestion

Implement conversational memory

Deploy as a unified web application

Add citation highlighting in responses

📌 Conclusion

This project demonstrates how Retrieval-Augmented Generation (RAG) can transform a general-purpose LLM into a reliable, enterprise-ready knowledge assistant.
By grounding responses in authorized documents, the system delivers accurate, explainable, and domain-specific answers, making it ideal for real-world enterprise applications.
