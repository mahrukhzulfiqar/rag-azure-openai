from fastapi import FastAPI
from app.services.azure_openai_service import AzureOpenAIService
from app.services.vector_store import InMemoryVectorStore


app = FastAPI()
vector_store = InMemoryVectorStore()

# Initialize service
azure_service = AzureOpenAIService()


@app.get("/")
def read_root():
    return {"message": "RAG Azure OpenAI is running 🚀"}


@app.post("/chat")
def chat_with_model(message: str):
    """
    Simple chat endpoint that sends a message
    to Azure OpenAI and returns the response.
    """
    response = azure_service.chat(message)
    return {"response": response}


@app.post("/embed")
def embed_text(text: str):
    embedding = azure_service.embed(text)
    return {"vector_length": len(embedding)}


@app.post("/documents")
def add_document(text: str):
    vector_store.add_document(text)
    return {"message": "Document added successfully"}


@app.post("/rag-chat")
def rag_chat(message: str):
    # 1️⃣ Search relevant documents
    relevant_docs = vector_store.search(message)

    # 2️⃣ Combine context
    context = "\n".join([doc["text"] for doc in relevant_docs])

    # 3️⃣ Build enhanced prompt
    enhanced_prompt = f"""
You are a helpful assistant.

Use the context below to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{message}
"""

    # 4️⃣ Ask Azure OpenAI
    response = azure_service.chat(enhanced_prompt)

    return {"context_used": relevant_docs, "response": response}
