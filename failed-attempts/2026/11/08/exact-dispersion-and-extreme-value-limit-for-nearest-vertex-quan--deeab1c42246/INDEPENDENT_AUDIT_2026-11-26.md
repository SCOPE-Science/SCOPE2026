# Independent mathematical audit

## correctness

PASS

The Gram matrix of the centered regular simplex gives Q_m=m(1+S_m−2M_m)/(m−1) with the largest coordinate attained at the nearest vertex. For an independent proof of the mixed moment, order the coordinates x_1≥⋯≥x_m and put W_j=j(x_j−x_{j+1}), x_{m+1}=0. The linear change takes the ordered chamber to the uniform unit simplex. Then M=a·W with a_i=1/i, and S=WᵀBW with B_ij=1/max(i,j). Write H=H_m, H2=H_m^(2). The row sum of B is 1+H−H_i; the trace is H and the total sum is 2m−H. Dirichlet third moments give m(m+1)(m+2) E[MS]=H(2m)+2∑_i a_i(1+H−H_i)+2∑_i a_i B_ii=2mH+2H+H²+H2. Subtracting (H/m)·2/(m+1) gives exactly the claimed positive covariance. Marginal variance formulas follow from standard Dirichlet moments for S and maximum-spacing moments for M. Applying the variance of S−2M checks the sign and factors in the dispersion. Independent rational ordered-simplex checks at m=2,…,16 confirmed the mixed moment, mean and variance; the smallest two cases are (mean,var)=(1/3,4/45) and (5/12,43/720). For iid unit exponentials Y_i representing the Dirichlet vector, mS_m→2 in probability and mM_m−log m⇒G (the denominator's relative error is O_P(m^−1/2) and the maximum is O_P(log m)). The prefactor m/(m−1) supplies the additional constant 1 in the shift 2G−3. The exact marginal variances and covariance give Var(S_m)∼4/m³, Var(M_m)∼π²/(6m²), and Cov∼(log m)²/m³, proving both quoted variance and correlation limits independently of convergence in law.

## originality

FAIL

Several materially earlier Results give the exact advertised nonstandard ingredient for the identical joint law, including its asymptotic correlation. Passing from it to nearest-vertex dispersion is the affine Gram-matrix identity plus the variance-of-a-linear-combination formula and known marginal moments. The stated high-dimensional law is the same affine identity applied to classical exponential maxima and a law of large numbers; the shift and variance constant do not require a distinct probabilistic claim. The absence of the geometric wording in the spacing records does not rescue the frozen result.

## value

FAIL

Typical nearest-vertex error of a uniform simplex point is a natural statistic, and the geometric reduction is useful exposition. But the frozen contribution is the already evaluated maximum/Greenwood covariance and its routine affine variance and LLN/extreme-value consequences. No further independently useful non-routine invariant, fluctuation result, or quantization obstacle remains in this claim once that coverage is accounted for.

The dated certificate retains the supplied scientific assessment, sources and limitations.
