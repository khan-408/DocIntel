from app.services.embedder import search_index
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from app.services.promt_builder import build_prompt

llm = ChatGroq(temperature=0, model="llama3-8b-8192")


def ask_documents(query:str = "Summarize the uploaded documents")-> str:
    retrieved_chunks = search_index(query)
    prompt = build_prompt(retrieved_chunks, query)
    response = llm.invoke(prompt)
    sources = [chunk.metadata['source'] for chunk in retrieved_chunks]
    return response.content, sources
