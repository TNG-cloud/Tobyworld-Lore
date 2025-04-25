from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

with open(os.path.join("shared", "Toadgod-tweets.txt"), "r", encoding="utf-8") as f:
    lore_data = f.read().splitlines()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/learn")
def learn():
    return render_template("learn.html", lore_data=lore_data[:500])

@app.route("/random")
def random_lore():
    random_line = random.choice(lore_data)
    return render_template("random.html", random_line=random_line)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = []
    if query:
        results = [line for line in lore_data if query.lower() in line.lower()]
    return render_template("search.html", query=query, results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

