from src.pdf_loader import load_pdf
from src.chunker import chunk_text
from src.embedder import Embedder

# Load PDF
pdf_path = "data/pdfs/Vanshika_Barua_Resume.pdf"
text = load_pdf(pdf_path)

# Chunk text
chunks = chunk_text(text)

# Create embedder
embedder = Embedder()

# Generate embeddings
embeddings = embedder.embed(chunks)

# Print results
print(f"Total chunks: {len(chunks)}")
print(f"Embedding shape: {embeddings.shape}")

print("\nFirst chunk:")
print(chunks[0][:200])

print("\nFirst embedding (first 10 values):")
print(embeddings[0][:10])