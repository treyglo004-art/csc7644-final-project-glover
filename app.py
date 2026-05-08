import streamlit as st
from pathlib import Path

DATA_PATH = Path("data/sample_engineering_notes.txt")


def load_documents():
    """Load engineering notes from the data folder."""
    return DATA_PATH.read_text(encoding="utf-8")


def simple_retrieve(question, document_text):
    """Retrieve relevant lines using simple keyword matching."""
    question_words = set(question.lower().replace("?", "").split())
    lines = [line.strip() for line in document_text.splitlines() if line.strip()]

    scored_lines = []
    for line in lines:
        line_words = set(line.lower().replace(".", "").split())
        score = len(question_words.intersection(line_words))
        if score > 0:
            scored_lines.append((score, line))

    scored_lines.sort(reverse=True)
    top_lines = [line for _, line in scored_lines[:3]]

    if not top_lines:
        return "No relevant document content found."

    return "\n".join(top_lines)


def generate_answer(question, context):
    """Generate a simple grounded answer from retrieved context."""
    if context == "No relevant document content found.":
        return "I could not find enough information in the documents to answer that."

    return (
        f"Based on the retrieved course material:\n\n"
        f"{context}\n\n"
        f"Answer: {context}"
    )


st.title("Engineering Question Answering System")
st.write("Ask an engineering question and the system will search course materials for an answer.")

question = st.text_input("Enter your question:")

if st.button("Submit"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        documents = load_documents()
        retrieved_context = simple_retrieve(question, documents)
        answer = generate_answer(question, retrieved_context)

        st.subheader("Retrieved Content")
        st.write(retrieved_context)

        st.subheader("AI Answer")
        st.write(answer)