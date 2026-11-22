# Scientific review: unimodular path controllability and D-optimal volume ties

## Correctness — PASS
The signed Kalman determinant is calculated from an exact path-Laplacian eigenbasis, an odd-modulus cosine-product permutation and the unit-triangular endpoint Krylov matrix. The Gramian modal factorization gives a strictly positive determinant at precisely the coprime node labels for all finite positive horizons, including zero damping. Exactly \(\varphi(2n)\) maxima follow by counting odd units modulo \(\,2n\). The independent standalone checker passed 602 finite assertions across exact integer Kalman matrices, high-precision modal determinants and physical-coordinate time quadrature. The proof, not these finite tests, establishes all orders and all horizons.

## Originality — PASS, qualified
Parlangeli and Notarstefano (arXiv:1109.3556v1, 2011), Theorem 4.4, already classify which nodes can control a path; that criterion is prior art. Their inspected full text does not establish that every nonzero Kalman determinant has absolute value one or that all controllable nodes share the exact finite-horizon Gramian determinant. Summers and Lygeros (arXiv:1306.2491v1, 2013) optimize traces of controllability Gramians, not these determinants. The full published normalized-path result `d0ca7333cb0f` has generally unique endpoint optima for a different symmetric degree-normalized operator, and does not imply the unnormalized path volume ties. Residual risk: another source may contain the same quantitative invariant, and its algebra can be derived from classical spectral data with an additional nontrivial product argument.

## Value — PASS
The determinant is the standard squared volume scale of the reachable ellipsoid. The universal exact tie across \(\varphi(2n)\) locations is mathematically surprising, especially when every vertex of a dyadic path is equally D-optimal despite having different degrees and different small-horizon trace values. The result supplies a complete arithmetic design classification, not merely a qualitative feasibility test.

## Scope and limitations
The claim is restricted to unweighted combinatorial-Laplacian paths, unit coordinate actuators, standard Euclidean state coordinates, and common damping. Equal volume does not assert equal eigenvalues or conditioning; external independent audit has not been performed. The proof and verification checker are packaged with the finding.

Self-review: passed. Independent audit: not yet performed.
