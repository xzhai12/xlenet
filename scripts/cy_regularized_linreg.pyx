# distutils: language = c++
# distutils: sources = cpp_regularized_linreg.cpp

cimport cy_regularized_linreg

def py_regularized_linreg(double[::1] data_x, double[::1] data_y, int num_samples, int num_features, 
                          double[::1] beta, double alpha, double L1_ratio, int max_iter, double tol):
    
    cy_regularized_linreg.coord_desc(&data_x[0], &data_y[0], num_samples, num_features, 
                                                 &beta[0], alpha, L1_ratio, max_iter, tol)
