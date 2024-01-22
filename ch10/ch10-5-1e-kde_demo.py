'''
FYI: I asked ChatGPT how the KDE process works. The sentence I asked was: given a number of samples point,
how to obtain its kde. According to its answer, hope you can understand the KDE process. The following code
is also the example code from the answer. I modify it a little bit to make it work on the tips dataset.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import seaborn as sns

df = sns.load_dataset("tips")

# Generate some example data
data = df['total_bill'] #np.random.normal(size=1000)

# Choose bandwidth
bandwidth = 0.3

# Create KDE object
kde = gaussian_kde(data, bw_method=bandwidth)

# Evaluate KDE on a grid of points
x_grid = np.linspace(min(data), max(data), 100)
kde_values = kde.evaluate(x_grid)

# Plot the results
plt.plot(x_grid, kde_values, label='KDE')
plt.hist(data, bins=30, density=True, alpha=0.5, label='Histogram')  # Optional: Plot histogram for comparison
plt.legend()
plt.show()