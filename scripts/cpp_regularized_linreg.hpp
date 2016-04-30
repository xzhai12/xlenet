double estimated_y_i(double *x, int N, int p, double *beta, int i);
double compute_intermediate_b(double *x, int m, int n, double *y, double *beta, int j);
double S(double z, double gamma);    
double* coord_desc(double *x, double *y, int num_samples, int num_features, double *beta, 
                   double alpha, double L1_ratio, int max_iter, double tol);