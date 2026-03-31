from fastapi import FastAPI
from models.models import ChatRequest
from chatbot import ask_bot
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

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
    try:
        response = ask_bot(req.message, req.session_id)

        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "response": response
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(e)
            }
        )