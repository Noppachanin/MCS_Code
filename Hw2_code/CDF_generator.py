# Direct sum area under the curve
import numpy as np
import matplotlib.pyplot as plt


def SumArea(samples,bin):
    plt.hist(samples, bin, density=True, histtype='step',cumulative=True, label='Empirical')
    plt.title("Cumulative Probability Distribution")
    plt.show()

