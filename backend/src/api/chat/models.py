from sqlmodel import SQLModel, Field

class ChatMessagePayload(SQLModel):
    # for validation and serialization
    message: str

class ChatMessage(SQLModel, table=True):
    # db table
    id: int | None = Field(default=None, primary_key=True)
    message:str


