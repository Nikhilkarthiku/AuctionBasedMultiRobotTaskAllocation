from Pythonreader_agent import PythonFileReaderAgent
from pdfreader_agent import PDFReaderAgent
from summarizer_agent import SummarizerAgent

class AgenticPDFProcessor:
    def __init__(self, root_py_dir, pdf_path, output_txt_path):
        self.reader_agent = PythonFileReaderAgent(root_py_dir,output_txt_path)
        self.pdf_agent = PDFReaderAgent(pdf_path)
        self.summarizer_agent = SummarizerAgent()

    def run(self):
        print("Reading Python files (for contextual usage)...")
        py_contents = self.reader_agent.read_python_files()

        print("Reading PDF content...")
        pdf_text = self.pdf_agent.extract_text()
        authors = self.pdf_agent.get_authors()

        print("Generating summary using LLM...")
        summary = self.summarizer_agent.summarize(pdf_text)

        print("Writing results to output file...")
        self.reader_agent.write(', '.join(authors), summary)

        print("Process completed!")