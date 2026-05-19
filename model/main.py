from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
import os
import re
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
# template=ChatPromptTemplate.from_messages([
#     ("system","You are an AI that summarizes the text"),
#     ("human","{data}")
# ])
# prompt=template.format_messages(data=docs)
# model=ChatMistralAI("mistral-small-2603",temperature=0.5)
