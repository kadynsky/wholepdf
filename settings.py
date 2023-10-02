import datetime


current = datetime.datetime.now()
year = current.year
month = current.month
day = current.day
timestamp = f"{year:02d}-{month:02d}-{day:02d}"
PDF_DIRECTORY = "./input"
OUTPUT_PDF = "_output.pdf"

