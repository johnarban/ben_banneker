# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 09:09:27 2016

@author: johnlewisiii
"""

import numpy as np
import matplotlib.pyplot as pl

# Generate my prior
def myprior(b):
    # Uniform prior for now
    return b*0. + 1

# Generate my Likelihood
# now loglikey
def likeli(b,flips):
    # Count the number of flips
    N = len(flips)
    # Count number of heads
    k = np.sum(flips)
    # Create likelihood function
    likey = np.log(b)*k + np.log(1-b)*(N-k)
    return likey



# Combine prior and likelihood
def comboplot(b, flips):
    prior = myprior(b)
    loglikelihood = likeli(b, flips)
    posterior = np.log(prior) +  loglikelihood
    print np.max(posterior)
    posterior -= np.max(posterior)
    pl.plot(b, np.exp(posterior))
    return np.exp(posterior)


# Generate coin flips
flips = np.array([1,0,1,0,1,1,0,0,1,1,1])
b = np.linspace(0.01,0.99,100)
posterior = comboplot(b, flips)