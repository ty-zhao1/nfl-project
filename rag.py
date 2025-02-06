from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import argparse

args = argparse.ArgumentParser()
args.add_argument('--query', type=str, default = "How is the game clock managed?")

args = args.parse_args()

query = args.query

os.environ["OPENAI_API_KEY"] = # TODO: Add your OpenAI API key here

llm = ChatOpenAI(model="gpt-4o-mini")

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

text = PyPDFLoader("2024-nfl-rulebook.pdf").load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)

splits = text_splitter.split_documents(text)

db_chroma = Chroma.from_documents(splits, embeddings, persist_directory="nfl_rulebook_chroma")

retriever = db_chroma.as_retriever(search_kwargs={"k": 5})

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(), 
    chain_type="stuff",  # simplest type
    retriever=retriever
)

result = qa_chain.invoke(query)
print(result['result'])