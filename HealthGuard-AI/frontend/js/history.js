// ================================
// HealthGuard-AI - History Page
// ================================

// Check if user is logged in
const user = JSON.parse(localStorage.getItem("user"));

if (!user) {
    alert("Please login first.");
    window.location.href = "login.html";
}

// Load history when page opens
window.addEventListener("DOMContentLoaded", loadHistory);

async function loadHistory() {

    const historyContainer = document.getElementById("historyContainer");

    historyContainer.innerHTML = `
        <div class="loading">
            Loading prediction history...
        </div>
    `;

    try {

        const response = await fetch("http://127.0.0.1:5001/history", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                user_email: user.email
            })

        });

        const history = await response.json();

        if (!response.ok) {
            throw new Error("Unable to fetch history.");
        }

        // No history found
        if (history.length === 0) {

            historyContainer.innerHTML = `
                <div class="no-history">
                    <h2>📭 No Prediction History Found</h2>
                    <p>Make your first prediction from the dashboard.</p>
                </div>
            `;

            return;
        }

        historyContainer.innerHTML = "";

        history.forEach(item => {

            const predictionClass =
                item.prediction === "Diabetic"
                    ? "diabetic"
                    : "healthy";

            const card = document.createElement("div");

            card.className = "history-card";

            card.innerHTML = `

                <div class="card-header">

                    <div class="prediction ${predictionClass}">
                        ${item.prediction}
                    </div>

                    <div class="date">
                        ${formatDate(item.date)}
                    </div>

                </div>

                <div class="card-body">

                    <div class="info-box">
                        <div class="info-title">Confidence</div>
                        <div class="info-value">${item.probability}%</div>
                    </div>

                    <div class="info-box">
                        <div class="info-title">Glucose</div>
                        <div class="info-value">${item.glucose}</div>
                    </div>

                    <div class="info-box">
                        <div class="info-title">BMI</div>
                        <div class="info-value">${item.bmi}</div>
                    </div>

                    <div class="info-box">
                        <div class="info-title">Age</div>
                        <div class="info-value">${item.age}</div>
                    </div>

                </div>

                <div class="progress">

                    <div
                        class="progress-bar"
                        style="width:${item.probability}%">
                    </div>

                </div>

                <div class="confidence">

                    Confidence: ${item.probability}%

                </div>

            `;

            historyContainer.appendChild(card);

        });

    }

    catch (error) {

        console.error(error);

        historyContainer.innerHTML = `
            <div class="no-history">
                <h2>❌ Unable to connect to the server.</h2>
                <p>Please make sure the backend is running.</p>
            </div>
        `;

    }

}

// Format date nicely
function formatDate(dateString) {

    if (!dateString) {
        return "N/A";
    }

    const date = new Date(dateString);

    if (isNaN(date.getTime())) {
        return dateString;
    }

    return date.toLocaleString("en-IN", {
        dateStyle: "medium",
        timeStyle: "short"
    });

}