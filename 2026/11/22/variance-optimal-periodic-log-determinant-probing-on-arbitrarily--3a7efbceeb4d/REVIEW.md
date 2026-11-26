# Independent mathematical audit

## correctness

PASS

Pairwise uncorrelated products of independent signs give variance 4 times the sum of same-class squared off-diagonal entries. Leading/trailing continuants give positive Green factors u_s(i), v_s(j); the flux recurrence at the ends and in the interior gives strictly increasing u_s and decreasing v_s. The product of the two factors at s,t has the same monotonicities, so its two telescoping sums have strictly positive interval coefficients. Finite integral of the positive Green entry for one pair also ensures σ-finiteness of the mixture measure by level sets of that entry. Integrating against the product measure gives the squared mixture certificate, not the mixture of individual variances. Balancing minimizes the number of pairs in each interval; length-k windows force period k and the first window uses all k classes. k=1 and k=n are trivial. Resolvent representations give log A and A^(−α). For the homogeneous density I independently checked localization by polynomial approximation: the expansion of log about μ+2 in powers of (A_n−(μ+2)I)/(μ+2) has geometric tail ratio 2/(μ+2); below degree d all entries at distance d vanish. The bilateral symbol factors as r^(−1)(1−r e^{iθ})(1−r e^{−iθ}), giving coefficient −r^d/d. Bulk averages at each d converge and the geometric bound allows summing multiples of fixed k. The private check python3 /workspace/independent_checks.py (section 1) verifies strict positivity and uniqueness in an independent, nonuniform six-vertex two-shift instance. The analytic certificate covers all n and allowed measures.

## originality

PASS

Bounded to positive resolvent mixtures with mixed-shift products (including log and nontrivial fractional inverses), and the fixed-k homogeneous log density. Exact fixed-budget all-partition optimization and the interval proof for a single Green matrix are already in a distinct same-date indexed record; no chronology is inferred. That proof makes the cross-product extension short but does not give a variance comparison for the square of an integral: the squared integral contains every cross product. The extension proves all the cross products have the requisite interval certificate, not merely that the separate variances are optimized at each shift.

## value

PASS

A complete fixed-budget estimator-design classification survives arbitrary heterogeneity, unequal groups and a non-single-resolvent target such as log A. The mixed-shift closure identifies a concrete structural mechanism for extending exact probe design, and the log variance law gives a quantitative benchmark. This is not a runtime or determinant-speed claim: a tridiagonal determinant is already available in linear time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
