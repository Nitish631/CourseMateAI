from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os
path = os.path.join(os.path.dirname(__file__), "notes.txt")
loader = TextLoader(path, encoding="utf-8")
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=20
)

chunks = text_splitter.split_documents(docs)
print(chunks[0])
print(len(chunks))
for i in chunks:
    print(i.page_content)
    print("===")
