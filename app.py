import streamlit as st
from dotenv import load_dotenv

from pdf_query.pdf_query import read_pdf, PDFQueryAgent
from pdf_query.db import connect

if __name__ == "__main__":
    load_dotenv()
    connect()

    st.title("PDF Query")
    pdf_file = st.file_uploader("Upload PDF")
    if pdf_file:
        pdf_text= read_pdf(pdf_file.read())
        agent = PDFQueryAgent(pdf_text)

        answer, doc = "", ""
        with st.sidebar:
            question = st.text_input("Ask a question")
            if question:
                answer, doc= agent.get_answer(question)
        if answer:
            st.write(f"Answer: {answer}")
            st.write(f"""
                    Document:
                    {doc}
                """)