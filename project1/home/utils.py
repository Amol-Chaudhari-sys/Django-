from home.models import student 
import time 
from django.core.mail import send_mail , EmailMessage
from django.conf import settings

def run_this_function():
    print ("Function start executing ............. ")
    time.sleep(5)
    print ("Function end exuction of the function  ")


def send_email_to_client():
    subject= "This mail from Django Server "
    message ="This message from server mail  Django "
    from_email =settings.EMAIL_HOST_USER
    recipients_list = ["amolchaudha@gmail.com"] 
    send_mail (subject , message, from_email , recipients_list )

def send_email_with_attachment(subject , message ,  recipient_list , file_path  ):
    mail = EmailMessage(subject= subject ,body= message , from_email=settings.EMAIL_HOST_USER, to=recipient_list)
    mail.attach_file(file_path)
    mail.send()
    

    