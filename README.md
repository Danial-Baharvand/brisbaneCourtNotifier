# brisbaneCourtNotifier
A simple script designed to notify the user via email when they are expected to apear in Brisbane court.

The script is setup on the Google cloud to run every day at 6:02 and scan the PDF released of the names expected to apear in court the next day.
the PDF is reformated into tables using tabula library and searched for the name. The script has the capibility to send emails from gmail or other mail services.
Note: Google will stop letting third party applications to send mail with only the username and password starting from May 2022.
