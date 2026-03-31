from pydantic import BaseModel , Field, field_validator

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)
    session_id: str = Field(default="admin", min_length=1, max_length=50) #: If chathistory is to be stored in future, for now the history is being store on running local server only.

    
    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str):
        value = value.strip()

        if not value:
            raise ValueError("Message cannot be empty")

        return value

    @field_validator("session_id")
    @classmethod
    def validate_session_id(cls, value: str):
        value = value.strip()

        if not value:
            return "admin" 

        return value