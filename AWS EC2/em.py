import smtplib
from email.mime.text import MIMEText

def email_sender(to_email, theme, message):
    sender = "andallarmy007@gmail.com"
    password = "mzkhjprmrzutezsn"
    body = message
    # make up message
    msg = MIMEText(body)
    msg['Subject'] = theme
    msg['From'] = sender
    msg['To'] = ", ".join(to_email)
    #sending
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender, password)
    send_it = session.sendmail(sender, to_email, msg.as_string())
    session.quit()
