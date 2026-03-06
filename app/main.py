from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.azure_openai_service import AzureOpenAIService
from app.services.vector_store import VectorStore
from app.models.rag_models import RagChatRequest

app = FastAPI()

# CORS (for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
azure_service = AzureOpenAIService()
vector_store = VectorStore()


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
    """
    Add a document to the vector store.
    """
    vector_store.add_document(text)
    return {"message": "Document added successfully"}


@app.post("/rag-chat")
def rag_chat(request: RagChatRequest):
    """
    RAG endpoint:
    1. Search relevant documents
    2. Inject context into prompt
    3. Send enhanced prompt to Azure OpenAI
    """
    relevant_docs = vector_store.search(request.message, top_k=request.top_k)

    # relevant_docs should now be a list of strings
    context = "\n".join(relevant_docs)

    enhanced_prompt = f"""
You are a helpful assistant.

Use the context below to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{request.message}
"""

    response = azure_service.chat(enhanced_prompt)

    return {"context_used": relevant_docs, "response": response}
