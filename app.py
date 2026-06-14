from flask import Flask, render_template
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")


def safe_read_txt(filename):
    path = os.path.join(STATIC_DIR, filename)

    if not os.path.exists(path):
        return f"[FILE TIDAK DITEMUKAN: {filename}]"

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return f"[ERROR MEMBACA: {filename}]"


@app.route("/")
def home():
    data_files = [
        ("history1.png", "history1.txt"),
        ("history2.jpg", "history2.txt"),
    ]

    data = []

    for img, txt in data_files:
        data.append({
            "img": img,
            "text": safe_read_txt(txt)
        })

    return render_template("index.html", data=data)


# Render butuh ini
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
