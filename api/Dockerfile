# Base API image
FROM python:3-slim-bookworm AS api_base

COPY . /app
WORKDIR /app
ENV PYTHONPATH="/app:$PYTHONPATH"

COPY --from=ghcr.io/astral-sh/uv:debian /usr/local/bin/uv /usr/local/bin/uv

ENV UV_SYSTEM_PYTHON=1
ENV UV_CACHE_DIR=/root/.cache/uv

RUN --mount=type=cache,target=$UV_CACHE_DIR \
    uv pip install --system -r pyproject.toml


# Dev API image
FROM api_base AS api_dev

CMD ["fastapi", "dev", "src/main.py", "--host", "0.0.0.0", "--port", "80"]


# Prod API image
FROM api_base AS api_prod

CMD ["fastapi", "run", "src/main.py", "--port", "8000"]
