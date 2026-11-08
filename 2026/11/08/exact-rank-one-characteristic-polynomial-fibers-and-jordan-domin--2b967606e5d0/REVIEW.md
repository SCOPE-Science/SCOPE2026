# Review: rank-one spectral fiber theorem

## Correctness — PASS
The stated equality is for all finite fields, all positive dimensions, all fixed base matrices, and every monic target polynomial of the same degree. The determinant lemma is a polynomial identity. The cyclic annihilator argument identifies both the exact image and fiber dimension of the covector-to-characteristic-polynomial map. The elementary-divisor count uses the exact primary kernel sizes, without assuming eigenvalue splitting. Strict dominance is a positive-coefficient comparison of the entire kernel sequence, not an extrapolation from examples. Ten explicit canonical forms and 92 complete target-fiber comparisons pass literal determinant enumeration; exhaustive matrix checks and 696 strict dominance comparisons corroborate the proof. Main risk: an error in the resolvent-to-cyclic-subspace argument would affect all targets; the triangular coefficient proof addresses precisely this step.

## Originality — PASS (provisional historical priority)
The closest inspected 2011 primary paper provides the resolvent characteristic-polynomial identity and studies generic complex eigenvalue curves; the current determinant step is not independently new. The 2021 and 2023 papers characterize which prescribed target polynomials are reachable, including over arbitrary fields in 2023, so support classification is also not new. Carriegos–Trobajo (2022) also review the classical fixed-input pole-assignment subspace. These results do not give complete **finite-field fiber multiplicities aggregated across all inputs** or the strict Jordan-dominance comparison. The explicit product law and monotonicity are narrower in perturbation rank but stronger in enumeration. Exact-source and alternative-formulation searches did not identify a covering enumeration theorem. Residual risks include uninspected older finite-field transfer-function counting literature and a possible implicit formula elsewhere; the search results alone do not prove novelty.

## Value — PASS
The invariant is natural: for any fixed linear transformation it gives the exact distribution of the characteristic polynomial under a uniformly chosen rank-one factorization, simultaneously for all targets, all finite fields, and all similarity types. It distinguishes matrices that share a characteristic polynomial by a strict, order-theoretic criterion. The irreducible case has a uniform distribution over all other monic targets, while the scalar case is confined to a one-parameter family. The information goes beyond the already-known reachability conditions and is usable in finite-field matrix sampling and spectral-preservation questions.

## Limits
The finite computations corroborate but do not replace the arbitrary-field proof. There is no independent validation, no classification of changed Jordan forms, and no guarantee of historical priority outside the inspected literature.

Self-review: passed. Independent audit: not yet performed.
