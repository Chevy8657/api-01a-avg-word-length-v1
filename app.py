from fastapi import FastAPI, Query
from pydantic import BaseModel
import re

app = FastAPI(title="Average Word Length", version="v1")

class Health(BaseModel):
    ok: bool

class AvgWordLengthResponse(BaseModel):
    input: str
    average_word_length: float

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/avg-word-length", response_model=AvgWordLengthResponse)
def avg_word_length(text: str = Query(..., description="Text to calculate average word length")):
    words = re.findall(r"\S+", text)
    if not words:
        avg = 0.0
    else:
        total = sum(len(w) for w in words)
        avg = total / len(words)
    return {"input": text, "average_word_length": avg}
