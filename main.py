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

def get_file_name(OUTPUT_PDF, timestamp):
    stampname = f"{timestamp}{OUTPUT_PDF}"
    RANDN = random.randint(100, 999)
    stampname = f"{RANDN}{stampname}"
    return(stampname)


def collate_list(PDF_DIRECTORY):
    """
    Searches directories for .pdf file only and then compiles them into lists
    """
    pdf_files = [os.path.join(PDF_DIRECTORY, filename)
                 for filename in os.listdir(PDF_DIRECTORY) if filename.endswith(".pdf")] 

    # Log message. Note: Add a proper log message.
    print('List collation DONE')
    print(len(pdf_files))
    return(pdf_files)


def compile_pdf(PDF_DIRECTORY, batch_size, pdf_files):
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
    This function is called to write a given set of pdfs
    """
    print(len(batch))
    print(f"{batch}  \n\n")

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
    pdf_list = collate_list(PDF_DIRECTORY)
    compile_pdf(PDF_DIRECTORY, 3, pdf_list)

run()




