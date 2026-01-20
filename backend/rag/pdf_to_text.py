from pypdf import PdfReader

def pdf_to_text(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    pages = []
    for page in reader.pages:
        # Extract text and handle None values
        text = page.extract_text() or ""
        pages.append(text)
    
    # Join pages with newlines
    full_text = "\n".join(pages)

    # Basic cleaning: remove weird carriage returns
    full_text = full_text.replace("\r", "\n")
    
    # Remove empty lines to make it compact
    lines = [line.strip() for line in full_text.split("\n") if line.strip()]
    return "\n".join(lines)

# Simple test to see if it works when we run this file directly
if __name__ == "__main__":
    # We test with our chennai pdf
    sample_text = pdf_to_text("backend/data/chennai_services.pdf")
    print(sample_text[:500]) # Print first 500 characters