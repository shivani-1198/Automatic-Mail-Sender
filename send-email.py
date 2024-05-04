# impo 
import ssl
import smtplib
from email.message import EmailMessage

email_sender = "agarwalshivani10411@gmail.com"
email_password = "my_password_was_here"
email_receiver = "shivaniag1112@gmail.com"


subject = "Check out my auto mail sender code"

body = "Hello this is my first time trying to do this. Please work for me."

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()  # Secure the connection
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())