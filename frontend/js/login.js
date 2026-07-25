document.getElementById("loginForm").addEventListener("submit", async function (e) {

    e.preventDefault();

    const message = document.getElementById("message");

    message.style.color = "black";
    message.innerHTML = "Logging in...";

    const data = {

        email: document.getElementById("email").value,

        password: document.getElementById("password").value

    };

    try {

        const response = await fetch("http://127.0.0.1:5001/login", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(data)

        });

        const result = await response.json();

        if (response.ok) {

            message.style.color = "green";

            message.innerHTML = "✅ Login Successful";

            // Save user in browser
            localStorage.setItem("user", JSON.stringify(result.user));

            // Redirect after 1 second
            setTimeout(() => {

                window.location.href = "../index.html";

            }, 1000);

        } else {

            message.style.color = "red";

            message.innerHTML = result.message;

        }

    } catch (error) {

        console.error(error);

        message.style.color = "red";

        message.innerHTML = "❌ Cannot connect to server.";

    }

});