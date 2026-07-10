from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding model.
        """
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: list[str]):
        """
        Convert a list of text chunks into embeddings.
        """
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings