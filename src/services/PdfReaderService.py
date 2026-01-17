from pypdf import PdfReader

def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = []

    for page in reader.pages:
        text_in_page = page.extract_text()

        if text_in_page:
            text.append(text_in_page)

    return "\n".join(text)