import PyPDF2
import os
import datetime
import argparse
import random
from settings import Settings

'''
Todo list:
    [DONE] If batch_size doesn't divide pdf_list completely - dump the rest of pdf separately
    either as another batch or single pdf files:
        [DONE] Make so that you first do batches regularly and than you do oveflow_pdfs lastly.
        And your list has to be sorted for that to meaningfully work.
    - Organize functions.

    - Build argparse options:
        - First choice:
            - [STUPID IDEA] Either the full directory to pdf merge Or select particular pdfs.
            - [PARTLY] Add an option to change directory temp
                - Do it after adding settings.py
        - [DONE] Input options:
            - [DONE] Batch size. How many pdfs will be merged at a time.
        - Choose the name for output file.
        - Final confirmation menu. Either proceed or repeat above process.

    - Write a settings.py for constants. 
    - Wrap the programm in GUM.
'''

current = datetime.datetime.now()
year = current.year
month = current.month
day = current.day
timestamp = f"{year:02d}-{month:02d}-{day:02d}"
PDF_DIRECTORY = "./input"
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
    # Sort the list from Z to A
    pdf_files.sort()

    pdf_files = deal_with_overflow(pdf_files, batch_size)

    # Log message. Note: Add a proper log message.
    print('List collation DONE')
    return(pdf_files)


def deal_with_overflow(pdf_files, batch_size):
    """ 
    Receives complete list of pdfs, counts  pdfs that don't fit into 
    specified batch_size, adds them to a new list, converts it into pdf(overflow batch)
    """ 
    if len(pdf_files) % batch_size != 0:
        overflow_pdfs = []
        num = len(pdf_files) % batch_size
        while num != 0:
            overflow_pdfs.append(pdf_files.pop())
            num-=1
        write_batch(overflow_pdfs)
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


def run(batch_size=1, print_table=None, output_name=None,
        file_start=None, file_end=None,):

    #Print out the whole input directory insides in a table view
    if print_table:
        pdf_list = collate_list(PDF_DIRECTORY, batch_size)

        print('INDEX | FILE_NAME ')
        TEMPLATE = '{index:>5} | {file_name}'

        index = 1 
        for file_name in pdf_list:
            row = TEMPLATE.format(index=index, file_name=file_name)
            print(row)
            index+=1

            #Dividing table to see batches more clearly.
            if index % batch_size == 0:
                print('\n\tNew batch:')

    pdf_list = collate_list(PDF_DIRECTORY, batch_size)
    chop_batches(PDF_DIRECTORY, batch_size, pdf_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('number', type=int, help='The number')
    parser.add_argument('-input', action='store_true', help='View inside input directory.')
    parser.add_argument('-dir', type=str, help="Paste temp directory path if you'd like")
    parser.add_argument('-n', type=str, help='Choose a name for your output batches')
    parser.add_argument('-start', type=int, help='Starting pdf file')
    parser.add_argument('-end', type=int, help='Ending pdf file')

    args = parser.parse_args()
    run(args.number, args.input, args.n, args.start, args.end)

