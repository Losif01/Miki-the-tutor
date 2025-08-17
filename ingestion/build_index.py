# ingestion/build_index.py
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from .load_docs import load_documents
import os
import time

def build_vector_index(persist_directory="./chroma_db"):
    """
    Load documents, embed, and save to ChromaDB.
    Fixed for langchain-chroma (no .persist() needed).
    """
    print(" Starting vector index build process and timer...")
    start_time = time.time()
    
    # 1. Verify data directory
    print("\n STEP 1: Verifying data directory")
    try:
        documents = load_documents()
        if not documents:
            raise ValueError("Document loading returned empty list")
    except Exception as e:
        print(f"\n CRITICAL ERROR: Document loading failed - {str(e)}")
        raise
    
    # 2. Test embeddings
    print("\n STEP 2: Testing embedding model")
    try:
        embeddings = OllamaEmbeddings(model="all-minilm")
        
        # Test embedding generation
        print(" Testing with sample text...")
        test_text = "This is a test sentence for embedding."
        test_embedding = embeddings.embed_query(test_text)
        print(f" Embedding test successful - vector length: {len(test_embedding)}")
    except Exception as e:
        print(f"\n CRITICAL ERROR: Embedding model failed - {str(e)}")
        print("Possible causes:")
        print("  - Ollama not running (start with 'ollama serve')")
        print("  - 'all-minilm' model not pulled (run 'ollama pull all-minilm')")
        raise
    
    # 3. Build index - NO .persist() NEEDED
    print("\n STEP 3: Building vector index")
    try:
        # Create directory if it doesn't exist
        os.makedirs(persist_directory, exist_ok=True)
        print(f"   Using persist directory: {os.path.abspath(persist_directory)}")
        
        # Clear existing collection
        print("   Clearing previous index (if exists)...")
        try:
            old_store = Chroma(
                collection_name="study_notes",
                embedding_function=embeddings,
                persist_directory=persist_directory
            )
            old_store.delete_collection()
            print("   Previous collection cleared")
        except Exception as e:
            print(f"   Collection clear attempt failed (may not exist): {str(e)}")
        
        # Create new collection and add documents
        print("   Creating new vector store and adding chunks...")
        vectorstore = Chroma(
            collection_name="study_notes",
            embedding_function=embeddings,
            persist_directory=persist_directory
        )
        
        vectorstore.add_documents(documents)
        print(f"   Successfully added {len(documents)} chunks to vector store")
        print(f"   Data is automatically saved to disk (no .persist() needed)")

        # Verify count
        count = vectorstore._collection.count()
        print(f"\n SUCCESS: {count} chunks indexed and saved to {persist_directory}")
        print(f" Total time: {time.time() - start_time:.2f} seconds")
        
        return vectorstore
        
    except Exception as e:
        print(f"\n CRITICAL ERROR: Index build failed - {str(e)}")
        raise