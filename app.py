from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/workouts")
def workouts():

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


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)