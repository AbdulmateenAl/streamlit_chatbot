import streamlit as st
import pandas as pd

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

from PyPDF2 import PdfReader


st.title("Here is my first streamlit app")

pdf_texts = "" # stores all text in pdf

uploaded_file = st.file_uploader("choose a file")

# Feeding the AI with some context
template = """"
Context: {context}

Question: {question}

Answer: Let's think step by step"""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model='llama3')

chain = prompt | model


if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        page_length = len(reader.pages)
        st.write(f"The uploaded pdf has {page_length} pages!")

        for i in range(page_length):
            page = reader.pages[i]
            page_text = page.extract_text()

            if page_text: # Ensures there is something to append
                pdf_texts += page_text + '\n\n'

        context = pdf_texts
        
        st.write("Extracted Text: ")
        st.text_area("PDF Content", pdf_texts, height=300)

        option = st.selectbox('What would you like to do with your pdf file?', ('Ask a question', 'Create a quiz'))
        st.text_input("Ask", key="question")
        question = st.session_state.question

        if option == 'Ask a question':
            # checks if there is aren't empty
            if context and question:
                response = chain.invoke({"context": context, "question": question})
                st.write("AI response")
                st.write(response)
            else:
                st.write("Please upload a pdf file and ask a question")
        elif option == 'Create a quiz':
            quiz_template = """
            You're a quiz generator, you should ask questions based on pdf: {pdf} and question: {question}
            Each question should have four multiple choice answer and one of them should be correct.
            The format is as:
            1. Question?\n
            A. Option 1\n
            B. Option 2\n
            C. Option 3\n
            D. Option 4\n
            The options should be on a seperate line
            Correct Answer: [Correct option]
            """
            quiz_prompt = ChatPromptTemplate.from_template(quiz_template)
            quiz_chain = quiz_prompt | model
            quiz_response = quiz_chain.invoke({"pdf": pdf_texts, "question": question})

            st.write("Generated quiz questions:")
            st.write(quiz_response)
    else:
        st.write("Please upload a pdf file")
