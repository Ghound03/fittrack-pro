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