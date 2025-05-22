from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from langchain_core.documents import Document


model = SentenceTransformer("all-MiniLM-L6-v2")
dimension  = model.get_sentence_embedding_dimension()
faiss_index = faiss.IndexFlatL2(dimension)
stored_chunks = []

# def split_text(text, chunk_size = 500, overlap = 50):
#         words = text.split()
#         chunks = []
#         for i in range(0, len(words), chunk_size-overlap):
#             chunk = " ".join(words[i:i+chunk_size])
#             chunks.append(chunk)
#         return chunks


def split_into_chunks(text, chunk_size=500, overlap=50, source="Unknown"):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk_text = " ".join(words[i:i + chunk_size])
        doc = Document(page_content=chunk_text, metadata={"source": source})
        chunks.append(doc)
    return chunks


# def build_vector_index(docs: list[str], save_paths = "vector_store/faiss_index.idx"):
#     global stored_chunks
#     all_chunks = []
#     for doc in docs:
#         all_chunks.extend(split_text(doc))
    
#     if not all_chunks:
#         raise ValueError("No chunks were created from documents!")

#     embeddings = model.encode(all_chunks)
#     faiss_index.add(np.array(embeddings))
#     stored_chunks = all_chunks
#     faiss.write_index(faiss_index, save_paths)
#     return "vector store build"

from langchain_core.documents import Document

stored_chunks = []  # clear or declare globally

# def build_vector_index(documents):
#     global stored_chunks, faiss_index, model

#     # Flatten all texts with metadata
#     chunks = []
#     for doc in documents:
#         filename = doc.get("filename", "Unknown")  # Assume document is dict with 'text' and 'filename'
#         # text_chunks = split_into_chunks(doc["text"])  # your custom chunking logic
#         # for chunk in text_chunks:
#         #     chunks.append(Document(page_content=chunk, metadata={"source": filename}))
#         text_chunks = split_into_chunks(doc["text"], source=filename)
#         chunks.extend(text_chunks)

#     stored_chunks = chunks  # store Document objects
def build_vector_index(documents):
    global stored_chunks, faiss_index, model

    chunks = []
    for i, doc_text in enumerate(documents):
        filename = f"Document_{i+1}"  # Generate a fallback filename
        text_chunks = split_into_chunks(doc_text, source=filename)
        chunks.extend(text_chunks)

    stored_chunks = chunks
    embeddings = model.encode([doc.page_content for doc in stored_chunks])
    faiss_index = faiss.IndexFlatL2(len(embeddings[0]))
    faiss_index.add(np.array(embeddings))


    # Create embeddings
    embeddings = model.encode([doc.page_content for doc in stored_chunks])
    faiss_index = faiss.IndexFlatL2(len(embeddings[0]))
    faiss_index.add(np.array(embeddings))


# def search_index(query, k=3):

    
#     query_vec = model.encode([query])
#     D,I = faiss_index.search(np.array(query_vec), k)
#     if len(I[0]) == 0 or len(stored_chunks) == 0:
#         return ["No relevant context found."]

#     # Safely return only available chunk indices
#     return [stored_chunks[i] for i in I[0] if i < len(stored_chunks)]

def search_index(query, k=3):
    query_vec = model.encode([query])
    D, I = faiss_index.search(np.array(query_vec), k)

    if len(I[0]) == 0 or len(stored_chunks) == 0:
        return ["No relevant context found."]

    return [stored_chunks[i] for i in I[0] if i < len(stored_chunks)]
