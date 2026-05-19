from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
import os

load_dotenv()
path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"document loaders","notes.txt")
loader=TextLoader(path,encoding="utf-8")
docs=loader.load()

prompt_template=ChatPromptTemplate.from_messages(
    [("system","you are a AI that summarizes the content of the text"),
     ("human","{data}")
     ]
)
final_prompt=prompt_template.invoke({"data":docs[0].page_content})
model=ChatMistralAI(model="mistral-small-2603",temperature=0.5)
print(model.invoke(final_prompt).content)