Recommender Case Study

Introduction

The recommender case study involved building a recommendation system from the Jester Dataset with four collaborators. The Jester Dataset consists of user ratings of over 100 jokes. The goal of the case study was to build a recommendation system and to suggest jokes to (new) users. The evaluation metric was how well the predicted top-rated jokes for the users' ratings in the test set. In particular, the scoring metric selected the 5% of jokes we predict to be most highly rated by that user. It then looks at the actual ratings that the user gave those jokes. The final score was the average of those ratings deviations. In effect, this means it the recommender only needed to identify which jokes a user is likely to rate most highly (so the absolute accuracy of ratings is less important than the rank ordering). GraphLab was used to build the recommendation system.

DATA CLEANING

The jokes were scraped from the internet. Thus, they were in the same format that the website was written in. To parse out the relevant text data we used the BeautifulSoup library with its html.parser. Upon inspection we were able to deduce that each joke was separated by a 'p'. For each of the jokes we removed the html tags with "re.sub(re.compile('<.?>'), '', html)". Once we removed the html tags we substituted \s+ for each of the documents in the parsed docs. This gave us our corpus of documents (jokes).


Natural Language Processing

Now that we had the corpus available it was time to create a useable matrix for GraphLabs recommendation systems. From the corpus we were able to get each individual document (joke). Using the nltk library, we tokenized the documents. Once we had the tokens we stripped them of punctuation and lowercased each. In addition, we decided to use a lemmatizer. We decided to do a lemmatizer rather than a stemmer because, upon inspection, it seemed that the morphology of each word had significant meaning. After adding a few words to the stopwords dictionary we removed all stop words and joined the tokens back to create new documents that, we believed to have significantly less noise than the previous documents. From the new documents we were able to apply a Tf Idf vectorizer to create a new workable matrix of word representations. From this TfIdf we retrieved the features, the term frequencies and the cosine similarities. To get more insight into the data we decided to apply a KMeans algorithm and investigate the ten top centroids for each of the clusters (with 1000 maximum features). In addition we decided to see if any signal resided in the most similar jokes by extracting the jokes with the highest cosine similarities.

CONCLUSION

Not surprisingly we found that there were a few distinguishable groupings of jokes. In particular, we found that jokes tended to fall into five categories. There were family jokes (involving parents/siblings), political jokes (mostly involving Hillary Clinton), religious jokes (think Catholic Priests), dirty jokes, and jokes that fell between two or more of these categories. With the GraphLab build in recommender systems we tested a factorization_recommender, a ranking_factorization_recommender, and an item_similarity_recommender. After close consideration of each recommender we eventually decided to put the factorization_recommender into production. 
# Recommender_Case_Study
