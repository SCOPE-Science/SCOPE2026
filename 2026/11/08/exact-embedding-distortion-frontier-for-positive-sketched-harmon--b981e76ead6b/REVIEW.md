# Self-review

## Correctness — PASS
The analytic proof treats arbitrary Krylov dimensions and arbitrary real embeddings, extends the SPD angle estimate to complex eigenvectors, and checks both accretivity of the reduced Gram matrix and positivity of its associated Gram matrix. The two-dimensional equality construction gives explicit scalar numerator and denominator, including an undefined reduced matrix at the strict boundary. The `VERIFY.py` supplementary computation returned `VERIFY_OK 783 checks`, including exact-rational and numerical tests. Limits: numerical tests alone do not establish a universal result; the spectral argument does.

## Originality — PASS, with residual historical risk
The directly relevant source arXiv:2607.10354v2 Section 5.3 proves a sufficient condition \(\varepsilon<\kappa^{-1}\) for the SPD specialization, not the claimed exact threshold or negative witness. The 2023 randomized projection theorem addresses quasi-optimality and uses another sufficient condition; the 2025 survey concerns general randomized Krylov methods. The well-known Kantorovich angle bound is explicitly treated as prior mathematics. An accessible earlier Gaussian one-step harmonic Ritz sign law is acknowledged and excluded from the new claim; it does not imply a deterministic guarantee for all sketches and Krylov dimensions. Equivalence, stronger-coverage, record, and implication comparisons found no decisive covering theorem. Residual risk: an unindexed sketching or antieigenvalue result may give the same application.

## Value — PASS
The source convergence proof relies upon a right-half-plane harmonic Ritz hypothesis. For SPD problems, the exact worst-case embedding threshold is stronger than the source's condition by an asymptotic factor of order \(\sqrt\kappa\); this changes the distortion scale from \(\kappa^{-1}\) to \(\kappa^{-1/2}\). The construction shows that no further uniform tolerance can protect the reduced pencil. This is a motivated numerical robustness classification rather than a generic inequality restatement. It does not replace the independent restart-contraction hypothesis.

## Scientific scope and unresolved risks
The result is restricted to SPD matrices, exact arithmetic, and squared-norm embedding on the entire next Krylov space. A finite set of full-text literature inspections plus targeted discovery searches does not certify global priority. No general nonnormal theorem or convergence-rate improvement is claimed.

Self-review: passed. Independent audit: not yet performed.
