from flask import Flask, session, redirect, render_template
app = Flask(__name__)
app.secret_key = "Graaahfgsbl"

@app.route("/")
def index():
    session.setdefault("viewed", 0)
    session["viewed"] += 1
    return render_template("index.html", count=session["viewed"])
@app.route("/add")
def add():
    session["viewed"] += 1
    return redirect("/")
@app.route("/reset")
def reset():
    session["viewed"] = 0
    return redirect("/")

app.run(debug=True)