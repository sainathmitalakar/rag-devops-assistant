import os
import json
from sentence_transformers import SentenceTransformer
from load_documents import all_chunks

print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings_list = []

for i, chunk in enumerate(all_chunks, start=1):
    vector = model.encode(chunk["chunk"]).tolist()
    embeddings_list.append({
        "filename": chunk["filename"],
        "chunk": chunk["chunk"],
        "vector": vector
    })
    print(f"✅ Generated embedding for chunk {i}/{len(all_chunks)}")

with open("embeddings.json", "w", encoding="utf-8") as f:
    json.dump(embeddings_list, f, ensure_ascii=False, indent=2)

print("\n✅ All embeddings saved to embeddings.json")
