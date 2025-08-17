# debug_index.py
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

def debug_vectorstore():
    embeddings = OllamaEmbeddings(model="all-minilm")
    vectorstore = Chroma(
        collection_name="study_notes",
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    )

    # Check total count
    count = vectorstore._collection.count()
    print(f"\n Total chunks in vector DB: {count}\n")

    # Get some sample documents
    results = vectorstore._collection.get(limit=3, include=["documents", "metadatas"])
    for i, (doc, meta) in enumerate(zip(results["documents"], results["metadatas"])):
        print(f" Chunk {i+1}:")
        print(f"   Source: {meta.get('source', 'unknown')}")
        print(f"   Content: {doc[:200]}...\n")

if __name__ == "__main__":
    debug_vectorstore()