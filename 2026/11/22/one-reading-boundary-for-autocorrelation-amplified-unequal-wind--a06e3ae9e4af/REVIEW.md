# Independent mathematical audit

## correctness

PASS

Direct counting of within-window and cross-window pairs reproduces all three disjoint lag-coefficient ranges, including the empty middle range when m=n. With m<=n and m>=2, the first same-window contribution already dominates 1/(mn), the other is positive, and the coefficients are strictly decreasing in the first range and negative thereafter. Descartes' rule bounds the number of positive derivative roots by one, counting multiplicity. Counting each pair's distance by the cuts separating it gives V'(1)/sigma^2=-2 times the sum of squared prefix weights, strictly negative. Thus the root is simple and in (0,1). For m=1 all coefficients are negative. Gaussianity converts the result into the same classification for every strictly positive threshold. Independent direct double summation of w_i w_j rho^|i-j|, bisection on its derivative, and normal density integration give rho=0.638158678162176, variance ratio V/sigma^2=0.889741973037229 and P=0.289075649894 at threshold sigma, versus 0.6 and 0.196705602459 at independence.

## originality

PASS

Best of current knowledge, the all-length classification with the singleton cutoff is distinct from the inspected earlier AR(1) Allan/Haar formulas and a scale maximization at fixed correlation. The exact Resultary match is the assigned work, not independent prior coverage.

## value

PASS

The answer to whether persistence can amplify an adjacent reporting-window contrast changes exactly when both windows contain at least two readings. This supplies a sharp boundary and a unique worst persistence for a natural family of filters, not just a larger variance in one example or a recomputation of Allan variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
