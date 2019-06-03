import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

"""
This module is meant to be called by many_plots.py.
Each method adds one plot.

"""

def scatter_sorted_vals(cur_ax):

    X = [100, 120, 95, 122]
    Y = [.8, .7, .6, .75]

    cur_ax.scatter(X,Y)
    cur_ax.set_title('title')
    cur_ax.set_ylabel('accuracy')
    cur_ax.set_xlabel('time')



