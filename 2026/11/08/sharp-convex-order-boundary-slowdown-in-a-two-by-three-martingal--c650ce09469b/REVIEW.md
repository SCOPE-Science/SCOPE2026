# Review of the two-by-three martingale Sinkhorn boundary theorem

## Correctness

PASS. The conditional exponential tilt solves the exact martingale row projection: its normalization and mean constraints are explicit, yielding the scalar \(s(t)\). Column KL scaling then yields \(F_{a,b}\) without approximation. Fixed point, derivatives, global supremum slope, KL Taylor coefficient and boundary square-growth are derived algebraically; a standalone verifier checks symbolic identities, 350 projection samples and boundary constants. The boundary is not covered by geometric convergence: its exact KL decay is reciprocal-time. A finite run never substitutes for the analytic limits.

## Originality

PASS under accessible-source and published-record comparison, with historical-priority risk. Actual published-finding corpus semantic searches on 2026 martingale Sinkhorn convergence, discrete two-by-three instances, exact scalar maps and boundary rates did not identify a covering statement. The closest relevant mathematical sources were inspected for algorithm, assumptions, and theorem scope: arXiv:2609.18850 proves qualitative exponential convergence under convex terminal support; arXiv:2407.14186 examines dependence on terminal measure but does not give the claimed small-state map or boundary constant; arXiv:2610.26504 treats the distinct SISTA martingale gradient update; arXiv:2508.17641 treats discrete entropic martingale algorithms with approximate constraints and Newton updates. This is **not** covered by a qualitative convergence statement for a different class, nor is failure of a text search evidence of uniqueness. Related general IPFP and small-state special cases may remain unindexed.

## Value

PASS. This is a complete classification of a natural minimal finite martingale-Sinkhorn bridge where the martingale constraint is nontrivial. It gives exact parameter-to-iteration sensitivity, a sharp global step contraction, and a structural geometric-to-algebraic slowdown exactly at the convex-order feasibility boundary. Such a benchmark distinguishes convergence behavior near degenerating transport faces, rather than computing an arbitrary small isolated invariant. No general higher-dimensional improvement is claimed.

## Boundaries and limitations

The result is valid for \(0<a<1\), \(a\le b<1\), zero cost, reflection symmetry, exact alternating *martingale* and marginal KL projections, and initialization from \(\mu\otimes\nu\). Terminal support is finite and not convex, so the general 2026 theorem cannot be invoked to prove this result. No independent validation or priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
