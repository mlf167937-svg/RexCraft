from flask import Flask, render_template
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")


def read_txt(filename):
    path = os.path.join(STATIC_DIR, filename)

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return f"[ERROR: {filename} tidak ditemukan]"


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


# WAJIB untuk Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
