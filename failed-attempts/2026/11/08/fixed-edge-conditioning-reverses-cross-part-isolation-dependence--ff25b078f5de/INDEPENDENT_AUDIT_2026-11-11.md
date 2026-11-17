# Independent mathematical audit

## correctness

PASS

Exact row/column exclusion gives Cov_k(X,Y)=ab[binom((a-1)(b-1),k)/binom(ab,k) - binom(ab-b,k)binom(ab-a,k)/binom(ab,k)^2]. The cross-product identity gives product factors 1-t/((N-b-t)(N-a-t)), strict negative exactly for 2<=k<=ab-max(a,b), zero otherwise. Bernoulli covariance ab p(1-p)^(a+b-1)>0, sparse alpha,beta,c limit -c²exp[-c(1/alpha+1/beta)]/(2alpha beta) versus Bernoulli O(n), balanced correlations from row variances. Rebuilt derivation, checked zero ranges, and separately enumerated binary matrices 2x2, 2x3, 3x3 at all k. Correct even though covered.

## originality

FAIL

FAIL: The full October 25 publication Isolation covariance reverses sign across three bipartite edge-sampling ensembles proves the exact SAME all-a,b,k covariance formula and sign classification, general linear-aspect-ratio sparse constant, Bernoulli covariance and scale comparison. Another October 25 full text Exact cross-part isolation dependence in three bipartite sampling ensembles proves stronger all-factorial-moment negative dependence. The subsequent balanced correlation constants are immediate normalization by standard same-part zero-row variances and do not rescue the submitted principal claim.

## value

FAIL

FAIL: The mathematical phenomenon is worthwhile, but the present submission recomputes an already published exact sign and sparse-scale theorem; adding routine correlation normalization for the balanced case does not create a distinctive motivated advance over the stronger prior factorial-moment classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
