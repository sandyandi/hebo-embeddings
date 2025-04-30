from fastapi import FastAPI
from .embeddings.controller import router as embeddings_router

def register_routes(app: FastAPI):
    app.include_router(embeddings_router)
