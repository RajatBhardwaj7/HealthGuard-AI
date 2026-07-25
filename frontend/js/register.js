document.getElementById("registerForm").addEventListener("submit", async function (e) {

    e.preventDefault();

    const message = document.getElementById("message");

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Password Match Check
    if (password !== confirmPassword) {

        message.style.color = "red";
        message.innerHTML = "❌ Passwords do not match.";

        return;
    }

    const data = {

        name: name,
        email: email,
        password: password

    };

    try {

        message.style.color = "black";
        message.innerHTML = "Creating Account...";

        const response = await fetch("http://127.0.0.1:5000/register", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(data)

        });

        const result = await response.json();

        if (response.ok) {

            message.style.color = "green";
            message.innerHTML = "✅ Account Created Successfully!";

            setTimeout(() => {

                window.location.href = "login.html";

            }, 1500);

        }

        else {

            message.style.color = "red";
            message.innerHTML = result.message;

        }

    }

    catch (error) {

        console.error(error);

        message.style.color = "red";
        message.innerHTML = "❌ Cannot connect to server.";

    }

});