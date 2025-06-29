import PyPDF2
from typing import List

class PDFReaderAgent:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self) -> str:
        text = ""
        with open(self.pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text

    def get_authors(self) -> List[str]:
        with open(self.pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            metadata = reader.metadata
            author = metadata.author if metadata and metadata.author else "Unknown"
            return [author]