from flask import Flask

app = Flask(__name__)

#members API route (change this)

@app.route("/members")
def members():
    return {"members": ["Member1", "member2", "Members3"]}


if __name__ == "__main__":
    app.run(port=8000, debug=True)