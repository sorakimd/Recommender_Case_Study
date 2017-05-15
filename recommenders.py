
import pandas as pd
import numpy as np
import graphlab as gl
import matplotlib.pyplot as plt

df_ratings = pd.read_table('ratings.dat')

data = pd.DataFrame(df_ratings)

data.columns = ['user_id', 'item_id', 'rating']

df = gl.SFrame(data)


def recommenders(df,solver):
    modelFR = gl.recommender.factorization_recommender.create(df, target = 'rating', solver=solver_FR)
    modelRFR = gl.recommender.ranking_factorization_recommender.create(df, target = 'rating', solver=solver_RFR)
    modelISR = gl.recommender.item_similarity_recommender.create(df, target = 'rating')
return ({'FR': modelFR, 'RFR': modelRFR, 'ISR': modelISR})
