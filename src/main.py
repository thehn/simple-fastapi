from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# Models
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI!"}


# GET endpoint with path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = Query(None)):
    return {"item_id": item_id, "query": q}


# POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}


# PUT endpoint
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": "Item updated", "item_id": item_id, "item": item}


# DELETE endpoint
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid item ID")
    return {"message": "Item deleted successfully", "item_id": item_id}
