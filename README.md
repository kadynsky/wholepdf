This tool will help you merge multiple PDF files into batches, the size of which is up to you of course. Only for Linux/Unix-based.

It is still developing. Not ready for use.

# How it works?
## Batches
You will be asked to write a number, which would specify **batch size**. This program will then merge your files in a specified quantity.

For example: I have 42 different PDF files in my **input** directory. If I were to specify batch size as 7, the program would then output 6 PDFs - because it divided 42 initial files into batches the size of 7. So every PDF file on the output would be the product of merged 7 initial PDF files.

### What if it doesn't divide?
Maybe instead of 42 files you have 41, but you still want to divide them in batches the size of 7. Of course they then can't be divided equally but the program will take care of it automatically and output the leftover PDFs into another PDF file. 

For example: you have 41 initial PDF files and you specified batch size as 7. The program will then process everything as compact as it can, meaning it will divide 35 into 5 batches the size of 7 initial PDFs and then do another, though incomplete for math reasons, batch the size of 6 initial PDFs. Simple stuff.

# Installation
This section is coming together soon. You'll have a .sh file with every step automated you'll just have to run something like run.sh and everything would be set to use. 

For now you can run this program as `$ python main.py `
NOTE: For now, you'll have to activate virtual environment manually by running `$ source pdf_combine/bin/activate`
