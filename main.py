# -----Imported Functions---------------------------------------------#
#
# Below are various import statements that are used in the script
#
# Import the function for opening online documents

from urllib.request import urlopen
# import library for reading tables from PDF files

from tabula import read_pdf, convert_into
from tabulate import tabulate


#import camelot

from tabulate import tabulate
# --------------------------------------------------------------------#



def download_file(download_url, filename):
    response = urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()


def extractInfo (srcPath, destPath): # Extracts info from a file at the given file path
    tables = read_pdf(srcPath, pages="all")
    # convert_into(srcPath, destPath)
    return tables


searchWord = "Abdi"
pdf_path = "https://www.courts.qld.gov.au/__external/CourtsLawList/BrisbaneMagCourt.pdf"
download_file(pdf_path, "names")
tables = read_pdf('namesLocal.pdf', pages="all")
for table in tables:
    if 'Matter' in table:
        for name in table['Matter']:
            print(name)
            if isinstance(name, str):
                if searchWord in name:
                    print("yes")

