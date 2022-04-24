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
#
# -----Options--------------------------------------------------------#
#
# Name to be searched on Brisbane court notice
searchWord = "Search Name"
#
# The address of the document to be searched
pdf_path = "https://www.courts.qld.gov.au/__external/CourtsLawList/BrisbaneMagCourt.pdf"
#
# Name of the saved file
fileName = "names"
# --------------------------------------------------------------------#

def send_mail():
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


def download_file(download_url, filename):
    # Download a PDF file from a URL and store it on storage
    response = urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()




download_file(pdf_path, fileName)
tables = read_pdf(fileName, pages="all")
for table in tables:
    if 'Matter' in table:
        for name in table['Matter']:
            if isinstance(name, str):
                if searchWord in name:
                    print("Found a match!")
                    send_mail()

