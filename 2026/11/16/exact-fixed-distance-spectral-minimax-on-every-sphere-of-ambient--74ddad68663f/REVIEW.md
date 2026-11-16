# Mathematical review

## Correctness

**PASS.** The normalized zonal Gegenbauer multipliers are derived using the harmonic polynomial integral representation, with its normalization and range explicit. Degrees one and two force a universal lower bound; at the sole possible optimal cosines, degree three is controlled algebraically, and every degree at least four is bounded simultaneously by the exact fourth moment \((3d+2)/d^3\). The inequality is strictly below \(1/d\) for every integer \(d\ge5\). All-step conclusions use self-adjoint diagonalization, not finite experiments. The supplied Python checker returned 59,232 exact rational assertions on a finite test range.

## Originality

**PASS with historical-priority uncertainty.** The direct 2023 randomized-angle spherical walk study gives Wasserstein bounds for a different kernel. The 2016 fixed-step curved-manifold study gives general Wasserstein mixing estimates, not this exact \(L^2\) sphere-specific optimizer. The 2004 hypersphere Gegenbauer analysis treats continuous diffusion. Known ambient-three and ambient-four isolated sphere results are logically insufficient to yield the all-dimensional theorem for \(d\ge5\). Search and implication comparisons did not identify a stronger covering theorem, but no search is an exhaustive uniqueness certificate; specialized earlier fixed-angle spectral minimax publications remain a risk.

## Mathematical value

**PASS.** Deterministic-step choices are a natural design variable in geodesic random walks. A sharp dimension-dependent spectral rate, exact two angles, all-degree strictness, multiplicities and all-step optimality give an infinite-dimensional optimization theorem with a short verifiable analytic certificate. This does not assert a result for other metrics, point-mass convergence, or arbitrary step mixtures.

Self-review: passed. Independent audit: not yet performed.
