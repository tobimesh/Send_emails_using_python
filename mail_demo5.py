import os
import smtplib
from email.message import EmailMessage
import imghdr


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['tobi@info-mesh.co.uk', 'tobimesh@yaho.com']

msg = EmailMessage()
msg['Subject'] = 'Check out the network topolgy'
msg['From'] = 'tobimesh@gmail.com'
msg['To'] = contacts
msg.set_content('Image attached...')


files = ['resume.pdf']

for file in files:

	with open(file, 'rb') as f:
		file_data = f.read()
		file_name = f.name
	
	msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# # added SSL and removed the smtp.ehlo()
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

	# smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	smtp.login("tobimesh@gmail.com", "letmein")

	# smtp.sendmail(SENDER, RECEIVER, msg)

	
	# smtp.sendmail(EMAIL_ADDRESS, 'tobi@info-mesh.co.uk', msg) 
	smtp.send_message(msg)