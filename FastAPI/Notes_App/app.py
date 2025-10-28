# Run: uvicorn app:app --reload 


from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
app = FastAPI()

# Database setup
MONGO_URI = "mongodb+srv://admin:1234@clustermern.ey7yj.mongodb.net/"
client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database("notes_db")
notes_collection = db.get_collection("notes")

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Helper function for MongoDB ObjectId
def note_helper(note):
    return {"id": str(note["_id"]), "title": note["title"], "content": note["content"]}

# Home page: Display all notes
@app.get("/")
async def read_notes(request: Request):
    notes = await notes_collection.find().to_list(100)
    return templates.TemplateResponse("index.html", {"request": request, "notes": [note_helper(note) for note in notes]})

# Create note: Form page
@app.get("/create/")
async def create_note_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

# Create note: Handle form submission
@app.post("/create/")
async def create_note(title: str = Form(...), content: str = Form(...)):
    note_data = {"title": title, "content": content}
    result = await notes_collection.insert_one(note_data)
    if result.inserted_id:
        return RedirectResponse("/", status_code=303)
    raise HTTPException(status_code=400, detail="Failed to create note")

# View a single note
@app.get("/notes/{note_id}/")
async def read_note(request: Request, note_id: str):
    note = await notes_collection.find_one({"_id": ObjectId(note_id)})
    if note:
        return templates.TemplateResponse("detail.html", {"request": request, "note": note_helper(note)})
    raise HTTPException(status_code=404, detail="Note not found")

# Edit note: Form page
@app.get("/notes/{note_id}/edit/")
async def edit_note_form(request: Request, note_id: str):
    note = await notes_collection.find_one({"_id": ObjectId(note_id)})
    if note:
        return templates.TemplateResponse("edit.html", {"request": request, "note": note_helper(note)})
    raise HTTPException(status_code=404, detail="Note not found")

# Edit note: Handle form submission
@app.post("/notes/{note_id}/edit/")
async def update_note(note_id: str, title: str = Form(...), content: str = Form(...)):
    updated_note = await notes_collection.update_one(
        {"_id": ObjectId(note_id)}, {"$set": {"title": title, "content": content}}
    )
    if updated_note.modified_count:
        return RedirectResponse("/", status_code=303)
    raise HTTPException(status_code=404, detail="Note not found")

# Delete a note
@app.post("/notes/{note_id}/delete/")
async def delete_note(note_id: str):
    result = await notes_collection.delete_one({"_id": ObjectId(note_id)})
    if result.deleted_count:
        return RedirectResponse("/", status_code=303)
    raise HTTPException(status_code=404, detail="Note not found")
