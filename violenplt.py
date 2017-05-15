import numpy as np
import graphlab
import pandas as pd
import matplotlib.pyplot as plt



def plot_violen(predictions, og_rs,show=False):

    data = [predictions[og_rs].astype(int) = rating] for rating in range(-10,11,1)]
    plt.violen(data,range(-10,11,1))
    if show:
        plt.show
