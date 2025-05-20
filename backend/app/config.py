from dotenv import load_dotenv
import os

load_dotenv()  # Load .env into environment

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("Loaded API Key:", GROQ_API_KEY[:6] + "..." if GROQ_API_KEY else "Not Found")
