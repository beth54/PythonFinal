from fastapi import APIRouter, Path, HTTPException, status
from model import Commission, CommissionRequest
from typing import Any
from pydantic_settings import BaseSettings, SettingsConfigDict
from beanie import init_beanie, PydanticObjectId
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from bson import ObjectId

commission_router = APIRouter()

commission_list = []
max_id: int = 0

client = MongoClient("mongodb+srv://bnipper54:j4qFSnTKPtxqLxH8@test.bhkjnan.mongodb.net/")
db = client["your-database-name"]
collection = db["your-collection-name"]

@commission_router.post("/commissions", status_code=status.HTTP_201_CREATED)
async def add_commission(commission: CommissionRequest) -> dict:
    # Connect to MongoDB (use your actual connection details)
    clientPost = AsyncIOMotorClient(
        "mongodb+srv://bnipper54:j4qFSnTKPtxqLxH8@test.bhkjnan.mongodb.net/"
    )
    dbPost = clientPost["your-database-name"]
    collectionPost = dbPost["your-collection-name"]

    # Insert the commission into MongoDB
    result = await collectionPost.insert_one(commission.model_dump())
    print(result.inserted_id)
    return {
        "message": "Commission added successfully",
        "item_id": str(result.inserted_id),
    }

@commission_router.get("/commissions", status_code = status.HTTP_201_CREATED)
async def get() -> list:
    try:
        cursor = collection.find({})
        results = []
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            results.append(doc)
        return results
    
    except Exception as e:
        print(f"error fetching data: {e}")
        return None



@commission_router.get("/commissions/{id}")
async def get_commission_by_id(id: int = Path(..., title="default")) -> dict:
    try:
        comm = collection.find_one({})
        results = []
        for doc in comm:
            doc["_id"] = str(doc["_id"])
            print("doc id: ", doc["_id"])
            results.append(doc)
        return results
    except Exception as e:
        print(f"error fetching data: {e}")
        return None

@commission_router.put(    
    "/commissions/{commission_id}", response_description="Update commission by ID"
)
async def update_commission(commission_id: str, updated_commission: CommissionRequest):
    result = await collection.update_one(
        {"_id": ObjectId(commission_id)},
        {"$set": updated_commission.model_dump(exclude_unset=True)},
    )
    if result.modifed_count > 0:
        return {"message": "Commission updated successfully"}
    else:
        raise HTTPException(
            status_code=404, detail=f"Commission with ID {commission_id} not found"
        )


'''
@commission_router.put("/commissions", status_code=status.HTTP_201_CREATED)
async def update_commission(commission: Commission) -> dict:
    clientPost = AsyncIOMotorClient(
        "mongodb+srv://bnipper54:j4qFSnTKPtxqLxH8@test.bhkjnan.mongodb.net/"
    )
    dbPost = clientPost["your-database-name"]
    collectionPost = dbPost["your-collection-name"]

    # Assuming you have an "_id" field in your CommissionRequest
    filter_query = {"id": commission.id}

    # Construct an update document with the fields you want to change
    update_document = {
        "$set": {
            "title": "new_value1",
            "description": "new_value2",
            "status": "new_value1",
            "width": "new_value2",
            "color": "new_value1",
            "date": "new_value2",
        }
    }

    # Update the document based on the filter query
    await collectionPost.update_one(filter_query, update_document)

    return commission

#    for x in commission:
 #       if x.id == id:
 #           x.title = commission.title
  #          x.description = commission.description
  #          x.status = commission.status
  #          x.width = commission.width
  #          x.color = commission.color
  #          x.date = commission.date
  #          return {"message": "Commission updated successfully"}

    return {"message": f"The commission item with ID= is not found."}'''


@commission_router.delete(
    "/commissions/{commission_id}", response_description="Delete commission by ID"
)
async def delete_commission(commission_id: str):
    result = await collection.delete_one({"_id": ObjectId(commission_id)})
    if result.deleted_count > 0:
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(
            status_code=404, detail=f"Commission with ID {commission_id} not found"
        )
