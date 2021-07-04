from flask_mail import Message
from flask import render_template
from . import mail

from os import getenv

from dotenv import load_dotenv

load_dotenv()


def mail_message(subject, template, to, **kwargs):
    sender_email = getenv('MAIL_USERNAME')

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)
