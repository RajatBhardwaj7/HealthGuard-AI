document.getElementById("predictionForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const resultDiv = document.getElementById("result");
    resultDiv.style.display = "block";
    resultDiv.innerHTML = "<h2>⏳ Predicting...</h2>";

    const data = {
        Pregnancies: Number(document.getElementById("Pregnancies").value),
        Glucose: Number(document.getElementById("Glucose").value),
        BloodPressure: Number(document.getElementById("BloodPressure").value),
        SkinThickness: Number(document.getElementById("SkinThickness").value),
        Insulin: Number(document.getElementById("Insulin").value),
        BMI: Number(document.getElementById("BMI").value),
        DiabetesPedigreeFunction: Number(document.getElementById("DiabetesPedigreeFunction").value),
        Age: Number(document.getElementById("Age").value)
    };

    try {

        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        let recommendations = "";

        if (result.prediction === "Diabetic") {

            recommendations = `
                <h3>🔴 Health Recommendations</h3>

                <ul>
                    <li>Consult a healthcare professional as soon as possible.</li>
                    <li>Reduce sugar and processed food intake.</li>
                    <li>Exercise for at least 30 minutes daily.</li>
                    <li>Monitor your blood glucose regularly.</li>
                    <li>Drink plenty of water.</li>
                    <li>Sleep 7–8 hours every night.</li>
                </ul>
            `;

        } else {

            recommendations = `
                <h3>🟢 Healthy Lifestyle Tips</h3>

                <ul>
                    <li>Maintain a balanced and nutritious diet.</li>
                    <li>Exercise regularly.</li>
                    <li>Maintain a healthy body weight.</li>
                    <li>Stay hydrated.</li>
                    <li>Get regular medical checkups.</li>
                    <li>Avoid excessive sugary drinks and junk food.</li>
                </ul>
            `;

        }

        resultDiv.innerHTML = `
            <h2>${result.prediction}</h2>

            <p><strong>Confidence:</strong> ${result.probability}%</p>

            <div class="progress">
                <div class="progress-bar" id="progressBar"></div>
            </div>

            <p>${result.probability}% Confidence</p>

            ${recommendations}
        `;

        document.getElementById("progressBar").style.width = result.probability + "%";

    } catch (error) {

        console.error(error);

        resultDiv.innerHTML = `
            <h2 style="color:red;">❌ Cannot connect to backend.</h2>
        `;
    }
});