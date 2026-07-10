from typing import List


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    """
    Splits text into overlapping chunks.

    Args:
        text: Input text.
        chunk_size: Maximum characters per chunk.
        overlap: Number of overlapping characters.

    Returns:
        List of text chunks.
    """

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks