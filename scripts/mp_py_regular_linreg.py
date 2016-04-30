# funciton file
# mp_py_regular_linreg.py

import numpy as np
from itertools import repeat
from concurrent.futures import ProcessPoolExecutor

def deco(j, X, y, N, p, beta, alpha, L1_ratio):
    
    def S(z, gamma):
        if np.abs(z) - gamma > 0:
            return np.sign(z)*(np.abs(z)-gamma)
        else:
            return 0
        
    return S(1./N*np.dot(X[:,j], (y - (np.dot(X,beta) - np.dot(X[:,j], beta[j]))))
                     , alpha*L1_ratio)/(1+alpha*(1-L1_ratio))


def mp_py_regular_linreg(X, y, beta_0, alpha, L1_ratio, max_iter=50, tol=0.0001):
    
    N, p = X.shape
    beta = beta_0.copy()
    b_new = np.zeros(p)
    
    for itr in range(max_iter):
        with ProcessPoolExecutor(max_workers=8) as pool:
            b_new = np.array(list(pool.map(deco, [j for j in range(p)], repeat(X), repeat(y), repeat(N),
                                           repeat(p), repeat(beta), repeat(alpha), repeat(L1_ratio))))
        beta = b_new
    return beta  