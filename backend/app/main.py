from fastapi import FastAPI
from app.api.routes import router as api_router
from fastapi.staticfiles import StaticFiles
import os
from fastapi.templating import Jinja2Templates

app = FastAPI(title= "Free LLm Document Research Chatbot")

app.include_router(api_router)


# Templates and static
templates = Jinja2Templates(directory="app/templates")

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(r'D:\Project_local\wasser\frontend\index.html')))
# FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")


# @app.get("/")
# def root():
#     return {"message": "Welcome to the LLm-Powered Theme Chatbot"}
