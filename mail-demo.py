import os
import smtplib


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
with smtplib.SMTP('localhost', 1025) as smtp:
	# smtp.ehlo()
	# smtp.starttls()
	# smtp.ehlo()

	# smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	# smtp.login("tobbvevh@gmail.com", "letmein")

	subject = 'Grab dinner this weekend?'
	body = 'How about dinner at 6pm this saturday?'

	msg = f'Subject: {subject}\n\n{body}'

	# smtp.sendmail(SENDER, RECEIVER, msg)

	
	# smtp.sendmail(EMAIL_ADDRESS, 'tobi@info-mesh.co.uk', msg) 
	smtp.sendmail('tobimesh@gmail.com', 'tohbodbve@mail.com', msg)
