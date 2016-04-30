import numpy as np
import scripts.nv_py_regular_linreg
import scripts.mp_py_regular_linreg
import scripts.cpp_py_regular_linreg
#import scripts.setup
import subprocess

class regularizedLinearRegression(object):
    def __init__(self, alpha=1.0, L1_ratio=0.5, method='cpp',
                 max_iter=1000, tol=1e-5):
        self.alpha = alpha
        self.L1_ratio = L1_ratio
        self.beta_0 = None
        self.max_iter = max_iter
        self.tol = tol
        self.method = method

        # check if a proper method is chosen
        self.error_check()


    def error_check(self):

        # method
        if not self.method in ['nav', 'cpp', 'mp']:
            raise 'error: not proper method selected'



    def fit(self, X, y, beta_0=None):
        # error check: data dimensions
        if len(X) != len(y):
            raise 'error: data dimension not compatible'

        X, y = np.array(X), np.array(y)

        X_shape = X.shape
        if len(X_shape) == 1:
            raise 'error: 1d data not supported yet'
        else:
            N, p = X_shape

        if beta_0 == None:
            self.beta_0  = np.zeros(p)
        else:
            self.beta_0 = np.array(beta_0)

        if self.method == 'nav':
            res = scripts.nv_py_regular_linreg.nv_py_regular_linreg(
                X, y, self.beta_0, self.alpha, self.L1_ratio,
                self.max_iter, self.tol)

            return res

        if self.method == 'mp':
            res = scripts.mp_py_regular_linreg.mp_py_regular_linreg(
                X, y, self.beta_0, self.alpha, self.L1_ratio,
                self.max_iter, self.tol)
            
            return res

        if self.method == 'cpp':
            res = scripts.cpp_py_regular_linreg.cpp_py_regular_linreg(
                X, y, self.beta_0, self.alpha, self.L1_ratio,
                self.max_iter, self.tol)
            return res

        