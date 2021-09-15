import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#fixing the seed for reproducibility
#of the result
np.random.seed(10)

size = 10000
#drawing 10000 sample from
#poisson distribution
sample = np.random.poisson(10, size)
# bin = np.arange(0,20,1)
# plt.hist(sample, bins=bin, edgecolor='blue')

#different poisson distribution
sns.kdeplot(np.random.poisson(5, size))
sns.kdeplot(np.random.poisson(10, size))
sns.kdeplot(np.random.poisson(15, size))

plt.legend([r"$\lambda = 5$",
            r"$\lambda = 10$",
            r"$\lambda = 15$"])

plt.title("Poisson Distribution")
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
