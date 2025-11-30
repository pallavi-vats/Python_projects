from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    amount_per_person = None

    if request.method == "POST":
        rent = int(request.form["rent"])
        food = int(request.form["food"])
        bijli = int(request.form["bijli"])
        persons = int(request.form["persons"])

        total = rent + food + bijli
        amount_per_person = total // persons

    return render_template("index.html", result=amount_per_person)


if __name__ == "__main__":
    app.run(debug=True)
