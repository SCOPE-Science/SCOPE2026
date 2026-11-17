# Independent mathematical audit

## correctness

PASS

The claimed estimator is a quadratic-minus-quartic polynomial. At alpha=0 all contributions are nonnegative; for alpha>0 a singular-vector sketch with first columns tv and tu yields sigma²[(1+alpha)t²/r-alpha t⁴/r²]<0 above t²>r(1+alpha)/alpha, giving a positive-probability Gaussian open set for every nonzero matrix. In rank one X,Y are independent chi-square_r/r and negativity means XY>c(X+Y) with c=(1+alpha)/(2alpha). The integral follows by conditioning. The rate function I(x)+I(y) has unique boundary saddle (2c,2c), J(c)=2c-1-log(2c); the local t/r and d/sqrt(r) coordinates produce prefactor 1/[sqrt(2pi r)(2c-1)sqrt(4c-1)]. The c_r=1+2/r perturbation yields the oracle e^-2 factor. We independently expanded the saddle Hessian and Jacobian; no finite check was substituted for the large-r argument.

## originality

PASS

Best-of-knowledge originality lies in sign-safety for fixed weighted Hutch#, the exact negative-rank-one chi-square probability and sharp Gaussian saddle prefactor, not the source paper variance calculation or its oracle alpha. The primary defining paper was located but its full text could not be independently retrieved in this run; title/abstract and source result comparisons are not whole-document noncoverage certifications.

## value

PASS

A norm-squared estimator returning negative output is a substantive reliability and interpretability issue. Quantifying a sharp exponential, leading coefficient and oracle weighting effect clarifies how infrequently this failure occurs and distinguishes deterministic sign safety from variance optimization. Rank-one restriction is sharply motivated as the simplest nontrivial spectrum rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
