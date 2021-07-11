from Word import Word
from WordExporter import export, IWordExporter
from Utils import log

# put in words
rawWords = ['fade', 'as', 'fdafdsafdsa']
log(rawWords)

# Processing
words = []
for rawWord in rawWords:
    try:
        word = Word(rawWord)
        print(word)
        words.append(word)
    except:
        print(rawWord + " not found")


# todo: add unit test
export(words, IWordExporter.Format.anki)
