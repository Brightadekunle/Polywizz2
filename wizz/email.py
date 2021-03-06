from threading import Thread
from flask_mail import Message
from flask import current_app, render_template
from wizz import mail


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(current_app.config['INSTAGRAM_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=current_app.config['INSTAGRAM_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
    # thr = Thread(target=send_async_mail, args=[app, msg])
    # thr.start()
    # return thr
