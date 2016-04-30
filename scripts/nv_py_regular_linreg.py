# function file
# nv_py_regular_linreg.py
import numpy as np

def nv_py_regular_linreg(X, y, beta_0, alpha, L1_ratio, max_iter=1000, tol=0.0001):
    def S(z, gamma):
        if np.abs(z) - gamma > 0:
            return np.sign(z)*(np.abs(z)-gamma)
        else:
            return 0

    N, p = X.shape
    beta = beta_0.copy()
    b_new = np.zeros(p)
    for itr in range(max_iter):
        for j in range(p):
            b_new[j] = S(1/N * np.dot(X[:,j], (y - (np.dot(X,beta) - np.dot(X[:,j], beta[j]))))
                     , alpha*L1_ratio)/(1+alpha*(1-L1_ratio))
        beta = b_new
    return beta            