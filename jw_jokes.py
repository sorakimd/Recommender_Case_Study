
import pandas as pd
import graphlab as gl
import re
import csv
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import linear_kernel
import string
from sklearn.cluster import KMeans
from nltk.stem.wordnet import WordNetLemmatizer

# EDA:
# jokes = gl.SFrame('data/jokes.dat')
ratings = gl.SFrame('data/ratings.dat', format='tsv')
# ratings_pd = pd.read_table('data/ratings.dat')
#
# df = rating_pd.pivot(index='user_id',columns='joke_id', values='rating')


#tfidf vectorizer
# write function that gets document and outputs tfidf

def remove_html_tags(raw_html):
    pat = re.compile('<.*?>')
    clean_html = re.sub(pat, '', raw_html)
    return clean_html

def clean_jokes(data_file):
    with open(data_file, 'r') as f:
        docs = f.read()


    docs = [re.sub('\s+', ' ', doc) for doc in docs]
    wordnet = WordNetLemmatizer()
    docs = [wordnet.lemmatize(words) for words in docs]

    return docs
    # with open('corpus.csv', 'w') as out:
    #     for i, doc in enumerate(docs):
    #         out.write(str(i) + ',' + doc + '\n')
    #

def my_tokenizer(doc, lemmatizer=WordNetLemmatizer(), stopwords=None):
    tokens = word_tokenize(doc)
    tokens = [t.lower() for t in tokens if t not in string.punctuation]
    if lemmatizer:
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
    if stopwords:
        tokens = [t for t in tokens if t not in stopwords]
    return ' '.join(tokens)

def vtize(data_file):
    documents = clean_jokes(data_file)
    new_docs = []
    for doc in documents:
        new_docs.append(my_tokenizer(doc))
    tfidf = TfidfVectorizer(stop_words='english')

    tf = tfidf.fit_transform(documents).toarray()
    features = tfidf.get_feature_names()

    # Cosine Similarity using TF-IDF

    # 1. Compute cosine similarity
    cosine_similarities = linear_kernel(tf, tf) #squareform(pdist(vec_mat, metric='cosine'))?
    return features, tf, cosine_similarities


features, x, sims = vtize('data/jokes.dat')
# for i in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
ks = KMeans(n_clusters = 4)
ks.fit(x)
top_centroids = ks.cluster_centers_.argsort()[:,-1:-11:-1]
print "\n\n top features for each cluster with 1000 max features:"
for num, centroid in enumerate(top_centroids):
    print "%d: %s" % (num, ", ".join(features[i] for i in centroid))

# five top similar
docs = clean_jokes('data/jokes.dat')
for ind in (sum(sims)).argsort()[:5]:
     print docs[ind], '\n'
     print '-----','\n\n'
#
# graphlab.recommender.create(ratings,user_id='user',item_id='movie')
# recs = m.recommend()

if '__name__' == '__main__':
    data_file = 'data/jokes.dat'
    docs = clean_jokes(data_file)
    tf, sims = vtize(data_file)
