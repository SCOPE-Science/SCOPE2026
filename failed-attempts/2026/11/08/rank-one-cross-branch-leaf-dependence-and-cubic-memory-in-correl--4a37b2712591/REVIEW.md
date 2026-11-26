# Independent mathematical audit

## correctness

PASS

For rooted terminal counts the seed is deterministically L_2=1. If the size is m and the count is k, the increment is 1 minus a Bernoulli(k/m) variable. The mean m/2 and variance recursion V_{m+1}=(1−2/m)V_m+1/4 follow; the variance is m/12 from m=3 onward. For s≥t the conditional centered mean at s is ((t−1)/(s−1))(L_t−t/2). Given the shared tree the branches are independent even when a tested time is t itself. The conditional means multiply to the stated rank-one covariance; the t=2 and t=n cases and the strictly increasing correlation follow independently of the limit. The same integer-order-preserving transition applied with common uniforms proves stochastic order of the whole future count paths. Both future path laws depend on the shared tree only through L_t; conditional independence and the scalar monotone covariance identity give the asserted association. For the Gaussian claim (m−1)(L_m−m/2) is a martingale with increment m(L_m/m−B_{m+1}). The diagonal predictable variances use m²(1/4−(L_m/m−1/2)²), and only m<t contributes off diagonal. The expected normalized error from replacing each conditional Bernoulli variance by 1/4 is O(1/n), and the increments after normalization are O(n^{−1/2}). The quadratic sums tend to 1 and α³ respectively, so the martingale CLT in fixed projections gives the stated limit, including the zero-variance projection at α=1.

## originality

FAIL

There is strong earlier indexed coverage in the same shared-prefix fixed-edge model. The earlier theorem counts undirected degree-one vertices, so its finite numerical formula is not identical; however, its proof gives exactly the same transition, arbitrary-time regression, and common-uniform monotone coupling. Replacing deterministic initial count 2 by 1 gives the rooted variance by the same recursion; selecting possibly different end times in the already available regressions gives the cross-time product immediately. The earlier coupling preserves order at each step and thus already orders whole paths, so using coordinatewise monotone path functionals in the same scalar conditioning argument is direct. The earlier cubic Gaussian law also transfers without any further limit proof by the single possible root discrepancy, bounded by one. This is a decision about demonstrable implications of the earlier record, not literal equality of rooted and unrooted statistics.

## value

FAIL

Shared-tree memory is a motivated observable, and the earlier cubic law is useful. For this frozen result the difference is the deterministic seed count induced by excluding the root. The cross-time covariance is the product of the same earlier regressions at two endpoints, and the path-association refinement uses the whole-path order already built into the prior scalar proof. The changed finite cutoff is a direct consequence of the altered initial count. The exact refinements therefore do not supply a separate, non-mechanically-implied invariant or phenomenon of sufficient scientific value under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
