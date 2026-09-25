from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.db import get_session
from .models import ChatMessagePayload, ChatMessage

router = APIRouter()

@router.get("/")
def chat_health():
    return {"status": "ok"}


# HTTP POST -> payload = {"message": "hello world"} -> {"message": "hello world", "id": 1}
@router.post("/", response_model=ChatMessage)
def chat_create_message(
    payload:ChatMessagePayload,
    session:Session = Depends(get_session)
    ):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    # ready to save to db
    session.add(obj)
    session.commit()
    session.refresh(obj) # ensures id is added to the object
    return obj