#include <iostream>

using namespace std;

double estimated_y_i(double *x, int N, int p, double *beta, int i) {
	double s = 0;
	int l;
	for(l = 0; l < p; l++) {
		s += x[i*p + l] * beta[l];
	}
	return s;
}


double compute_intermediate_b(double *x, int m, int n, double *y, double *beta, int j) {
	double res = 0;
	int i;
	
	for(i = 0; i < m; i++) {
		res += x[i*n + j] * (y[i] - estimated_y_i(x, m, n, beta, i));
	}
	return res;
}

double S(double z, double gamma) {
	if(z >= 0) {
		if (z - gamma > 0) {
			return z - gamma;
		}
		else {
			return 0;
		}
	}
	else {
		if (-z - gamma > 0) {
			return z + gamma;
		}
		else {
			return 0;
		}
	}
}


double* coord_desc(double *x, double *y, int num_samples, int num_features, double *beta, 
                   double alpha, double L1_ratio, int max_iter=1000, double tol=0.0001) {
    
	int itr, j, i, 
    N = num_samples, 
    p = num_features;
    
	double bb;
    double b[p];
    
    double beta_new[p];
    
    double res;
    
    for(j = 0; j < p; j++){
        b[j] = beta[j];
    }
    
	for(itr = 0; itr < max_iter; itr++) {
		for(j = 0; j < p; j++) {
		       bb = S(b[j] + compute_intermediate_b(x, N, p, y, b, j) / N, alpha*L1_ratio) / (1. + alpha * (1 - L1_ratio));
		       beta_new[j] = bb;
		}
        
        for(j = 0; j < p; j++){
            b[j] = beta_new[j];
        } 
  
	}
    
    
    
    
    for(j = 0; j < p; j++){
            beta[j] = b[j];
        }
    
	return beta;
}
