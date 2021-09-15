import numpy as np
from scipy import stats
from timeit import default_timer as timer
import Bio
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import matplotlib.pyplot as plt


params_list = np.arange(1,16,1)
length = len(params_list)
a_idx = 0

def Binary(input, target):
    #print('Binary Search')
    #print("input target: %d"%target)
    start = timer()
    left = 0
    right = len(input) -1
    idx = -1
    while (left <= right) and (idx == -1):
        mid = (left+right)//2
        if input[mid] == target:
            idx = mid
        else:
            if target<input[mid]:
                right = mid -1
            else:
                left = mid +1

    #print("Elapsed time : %.8f second(s)"%(timer()-start))
    return (timer()-start,idx)

skew_data = []
time_binary = []
time_query = []

for i in range(length**2):
  
    b_idx = i%15

    initial_text = ['A']*100
    query_str = 'BCDEF'

    # Generate Beta distribution list
    B_distribution = np.random.beta(6, 2, size=100)
    round_list = [round(num, 1) for num in B_distribution]

    #Get pos to add query
    mode= stats.mode(round_list)
    pos = int(mode[0][0]*100)

    # Skewness
    skewness = (np.mean(B_distribution) - np.median(B_distribution))/np.std(B_distribution)
    skew_data.append(skewness)
    # place query to text then joint
    initial_text[pos] = query_str
    full_txt = ''.join(initial_text)

    if b_idx == 0 and i != 0:
        a_idx += 1

    #Query Search
    start = timer()

    alignments = pairwise2.align.globalxx(full_txt, query_str)  
    #print("alignment: {}".format(format_alignment(*alignments[0],full_sequences=True)))
    time_query.append(timer()-start)

    #Binary Search
    start = timer()
    result = Binary(initial_text,query_str)
    time_binary.append(timer()-start)
    #print(timer()-start)


#Plot
plt.title('Skewness vs Query Time')
plt.scatter(skew_data,time_query)
plt.show()
plt.title('Skewness vs Binary Time')
plt.scatter(skew_data,time_binary)
plt.show()