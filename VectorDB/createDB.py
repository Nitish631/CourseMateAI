from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os
#LOAD THE FILE PATH AND THE ENVIRONMENT VARIABLES
path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"VectorDB","AiNotes.pdf")
load_dotenv()
#DOCUMENT LOADER
loader=PyPDFLoader(path)
docs=loader.load()
for doc in docs:
    text=doc.page_content
    text=re.sub(r"-\n"," ",text)
    text=re.sub(r"\s+"," ",text)
    doc.page_content=text.strip()
#CHUNKING
splitter=RecursiveCharacterTextSplitter(chunk_size=300,chunk_overlap=70)
chunks=splitter.split_documents(documents=docs)
for chunk in chunks:
    print(chunk.page_content)
    print("===================================")
#EMBEDDINGS AND VECTOR DB
embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore=Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
    )
