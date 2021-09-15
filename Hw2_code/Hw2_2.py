import numpy as np
import matplotlib.pyplot as plt
#Poisson Dice


def P_Dice(rate,size):

    dice_array = np.random.randint(99,size=size)
    bool_dice = dice_array < int(rate*100/size)

    return sum(bool_dice)

lambd = [5]
n_interval = [500]

rep_per_set = 500
k_list = []

for l,interv in zip(lambd,n_interval):
    
    for rep in range(rep_per_set):
        k_list.append(P_Dice(l,interv))

    norm_k = np.array(k_list)*100/rep_per_set
    bin = np.arange(0,l*4,1)
    plt.title("lambda = {} n = {}".format(l,interv))
    plt.hist(norm_k, bins=bin, edgecolor='blue')
    plt.hist(np.random.poisson(l, interv), bins=bin, histtype='step')
    plt.show()