from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.services.document_processor import process_file
from app.services.qa_engine import ask_documents
from app.services.embedder import build_vector_index

router= APIRouter()
templates = Jinja2Templates(directory="app/templates")




DOCUMENT_STORE = []

@router.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/upload")

async def upload(request: Request, file: UploadFile=File(...)):
    context = await file.read()
    text = process_file(file.filename, context)
    DOCUMENT_STORE.clear()
    DOCUMENT_STORE.append(text)
    build_vector_index(DOCUMENT_STORE)
    return templates.TemplateResponse("chat.html", {"request": request, "message": "Upload successful!"})


CHAT_HISTORY = []
@router.post("/ask")
async def ask_query(request: Request, query: str = Form(...)):
    answer, sources = ask_documents(query)    
    CHAT_HISTORY.append({"Question":query, "Answer": answer, "Sources": sources})
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "answer": answer,
        "chat_history": CHAT_HISTORY,
        "sources": sources,
        })


# @router.get("/ask")
# async def ask(query: str):
#     answer = ask_documents(query)
#     return {"answer": answer}


@router.get("/ping")
def ping():
    return {"status": "ok"}
