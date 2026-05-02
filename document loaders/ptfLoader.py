from langchain_community.document_loaders import PyPDFLoader
import os
path=os.path.join(os.path.dirname(__file__),"AiNotes.pdf")    
loader=PyPDFLoader(path)
docs=loader.load()
