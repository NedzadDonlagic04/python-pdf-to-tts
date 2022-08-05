# Importing all the needed modules
import os
import argparse as arg
from PyPDF2 import PdfReader
from gtts import gTTS 

# Defining the function fileExistsCheck which will
# take as an argument the file passed an argument
# to the script and check does it exist and end with
# the .pdf extension, if it meets the conditions the
# function will return True, if it does not it will
# return False
def fileExistsCheck(fileName):
    if not os.path.exists(fileName):
        print("File doesn't exist!")
        return False
    elif not fileName.endswith('.pdf'):
        print("File has to be a pdf file!")
        return False
    return True

# Defining the function getPdfText which will
# take as an argument the file passed an argument
# to the script, after which it will create an instance
# of the class PdfReader to help us read the text
# inside the pdf page by page and store it all in 
# a string variable called text, which it will return
def getPdfText(fileName):
    reader = PdfReader(fileName)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text

# Defining the function createWav which will 
# take as an argument the text from the file,
# and the file, it will then enter a try except
# section where it will take the fileName and based
# of it create a .wav file with the same name, after
# this it will use an instance of the gTTs class and
# use it to create the file with the correct text
# in text to speech format in it
# If all goes well it will print a success message
# If something goes wrong it will print an error message
def createWav(text,fileName):
    try:
        fileName = fileName.split('.')
        fileName = fileName[0] + '.wav'
        speech = gTTS(text = text, lang = 'en', slow = False)
        speech.save(fileName)

        print('Conversion success')
    except:
        print('Conversion error')

# Defining the main function which will be called
# to execute when the script is called
def main():
    # Setting up the needed argument which will represent the
    # passed pdf file
    parser = arg.ArgumentParser( description='Pdf to Text To Speech Converter' )
    parser.add_argument('filename' , help='Name of the pdf file')

    # Getting the argument passed to the script
    fileName = parser.parse_args()
    fileName = fileName.filename;

    # Checking if the file exists, getting all 
    # the text from it and creating a .wav file
    # all done using functions defined above
    if fileExistsCheck(fileName):
        text=getPdfText(fileName)
        createWav(text,fileName)

# Using the __name__ variable to check is the name
# of the used module __main__ , if so it will run 
# the main function
if __name__ == '__main__':
    main()