import os
import PyPDF2

PDF_FOLDER = "docs"

all_chunks = []

for pdf_file in os.listdir(PDF_FOLDER):
    if pdf_file.endswith(".pdf"):
        path = os.path.join(PDF_FOLDER, pdf_file)
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for i, page in enumerate(reader.pages):
                text = page.extract_text().strip()
                if text:
                    all_chunks.append({
                        "filename": pdf_file,
                        "chunk": text
                    })

print(f"✅ Loaded {len(all_chunks)} chunks from PDFs.")
