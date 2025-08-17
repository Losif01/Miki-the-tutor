# ingestion/load_docs.py
import os
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    UnstructuredFileLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(data_dir="./data"):
    """
    Load and split documents from a directory.
    Supports: .pdf, .docx, .txt
    """
    print(f"\n🔍 Checking data directory: {os.path.abspath(data_dir)}")
    
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")
    
    documents = []
    file_count = 0
    
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        print(f" Found file: {file}")
        
        try:
            if file.endswith(".pdf"):
                print(f"   Attempting to load PDF: {file}")
                loader = PyPDFLoader(file_path)
                docs = loader.load()
                print(f"   Successfully loaded {len(docs)} pages from {file}")
            elif file.endswith(".docx"):
                print(f"   Attempting to load DOCX: {file}")
                loader = Docx2txtLoader(file_path)
                docs = loader.load()
                print(f"   Successfully loaded DOCX: {file}")
            elif file.endswith(".txt"):
                print(f"   Attempting to load TXT: {file}")
                loader = TextLoader(file_path, encoding="utf-8")
                docs = loader.load()
                print(f"   Successfully loaded TXT: {file}")
            else:
                print(f"   Skipping unsupported file: {file}")
                continue
                
            for doc in docs:
                doc.metadata["source"] = file
                if "page" in doc.metadata:
                    doc.metadata["page"] += 1  # Make 1-indexed
            documents.extend(docs)
            file_count += 1
            
        except Exception as e:
            print(f"   ERROR loading {file}: {str(e)}")
            print(f"     This usually means:")
            print(f"     - Missing package (try 'pip install pypdf' for PDFs)")
            print(f"     - Corrupted file")
            print(f"     - Permission issues\n")

    if file_count == 0:
        raise ValueError(
            f"No supported files found in {data_dir}!\n"
            "Please add PDF, DOCX, or TXT files to your data directory."
        )
    
    print(f"\n Splitting {len(documents)} documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", "(?<=\\.) ", " ", ""],  # Split at paragraphs/sentences
    keep_separator=False
)
    
    chunks = text_splitter.split_documents(documents)
    print(f" Created {len(chunks)} chunks from {file_count} files")
    
    # Print first chunk for verification
    if chunks:
        print("\n First chunk sample:")
        print(f"Source: {chunks[0].metadata['source']}")
        print(f"Content: {chunks[0].page_content[:200]}...\n")
    
    return chunks