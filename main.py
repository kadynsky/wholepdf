import PyPDF2
import os
import datetime
import argparse
import random

# Compile a list of pdf files
# Compiles related files into one (or more)
# Saves compiled version into .

current = datetime.datetime.now()
year = current.year
month = current.month
day = current.day
timestamp = f"{year:02d}-{month:02d}-{day:02d}"
PDF_DIRECTORY = "/home/hades/Books/pythonpractice/pdf_combinator/input"
OUTPUT_PDF = "_output.pdf"


def collate_list(PDF_DIRECTORY):
    """
    Searches directories for .pdf file only and then compiles them into lists
    """
    pdf_files = [os.path.join(PDF_DIRECTORY, filename)
                 for filename in os.listdir(PDF_DIRECTORY) if filename.endswith(".pdf")] 
    print('List collation DONE')
    return(pdf_files)


def compile_pdf(PDF_DIRECTORY, batch_size, pdf_files):
    """
    Compiles each list with pdfs into pdf file
    """
    i=0
    print(pdf_files)
    while pdf_files:
        stampname = f"{timestamp}{OUTPUT_PDF}"
        for file in pdf_files:
            MERGE = PyPDF2.PdfMerger()
            MERGE.append(file)
            pdf_files.remove(file)
            i+=1
            if i >= batch_size:
                RANDN = random.randint(100, 999)
                stampname = f"{RANDN}{stampname}"
                with open(stampname, "wb") as output:
                    MERGE.write(output)

                MERGE.close()
            #print(f"PDF files in {PDF_DIRECTORY} have been compiled into {stampname} file.")

#def save_pdf(filename, pdf_object):
    #if isinstane(pdf_object, PyPDF2.File

def run():
    pdf_list = collate_list(PDF_DIRECTORY)
    compile_pdf(PDF_DIRECTORY, 5, pdf_list)

run()




