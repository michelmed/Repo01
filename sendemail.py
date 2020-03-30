#https://myaccount.google.com/lesssecureapps
#https://petermolnar.net/not-mime-email-python-3/
import smtplib, ssl

smtp_server = "smtp.gmail.com" #"smtp.mail.yahoo.com"
portstartttls = 465 # 587  # For starttls
portssl = 587
sender_email = "username@gmail.com" 
password = "senha" #input("Type your password and press enter: ")

# Create a secure SSL context

var = 'ssl'
receiver_email = 'xxxxx@yahoo.com' 
message ="""From: Nome <username@gmail.com>
To:<xxxx@yahoo.com>
Subject: Email para testar SMTP library

mensagem aqui.

Atenciosamente
"""
# Try to log in to server and send email
context = ssl.create_default_context()
if var == 'tls':
    server = smtplib.SMTP(smtp_server,portstartttls)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    #server.sendmail()
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
elif var == 'ssl':
    #with smtplib.SMTP_SSL(smtp_server, portssl, context=context) as server:
    with smtplib.SMTP(smtp_server, portssl) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.encode("utf8"))

#except Exception as e:
    # Print any error messages to stdout
#   print(e)
#finally:
