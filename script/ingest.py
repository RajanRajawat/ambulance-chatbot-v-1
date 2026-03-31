from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from db.database import collection

#One time Run!

load_dotenv()

loader = TextLoader("data\about.txt", encoding="utf-8") #!update path
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      
    chunk_overlap=50,)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = MongoDBAtlasVectorSearch.from_documents(
    documents=chunks,            
    embedding=embeddings,    
    collection=collection,      
    index_name="vector_index_wl"   #!update vector index name 
)

print("Chunks embedded and stored in MongoDB!")