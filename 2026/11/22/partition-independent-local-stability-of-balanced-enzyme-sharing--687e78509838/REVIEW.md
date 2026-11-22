# Mathematical review

## Correctness
**PASS.** The proof first derives the full conserved-variable mass-action equations and their Jacobian, then uses an incidence Gram matrix and the numerical-range disk of a cyclic permutation. The disk inequality excludes every eigenvalue with nonnegative real part except the conservation zero mode, which is removed on the fixed-substrate-total tangent space. No diagonalizability or generic-rate hypothesis is used. The exact-rational checker tests the independent Jacobian formula on \(126\) rational families; stability for all dimensions follows from the analytic inequality, not the finite tests.

## Originality
**PASS on inspected evidence, subject to historical-priority risk.** Joshi–Nguyen (arXiv:2611.02523v1), Theorems 1.1–1.3 and Section 7, cover general uniqueness/persistence, distinct-enzyme global convergence, and selected shared-enzyme Hopf examples, not the balanced all-partition local-stability theorem. Donnell–Banaji (arXiv:1211.2153) work under structural factorization which need not hold with shared enzymes. Closest indexed work on enzyme sharing treats stationary flux cross-responses or perturbations of a particular Hopf threshold; those conclusions neither imply nor contradict uniform balanced stability for all partitions. The literature search cannot exclude an unindexed equivalent Gram-matrix proof.

## Value
**PASS.** Enzyme sharing is known to introduce oscillatory regimes, but this theorem isolates a broad, explicit stable manifold of parameter-and-conservation choices for *every* enzyme partition. The generality over ring length and arbitrary grouping, including irregular noncirculant grouping, explains exactly why a common-rate balanced regime avoids the Hopf mechanism and provides a useful constructive stability benchmark for full mass-action cycles. The result is structural rather than a numerical special case.

## Limitations
The conclusion is local, not global; arbitrary kinetic heterogeneity and unbalanced positive equilibria are not covered. The condition of equal free enzyme concentrations is obtained by choosing pool totals according to the pool sizes, and is a substantive restriction. No independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
