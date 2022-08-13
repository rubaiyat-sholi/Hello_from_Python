import pyttsx3
import PyPDF2
book = open('demo.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

robo = pyttsx3.init()
for num in range(0,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    robo.say(text)
    robo.runAndWait()
