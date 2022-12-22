# PingüiMaya. Open SourceCode
# https://pingui.tk

from cryptography.fernet import Fernet
import os
import shutil
from docx import Document
from fpdf import FPDF
import time



key = "7nznUGP6Pbbgjrq6FrpP2hrb8B1xQz2f3O62YDhw-M8="


def __init__():
    #---
    try:
        os.mkdir("txtstrPREFERENCES")
    
    except:
        pass


    try:
        
        
        write("DEFAULTKEY",key,False)
        os.rename("DEFAULTKEY.txt","DEFAULTKEY.key")
        shutil.move("DEFAULTKEY.key","txtstrPREFERENCES/DEFAULTKEY.key")
       

    except:
        pass
    

def newkey(name):
    if  ".key" in name:
        name = name

    if ".key" not in name:
        name = name + ".key"

    key = Fernet.generate_key()
    with open(name,"wb") as mk:
        mk.write(key)


def loadkey(name):
    if  ".key" in name:
        name = name

    if ".key" not in name:
        name = name + ".key"


    with open(name,"rb") as mk:
        key = mk.read()
        

    return key


def encrypt(file, CUSTOM, times):
    valuenum = 0
    if  ".txt" in file:
        file = file

    if ".txt" not in file:
        file = file + ".txt"


    if CUSTOM == None:
        keyn = loadkey("txtstrPREFERENCES/DEFAULTKEY.key")

    if CUSTOM != None:
        if  ".key" in CUSTOM:
            CUSTOM = CUSTOM

        if ".key" not in CUSTOM:
            CUSTOM = CUSTOM + ".key"

        keyn = loadkey(CUSTOM)
        #print(keyn)

    for x in range(times):
        valuenum = valuenum + 1
        if valuenum <= times:
            print("*Encrypting for " + str(valuenum) + " times")

        
        system = os.name
        if system == "nt":
            os.system("cls")

        if system == "posix":
            os.system("clear")

        

        time.sleep(0.2)
        
        f = Fernet(keyn)
        with open(file,"rb") as org:
            original = org.read()

        encrypted = f.encrypt(original)

        with open(file, "wb") as encryp:
            encryp.write(encrypted)
            
            
    


def decrypt(file,CUSTOM,times):
    valuenum = 0
    if  ".txt" in file:
        file = file

    if ".txt" not in file:
        file = file + ".txt"


    if CUSTOM == None:
        keyn = loadkey("txtstrPREFERENCES/DEFAULTKEY.key")

    if CUSTOM != None:
        if  ".key" in CUSTOM:
            CUSTOM = CUSTOM

        if ".key" not in CUSTOM:
            CUSTOM = CUSTOM + ".key"

        keyn = loadkey(CUSTOM)
        #print(keyn)

    for x in range(times):
        valuenum = valuenum + 1
        if valuenum <= times:
            print("*Encrypting for " + str(valuenum) + " times")

        
        system = os.name
        if system == "nt":
            os.system("cls")

        if system == "posix":
            os.system("clear")

        time.sleep(0.2)
        f = Fernet(keyn)
    
        with open(file, "rb") as encfile:
            encrypted = encfile.read()

        decrypted = f.decrypt(encrypted)

        with open(file,"wb") as decfile:
            decfile.write(decrypted)

    


def write(name,text,add):
    if  ".txt" in name:
        name = name

    if ".txt" not in name:
        name = name + ".txt"

    if add == False:
        file = open(name, "w")
        file.write(text)
        file.close()

    if add == True:
        old_text = read(name)
        new_text = old_text + " " + text
        file = open(name,"w")
        file.write(new_text)
        file.close

    
        
def newtxt(path):
    write(path,"",False)


def search(name,searchfor,advanced):
    text = searchfor
    isin = False
    cant = 0
    l_num = 0
    line_appear = []
    
    if  ".txt" in name:
        name = name

    if ".txt" not in name:
        name = name + ".txt"


    for i in open(name).readlines():
        l_num = l_num + 1

        if text in i:
            line_appear.append(l_num)
            isin = True
            cant = cant + 1
            

    if advanced == True:
        info = {
            "isin" : isin,
            "Quantity" : cant,
            "LinesAmount" : l_num,
            "LineAppear" : line_appear,
        }
        return info

    if advanced == False:
        return isin,cant,l_num,line_appear


def readlines(name):
    lines = []
    if  ".txt" in name:
        name = name

    if ".txt" not in name:
        name = name + ".txt"

    for i in open(name).readlines():
        lines.append(i)

    return lines


def addline(name,line):
    text = "\n" + line
    write(name,text,True)




def read(rute):
    textc = ""
    if "txt" in rute:
        
        with open(rute, "r") as archive:
            for line in archive:
                textc = textc + "" + line
                
        return textc

    else:
        
        rute = rute + ".txt"
        with open(rute, "r") as archive:
            for line in archive:
                textc = textc + "" + line

        return textc

    

def rename(rute,name):
    if  "txt" in rute:
        rute = rute

    if "txt" not in rute:
        rute = rute + ".txt"


    if  ".txt" in name:
        name = name

    if ".txt" not in name:
        name = name + ".txt"

    
    os.rename(rute, name)


def toword(file):
    if  ".txt" in file:
        file = file

    if ".txt" not in file:
        file = file + ".txt"

    text = read(file)
    text = str(text)

    document = Document()
    document.add_paragraph(text)
    file = file.replace(".txt",".docx")
    document.save(file)


def topdf(file):
    if  ".txt" in file:
        file = file

    if ".txt" not in file:
        file = file + ".txt"

    pdf = FPDF()  
  

    # Add a page
    pdf.add_page()
 
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 8)

    # open the text file in read mode
    f = open(file, "r")
 
    # insert the texts in pdf
    for x in f:
        pdf.cell(1, 10, txt = x,ln = 1)
 


    file = file.replace(".txt",".pdf")
    pdf.output(file)  

    

    
    

def checkupdate():
    system = os.name
    if system == "nt":

        os.system("py -m pip install --upgrade txtstr")
        

    if system == "posix":
        os.system("python3 -m pip install --upgrade txtstr")







