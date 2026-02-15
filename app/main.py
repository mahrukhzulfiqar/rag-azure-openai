from fastapi import FastAPI
from app.services.azure_openai_service import AzureOpenAIService
from app.services.vector_store import InMemoryVectorStore
from app.models.rag_models import RagChatRequest
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
def rag_chat(request: RagChatRequest):
    relevant_docs = vector_store.search(request.message, top_k=request.top_k)

    context = "\n".join([doc[0] for doc in relevant_docs])

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
