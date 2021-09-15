import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#fixing the seed for reproducibility
#of the result
np.random.seed(10)

size = 10000
#drawing 10000 sample from
#standard normal distribution
sample = np.random.normal(0, 1, size)
bin = np.arange(-5,5,0.1)
plt.hist(sample, bins=bin, edgecolor='blue')

# sns.kdeplot(np.random.normal(0, 1, size))
# sns.kdeplot(np.random.normal(0, 2, size))
# sns.kdeplot(np.random.normal(0, 3, size))
#
# plt.legend([r"$\mu = 0, \sigma = 1$",
#             r"$\mu = 0, \sigma = 2$",
#             r"$\mu = 0, \sigma = 3$"])
plt.title("Normal Distribution")
plt.show()
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

