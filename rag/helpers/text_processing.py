import PyPDF2


def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file.

    Args:
        file_path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text from the PDF.
    """
    text = []
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text.append(content)
        
    return "\n".join(text)


def chunk_text(text, chunk_size=500):
    """
    Chunk text into smaller pieces. 
    
    Args:
        text (str): The text to chunk.
        chunk_size (int): The size of each chunk.
    
    Returns:
        list of str: List of text chunks.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size])) 
    
    return chunks