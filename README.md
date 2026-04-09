🤖 RAG Assistant: Chat with your PDFs
A streamlined Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions. It uses high-performance AI models to provide instant, accurate answers based only on the uploaded content.

💡 The Concept (In Simple Words)
Most AI models (like ChatGPT) only know what they were trained on. RAG gives the AI a "temporary memory" (your PDF).

Ingestion: It reads your PDF and breaks it into small chunks.

Retrieval: When you ask a question, it searches those chunks for the most relevant information.

Generation: It sends that specific information to the LLM (Groq) to generate a precise answer.

🛠️ Tech Stack
Frontend: Streamlit (Clean, web-based UI)

Orchestration: LangChain (Connects the AI components)

LLM: Groq (Mixtral-8x7b) – chosen for ultra-fast response times.

Vector Database: FAISS (Efficient similarity search)

Embeddings: HuggingFace (Converts text into searchable math vectors)
