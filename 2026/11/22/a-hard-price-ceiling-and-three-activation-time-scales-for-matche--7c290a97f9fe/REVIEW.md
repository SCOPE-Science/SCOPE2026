# Scientific review: matched bipartite finite-horizon conductance allocation

## Correctness — PASS

The feasible simplex is compact. Strict convexity of \(\operatorname{tr}(e^{-tL})\) in individual edge rates proves an unrestricted unique optimum, even when the graph can disconnect. Cost-preserving matching-pair permutations force exactly two edge classes. Their complete four-block spectral decomposition yields an exact derivative along the budget line. Its endpoint signs give the matching-only and nonmatching-only thresholds, including equality, while strict convexity resolves all interior cases. The monotone exponential equation has exactly one positive root for \(1<r<2(m-1)/(m-2)\). The limit proofs distinguish fixed-price \(m\), \(m^2\), and \(m^2\log m\) activation scales. Independently constructed exact eigenvector equations and finite graph Laplacians pass 5,289 reproducibility checks; these finite tests are not used as an infinite proof.

## Originality — PASS on inspected evidence, qualified

The closest exact matching-priced \(K_{m,m}\) results classify **spectral-gap**, **inverse spectral moment**, **Kirchhoff index**, and **spanning-tree determinant** objectives. The already known spectral-gap boundary equals the permanent deletion price \(2(m-1)/(m-2)\), so that coincidence is not new. None of the materially inspected results provides the full finite-time heat trace minimizer or its switching equation; the present theorem cannot be deduced from a spectral-gap allocation, since finite positive-time traces depend on all eigenvalues and their multiplicities. Related finite-time heat-trace calculations on stars, marked complete graphs, and complete prisms have different eigenvalue decompositions, so do not imply the biclique result by a graph relabeling. The 2006 source optimizes the Laplacian gap, and the 2007 source optimizes discrete-time SLEM. Unindexed exact duplicates or translations remain a priority risk.

## Value — PASS

The price ceiling cleanly separates networks where a costly matching is eventually worth funding from those where it is never worth funding, despite allowing arbitrarily long finite observation. On the same natural graph family, the sharp activation delay changes from linear to quadratic to quadratic-logarithmic growth across fixed-price regimes. The short-time optimal network can be disconnected while the long-time optimum is connected below the ceiling. These are quantitative design boundaries for all graph sizes, not one-off numeric examples or generic convexity consequences.

## Limitations and closely related literature

The price ceiling is shared with the earlier continuous-time spectral-gap optimum, whose full set of boundary optimizers is a different object. The result applies only to balanced complete bipartite graphs with one uniformly priced perfect matching. Fully asymmetric cost matrices and discrete-time Markov transitions are not classified. An independently conducted mathematical audit has not been performed; search-based novelty checks cannot establish absolute uniqueness of priority.

Self-review: passed. Independent audit: not yet performed.
