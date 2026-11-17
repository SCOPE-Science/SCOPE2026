# Independent mathematical audit

## correctness

PASS

Reconstructed the same-sample OLS intercept decomposition: for centered design U and Wishart S, m is independent of U and hat_mu=c+tr(AS)/n-m^TAm-m^T gamma, gamma=S^{-1}U^Tz, z_i=U_i^TAU_i. Orthogonally diagonalizing nonzero symmetric A and applying Frisch-Waugh-Lovell to a column leaves Gaussian residual w in dimension n-d; gamma_j has a 1/||w|| upper singularity, and a positive-probability nonzero projection P_W z_0 for a nonzero eigenvalue gives the matching lower singularity in a cone. Chi_(n-d) negative q moments exist exactly q<n-d, and independent Gaussian m transfers this threshold to absolute integration error. Polynomial remainders have all moments; no cancellation can rescue an infinite moment. For d=1, gamma=a sum u_i^3/sum u_i² is bounded by |a|max|u_i|, and rotational sixth-moment algebra gives the displayed exact MSE. For n-d>1, independent centered m yields bias -2tr(A)/n. Verified algebraically the near-singular n=3,d=2 witness gamma_1=1/(3 epsilon)-epsilon; the certificate checks 509 finite exact designs but cannot prove the all-q threshold.

## originality

PASS

No prior exact all-q same-sample quadratic fitted-intercept moment threshold was identified in bounded semantic/result and primary research comparisons. Portier-Segers make the OLS control-variate connection and asymptotics, and classical inverse-Wishart phenomena explain possible heavy tails, but neither alone supplies necessity for every nonzero A, d=1 exception, or the exact q<n-d integrability equivalence; best-of-knowledge rather than absolute priority.

## value

PASS

The exact moment-existence boundary for a natural, widely used same-sample OLS Monte Carlo estimator is a consequential and dimension-sensitive integrability fact: a seemingly helpful control fit loses even its mean near interpolation while raw Monte Carlo stays integrable. The d=1 cancellation and precise q=n-d frontier explain estimator reliability and are not routine substitutions or cosmetic finite examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
