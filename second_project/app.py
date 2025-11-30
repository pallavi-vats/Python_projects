from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    user = None
    computer = None

    if request.method == "POST":
        options = ["rock", "paper", "scissor"]
        user = request.form.get("choice")
        computer = random.choice(options)

        if user == computer:
            result = "It's a Tie!"

        elif user == "rock":
            result = "You Win!" if computer == "scissor" else "Computer Wins!"

        elif user == "paper":
            result = "You Win!" if computer == "rock" else "Computer Wins!"

        elif user == "scissor":
            result = "You Win!" if computer == "paper" else "Computer Wins!"

    return render_template("index.html", result=result, user=user, computer=computer)


if __name__ == "__main__":
    app.run(debug=True)
