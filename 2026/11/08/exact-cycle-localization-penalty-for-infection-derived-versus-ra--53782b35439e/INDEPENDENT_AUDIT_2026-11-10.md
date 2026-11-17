# Independent mathematical audit

## correctness

PASS

PASS: First CTMC outbreak infects a connected cyclic interval when size<n, and its conditional location is uniform by rotational symmetry; residual susceptible vertices form a path. Along a unique path of length d, d independent source-vertex races transmit with probability p^d (no false assumption that two edges out of the same infected vertex are independent). Averaging over all susceptible new seeds and vertex targets yields 1+2/L Σ_d (ℓ−d)p^d per path component. For random immunes exactly n*C(n−d−1,k)/C(n,k) oriented d-edge segments survive; each unique residual path pair is counted exactly once. Coefficients are strictly positive by ∏_{j=1}^d(1−(k−1)/(n−j))<1. Hockey-stick summation at p↑1 gives (k−1)(L−1)/(k+1); dominated convergence and k=2 Riemann sum yield the three limiting regimes, with all boundary restrictions explicit. Independent exact Fraction enumeration of every k-immune subset and every susceptible index on cycles n=4..11 at p=1/3,1/2,3/4 reproduced the polynomial. The packaged CTMC first-step recursion was separately inspected but its logged results are not used as the proof.

## originality

PASS

PASS, qualifying well-established qualitative phenomenon: Ueki–Thompson–Banaji (Jan20 2026) and Hiraoka et al. already analyze differences in infection-acquired versus random immunity and topological localization. The reviewed materials do not give the identical conditional fixed-k finite homogeneous-cycle CTMC formula, coefficientwise strict inequality, exact saturated bound, or two scaling regimes and k2 crossover. Another 2026 cycle study concerns two high-contact independent percolation edges, and 2026 vaccination study independently seeds many vertices; neither implies the fixed-k conditional SIR law. Literature priority of possible one-dimensional percolation formulations remains a risk.

## value

PASS

PASS: Quantifying protection differences at the same immune count isolates topology from prevalence, a natural network-epidemic comparison. The full finite-n positive-coefficient polynomial and exact fixed-k versus proportional-k and near-perfect transmission crossover capture distinct population regimes. The statement is an exact model theorem with clear scope, not an empirical clinical forecast or a generic statement that clusters are different.

The dated certificate retains the supplied scientific assessment, sources and limitations.
