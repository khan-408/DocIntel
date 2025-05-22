from app.services.embedder import search_index
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from app.services.promt_builder import build_prompt

llm = ChatGroq(temperature=0, model="llama3-8b-8192")


# def ask_documents(query:str = "Summarize the uploaded documents")-> str:
#     retrieved_chunks = search_index(query)
#     prompt = build_prompt(retrieved_chunks, query)
#     response = llm.invoke(prompt)

#     sources = []
#     for chunk in retrieved_chunks:
#         src = chunk.metadata.get("source", "Unknown Source")
#         if src not in sources:
#             sources.append(src)

#     return response.content, sources

def ask_documents(query: str = "Summarize the uploaded documents") -> tuple[str, list[str]]:
    retrieved_chunks = search_index(query)
    if not retrieved_chunks:
        return "No relevant context found.", []

    prompt = build_prompt(retrieved_chunks, query)
    response = llm.invoke(prompt)

    sources = []
    for chunk in retrieved_chunks:
        src = chunk.metadata.get("source", "Unknown Source")
        if src not in sources:
            sources.append(src)

    return response.content, sources
