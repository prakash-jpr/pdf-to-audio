# importing required modules 
import PyPDF2
from gtts import gTTS
import os
    

# Language in which you want to convert
language = 'en'

# creating a pdf file object 
pdfFileObj = open('11.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print("No of pages ",pdfReader.numPages) 
    
# creating a page object 
pageObj = pdfReader.pages[0] 

print("pageObj in file ",pageObj)
  
# extracting text from page 
mytext = pageObj.extractText()
print("Text in file ",mytext)

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")
    
# closing the pdf file object 
pdfFileObj.close() 

