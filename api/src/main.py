from fastapi import FastAPI
from .logging import configure_logging, LogLevels
from .api import register_routes

configure_logging(LogLevels.info)

app = FastAPI()

register_routes(app)
