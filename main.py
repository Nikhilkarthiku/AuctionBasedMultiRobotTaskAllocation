from pathlib import Path
from orchestrator import AgenticPDFProcessor

def main():
    base_dir = Path.cwd()
    pdf_dir = base_dir/Path("./cnp")
    pdf_files = list(pdf_dir.glob("*.pdf")) 

    if not pdf_files:
        print("No PDF files found in ./cnp")
        return

    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        output_txt=pdf_dir/f"{pdf_file.stem}_summary.txt"
        processor = AgenticPDFProcessor(
            root_py_dir=pdf_dir,
            pdf_path=str(pdf_file),
            output_txt_path=str(output_txt)  
        )
        processor.run()

if __name__ == "__main__":
    main()