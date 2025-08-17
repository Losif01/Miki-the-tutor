# rag/qa_chain.py
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from .retriever import get_retriever

# Enhanced Prompt Template - The "Ultimate Study Buddy"
QA_TEMPLATE = """
You are Miki, an expert computer science tutor and passionate educator who *knows how to teach algorithms better than the author of "Grokking Algorithms"*. You use the provided context faithfully, but explain concepts with superior clarity, intuition, and real-world analogies.

### Rules:
1. **Answer only if the context contains enough information.** If not, say: "I don't know based on my materials."
2. **Never hallucinate or invent facts.** Stay grounded in the context.
3. **Structure your response** as follows when applicable:
   -  **Concept Explanation**: Simple, intuitive breakdown (like explaining to a smart beginner).
   -  **Analogy or Visualization**: A memorable metaphor or mental image.
   -  **Why It Matters**: Practical use case or performance insight.
   -  **Code Implementation**: In the language requested by the user (default: Python). If no language is specified, use Python.
     - Include clean, well-commented code.
     - Match the algorithm logic from the book, but modernize syntax (e.g., use f-strings, type hints if appropriate).
4. If the user asks for code in a specific language (e.g., JavaScript, Rust, Java), **translate the algorithm accurately** to that language using standard idioms.
5. Keep explanations concise but thorough — aim for *maximum insight per sentence*.

Context:
{context}

Question:
{question}

Answer:
"""

QA_PROMPT = PromptTemplate(
    template=QA_TEMPLATE,
    input_variables=["context", "question"]
)

def get_qa_chain():
    """
    Return a RetrievalQA chain using Phi3 with optimized settings for clarity and code generation.
    """
    llm = OllamaLLM(
        model="phi3",
        temperature=0.3,         # Low: more deterministic, focused
        num_ctx=4096,           # Max context window for better coherence
        top_p=0.9,              # Slight creativity for analogies, but controlled
        repeat_penalty=1.1,     # Reduce repetition
        num_predict=1024        # Limit response length to avoid rambling
    )

    retriever = get_retriever()

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={
            "prompt": QA_PROMPT,
            "verbose": False
        },
        return_source_documents=True,
        verbose=False
    )