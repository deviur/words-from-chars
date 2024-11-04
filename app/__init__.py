from flask import Flask

from .find_words import find_words
from pathlib import Path

HERE = Path(__file__).parent

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return {"status": "fastapi server is running."}


@app.route("/words-from/<chars>", methods=["GET"])
def words(chars: str):
    with open(f"{HERE}/russian_nouns.txt", "r", encoding="utf8") as file:
        found_words = find_words(chars, file)
        return str({"found_words": found_words})
