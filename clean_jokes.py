import re
import csv
from bs4 import BeautifulSoup


def remove_html_tags(raw_html):
    pat = re.compile('<.*?>')
    clean_html = re.sub(pat, '', raw_html)
    return clean_html

def clean_jokes(data_file):
    with open(data_file, 'r') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')
    paras = soup.find_all('p')
    docs = [remove_html_tags(p.text) for p in paras]
    docs = [re.sub('\s+', ' ', doc) for doc in docs]

    with open('corpus.csv', 'w') as out:
        for i, doc in enumerate(docs):
            out.write(str(i) + ',' + doc + '\n')

if '__name__' == '__main__':
    data_file = 'data/jokes.dat'
    clean_jokes(data_file)
