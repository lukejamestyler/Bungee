from django.core.mail import EmailMessage

from django.template.loader import get_template

def contact_send_email(name, email, amessage):
    context = {

    'name': name,

    'email': email,

    'subject': "Form Submission",

    'amessage': amessage,

    }

    cfrom = 'Luketyler.business@gmail.com'
    subject = "Form Submission"
    to = [email]
    #pass context to template

    message = get_template('contact-email.html').render(context)

    msg = EmailMessage(subject, message, cfrom, to)

    msg.content_subtype = "html"

    msg.send()