from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

# 📥 正确读取 shared/Toadgod-tweets.txt
LORE_PATH = os.path.join(os.path.dirname(__file__), "..", "shared", "Toadgod-tweets.txt")
with open(LORE_PATH, "r", encoding="utf-8") as f:
    lore_data = f.read().splitlines()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/learn")
def learn():
    return render_template("learn.html", lore_data=lore_data[:500])

@app.route("/random")
def random_lore():
    line = random.choice(lore_data)
    return render_template("random.html", random_line=line)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = []
    if query:
        results = [line for line in lore_data if query.lower() in line.lower()]
    return render_template("search.html", query=query, results=results)

@app.route("/explore")
def explore():
    line = random.choice(lore_data)
    return render_template("explore.html", line=line)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"✅ Lore Guardian Web running on port {port}")
    app.run(host="0.0.0.0", port=port)
