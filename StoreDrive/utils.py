from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_client(username,email,token):
    token =token
    username = username
    recipient_list = [email]
    subject = f"Verification Code for {username}"
    message = f'''
    Hi {username},

    Your verification code is: {token}

    Please use this code to verify your account.

    The Code Expires in 5 Min 

    
    Thank you!
    '''
    from_email = settings.EMAIL_HOST_USER
    
    send_mail(subject,message, from_email, recipient_list)

