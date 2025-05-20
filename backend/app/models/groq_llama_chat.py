from langchain_groq import ChatGroq
from langchain.schema import HumanMessage


llm = ChatGroq(temperature=0, model="llama3-8b-8192")


def ask_llama(query:str)->str:
    messages = [HumanMessage(content=query)]
    return llm(messages).content
