from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/workouts")
def workouts():
    return render_template("workouts.html")


@app.route("/goals")
def goals():
    return render_template("goals.html")


@app.route("/progress")
def progress():
    return render_template("progress.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)