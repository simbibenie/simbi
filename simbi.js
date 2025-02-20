document.getElementById('message').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form values
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var subject = document.getElementById('subject').value;
    var message = document.getElementById('message').value;

    // Construct the email body
    var emailBody = `
        Name: ${name}
        Email: ${email}
        Subject: ${subject}
        Message: ${message}
    `;

// Send form data to Flask app using fetch API
fetch('/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ 
        name: name,
        email: email,
        subject: subject,
        message: message
    })
})
.then(response => {
    if (response.ok) {
        // Redirect to thank you page
        window.location.href = "thx.html"; 
    } else {
        // Handle errors (e.g., display an error message)
        alert("Error sending message. Please try again."); 
    }
})
.catch(error => {
    console.error('Error:', error);
    alert("Error sending message. Please try again.");
});
});