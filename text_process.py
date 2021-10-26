import nltk
import handler

from nltk.tokenize    import word_tokenize
from nltk.tokenize    import sent_tokenize
from nltk.corpus      import stopwords
from nltk.probability import FreqDist
nltk.download()

from string import punctuation
from heapq import nlargest
from collections import defaultdict

# from bs4 import BeautifulSoup

# from urllib.request import Request, urlopen

# link = Request('http://ultimosegundo.ig.com.br/politica/2017-04-25/reforma-da-previdencia.html',
#                headers={'User-Agent': 'Mozilla/5.0'})
# pagina = urlopen(link).read().decode('utf-8', 'ignore')

# soup = BeautifulSoup(pagina, "lxml")

text = handler.get_text('source.txt')

sentencas = sent_tokenize(text)
palavras = word_tokenize(text.lower())

stopwords = set(stopwords.words('portuguese') + list(punctuation))
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

frequencia = FreqDist(palavras_sem_stopwords)

sentencas_importantes = defaultdict(int)

for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
        if palavra in frequencia:
            sentencas_importantes[i] += frequencia[palavra]

idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)
file_handler = handler.create_file("text_processed.txt")

for i in sorted(idx_sentencas_importantes):
    print(sentencas[i])
    file_handler.write(sentencas[i]+"\n")

file_handler.close()