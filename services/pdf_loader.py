from PyPDF2 import PdfReader

def load_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file.file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text
