# DocIntel

## Overview
DocIntel is an AI-powered **document research and theme identification chatbot**. It allows users to upload, analyze, and extract insights from a large set of documents. The chatbot enables **accurate citation-based responses**, identifies common themes across multiple documents, and synthesizes structured answers.

## Features
- **Document Upload & OCR Processing**: Supports PDFs and scanned images, leveraging OCR for text extraction.
- **Query-Based Response Generation**: Users can ask questions in natural language and receive cited answers.
- **Theme Identification**: Recognizes patterns and key themes across documents.
- **Comprehensive Citations**: Provides document-level citations with optional granular reference (paragraph/sentence).
- **Interactive UI**: Clean interface for document management, querying, and result visualization.

## Technical Stack
- **AI Models**: OpenAI GPT, Gemini, Groq (LLAMA)
- **Vector Databases**: Qdrant, ChromaDB, FAISS
- **OCR**: Tesseract, PaddleOCR
- **Backend Frameworks**: FastAPI, Flask
- **Deployment Options**: Render, Railway, Replit, Hugging Face Spaces, Vercel

## Installation & Setup
### Prerequisites
- Python 3.8+
- Dependencies listed in `requirements.txt`
- Access to LLM APIs (OpenAI, Gemini, etc.)

### Steps
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/docintel.git
   cd docintel

### To Install the Requirements.
```sh
pip install -r requirements.txt
```
### To Run the Program.

```sh
python backend/app/main.py
```