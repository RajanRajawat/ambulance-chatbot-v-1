from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    session_id: str #: If chathistory is to be stored in future, for now the history is being store on running local server only.