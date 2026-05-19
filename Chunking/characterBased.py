from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
import os
path=os.path.join(os.path.dirname(__file__),"notes.txt")
loader=TextLoader(path,encoding="utf-8")
docs=loader.load()

splitter=CharacterTextSplitter(separator="\n",chunk_size=50,chunk_overlap=2)
chunks=splitter.split_documents(docs)
for i in chunks:
    print(i.page_content)
    print("===")