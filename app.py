import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
#from langchain.chains.combine_documents import create_stuff_documents_chain
#from langchain.chains import create_retrieval_chain
# 1. Setup
load_dotenv()
st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("🤖 Document Q&A Assistant")

# Initialize LLM & Embeddings
llm = ChatGroq(model="mixtral-8x7b-32768")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Sidebar for Uploading
with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
    process_button = st.button("Process Document")

# 3. RAG Logic
if uploaded_file and process_button:
    with st.spinner("Processing document..."):
        # Save temp file to disk so PyPDFLoader can read it
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getvalue())
        
        # Load and Split
        loader = PyPDFLoader("temp.pdf")
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        final_documents = text_splitter.split_documents(docs)
        
        # Create Vector Store
        vectorstore = FAISS.from_documents(final_documents, embeddings)
        st.session_state.retriever = vectorstore.as_retriever()
        st.success("Document ready!")

# 4. Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about your PDF..."):
    if "retriever" not in st.session_state:
        st.error("Please upload and process a document first!")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Create the chain
            system_prompt = (
                "Use the following pieces of retrieved context to answer the question. "
                "If you don't know the answer, say you don't know.\n\n{context}"
            )
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                ("human", "{input}"),
            ])
            
            question_answer_chain = create_stuff_documents_chain(llm, prompt_template)
            rag_chain = create_retrieval_chain(st.session_state.retriever, question_answer_chain)
            
            # Get response
            response = rag_chain.invoke({"input": prompt})
            answer = response["answer"]
            st.markdown(answer)
            
        st.session_state.messages.append({"role": "assistant", "content": answer})