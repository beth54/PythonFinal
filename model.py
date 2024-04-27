from pydantic import BaseModel, ConfigDict, EmailStr, Field
from beanie import Document


class Commission(BaseModel):
    id: int
    title: str
    description: str
    status: str
    width: str
    color: str
    date: str


class CommissionRequest(BaseModel):
    title: str
    description: str
    status: str
    width: str
    color: str
    date: str

class Portfolio(BaseModel):
    _id: str
    creator: str
    image: str
    description: str

class PortfolioRequest(BaseModel):
    _id: str
    creator: str
    image: str
    description:str

class User(Document):
    email: EmailStr = ""
    password: str = ""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"email": "python-web-dev@cs.uiowa.edu", "password": "strong!!!"}
        }
    )

    class Settings:
        name = "users"

