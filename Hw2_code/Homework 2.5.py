import numpy as np
from scipy import stats
from timeit import default_timer as timer
import Bio
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import matplotlib.pyplot as plt


a_idx = np.arange(1,16,1)
b_idx = np.arange(1,16,1)

def Linear(input, target):
    #print('Linear Search')
    #print("input target: %d"%target)
    start = timer()
    for i in range(len(input)):
        if input[i] == target:
            #print("Elapsed time : %.8f second(s)"%(timer()-start))
            return (timer()-start,i)
    return (timer()-start,-1)

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
time_linear = []
l_skew_data = []
b_skew_data = []
for i in b_idx:
    for j in a_idx:

        initial_text = ['A']*100
        query_str = 'BCDEF'

        # Generate Beta distribution list
        B_distribution = np.random.beta(j, i, size=100)
        round_list = [round(num, 1) for num in B_distribution]

        #Get pos to add query
        mode= stats.mode(round_list)
        pos = int(mode[0][0]*100-1)

        # Skewness
        skewness = (np.mean(B_distribution) - np.median(B_distribution))/np.std(B_distribution)
        skew_data.append(skewness)
        # place query to text then joint
        initial_text[pos] = query_str
        full_txt = ''.join(initial_text)


        #Query Search
        start = timer()

        alignments = pairwise2.align.globalxx(full_txt, query_str)  
        #print("alignment: {}".format(format_alignment(*alignments[0],full_sequences=True)))
        time_query.append(timer()-start)

        #Binary Search
        start = timer()
        result = Binary(initial_text,query_str)
        b_time = timer()-start
        if b_time < 2.5e-5 :
            time_binary.append(timer()-start)
            b_skew_data.append(skewness)
            #print(timer()-start)

        #Linear Search
        start = timer()
        result = Linear(initial_text,query_str)
        l_time = timer()-start
        if l_time < 1e-5:
            time_linear.append(l_time)
            l_skew_data.append(skewness)

#Plot
plt.title('Skewness vs Query search Time')
plt.scatter(skew_data,time_query)
plt.savefig('Query.png', dpi= 300)
plt.show()
plt.title('Skewness vs Binary search Time')
plt.scatter(b_skew_data,time_binary)
plt.savefig('Binary.png', dpi= 300)
plt.show()

plt.title('Skewness vs Linear search Time')
plt.scatter(l_skew_data,time_linear)
plt.savefig('Linear.png', dpi= 300)
plt.show()