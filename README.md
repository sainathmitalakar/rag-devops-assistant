# DevOps RAG Assistant

A **Retrieval-Augmented Generation (RAG) Assistant** for DevOps that answers questions based on your PDF documentation.  

Powered by **FLAN-T5-small**, **SentenceTransformers**, and **FAISS**, it can run **locally** or use **AWS S3** for cloud storage of embeddings.  

Think of it as a **mini ChatGPT for DevOps**, delivering **long, detailed, professional answers**.

---

## 🔹 Why This Project?

- DevOps knowledge is vast and scattered across multiple PDFs and handbooks.  
- RAG allows **contextual retrieval**: your question triggers relevant sections from PDFs, then an LLM generates a **comprehensive answer**.  
- Using **FLAN-T5-small** ensures **CPU/GPU compatibility** and faster inference.  
- Optional **AWS S3 integration** allows **cloud storage** of embeddings for easy reuse and sharing.

---

## 🔹 Prerequisites

- **Python 3.11+**  
- **pip** package manager  
- **AWS account** (optional, for S3)  
- Basic knowledge of **Git**  

---

## 🔹 Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sainathmitalakar/rag-devops-assistant.git
cd rag-devops-assistant 

2. Create and Activate Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

Dependencies include:

transformers – FLAN-T5-small

sentence-transformers – PDF embeddings

faiss – fast similarity search

PyPDF2 – extract text from PDFs

boto3 – AWS S3 integration

🔹 Add Your PDFs

Place your DevOps PDFs in the docs/ folder:

docs/
├─ AWS_DevOps_Handbook__Commands__Best_Practices__and_Real_Time_Scenarios.pdf
├─ Docker_Handbook_2025.pdf
├─ Jenkins_Handbook.pdf
├─ Kubernetes_Handbook__DevOps_.pdf
├─ Git_Ninja_Handbook.pdf

These PDFs are the source knowledge base for the assistant.

🔹 Generate Embeddings

Generate embeddings for each PDF chunk:

python tools/generate_embeddings_offline.py


✅ Example output:

Loading embedding model...
✅ Generated embedding for chunk 1/587
✅ Generated embedding for chunk 2/587
...
✅ All embeddings saved to embeddings.json


Why: Embeddings allow fast retrieval of relevant chunks for answering your questions.

🔹 FAISS Index

Built automatically when you run rag_query.py.

Stores embeddings for fast similarity search.

Example output:

✅ FAISS index built with 587 vectors

🔹 AWS S3 Integration (Optional)

Purpose: Store embeddings.json in S3 for cloud backup and multi-device access.

Create a .env file with your credentials:

AWS_ACCESS_KEY_ID=YOUR_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET
AWS_BUCKET_NAME=YOUR_BUCKET


Upload embeddings:

python tools/upload_to_s3.py


Verify file exists:

python tools/check_s3.py


✅ Output:

✅ embeddings.json found on S3

🔹 Run the Assistant
python tools/rag_query.py


You will see:

Loading embedding model...
Using device: cpu
Ask your DevOps question (or type 'exit'):


Type questions like:

"What is DevOps and its main principles?"
"Explain Jenkins pipelines step by step."
"How to deploy Docker containers in Kubernetes?"


The assistant will give long, detailed answers. Type exit to quit.

FLAN-T5 Settings for Detailed Answers
outputs = model.generate(
    **inputs,
    max_new_tokens=800,    # maximum answer length
    temperature=0.7,       # creativity control
    do_sample=True,        # sampling instead of greedy
    top_p=0.9              # nucleus sampling
)

🔹 File Structure
rag-devops-assistant/
│
├─ docs/                       # PDF knowledge base
├─ tools/
│  ├─ rag_query.py             # Query interface
│  ├─ generate_embeddings_offline.py
│  ├─ load_documents.py
│  ├─ retriever.py
│  ├─ upload_to_s3.py
│  └─ check_s3.py
├─ embeddings.json              # Generated embeddings (local/S3)
├─ .env                        # AWS credentials (never commit)
├─ README.md
└─ requirements.txt

🔹 Python Version

Python 3.11+ recommended

Compatible with Windows/Linux/macOS

Ensures transformers, faiss, and sentence-transformers work smoothly

🔹 Tech Stack

Python – Main language

Transformers – FLAN-T5-small model

SentenceTransformers – PDF embeddings

FAISS – Fast vector search

PyPDF2 – PDF text extraction

AWS S3 – Cloud storage for embeddings 

<img width="943" height="539" alt="image" src="https://github.com/user-attachments/assets/433eb0a0-5b4f-482a-882c-5302fd0dbab6" />

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/9be02e1d-b59f-4cd3-b775-4d95c5a55bab" />

<img width="950" height="540" alt="image" src="https://github.com/user-attachments/assets/62868918-a8df-4feb-b4c6-56433ca6f2ff" />

