
class Settings():

    def __init__(self):
        self.current = datetime.datetime.now()
        year = current.year
        month = current.month
        day = current.day
        self.timestamp = f"{year:02d}-{month:02d}-{day:02d}"
        self.PDF_DIRECTORY = "./input"
        self.OUTPUT_PDF = "_output.pdf"
