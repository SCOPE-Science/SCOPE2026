# Independent mathematical audit

## correctness

PASS

For fixed u with annihilator g and d=deg(g), the determinant lemma reduces the target to a linear equation in v. The coefficient vectors of g(t)(tI-A)^(-1)u form a triangular basis of the cyclic span of u,Au,...,A^(d-1)u. Thus the image is all (chi_A/g) times polynomials of degree <d, with q^(n-d) lifts per target, including u=0 by the zero-dimensional convention. Primary exponent e has precisely K_e-K_(e-1) choices by the kernel dimensions of the f-power maps; divisibility by chi_A/g gives exactly the lower limits r_f, and summation factors. Every nonzero rank-one matrix has q-1 factorizations and zero has 2q^n-1, giving the correction. At the unchanged target the summation-by-parts coefficients on the kernel sizes before stabilization are strictly positive. Indeed sum_j min(e,lambda_j) equals M minus max_r(sum_(j<=r) lambda_j - re), so dominance gives the stated direction; distinct partitions have different increments of these dimensions, ensuring strictness somewhere before M. Rank-one extremes follow from a single irreducible factor or from the scalar dot-product count. These arguments work in characteristic two and in dimension one as well. Independent finite checks used direct determinant expansion and literal updates for 92 targets across 13 types over F_2 and F_3, plus 699 exact partition comparisons for q=2,3,5 and partition size up to seven. Replay: python3 /workspace/branches/2dcda91d-ea99-4105-aaf8-f8900e12579b/independent_fiber_check.py. Those checks are bounded and do not establish the theorem for general q or n.

## originality

PASS

The scoped distinct contribution is the complete multiplicity across all input vectors for each target and its strict isospectral dominance law, not the rank-one characteristic-polynomial identity, fixed-input pole placement, or the set of attainable targets. The available comparisons support this distinction.

## value

PASS

The exact fiber size gives the probability of each characteristic polynomial under uniform factorized rank-one updates, or under uniform distinct nonzero rank-one updates after correction. The unchanged-target counts also strictly detect comparable changes in the primary partitions that the support condition cannot distinguish. These are motivated finite-field statistics for arbitrary input matrices, not just an extra test of a known attainability criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
