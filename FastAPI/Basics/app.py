# pip install fastapi uvicorn motor pydantic

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

# MongoDB Connection
MONGO_URI = "mongodb+srv://admin:1234@clustermern.ey7yj.mongodb.net/"
client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database("fastapi_db")  # Database name
collection = db.get_collection("items")  # Collection name

# Pydantic Model
class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

@app.on_event("startup")
async def startup_db_client():
    print("Connected to MongoDB!")

@app.on_event("shutdown")
async def shutdown_db_client():
    await client.close()
    print("Disconnected from MongoDB.")

# Create Item
@app.post("/items/", response_model=dict)
async def create_item(item: Item):
    item_data = item.dict()
    result = await collection.insert_one(item_data)
    if result.inserted_id:
        return {"id": str(result.inserted_id), "message": "Item created successfully"}
    raise HTTPException(status_code=400, detail="Item creation failed")

# Read All Items
@app.get("/items/", response_model=list)
async def get_items():
    items = await collection.find().to_list(100)  # Fetch up to 100 items
    return items

# Read Single Item
@app.get("/items/{item_id}")
async def get_item(item_id: str):
    item = await collection.find_one({"_id": item_id})
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

# Update Item
@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    updated_item = await collection.update_one(
        {"_id": item_id}, {"$set": item.dict()}
    )
    if updated_item.modified_count:
        return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# Delete Item
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = await collection.delete_one({"_id": item_id})
    if result.deleted_count:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")


# # pip install fastapi jinja2 uvicorn motor pydantic python-multipart

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from motor.motor_asyncio import AsyncIOMotorClient
# from bson import ObjectId
# import os

# app = FastAPI()

# # MongoDB Connection
# MONGO_URI = "your_mongodb_atlas_connection_string_here"  # Replace with your connection string
# client = AsyncIOMotorClient(MONGO_URI)
# db = client.get_database("notes_db")  # Database name
# notes_collection = db.get_collection("notes")  # Collection name

# # Pydantic Model for Notes
# class Note(BaseModel):
#     title: str
#     content: str

# # Helper Function to Convert MongoDB ObjectId to String
# def note_helper(note):
#     return {"id": str(note["_id"]), "title": note["title"], "content": note["content"]}

# # Startup and Shutdown Events
# @app.on_event("startup")
# async def startup_db_client():
#     print("Connected to MongoDB!")

# @app.on_event("shutdown")
# async def shutdown_db_client():
#     await client.close()
#     print("Disconnected from MongoDB.")

# # Create a New Note
# @app.post("/notes/", response_model=dict)
# async def create_note(note: Note):
#     note_data = note.dict()
#     result = await notes_collection.insert_one(note_data)
#     if result.inserted_id:
#         return {"id": str(result.inserted_id), "message": "Note created successfully"}
#     raise HTTPException(status_code=400, detail="Failed to create note")

# # Get All Notes
# @app.get("/notes/", response_model=list)
# async def get_notes():
#     notes = await notes_collection.find().to_list(100)
#     return [note_helper(note) for note in notes]

# # Get a Single Note by ID
# @app.get("/notes/{note_id}", response_model=dict)
# async def get_note(note_id: str):
#     note = await notes_collection.find_one({"_id": ObjectId(note_id)})
#     if note:
#         return note_helper(note)
#     raise HTTPException(status_code=404, detail="Note not found")

# # Update a Note by ID
# @app.put("/notes/{note_id}", response_model=dict)
# async def update_note(note_id: str, note: Note):
#     updated_note = await notes_collection.update_one(
#         {"_id": ObjectId(note_id)}, {"$set": note.dict()}
#     )
#     if updated_note.modified_count:
#         return {"message": "Note updated successfully"}
#     raise HTTPException(status_code=404, detail="Note not found")

# # Delete a Note by ID
# @app.delete("/notes/{note_id}", response_model=dict)
# async def delete_note(note_id: str):
#     result = await notes_collection.delete_one({"_id": ObjectId(note_id)})
#     if result.deleted_count:
#         return {"message": "Note deleted successfully"}
#     raise HTTPException(status_code=404, detail="Note not found")