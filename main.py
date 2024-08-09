import pyttsx3
import PyPDF2





droid = pyttsx3.init()

volume = droid.setProperty('volume',2.0)
 


droid.say("Bonjour je suis Alexia assistante chez ULB corporation")
droid.say("et je suis la pour vous donnez des taches a excuter")

livre= open("mom.pdf", 'rb')
lecture= PyPDF2.PdfReader(livre)
page = len(lecture.pages)
print(page)
debutlecture = lecture.pages[0]
text= debutlecture.extract_text()
droid.say(text)




droid.runAndWait()