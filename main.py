from pathlib import Path
from orchestrator import AgenticPDFProcessor

def main():
    base_dir = Path.cwd()
    pdf_dir = base_dir/Path("./cnp")
    pdf_files = list(pdf_dir.glob("*.pdf")) 

    if not pdf_files:
        print("No PDF files found in ./cnp")
        return

    processor = AgenticPDFProcessor(
        root_py_dir=pdf_dir,
        pdf_path=str(pdf_files[0]),  
        output_txt_path="./summary_output.txt"
    )
    processor.run()

if __name__ == "__main__":
    main()
