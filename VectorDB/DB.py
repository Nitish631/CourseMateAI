from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document
load_dotenv()
docs = [
    Document(
        page_content="Artificial Intelligence is the study of intelligent agents that perceive and act in an environment.",
        metadata={"page": 1, "topic": "AI Introduction"}
    ),
    Document(
        page_content="Machine Learning is a subset of AI that enables systems to learn patterns from data without explicit programming.",
        metadata={"page": 2, "topic": "Machine Learning"}
    ),
    Document(
        page_content="Deep Learning uses neural networks with multiple layers to model complex patterns in data.",
        metadata={"page": 3, "topic": "Deep Learning"}
    ),
    Document(
        page_content="Search algorithms like BFS and DFS are fundamental in AI problem solving and graph traversal.",
        metadata={"page": 4, "topic": "Search Algorithms"}
    ),
    Document(
        page_content="A Constraint Satisfaction Problem involves variables, domains, and constraints that must all be satisfied simultaneously.",
        metadata={"page": 5, "topic": "CSP"}
    )
]
embedding_model=MistralAIEmbeddings()
vectorstore=Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma-db"
)
result=vectorstore.similarity_search("what is machine learning",k=2)
for r in result:
    print(r.page_content)
retriver=vectorstore.as_retriever()
docs=retriver.invoke("Explain machine learning")
print("===============================")
for d in docs:
    print(d.page_content)