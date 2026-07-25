const button = document.querySelector("button");

button.addEventListener("click", async () => {

    const inputs = document.querySelectorAll("input");

    const data = {
        Pregnancies: Number(inputs[0].value),
        Glucose: Number(inputs[1].value),
        BloodPressure: Number(inputs[2].value),
        SkinThickness: Number(inputs[3].value),
        Insulin: Number(inputs[4].value),
        BMI: Number(inputs[5].value),
        DiabetesPedigreeFunction: Number(inputs[6].value),
        Age: Number(inputs[7].value)
    };

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    alert(
        "Prediction: " +
        result.prediction +
        "\nProbability: " +
        result.probability +
        "%"
    );
});