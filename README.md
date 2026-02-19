# 🧠 Enterprise Knowledge Assistant using RAG

A Retrieval-Augmented Generation (RAG) based AI system that retrieves enterprise documents and generates highly accurate, context-grounded answers using Large Language Models (LLMs).

---

🔗 **Live Demo (MVP):**  
 https://2403717624321014-sudo.github.io/RAG-SYSTEMS/

---

## 🎯 Objectives

🎯 Improve contextual accuracy in AI responses  
🛡 Reduce hallucinations using document-grounded retrieval  
💸 Avoid expensive model fine-tuning  
🌍 Enable multi-domain question answering  
📊 Provide confidence-aware responses  
🏢 Demonstrate enterprise-grade AI solutions  

---

## 🏗 System Architecture

📂 Load enterprise documents  
✂️ Split documents into text chunks  
📐 Convert text into TF-IDF vectors  
❓ Accept user query  
📏 Compute cosine similarity  
🏆 Retrieve Top-K relevant chunks  
🎯 Apply confidence threshold  
🧠 Inject context into LLM  
🤖 Generate grounded response  

---

## 📂 Use Cases Implemented

### 🧑‍💼 Internal Employee Knowledge Base
📜 Company policies  
🏡 Remote work rules  
🏖 Leave policy  
💻 IT support  
📘 Code of conduct  

### 🎫 Customer Support Ticket Autocomplete
📂 Past support tickets  
🛠 Issue resolution  
⏱ SLA handling  

### ⚖ Legal & Compliance Document Audit
📑 Contracts  
🛡 Compliance clauses  
❌ Termination terms  
🔐 Data protection policies  

### 🌍 General Knowledge Retrieval
🏛 Landmarks  
🗿 Monuments  
🏗 Engineering achievements  
📍 Ondiputhur dataset  

### 📚 Technical Documentation Support
🔐 Authentication flows  
📡 API documentation  
🛡 Security guidelines  

---

## 🛠 Technologies Used

🐍 Python  
🧮 Scikit-learn  
📐 TF-IDF Vectorizer  
📏 Cosine Similarity  
🔢 NumPy  
🌐 Flask  
🦙 Ollama  
🤖 LLM Model: Llama3  

---

## 🖥️ Demo

Open terminal in project folder:

```bash
pip install -r requirements.txt
ollama run llama3
cd Compliance_Audit
python app.py
