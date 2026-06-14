from flask import Flask, render_template
import os

app = Flask(__name__)

def read_txt(filename):
    path = os.path.join("static", filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Teks belum tersedia."

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
    app.run(host="0.0.0.0", port=5000, debug=True)
