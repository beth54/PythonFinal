from beanie import Document
from pydantic import BaseModel, ConfigDict, Field

class Portfolio(Document):
    creator: str
    identif: str
    profileImg: str
    img: str
    desc: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "creator": "Beth",
                "identif": "352351145",
                "profileImg": "https://placehold.co/600x400?text=Project+1+Presentation",
                "img": "https://placehold.co/600x400?text=Project+1+Presentation",
                "desc": "Look at this nice picture! Wow, what a picture."
            }
        }
    )

    class Settings:
        name = "portfolios"

class PortfolioUpdate(BaseModel):
    creator: str = ""
    identif: str = ""
    profileImg: str = ""
    img: str = ""
    desc: str = ""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "creator": "Beth",
                "identif": "352351145",
                "profileImg": "https://placehold.co/600x400?text=Project+1+Presentation",
                "img": "https://placehold.co/600x400?text=Project+1+Presentation",
                "desc": "Look at this nice picture! Wow, what a picture."
            }
        }
    )