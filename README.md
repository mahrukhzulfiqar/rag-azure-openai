# 🤖 BOT ChatBot — Retrieval Augmented Generation with Azure OpenAI

A full-stack AI chatbot built using:

- ⚡ FastAPI (Python backend)
- 🧠 Azure OpenAI (GPT-4o-mini + Embeddings)
- 🔎 Retrieval Augmented Generation (RAG)
- 💬 React + Vite frontend
- 📦 In-memory vector store

This project demonstrates how to build a complete RAG pipeline using Azure OpenAI and modern full-stack architecture.

---

## 🚀 Features

- Chat with Azure OpenAI
- Generate embeddings using Azure
- Store documents in a vector store
- Semantic similarity search
- Context-aware RAG responses
- Clean FastAPI backend
- Modern React chatbot UI
- Environment-based configuration
- Swagger API documentation

---

## 🧠 What is RAG?

**Retrieval Augmented Generation (RAG)** improves LLM responses by grounding them in external data.

Instead of relying only on the model’s internal knowledge:

1. Documents are converted into embeddings
2. Stored in a vector store
3. Relevant chunks are retrieved based on similarity
4. Context is injected into the LLM prompt
5. The model generates a grounded response

This reduces hallucinations and makes responses more reliable.

---

## 🏗️ Project Structure

```
rag-azure-openai-1/
│
├── app/
│   ├── main.py
│   ├── config.py
│   └── services/
│       ├── azure_openai_service.py
│       └── vector_store.py
│
├── frontend/
│   └── React (Vite)
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Backend Setup (FastAPI)

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env` File

Create a `.env` file in the root directory:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_KEY=your_azure_key_here
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4o-mini
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
```

### 4️⃣ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🖥️ Frontend Setup (React + Vite)

### 1️⃣ Navigate to Frontend

```bash
cd frontend
```

### 2️⃣ Install Node 22 (Recommended)

If using `nvm`:

```bash
nvm install 22
nvm use 22
```

### 3️⃣ Install Dependencies

```bash
npm install
```

### 4️⃣ Run Dev Server

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 📡 API Endpoints

### ➤ Add Document

```
POST /documents
```

Query parameter:

```
text=Your document text here
```

---

### ➤ Basic Chat (No RAG)

```
POST /chat
```

Query parameter:

```
message=Hello
```

---

### ➤ RAG Chat

```
POST /rag-chat
```

Request Body:

```json
{
  "message": "What is RAG?",
  "top_k": 3
}
```

---

## 🔎 RAG Flow

1. User uploads a document
2. Document → embedding
3. Stored in vector store
4. User asks a question
5. Question → embedding
6. Similar documents retrieved
7. Context injected into prompt
8. GPT generates grounded answer

---

## 🧩 Technologies Used

### Backend

- FastAPI
- Pydantic
- Azure OpenAI SDK
- Uvicorn

### Frontend

- React
- Vite
- Modern CSS

### AI Services

- Azure OpenAI
- GPT-4o-mini
- text-embedding-3-small

---

## 📌 Why This Project Matters

This project demonstrates:

- Real-world LLM integration
- Azure OpenAI deployment usage
- Embeddings + semantic search
- Prompt engineering
- Full-stack AI architecture
- REST API design
- Modern frontend integration

This is a structured RAG implementation, not just a basic chatbot.

---

## 🔮 Future Improvements

- Persistent vector database (FAISS / Pinecone / Azure AI Search)
- Streaming responses
- Conversation memory
- Document chunking
- Source citations in answers
- Dockerization
- Azure App Service deployment
- Authentication system

---

## 🧪 Example

Upload document:

```
RAG means Retrieval Augmented Generation.
```

Ask:

```
What is RAG?
```

Model responds using the stored context.

---

## ⭐ If You Like This Project

Give it a star on GitHub!
