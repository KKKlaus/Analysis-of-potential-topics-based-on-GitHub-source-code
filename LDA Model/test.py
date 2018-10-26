import nltk
import codecs
from nltk.corpus import stopwords

f2 = codecs.open('codestopwords.txt',"r",encoding = 'utf-8')
codewd = f2.read()
codewd = codewd.splitlines()
for desc in codewd:
    codewdLst = nltk.word_tokenize(desc)

print(codewdLst)