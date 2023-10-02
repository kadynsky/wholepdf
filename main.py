'''
    To whom it may interest - excuse me, for it is not finished and lacks many features that I though of initially.
    I am currently in a bit of a rush and can't work on this more. I hope my pet project could be usefull to you.
'''

import PyPDF2
import os
import datetime
import argparse
import random
import settings

'''
Todo list:
    [DONE] If batch_size doesn't divide pdf_list completely - dump the rest of pdf separately
    either as another batch or single pdf files:
        [DONE] Make so that you first do batches regularly and than you do oveflow_pdfs lastly.
        And your list has to be sorted for that to meaningfully work.
    - [DONE-ish] Organize functions.

    - Build argparse options:
        - First choice:
            - [STUPID IDEA] Either the full directory to pdf merge Or select particular pdfs.
            - [PARTLY] Add an option to change directory temp
                - Do it after adding settings.py
        - [DONE] Input options:
            - [DONE] Batch size. How many pdfs will be merged at a time.
        - [DONE] Choose the name for output file.
        - Final confirmation menu. Either proceed or repeat above process.

    - [DONE] Write a settings.py for constants.
    - [SHOULD I REALLY?] Wrap the programm in GUM.
'''

timestamp = settings.timestamp
PDF_DIRECTORY = settings.PDF_DIRECTORY



def get_file_name(OUTPUT_PDF, timestamp):
    # Adds random three digits and year,month,day before the name.
    RANDN = random.randint(100, 999)
    stampname = f"{timestamp}{RANDN}{OUTPUT_PDF}"
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
    print('[DONE]   List collation')
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

    parser.add_argument('number', type=int, help='Your desired number of PDFs in one batch.')
    parser.add_argument('-input', action='store_true', help='View inside input
                        directory without making any changes.')
    # I don't think I implemented dir funtion. I can change it in the settings.py file.
    parser.add_argument('-dir', type=str, help="[does not work now] Paste temp directory path if you'd like")
    parser.add_argument('-n', type=str, help='Choose part of a name for your output batches')
    # I don't remember implementing start, end functions...
    parser.add_argument('-start', type=int, help='[does not work now] Starting pdf file')
    parser.add_argument('-end', type=int, help='[does not work now] Ending pdf file')

    args = parser.parse_args()

    # Batches Name negotiation.
    if args.n:
        OUTPUT_PDF = f"_{args.n}.pdf"
    else:
        OUTPUT_PDF = settings.OUTPUT_PDF

    run(args.number, args.input, args.n, args.start, args.end)

