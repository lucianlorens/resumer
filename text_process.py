import nltk
#nltk.download()

# from urllib.request import Request, urlopen

# link = Request('http://ultimosegundo.ig.com.br/politica/2017-04-25/reforma-da-previdencia.html',
#                headers={'User-Agent': 'Mozilla/5.0'})
# pagina = urlopen(link).read().decode('utf-8', 'ignore')

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(pagina, "lxml")
def get_text(filename):
    with open(filename, 'r') as file:
        string = file.read()
    return string

import os 
def clean_previous_text():
    os.remove("text_processed.txt")

texto = get_text('text_file.txt')
    

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sentencas = sent_tokenize(texto)
palavras = word_tokenize(texto.lower())

from nltk.corpus import stopwords
from string import punctuation

stopwords = set(stopwords.words('portuguese') + list(punctuation))
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

from nltk.probability import FreqDist

frequencia = FreqDist(palavras_sem_stopwords)

from collections import defaultdict

sentencas_importantes = defaultdict(int)

for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
        if palavra in frequencia:
            sentencas_importantes[i] += frequencia[palavra]

from heapq import nlargest

idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)
file_handler = open("text_processed.txt","a+")

for i in sorted(idx_sentencas_importantes):
    print(sentencas[i])
    file_handler.write(sentencas[i]+"\n")

file_handler.close()
    