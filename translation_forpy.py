#Libraries in use
import PyPDF2
import docx

#End of libraries

#Functions
def INpdf(fLoc: str):
    #Collects the txt from a pdf file:
    with open(fLoc, 'rb') as file:
        reading = PyPDF2.PdfFileReader(file)
    txt = ''
    for page in reading.pages:
        txt += page.extract_text()

    return txt

def INdocx(fLoc: str):
    #Collects the txt from a docx file:
    file = docx.Document(fLoc)
    txt = ''
    for i,paragraph in enumerate(file.paragraphs):
        txt += paragraph.text

    return txt

def INtxt(fLoc:str):
    #Collects the txt from a txt file:
    #still todo (got lazy)
    pass

def INdigit():
    #scans for a user written string
    pass

def OUTpdf(string :str):
    #writes a pdf with the edited string
    pass

def OUTdocx(string :str):
    #writes a docx with the edited string
    pass

def OUTtxt(string : str):
    #writes a txt file with the edited string
    pass
def OUTdigit(string : str):
    #writes the modified string on the console
    pass

def getWordsize(string: str, i):
    #returns the size of the word given an string and a n to start the word
    pass

def aplyBioniceye(inSTR :str):
    #takes the text given and applies the bionic reading tecniques
    for i in range(len(inSTR)):
        l = inSTR[i]
