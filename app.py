import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as palm
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os

# Set your Google API key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyB-TV0TQ2sI6eGshh3_8zqKoDuoIsFxcRs'

def get_pdf_text(pdf_docs):
    """Extract text from uploaded PDF documents."""
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    """Split text into smaller chunks for processing."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    """Create a vector store using text chunks and embeddings."""
    embeddings = GooglePalmEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

def get_conversational_chain(vector_store):
    """Create a conversational chain for interactive Q&A."""
    llm = GooglePalm()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
    return conversation_chain

def user_input(user_question):
    """Handle user input and display conversation."""
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write(f"**Human:** {message.content}")
        else:
            st.write(f"**Bot:** {message.content}")

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(page_title="PDF-Conv", layout="wide")
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(to right, #ffcccc, #ccffcc);
        }
        .stButton>button {
            background-color: #4CAF50;
        }
        .stTextInput>div>input {
            border: 2px solid #4CAF50;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.header("PDF-Conv 💬")
    user_question = st.text_input("Ask a Question from the PDF Files")
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = []
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Settings ⚙️")
        st.subheader("Upload your Documents 📎")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Process Button", accept_multiple_files=True)
        if pdf_docs:
            for pdf in pdf_docs:
                st.markdown(f"📄 **{pdf.name}**")
        if st.button("🔄 Process"):
            with st.spinner("Processing..."):
                try:
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vector_store = get_vector_store(text_chunks)
                    st.session_state.conversation = get_conversational_chain(vector_store)
                    st.success("✅ PDFs processed successfully!")
                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
