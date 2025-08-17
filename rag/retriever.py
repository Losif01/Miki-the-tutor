# rag/retriever.py
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


def get_retriever(persist_directory="./chroma_db"):
    """
    Return a retriever connected to the persisted ChromaDB.
    """
    embeddings = OllamaEmbeddings(model="all-minilm")
    
    vectorstore = Chroma(
        collection_name="study_notes",
        embedding_function=embeddings,
        persist_directory=persist_directory
    )
    
    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )