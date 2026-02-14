import math
from typing import List, Tuple
from app.services.azure_openai_service import AzureOpenAIService


class InMemoryVectorStore:
    def __init__(self):
        self.azure_service = AzureOpenAIService()
        self.documents: List[str] = []
        self.embeddings: List[List[float]] = []

    def add_document(self, text: str):
        embedding = self.azure_service.embed(text)
        self.documents.append(text)
        self.embeddings.append(embedding)

    def cosine_similarity(self, v1: List[float], v2: List[float]) -> float:
        dot_product = sum(a * b for a, b in zip(v1, v2))
        norm_v1 = math.sqrt(sum(a * a for a in v1))
        norm_v2 = math.sqrt(sum(b * b for b in v2))
        return dot_product / (norm_v1 * norm_v2)

    def search(self, query: str, top_k: int = 1) -> List[Tuple[str, float]]:
        query_embedding = self.azure_service.embed(query)

        similarities = []
        for doc, emb in zip(self.documents, self.embeddings):
            score = self.cosine_similarity(query_embedding, emb)
            similarities.append((doc, score))

        similarities.sort(key=lambda x: x[1], reverse=True)

        return similarities[:top_k]
