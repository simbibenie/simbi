from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Replace with your actual email credentials (or use environment variables)
SENDER_EMAIL = request.form.get('email') # Your Gmail address
#SENDER_EMAIL = "simbibenie@gmail.com"
SENDER_PASSWORD = "jfxqlyfshuvfraor"
RECEIVER_EMAIL = "simbibenie@gmail.com" # Your recipient email

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        try:
            # Create the email message (to the receiver_me)
            msg = MIMEText(f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\n{message}")
            msg['Subject'] = subject  # Use the subject from the form
            msg['From'] = request.form.get('email')
            msg['To'] = RECEIVER_EMAIL

            # Create a confirmation message (to the sender)
            confirmation_msg = MIMEText("Thank you for your message! I will get back to you soon.")
            confirmation_msg['Subject'] = "Message Received"
            confirmation_msg['From'] = SENDER_EMAIL
            confirmation_msg['To'] = RECEIVER_EMAIL

            # Connect to the SMTP server (Gmail's in this case)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Use SMTP_SSL for secure connection
                server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login
                server.send_message(msg) # Send email

            return redirect(url_for('success'))  # Redirect to a success page
        except Exception as e:
            print(f"Error sending email: {e}") #Print error for debugging
            return render_template('contact.html', error="Error sending message. Please try again.") # Show error on the contact page
            # Handle errors (e.g., display an error message)
            return "Error sending email" # Return to the contact page
    return render_template('contact.html') #Render the contact page


@app.route('success')
def success():
    return render_template('/thx.html')  # Render thx.html template

if __name__ == '__main__':
    app.run(debug=True) # Set debug=False in production