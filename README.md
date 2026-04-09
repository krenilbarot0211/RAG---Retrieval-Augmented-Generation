🤖 Advanced RAG Assistant: Intelligent PDF Conversation Engine
An enterprise-grade Retrieval-Augmented Generation (RAG) pipeline designed to bridge the gap between static documents and actionable intelligence. This project leverages a state-of-the-art tech stack to provide near-instant, context-aware responses to complex queries.

🌟 Overview
Traditional LLMs suffer from "knowledge cutoff" and hallucinations when asked about private data. This project solves that by implementing a RAG workflow: grounding the AI's responses in specific, retrieved facts from your own uploaded PDF documents.

🏗️ Technical Architecture
The system is built on a modular four-stage pipeline:

1. Data Ingestion & Pre-processing

Loading: Uses PyPDFLoader to parse and extract raw text from PDF files.

Chunking: Implements RecursiveCharacterTextSplitter.

Strategy: 1000 character chunks with a 200-character overlap to ensure no context is lost at the "seams" of the split.

2. Embedding & Vector Storage

Model: all-MiniLM-L6-v2 from HuggingFace. This was chosen for its perfect balance between speed and semantic accuracy.

Vector Database: FAISS (Facebook AI Similarity Search). It allows for efficient similarity searches in high-dimensional spaces, enabling the assistant to find relevant document sections in milliseconds.

3. Retrieval & Prompt Engineering

Context Retrieval: The system uses a similarity search to find the top k most relevant chunks.

Prompt Template: A custom ChatPromptTemplate is used to strictly instruct the LLM to only use the provided context, reducing hallucinations.

4. Generation (The Inference Engine)

LLM: Groq (Mixtral-8x7b-32768).

Reasoning: Using Groq’s LPU (Language Processing Unit) inference engine allows this app to achieve token-per-second speeds that are significantly faster than traditional cloud providers.


🚀 Getting Started
Prerequisites

A Groq API Key (Obtainable from the Groq Console)

A Python environment (Conda or venv recommended)
