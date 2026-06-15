from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = "fittrack-secret-key"

workout_list = [

    {
        "name": "Push Day",
        "duration": 60,
        "calories": 450
    },

    {
        "name": "Leg Day",
        "duration": 75,
        "calories": 650
    },

    {
        "name": "Cardio Session",
        "duration": 45,
        "calories": 500
    }

]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/workouts", methods=["GET", "POST"])
def workouts():

    if request.method == "POST":

        workout_name = request.form.get("name")

        duration = request.form.get("duration")

        calories = request.form.get("calories")

        workout_list.append(
            {
                "name": workout_name,
                "duration": duration,
                "calories": calories
            }
        )

    return render_template(
        "workouts.html",
        workouts=workout_list
    )


@app.route("/goals")
def goals():

    goals = [

        {
            "goal": "Lose 5kg",
            "status": "In Progress"
        },

        {
            "goal": "Run 10km",
            "status": "Completed"
        },

        {
            "goal": "Workout 4 times weekly",
            "status": "Active"
        }

    ]

    return render_template(
        "goals.html",
        goals=goals
    )


@app.route("/progress")
def progress():

    stats = {

        "workouts_completed": 48,
        "current_weight": 82,
        "target_weight": 75,
        "goals_completed": 7

    }

    return render_template(
        "progress.html",
        stats=stats
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        flash(
            f"Thank you {name}, your message has been received!"
        )

        return redirect(
            url_for("contact")
        )

    return render_template(
        "contact.html"
    )


if __name__ == "__main__":
    app.run(debug=True)