import PyPDF2
import os
import datetime
import argparse
import random

'''
Todo list:
    - If batch_size doesn't divide pdf_list completely - dump the rest of pdf separately
    either as another batch or single pdf files:
        - Make so that you first do batches regularly and than you do oveflow_pdfs lastly.
        And your list has to be sorted for that to meaningfully work.
    - Organize funcitons.

    - Build argparse options:
        - First choice:
            - Either the full directory to pdf merge Or select particular pdfs.
        - Input options:
            - Batch size. How many pdfs will be merged at a time.
        - Choose the name for output file.
        - Final confirmation menu. Either proceed or repeat above process.

    - Write a settings.py for often used parameters.
    - Wrap the programm in GUM.
'''

current = datetime.datetime.now()
year = current.year
month = current.month
day = current.day
timestamp = f"{year:02d}-{month:02d}-{day:02d}"
PDF_DIRECTORY = "/home/hades/Books/pythonpractice/pdf_combinator/input"
OUTPUT_PDF = "_output.pdf"

def get_file_name(OUTPUT_PDF, timestamp):
    # Adds random three digits and year,month,day before the name.
    stampname = f"{timestamp}{OUTPUT_PDF}"
    RANDN = random.randint(100, 999)
    stampname = f"{RANDN}{stampname}"
    return(stampname)


def collate_list(PDF_DIRECTORY, batch_size):
    """
    Searches directories for .pdf file only and then compiles them into lists
    """
    pdf_files = [os.path.join(PDF_DIRECTORY, filename)
                 for filename in os.listdir(PDF_DIRECTORY) if filename.endswith(".pdf")]

    if len(pdf_files) % batch_size != 0:
        overflow_pdfs = []
        num = len(pdf_files) % batch_size
        while num != 0:
            overflow_pdfs.append(pdf_files[num])
            num-=1
        print(overflow_pdfs)
        write_batch(overflow_pdfs)

    # Log message. Note: Add a proper log message.
    print('List collation DONE')
    return(pdf_files)


def chop_batches(PDF_DIRECTORY, batch_size, pdf_files):
    """
    Compiles a list with pdfs according to batch_size and...
    Note: add pdf-drop if pdf_files is not divisible by batch_size.
    """
    i=0
    batch = []
    for file in pdf_files:
        batch.append(file)
        i+=1

        # If batch size is correct, then we call a write function.
        if i >= batch_size:
            write_batch(batch)
            batch.clear()
            i=0


def write_batch(batch):
    """
    This function is called to write a given set of pdfs.
    You call it once per list of pdfs that you want to merge.
    """

    # Get a special name for new file and declare a MERGE function.
    file_name = get_file_name(OUTPUT_PDF, timestamp)
    MERGE = PyPDF2.PdfMerger()

    # Append files from batch into PyPDF.FileMerge()
    for batch_singles in batch:
        MERGE.append(batch_singles)

    # Write down batch.
    with open(file_name, "wb") as output:
        MERGE.write(output)
    MERGE.close()

    # Note: Add log message here.

def run():
    pdf_list = collate_list(PDF_DIRECTORY, 3)
    chop_batches(PDF_DIRECTORY, 3, pdf_list)

run()
