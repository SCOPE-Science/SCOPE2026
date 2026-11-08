# Review of sharp one-spoke defect tolerance

## Correctness — PASS

The spectral and rational derivation applies to all integers \(m\ge4\), all \(t>0\), and all nonnegative time steps. Its denominator factors are strictly positive; four exact off-diagonal formulas cover all vertex orbit pairs. The interval \(1/2\le t\le m/(m-1)\) makes all numerator coefficients positive, whereas each excluded side forces a negative hub-entry numerator for sufficiently large steps. The scalar Gauss stability function is positive on the nonnegative real axis, settling diagonals. Symbolic and exact rational verification in `verify.py` returned `VERIFY_OK 96`; finite samples are not the proof.

## Originality — PASS, qualified

Kirkland–Neumann (1998) and Carmona–Encinas–Patra–Sivakumar (2026) already yield the same cutoff for the Laplacian **group inverse** M-matrix condition. That asymptotic sign criterion is credited and not presented as new. Earlier exact Gauss calculations for a three-leaf weighted star settle that fixed case. The new claim is all-finite-step Gauss positivity for every higher degree and its sharp degree-dependent one-spoke tolerance, not automatically implied by the group-inverse criterion. Ketcheson–Gottlieb–Macdonald (2011) considers SSP two-step integrators, not the exact claimed rational graph family. The 1998 full text was inaccessible and unindexed equivalent derivations remain possible.

## Value — PASS

A single anomalous conductance can destroy nonnegativity in an A-stable fourth-order heat step. The theorem gives a complete practical tolerance interval across every degree, including asymmetric limits: weakening by a factor two is admissible regardless of degree, but allowed strengthening approaches zero excess as degree increases. This exact finite-time statement is more informative than the pre-existing eventual-sign necessary condition.

## Limitations

Only completed endpoint values, a star with exactly one exceptional edge, positive conductances, and the specified fourth-order Gauss method are addressed. No independent mathematical review is claimed.

Self-review: passed. Independent audit: not yet performed.
