import os
import smtplib
from email.message import EmailMessage


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend?'
msg['From'] = 'tobimesh@gmail.com'
msg['To'] = 'tobi@info-mesh.co.uk'
msg.set_content('How about dinner at 6pm this saturday?')

# added SSL and removed the smtp.ehlo()
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

	# smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	smtp.login("tobimesh@gmail.com", "letmein")

	# smtp.sendmail(SENDER, RECEIVER, msg)

	
	# smtp.sendmail(EMAIL_ADDRESS, 'tobi@info-mesh.co.uk', msg) 
	smtp.send_message(msg)