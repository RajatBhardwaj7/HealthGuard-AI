const button = document.querySelector("button");

button.addEventListener("click", async () => {


    const inputs = document.querySelectorAll("input");


    const user = JSON.parse(localStorage.getItem("user"));


    if (!user) {

        alert("Please login first.");

        window.location.href = "pages/login.html";

        return;

    }



    const data = {

        user_email: user.email,

        Pregnancies: Number(inputs[0].value),

        Glucose: Number(inputs[1].value),

        BloodPressure: Number(inputs[2].value),

        SkinThickness: Number(inputs[3].value),

        Insulin: Number(inputs[4].value),

        BMI: Number(inputs[5].value),

        DiabetesPedigreeFunction: Number(inputs[6].value),

        Age: Number(inputs[7].value)

    };



    try {


        const response = await fetch(
            "https://healthguard-ai-backend-0xrz.onrender.com/predict",
            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify(data)

            }
        );



        const result = await response.json();



        alert(

            "Prediction: " +

            result.prediction +

            "\nProbability: " +

            result.probability +

            "%"

        );


    } catch (error) {


        console.error(error);


        alert("❌ Cannot connect to backend.");

    }

});