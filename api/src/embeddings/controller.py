from fastapi import APIRouter, status

from . import service

router = APIRouter(
    prefix="/embeddings",
    tags=["embeddings"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_embedding(embedding: str):
    return service.create_embedding(embedding)
