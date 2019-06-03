import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import one_plot

"""
This module creates a figure, then adds individual plots by calling one_plot.py.
"""

def generate():
    fig = plt.figure()
    cur_ax = fig.add_subplot(1,1,1)

    one_plot.scatter_sorted_vals(cur_ax)

    plt.savefig('plot_drafts/sorted_scatter.pdf')

    
