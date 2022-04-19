#for decoding
import codecs
#using Textract
import textract
from gtts import gTTS


# Language in which you want to convert
language = 'en'


#extract text in byte format
textract_text = textract.process('1_100.pdf')
#convert bytes to string
textract_str_text = codecs.decode(textract_text)


# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=textract_str_text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("1_100.mp3")
