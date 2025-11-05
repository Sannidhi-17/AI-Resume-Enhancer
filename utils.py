import pdfplumber
import re

def pdf_to_text(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"
    return text

def split_sections(text):
    # simple fallback: just return full text
    return {"full": text}

def split_experience_bullets(experience_text):
    bullets = [b.strip() for b in re.split(r"[\n•-]", experience_text) if b.strip()]
    return bullets
