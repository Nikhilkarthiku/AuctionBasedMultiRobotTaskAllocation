import PyPDF2
from typing import List,Union
from pathlib import Path

chunk_size = 6000
class PDFReaderAgent:
    def __init__(self, pdf_path: str):
        # Ensure pdf_path is a string
        self.pdf_path = Path(pdf_path)

    def extract_text(self) -> str:
        text = ""
        with open(self.pdf_path, "rb") as f:  
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    
    def extract_metadata(self, pdf_path: Path):
        """Extracts metadata like title and author from the PDF metadata."""
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            metadata = reader.metadata
            title = metadata.title if metadata and metadata.title else pdf_path.stem
            author = metadata.author if metadata and metadata.author else "Unknown"
        return title, author

    def get_authors(self) -> List[str]:
        with open(self.pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            metadata = reader.metadata
            author = metadata.author if metadata and metadata.author else "Unknown"
            return [author]