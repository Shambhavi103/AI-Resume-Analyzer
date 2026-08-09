from pypdf import PdfReader
from docx import Document
import os


def extract_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx(docx_path):
    doc = Document(docx_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


if __name__ == "__main__":

    file_path = "sample_resumes/Resume.pdf"

    if file_path.endswith(".pdf"):
        resume_text = extract_pdf(file_path)

    elif file_path.endswith(".docx"):
        resume_text = extract_docx(file_path)

    else:
        print("Unsupported file type")
        exit()

    print("\n===== EXTRACTED RESUME TEXT =====\n")
    print(resume_text)