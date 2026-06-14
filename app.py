from flask import Flask, render_template
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_txt(filename):
    try:
        path = os.path.join(BASE_DIR, "static", filename)
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"[ERROR LOAD TXT: {filename}]"

@app.route("/")
def home():
    data = [
        {
            "img": "history1.png",
            "text": read_txt("history1.txt")
        },
        {
            "img": "history2.jpg",
            "text": read_txt("history2.txt")
        }
    ]
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()
