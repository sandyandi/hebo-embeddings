from litellm import embedding


def create_embedding(content: str):
    return embedding(
        model="voyage/voyage-01",
        input=[content],
    )
