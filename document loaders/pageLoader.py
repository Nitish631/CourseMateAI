from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
import re
load_dotenv()
url="https://www.oic.edu.np/about-us/"
loader=WebBaseLoader(url)
docs=loader.load()
data=re.sub(r"\n+","\n",docs[0].page_content)
print(data)