from dotenv import load_dotenv
from pymongo import MongoClient
from models.info import project_name
import os


load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[f"{project_name}_ChatBot"]
collection = db["rag_embeddings"]



#: If RAG / Chat History is to be sotred, this will be needed in future.