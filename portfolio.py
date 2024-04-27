from fastapi import APIRouter, Path, HTTPException, status
from model import Portfolio, PortfolioRequest
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

portfolio_router = APIRouter()

portfolio_list = []
max_id: int = 0

@portfolio_router.post("/portfolios", status_code=status.HTTP_201_CREATED)
async def add_portfolio(portfolio: PortfolioRequest) -> dict:
    client = AsyncIOMotorClient(
        "mongodb+srv://bnipper54:j4qFSnTKPtxqLxH8@test.bhkjnan.mongodb.net/"
    )
    db = client["your-database-name"]
    collection = db["portfolio"]

    result = await collection.insert_one(portfolio.model_dump())
    return {
        "message": "Commission added successfully",
        "item_id": str(result.inserted_id),
    }

@portfolio_router.get("/portfolios")
async def get_portfolio_by_id(id: int = Path(..., title = "default")) -> dict:
    return 0