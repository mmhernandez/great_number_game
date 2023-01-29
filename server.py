from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Fr6MWc5GF2nw5sKgg3YX"

@app.route("/")
def index():
    if not "random_num" in session:
        session["random_num"] = random.randint(1,100)
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    session["guess"] = request.form["guessed_number"]
    if "count_guesses" in session:
        if session["count_guesses"] < 4:
            session["count_guesses"] += 1
        else:
            session["count_guesses"] += 1
            session["status"] = "game_over"
    else:
        session["count_guesses"] = 1
    return redirect ("/")

@app.route("/clear_session", methods=["POST"])
def clear():
    if session["random_num"]:
        session.pop("random_num")
        if session["guess"]:
            session.pop("guess")
            if session["status"]:
                session.pop("status")
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
