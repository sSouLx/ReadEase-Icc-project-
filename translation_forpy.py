#Libraries in use
import PyPDF2
import docx
#End of libraries

#Colors
RED = "\033[31m"
BOLD =  "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[34m"
PINK = "\033[35m"
BLUE = "\033[36m"
OFF = "\033[0m"
#End of Colors



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
    string = input("Entre seu texto: ")
    return string

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

def getWordsize(string: str, i: int):
    #returns the size of the word given an string and a n to start the word
    size = 0
    tam = len(string)- 1
    while string[i].isalpha() and i < tam:
        size += 1
        i+=1
    return size//2

def aplyBioniceye(inSTR :str):
    #takes the text given and applies the bionic reading tecniques
    sizeW = getWordsize(inSTR, 0)
    i = 0
    isB = 0

    for i in range(len(inSTR)-1):
        l = inSTR[i]
        if l.isalpha():
            if sizeW > 0:
                sizeW -= 1
                print(YELLOW  + l + OFF, end='')
            else:
                print(l, end='')


        elif inSTR[i] == ' ':
            sizeW = getWordsize(inSTR, (i+1))
            print(l, end='')

        else:
            print(CYAN + l + OFF, end='')
        
    
    return 0



stri = INdigit()
aplyBioniceye(stri + ' ')
