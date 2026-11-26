# Independent mathematical audit

## correctness

PASS

Write Omega=QJ with J invertible almost surely and choose a unit normal v. Conditional on the sketch range, X=Psi^T Q and y=Psi^T v are independent standard Gaussians; full column rank gives (XJ)^dagger=J^-1 X^dagger. Thus P=[[I,b],[0,0]] with b=X^dagger y in orthonormal coordinates. For b nonzero the leading singular value is simple and truncation keeps exactly the block [[1,||b||],[0,0]] on span(b,v), making D=(sqrt(1+||b||^2)-1)/2. Independently reconstruct the regression law: conditional on X, b has the law of (X^T X)^-1/2 g for an independent standard Gaussian g. Separate its radius and direction; orthogonal invariance replaces the resulting directional inverse-Gram quadratic form by the first diagonal entry in law, independently of the radius. The Schur complement identifies that inverse entry as 1/(X_1^T(I-Pi_{X_{-1}})X_1); the projected Gaussian norm squared has t-k+1=ell+1 degrees of freedom (also for k=1 with empty X_{-1}). Therefore ||b||^2 has law U/V with independent chi-squares, and b is nonzero almost surely. The beta change of variable yields the exact CDF, including x=0. Integrating the beta density at zero gives the stated coefficient and sharp endpoint; the mean integrates its inverse square root. At k=6,ell=4 the beta quotient is 105/64, giving 41/128. The distribution extends to ell=0, but finiteness of the mean requires ell>0; the Finding states ell>=4. The frozen verifier was inspected, not run, and its simulations do not prove these laws.

## originality

FAIL

The exact distribution is covered by an already indexed theorem for the same Gaussian Nyström estimator, not merely by a Wishart analogy. In Resultary 23a3fc6123ad take A=I_(k+1), r=k, left test width t=k+ell and condition on the right sketch. Its orthogonal residual B=I-QQ^T has rank one and squared Frobenius norm 1. Its normalized squared reconstruction error R equals ||I-P||_F^2=1+||b||^2 exactly. In codimension one the only nonorthogonal block gives 1+2D=sqrt(R) under rank-one SVD truncation. The existing R-1~BetaPrime(k/2,(ell+1)/2) specializes to the claimed R^-1 beta law; the tails, moments and numerical mean are its direct transformations. The earlier record need not name the signed eigenvalue to cover that stochastic result. This is evidence of coverage, not a claim about authorship or historical priority.

## value

FAIL

Positivity is a legitimate diagnostic and the identity stress test is natural. But for this narrowly codimension-one construction the entire sharp quantitative result is a scalar re-expression of the already known error law for the very same samples. The 2-by-2 block immediately gives indefiniteness and the change of variable; no additional invariant independent of that error statistic, or nontrivial remaining classification, is established. The interpretation is useful exposition, but does not rescue the submitted claim as an independently valuable new exact law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
