from django.core.mail import EmailMultiAlternatives # will be responsible for sending the emails
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Warm Welcome'
    sender = 'kangabejuliette@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/email.txt',{"name": name})
    html_content = render_to_string('email/email.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
    