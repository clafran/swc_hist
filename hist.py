# Randomizing data, generating summary stats, and histigram

import numpy as np

#mu is mean

mu = 80
sigma = 10

x = np.random.normal(mu, sigma, 100)

print("Random Normal Array Mean Centered", x[:10])
