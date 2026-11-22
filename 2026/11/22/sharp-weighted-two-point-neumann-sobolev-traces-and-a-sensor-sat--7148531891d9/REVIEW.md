# Scientific review

**Correctness — PASS.** The reproducing kernel is checked directly by differentiation and integration by parts. An explicit positive-definite trace-one dual matrix gives a strictly convex global spectral minorant for every weight ratio below \(5-2\sqrt3\). The diagonal lower bound covers every larger ratio. These two independent analytical certificates prove the optimum, the threshold, all equality positions and endpoint cases. `check.py` provides additional finite computations, not an infinite proof.

**Originality — PASS, with residual historical-priority risk.** The claim is the minimum largest eigenvalue of the two-weight Neumann Sobolev evaluation Gram matrix over *distinct* interval points. Wang–Zhang (2012) optimize reconstruction error, a different operator objective; Privat–Trélat–Zuazua (2014) optimize random-data parabolic observation domains, a different geometry and loss; Jorgensen–Tian (2015) study discrete RKHS point masses. None of these inspected results implies the exact dual-certificate classification or the threshold. An unindexed direct equivalence in two-point Green-kernel frame design is the principal unresolved priority risk.

**Value — PASS.** Joint trace stability of two sensors is a natural operator-design invariant distinct from recovery error. The complete phase diagram exposes a sharp threshold between equalized orthogonal representers and saturation of the single-sensor lower bound, with unique positions and an explicit algebraic threshold. The optimizer is not just a grid evaluation or textbook specialization.

**Scope and reproducibility.** The theorem is real-valued, one-dimensional, unweighted in arclength but unequal in sensor penalties, with exactly two points and squared derivative norm. The standalone script is a finite consistency check; the proof is the strict quadratic dual certificate. Neither an independent audit nor uniqueness relative to all historical mathematics is claimed.

Self-review: passed. Independent audit: not yet performed.
