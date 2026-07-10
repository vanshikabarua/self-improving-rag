from src.pdf_loader import load_pdf
from src.chunker import chunk_text

pdf_path = "data/pdfs/Vanshika_Barua_Resume.pdf"

text = load_pdf(pdf_path)

chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}")
print("\nFirst chunk:\n")
print(chunks[0])