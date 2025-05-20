from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedder = SentenceTransformer("all-MiniLM-L6-v2")
def get_embeddings(text_chunks: list[str])->tuple[faiss.IndexFlatL2, list[str]]:
    embeddings = embedder.encode(text_chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))
    return index, text_chunks


def query_faiss(query:str, index, documents: list[str],k:int=3)->list[str]:
    q_embedding = embedder.encode([query])
    D,I = index.search(np.array(q_embedding),k)
    return [documents[i ] for i in I[0]]