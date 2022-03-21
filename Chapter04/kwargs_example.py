# sets up plotting in jupyter
import pylab as plt

def draw_scatter(x, y, color='k', **kwargs):
    plt.scatter(x, y, color=color, **kwargs)
