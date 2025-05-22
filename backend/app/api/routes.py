from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.services.document_processor import process_file
from app.services.qa_engine import ask_documents
from app.services.embedder import build_vector_index
from fastapi.responses import JSONResponse
from typing import List

router= APIRouter()
templates = Jinja2Templates(directory="app/templates")




DOCUMENT_STORE = []

@router.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/upload")

async def upload(request: Request, files: List[UploadFile] = File(...)):
    documents = []

    for file in files:
        context = await file.read()
        text = process_file(file.filename, context)
        documents.append({
            "text": text,
            "filename": file.filename
        })

    DOCUMENT_STORE.clear()
    DOCUMENT_STORE.append(documents)
    build_vector_index(DOCUMENT_STORE)
    return templates.TemplateResponse("chat.html", {"request": request, "message": f"Uploaded {len(DOCUMENT_STORE)} files successfully."})


CHAT_HISTORY = []
# @router.post("/ask")
# async def ask_query(request: Request, query: str = Form(...)):
#     answer, sources = ask_documents(query)    
#     CHAT_HISTORY.append({"Question":query, "Answer": answer, "Sources": sources})
#     return templates.TemplateResponse("chat.html", {
#         "request": request,
#         "answer": answer,
#         "chat_history": CHAT_HISTORY,
#         "sources": sources,
#         })
@router.post("/ask")
async def ask_query(request: Request, query: str = Form(...)):
    try:
        answer, sources = ask_documents(query)

        CHAT_HISTORY.append({
            "Question": query,
            "Answer": answer,
            "Sources": sources or []
        })

        return templates.TemplateResponse("chat.html", {
            "request": request,
            "chat_history": CHAT_HISTORY,
        })

    except Exception as e:
        print("Error occurred in /ask route:", str(e))
        return JSONResponse(
            status_code=500,
            content={"message": "Internal Server Error", "error": str(e)}
        )



# @router.get("/ask")
# async def ask(query: str):
#     answer = ask_documents(query)
#     return {"answer": answer}


@router.get("/ping")
def ping():
    return {"status": "ok"}
