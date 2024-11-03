from fastapi import FastAPI

from .find_words import find_words
from pathlib import Path

HERE = Path(__file__).parent

app = FastAPI()


@app.get("/")
def index():
    return {"status": "fastapi server is running."}


@app.get("/words-from/{chars}")
def words(chars: str):
    with open(f"{HERE}/russian_nouns.txt", "r", encoding="utf8") as file:
        line = file.read(1).split()
        found_words = find_words(chars, file)
        return {"found_words": found_words, "line": line}
