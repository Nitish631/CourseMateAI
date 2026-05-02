from langchain_community.document_loaders import PyPDFLoader
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()
path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"document loaders","AiNotes.pdf")
loader=PyPDFLoader(path)
docs=loader.load()

promptTemplate=ChatPromptTemplate.from_messages([
    ("system","you are a AI that summarizes the content of the text"),
    ("human","{data}")
])
content=""
for doc in docs:
    content+=doc.page_content
final_prompt=promptTemplate.invoke({"data":content})
model=ChatMistralAI(model="mistral-small-2603",temperature=0.5)
print(model.invoke(final_prompt).content)