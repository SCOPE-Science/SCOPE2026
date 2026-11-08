# Scientific review

## Correctness — PASS
The Gaussian polar factorization yields exact unbiasedness and conditional mean preservation. The second moments agree with the fourth-coordinate-moment identity, and the upper-tail constant has a matching analytic upper and lower bound via AM–GM and chi-square tail asymptotics. The one-factor exponential-moment threshold is established strictly away from its unclassified endpoint; all other quantifiers and the bounded full-normalization case follow. `verify.py` passed 52 exact-rational algebra checks from the files in this package. Nonzero positive semidefiniteness, finite dimensions, and a fixed sample count are essential.

## Originality — PASS, qualified
Bujanović–Kressner (arXiv:2004.06433, proof and experiments) address rank-one Gaussian estimates and probability bounds. Meyer–Avron (arXiv:2309.04952, Corollary 3 and Section 3.2) already use radial Gaussian decomposition to compare all-Gaussian and all-spherical variances; those ingredients are known, not newly claimed. Chen–Sun–Xi (arXiv:2610.12534) study tensor Frobenius-norm probes and moments. The comparison found no statement establishing the full intermediate-normalization convex-order family together with the exact large-threshold logarithmic coefficient \(\frac r2(m/(c_J\rho(H)))^{1/r}\). Generic homogeneous Gaussian large-deviation theory may imply the exponent after an additional optimization; the degree of prior implicit coverage warrants specialist review. No directly dominating equivalent was identified in the inspected open literature. An unsuccessful search alone is not a proof of priority.

## Value — PASS
Kronecker probing is a motivated numerical linear-algebra oracle model. The design question of how many Gaussian factors must be normalized to eliminate non-exponential outliers has an exact, general answer, even when the matrix is not itself a Kronecker product. The sharp angular constant is a product-state norm that can differ strictly from the operator norm, as the two-qubit rank-one example demonstrates. The transition is mathematically useful despite the potential difficulty of computing the coefficient in applications.

## Limitations and closest literature
The result covers only real PSD matrices, Gaussian factors, fixed dimensions, independent probes and a fixed sample count; it does not give prefactors, dimension-free concentration or a tractable product-state norm algorithm. The all-spherical variance mechanism belongs to Meyer–Avron, and the general large-deviation principle may narrow the claim's conceptual originality. These are recorded publication-precedence risks rather than hidden uncertainties.

Self-review: passed. Independent audit: not yet performed.
