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
