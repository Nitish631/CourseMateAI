from langchain_community.document_loaders import TextLoader
import os
path=os.path.join(os.path.dirname(__file__),"notes.txt")
loader=TextLoader(path,encoding="utf-8")
docs=loader.load()
print(docs[0].page_content)