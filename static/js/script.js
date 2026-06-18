document.addEventListener(
    "DOMContentLoaded",
    function () {

        const contactForm =
            document.getElementById(
                "contactForm"
            );

        if (contactForm) {

            contactForm.addEventListener(
                "submit",
                function (event) {

                    const message =
                        document.getElementById(
                            "message"
                        );

                    if (
                        message.value.length < 10
                    ) {

                        alert(
                            "Message must contain at least 10 characters."
                        );

                        event.preventDefault();

                    }

                }
            );

        }

    }
);

const workoutChart =
    document.getElementById("workoutChart");

if (workoutChart) {

    new Chart(
        workoutChart,
        {
            type: "bar",

            data: {
                labels: [
                    "Mon",
                    "Tue",
                    "Wed",
                    "Thu",
                    "Fri",
                    "Sat",
                    "Sun"
                ],

                datasets: [
                    {
                        label: "Workouts Completed",
                        data: weeklyWorkouts,
                        backgroundColor: "#101827"
                    }
                ]
            },

            options: {
                responsive: true,

                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        }
    );

}


const bmiButton =
    document.getElementById(
        "calculateBMI"
    );

if (bmiButton) {

    bmiButton.addEventListener(
        "click",
        function () {

            const weight =
                parseFloat(
                    document.getElementById(
                        "weight"
                    ).value
                );

            const height =
                parseFloat(
                    document.getElementById(
                        "height"
                    ).value
                ) / 100;

            if (
                !weight ||
                !height
            ) {

                alert(
                    "Please enter valid values."
                );

                return;

            }

            const bmi =
                weight /
                (
                    height *
                    height
                );

            document.getElementById(
                "bmiResult"
            ).innerText =
                "Your BMI is: " +
                bmi.toFixed(1);

        }
    );

}