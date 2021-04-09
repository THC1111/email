import smtplib
from email.message import EmailMessage
from string import Template 
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Srishti Arora'
email['to'] = 'srishtiarora6322@gmail.com'
email['subject'] = 'you won 100000 dollars'

email.set_content(html.substitute({'name': 'tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('srishtiarora6322@gmail.com', 'meinlasvegas')
	smtp.send_message(email)
	print('all good dude!')
