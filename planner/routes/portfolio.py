import logging
from auth.authenticate import authenticate
from beanie import PydanticObjectId
from database.connection import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.portfolios import Portfolio, PortfolioUpdate

logger = logging.getLogger(__name__)

portfolio_router = APIRouter(tags=["Portfolio"])

portfolio_database = Database(Portfolio)


@portfolio_router.get("/", response_model=list[Portfolio])
async def retrieve_all_portfolio() -> list[Portfolio]:
    portfolio = await portfolio_database.get_all()
    logger.info(f"viewing {len(portfolio)} portfolio")
    return portfolio


@portfolio_router.get("/{id}", response_model=Portfolio)
async def retrieve_event(id: PydanticObjectId) -> Portfolio:
    logger.info(f"viewing portfolio #{id} details.")
    portfolio = await portfolio_database.get(id)
    if not portfolio:
        logger.warning(f"\t The portfolio #{id} NOT Found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    return portfolio


@portfolio_router.post("/new")
async def create_event(body: Portfolio, user: str = Depends(authenticate)) -> dict:
    body.creator = user
    logger.info(f"User [{user}] is creating a portfolio.")
    id = await portfolio_database.save(body)
    logger.info(f"\t A new portfolio #[{id}] created.")
    return {"message": "Portfolio created successfully"}


@portfolio_router.put("/{id}", response_model=Portfolio)
async def update_event(
    id: PydanticObjectId, body: PortfolioUpdate, user: str = Depends(authenticate)
) -> Portfolio:
    logger.info(f"User [{user}] is updating event #{id}.")
    event = await portfolio_database.get(id)
    if not event:
        logger.warning(f"\t The event #{id} NOT Found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Operation not allowed"
        )
    updated_event = await portfolio_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    logger.info(f"\t Event #[{id}] is updated.")
    return updated_event


@portfolio_router.delete("/{id}")
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    logger.info(f"User [{user}] is deleting event #{id}.")
    event = await portfolio_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    if not event:
        logger.warning(f"\t The event #{id} NOT Found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Operation not allowed"
        )
    event = await portfolio_database.delete(id)
    logger.info(f"\t Event #[{id}] is deleted.")
    return {"message": "Event deleted successfully."}
