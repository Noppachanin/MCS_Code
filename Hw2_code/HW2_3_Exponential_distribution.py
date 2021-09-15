import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from CDF_generator import SumArea

#fixing the seed for reproducibility
#of the result
# np.random.seed(10)

size = 10000
#drawing 10000 sample from
#exponential distribution
sample = np.random.exponential(1, size)
bin = np.arange(0,10,0.1)
plt.hist(sample, bins=bin, edgecolor='blue')
plt.title("Exponential Distribution")

#different exponential distribution
# sns.kdeplot(np.random.exponential(1, size))
# sns.kdeplot(np.random.exponential(2, size))
# plt.legend([r"$\beta = 1, \lambda = 1$",
#             r"$\beta = 2, \lambda = 0.5$"])

plt.show()
SumArea(sample,bin)


print("\n************Original array:")
print(sample)
r1 = np.mean(sample)
r2 = np.average(sample)
print("\n************the Mean:")
print("Mean of the random variables directly: ", r1)
print("Mean of the formula: ", r2)
r1= np.var(sample)
r2 = np.mean((sample - np.mean(sample)) ** 2 )
print("\n************the Variance:")
print("Variance of the random variables directly: ", r1)
print("Variance of the formula: ", r2)

