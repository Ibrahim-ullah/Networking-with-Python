import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  #connecting to the server
server.ehlo()  #starting the server
server.login('sender@gmail.com',123456789)  #sender's email address and password


#reading the main body's message and attaching it to the email
msg = MIMEMultipart()
msg['From'] = 'Emon'
msg['To'] = 'receiver@gmail.com' #receiver's gmail address
msg['subject'] = "just a test"
with open('J:\\file\\python\\networking_python\\message.txt','r') as f:
    message = f.read()
msg.attach(MIMEText(message,'plain')) 


#attaching a image to the body
filename = 'J:\\file\\python\\networking_python\\image.jpg'
attachment = open(filename, 'rb')
p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')
msg.attach(p)


text = msg.as_string()
server.sendmail('sender@gmail.com','receiver@gmail.com', text)
server.quit()