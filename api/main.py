from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

NOTES = {
        1:"Test 1",
        2: "Test 2"
        }

@app.get("/")
def root():
    return {"status":"Running."}

@app.get("/notes")
def list_notes():
    return NOTES

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/notes/{note_id}")
def read_note(note_id: int):
    if note_id not in NOTES:
        raise HTTPException(status_code=404, detail="Not Found")
    return {"id": note_id, "text": NOTES.get(note_id)}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in NOTES:
        raise HTTPException(status_code=404, detail="Not Found")
    NOTES.pop(note_id)
    return {"message": f"Success. Note {note_id} has been deleted."}

@app.exception_handler(RequestValidationError)
def validation_error(request: Request, exc:RequestValidationError):
    return JSONResponse(status_code=422, content={"detail": "Invalid Request."})
