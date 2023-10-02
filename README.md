This tool will help you merge multiple PDF files into batches, the size of which is up to you of course and a little more.

I accounted mostly for unix-based systems, but It should be no problem figuring how to run it on windows machines.

# How it works?
## Batches
You will be asked to write a number, which would specify **batch size**. This program will then merge your files in a specified quantity.

For example: I have 42 different PDF files in my **input** directory. If I were to specify batch size as 7, the program would then output 6 PDFs - because it divided 42 initial files into batches the size of 7. So every PDF file on the output would be the product of merged 7 initial PDF files.

### What if it doesn't divide?
Maybe instead of 42 files you have 41, but you still want to divide them in batches the size of 7. Of course they then can't be divided equally but the program will take care of it automatically and output the leftover PDFs into another PDF file. 

For example: you have 41 initial PDF files and you specified batch size as 7. The program will then process everything as compact as it can, meaning it will divide 35 into 5 batches the size of 7 initial PDFs and then do another, though incomplete for math reasons, batch the size of 6 initial PDFs. Simple stuff.

# Installation and Running
This pet project still is very green, so the installation and running procedure might change through time to a simpler and more flexible solutions.

NOTE: For now, you'll have to activate virtual environment manually by running `$ source pdf_combine/bin/activate` or `pdf_combine/bin/activate` for windows users.

You can run this program by `$ python main.py `

# How to use?
You can dump all of your PDFs you'd like to merge into the `input` directory which is located inside `wholepdf` directory you cloned to your PC. This would be the operation directory of the program - the program can only see this directory. You may change the desired directory by changing PDF_DIRECTORY to your liking.

By running this program via `$ python main.py` you will need to also include your desired batch size (a number from your head. This is mandatory) and you may also add other options. Such as:
- `-input` To show how wholepdf would devide your catalog in batches. So the command need to look like this: `$ python main.py 5 -input`, where 5 is the desired number of PDFs in a single batch. It would output a table divided in five.
- `-n` To add a desired name for the output batches. So the command would look like this `$ python main.py 5 -n A_Great_Name`. 

These are all options for now.