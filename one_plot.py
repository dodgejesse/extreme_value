import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

"""
This module is meant to be called by many_plots.py.
Each method adds one plot.

"""

def scatter_sorted_vals(cur_ax, dev_accs):

    #X = [100, 120, 95, 122]
    #Y = [.8, .7, .6, .75]


    tmp = [ 4.03,3.83,3.65,3.88,4.01,4.08,4.18,3.8, 4.36,3.96,3.98,4.69, 3.85,3.96,3.85,3.93,3.75,3.63,3.57,4.25,3.97,4.05,4.24,4.22,3.73,4.37,4.06,3.71,3.96,4.06,4.55,3.79,3.89,4.11,3.85,3.86,3.86,4.21,4.01,4.11,4.24,3.96,4.21,3.74,3.85,3.88,3.66,4.11,3.71,4.18,3.9, 3.78,3.91,3.72,4.0,3.66,3.62,4.33,4.55,3.75, 4.08,3.9, 3.88,3.94,4.33]

    tmp.sort()
    dev_accs = tmp
    
    dev_accs.sort()
    cur_ax.scatter( range(len(dev_accs)), dev_accs)
    cur_ax.set_title('title')
    cur_ax.set_ylabel('accuracy')
    cur_ax.set_xlabel('hparam trial')



