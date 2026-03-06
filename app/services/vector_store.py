import chromadb
from chromadb.config import Settings
from app.services.azure_openai_service import AzureOpenAIService


class VectorStore:
    def __init__(self):
        self.azure_service = AzureOpenAIService()

        # Persistent DB folder
        self.client = chromadb.Client(
            Settings(persist_directory="./chroma_db", is_persistent=True)
        )

        self.collection = self.client.get_or_create_collection(name="rag_collection")

    def add_document(self, text: str):
        embedding = self.azure_service.embed(text)

        self.collection.add(
            documents=[text], embeddings=[embedding], ids=[str(hash(text))]
        )

    def search(self, query: str, top_k: int = 3):
        query_embedding = self.azure_service.embed(query)

        results = self.collection.query(
            query_embeddings=[query_embedding], n_results=top_k
        )

        documents = results["documents"][0]

        return documents
