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