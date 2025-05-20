import fitz
from PIL import Image
import pytesseract
from io import BytesIO



def process_file(filename: str, content: bytes) -> str:
    if filename.endswith(".pdf"):
        return extract_pdf_text(content)
    elif filename.endswith((".jpg",".jpeg",".png")):
        return (extract_image_text(content))
    return "Unsupported File Type"

def extract_pdf_text(content:bytes)->str:
    doc = fitz.open(stream=BytesIO(content), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def extract_image_text(content:bytes)-> str:
    image = Image.open(BytesIO(content))
    return pytesseract.image_to_string(image)

