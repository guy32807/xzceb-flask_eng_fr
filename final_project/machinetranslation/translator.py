from deep_translator import MyMemoryTranslator
 
def englishToFrench(englishText):
    #write the code here
    frenchText = MyMemoryTranslator(source='en-US', target='fr-FR').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    englishText = MyMemoryTranslator(source='fr-FR', target='en-US').translate(frenchText)
    return englishText