from fastapi import FastAPI
from models.models import ChatRequest
from chatbot import ask_bot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(req: ChatRequest):
    response = ask_bot(req.message, req.session_id)
    return {"response": response}