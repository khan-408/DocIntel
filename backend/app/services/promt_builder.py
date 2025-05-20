def build_prompt(chunks, query):
    """
    Builds a prompt from the retrieved document chunks and the user query.
    Each chunk should contain the document text and a reference to its source.
    """
    context = ""
    for i, chunk in enumerate(chunks):
        source = chunk.metadata.get("source", f"Doc {i+1}")
        text = chunk.page_content if hasattr(chunk, "page_content") else str(chunk)
        context += f"\nSource [{i+1}] ({source}):\n{text}\n"

    prompt = f"""
You are a helpful AI assistant. Use the following context extracted from documents to answer the user's question.

Context:
{context}

User Question:
{query}

Answer:
"""
    return prompt.strip()
