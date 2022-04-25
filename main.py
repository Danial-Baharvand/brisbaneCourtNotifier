# -----Imported Functions---------------------------------------------#
#
# Below are various import statements that are used in the script
#
# Import the function for opening online documents
from urllib.request import urlopen
#
# Import library for reading tables from PDF files
from tabula import read_pdf
#
# Import library for sending emails
import smtplib, ssl
from email import message
#
# -----Options--------------------------------------------------------#
#
# Name to be searched on Brisbane court notice
searchWord = "Name"
#
# The address of the document to be searched
pdf_url = "https://www.courts.qld.gov.au/__external/CourtsLawList/BrisbaneMagCourt.pdf"
# pdf_url = "https://danialvand.com/wp-content/uploads/2022/04/namesLocal.pdf"
#
# --------------------------------------------------------------------#


def send_mail_gmail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "senderMail@gmail.com"  # Where the email is going to be sent from
    receiver_email = "receiverMail@gmail.com"  # Where the email is going to be received
    password = "yourPassword"
    message = """\
    Subject: Brisbane court alert

    A new match has been found."""
    # Create SSL connection
    context = ssl.create_default_context()
    # Initiate the SMTP server
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        # send the e-mail
        server.sendmail(sender_email, receiver_email, message)


def send_mail(body):
    # Email options
    from_addr = 'brisbanecourtalert@danialvand.com'
    to_addr = 'dbdpcg@gmail.com'
    subject = 'Alert from Brisbane court'
    msg = message.Message()
    msg.add_header('from', from_addr)
    msg.add_header('to', to_addr)
    msg.add_header('subject', subject)
    msg.set_payload(body)
    server = smtplib.SMTP('smtp.dreamhost.com', 587)
    server.login(from_addr, 'Password')
    server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])


# Open the PDF from URL
tables = read_pdf(urlopen(pdf_url), pages="all")
# Store if a match was found
matchFound = False
# Looping through all tables
for table in tables:
    if 'Matter' in table:   # Names are stored in the 'Matter' column
        for name in table['Matter']:
            if isinstance(name, str):
                if searchWord in name:
                    print("Found a match!")
                    matchFound = True
                    send_mail('A new match has been found.')
if not matchFound:
    print("No matches found!")
    send_mail('No matches found!')

