from app.services.embedder import search_index
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage


llm = ChatGroq(temperature=0, model="llama3-8b-8192")


def ask_documents(query:str = "Summarize the uploaded documents")-> str:
    retrieved_chunks = search_index(query)
    context = "\n\n".join(retrieved_chunks)
    prompt = f"Answer the following questions using the context below. Be concise and cite evidence if Possible. \n\nContext:\n{context}\n\nQuestion: {query}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content