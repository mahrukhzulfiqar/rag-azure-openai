from pydantic import BaseModel


class RagChatRequest(BaseModel):
    message: str
    top_k: int = 1
