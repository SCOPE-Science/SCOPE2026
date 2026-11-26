# Independent mathematical audit

## correctness

PASS

The gradients are independent Gaussians of variances r_i conditioned to sum to zero, so an arc of resistance s has variance s−s²/R. The constraint on h gives the sum of pair variances divided by n². For prefix discrepancy T_i=∑_(j<i)b_j−im/n this yields W²=R(n²−1)/(12n²)−δ²∑_i(T_i−mean(T))²/(nR). Minimizing the arrangement penalty requires each interval-count vector to attain its separate sharp integer variance bound: all counts are floor or ceiling of their length times m/n. The floor-difference word attains all bounds, and max T−min T<1 forces a common floor intercept, giving exactly its rotations. The gcd formula follows from the equally spaced discrepancy residues. For the other extremum, expanding squared arc counts by pairs reduces minimizing width to minimizing the sum of d(n−d) over marked pairs. It is strictly concave on the gap simplex, since adjacent marked pairs alone give strictly concave quadratics in the independent gaps. The minimizing vertices describe exactly contiguous clusters; the triangular prefix discrepancy gives centered sum of squares m(n−m)[m(n−m)+2]/(12n). Interior clusters contain both 00 and 11, incompatible with optimum balanced length-two counts, so the gap is strict only for interior inventories. Boundary inventories have one rotation class. The packaged finite checker was inspected, not run; these arguments cover all n and real positive a,δ.

## originality

FAIL

Resultary 0b67a9f3e612 explicitly supplies both exact extrema, both equality classes and the gcd term for rotation variance of scattered 01 counts. The width optimization is the same arrangement theorem under an exact negative affine map. The change in observable is useful context but does not make the asserted sharp extremal classification distinct from the inspected one. No historical-priority conclusion is drawn from the catalogue dates.

## value

PASS

As a physical design rule the exact laws address a natural observable, the stationary Gaussian roughness at fixed two-resistance inventory. The closed gap and equality classes quantify how clustering and uniform spacing change roughness, including gcd and degenerate inventory effects. This usefulness does not make the equivalent extremal classification original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
