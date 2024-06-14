import streamlit as st  # Import Streamlit for building the web app
from PyPDF2 import PdfReader  # Import PdfReader from PyPDF2 to read PDF files
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Import text splitter
import google.generativeai as palm  # Import Google generative AI
from langchain.embeddings import GooglePalmEmbeddings  # Import Google Palm embeddings
from langchain.llms import GooglePalm  # Import Google Palm LLM
from langchain.vectorstores import FAISS  # Import FAISS for vector storage
from langchain.chains import ConversationalRetrievalChain  # Import Conversational Retrieval Chain
from langchain.memory import ConversationBufferMemory  # Import Conversation Buffer Memory
import os  # Import OS for environment variables
import warnings

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Set Google API Key for Google Palm
os.environ['GOOGLE_API_KEY'] = ''

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
