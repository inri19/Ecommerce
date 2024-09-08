from email.message import EmailMessage
import ssl 
import smtplib

def envoyer_email(email_send, subject, content, email_receive):

	email_sender = email_send
	email_password = "ujvq jqtg ohnt gybr"
	email_receiver = email_receive # "andresmotoha1995@gmail.com"

	subject = subject
	body = content

	em = EmailMessage()
	em["From"] = email_sender
	em["To"] = email_receiver
	em["Subject"] = subject
	em.set_content(body)

	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp :

		smtp.login(email_sender, email_password)
		smtp.sendmail(email_sender, email_receiver, em.as_string())