# Scientific review

## Correctness
PASS — Exact quadratic-form reduction yields the sketched scalar Ritz coefficient and the required symmetric numerator. The undersampled proof constructs an explicit real-surjective family from a kernel vector not invariant under the SPD operator, and the full-column two-mode proof reduces the global negative-direction event to the squared angle between independent Gaussian columns. The latter has the beta law, with endpoint integration giving the claimed sharp asymptotic. A standalone numerical checker passed 11,209 identity, event, scalar-exception, and probability-consistency checks. Those checks are supplemental to, and not a substitute for, the proof.

## Originality
PASS, with historical-priority limitations — The 2026 similarity-restoration paper, 2024 study of spurious sketched Ritz values, and 2023 randomized orthogonal projection analysis were inspected in full text. They give the sketched coefficient, loss of numerical-range containment, correction mechanisms, and convergence context; they do not furnish the all-start event with its exact beta probability or the almost-sure full-real-range obstruction under undersampling. The classical beta-angle identity is acknowledged rather than claimed as new; similarly a fixed independent-start distribution does not imply a worst-case-over-starts law. Historical risks include unpublished equivalent matrix-pencil positivity calculations and additional unindexed numerical-linear-algebra literature.

## Value
PASS — The result distinguishes the reliable behavior of an individually prescribed Krylov start from uniform safety across all possible starts for a single sketch. It identifies a sharp rank obstruction and, in the smallest injective nontrivial dimension, a computable exact failure probability plus a sample-complexity exponent. This informs interpretation of universal sketch-based Ritz safeguards, without claiming an adaptive algorithm has this realized failure rate.

## Scope and limitations
Real SPD input and standard Gaussian sketch; exact arithmetic; one-vector unmodified randomized Arnoldi; existential start is chosen after the sketch. The result is not a finite-precision instability theorem or a guarantee about a particular low-dimensional embedded Krylov subspace. Independent historical-priority and mathematical audits are still needed.

Self-review: passed. Independent audit: not yet performed.
