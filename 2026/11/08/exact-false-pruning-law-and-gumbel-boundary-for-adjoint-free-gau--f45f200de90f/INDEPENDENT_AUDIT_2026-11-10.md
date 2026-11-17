# Independent mathematical audit

## correctness

PASS

For all integers b>=2, ambient N>b, and 0<tau<1, the first Gaussian block spans the rank-b diagonal range almost surely when it survives the initial test. Chi-square_{b²}/b is its squared Frobenius norm. On the surviving branch the next residual is exactly zero, and by Gaussian rotational invariance the independent second-block projected-row norms squared are independent chi-square_b/b. The minimum is < tau² iff at least one necessary unit-energy direction is removed; such removal makes true error >=1>tau. This gives precisely [1-F_{b²}(b tau²)](1-[1-F_b(b tau²)]^b). Stirling density and endpoint Laplace estimate for b^{-1}chi-square_b give the c=2 moderate-deviation threshold (including c=2 -> 0) and centered 1-exp(-exp(-x)) Gumbel law. The initial premature-stop branch is deliberately excluded; the paper does not define a previous basis on that branch. Actual released independent-sketch code and pruning loop were read; finite high-precision gamma-CDF computations independently match b=16 tau=.9 and .99 to >9 significant digits.

## originality

PASS

Specific adjoint-free independent projected-row proxy under-retention and its finite-block conditional law are not entailed by the cited existing exact-row over-retention formulas or by a different fresh-look beta stopping procedure; classical chi-square/Gumbel tools credited. Best-of-knowledge with explicit source-coverage and implementation-version risks.

## value

PASS

A concrete method-specific correctness hazard: an exactly recovered rank-b subspace can lose a necessary basis vector after noisy coefficient pruning, violating a nominal absolute Frobenius tolerance. Exact finite failure probability and sharp extreme-value window give a reproducible diagnostic for adaptive range-finder design; not just a textbook tail calculation divorced from an algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
