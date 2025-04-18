# app/processor.py

import os
import fitz  # PyMuPDF
import docx
import pandas as pd

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def read_excel(file):
    df = pd.read_excel(file)
    return df.to_string()

def read_text(file):
    return file.read().decode("utf-8")

def extract_text_from_file(file):
    file_type = file.name.split('.')[-1].lower()
    
    if file_type == "pdf":
        return read_pdf(file)
    elif file_type == "docx":
        return read_docx(file)
    elif file_type in ["xls", "xlsx"]:
        return read_excel(file)
    elif file_type == "txt":
        return read_text(file)
    else:
        return "❌ Unsupported file type"
