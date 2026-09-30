# Independent audit — 2026-09-30

## Disposition: FAILED — central theorem is false

### Correctness
FAIL. The proposed Hermite-edge threshold is contradicted in the first two nontrivial degrees. For `n=4`, the upper-half-plane continuation of the largest zero has `z_4(λ) ~ √3 (λ+3)^(-1/2)` at the next degree-loss point. Thus for every `d>3`, `√(λ+d) z_4(λ)` acquires a negative-imaginary boundary value immediately to the left of `-3` and cannot be a Pick/complete-Bernstein function. The exact threshold is `d=3`, not `(10+√6)/4≈3.112372`. The same argument gives exact threshold `d=4` for `n=5`, not `(14+√10)/4≈4.290569`.

The proof mistake is treating the source paper's boundary-minimum argument as independent of `d` except for the Laurent coefficient at positive infinity. The moving square-root factor changes the negative-axis boundary singularity structure, and that obstruction appears before the Hermite-edge Laurent coefficient changes sign.

### Originality
FAIL as stated. The false classification cannot support an originality claim, and the exact `n=4,5` correction already appears in `2026/09/18/exact-ultraspherical-largest-zero-cbf-thresholds-n4-n5--f0490e7ec2cc`.

### Scientific value
FAIL as a validated theorem. The Hermite-edge coefficient remains a useful necessary condition, but it is not the claimed exact threshold.

### Evidence
- Castillo, arXiv:2609.19186.
- SCOPE record `2026/09/18/exact-ultraspherical-largest-zero-cbf-thresholds-n4-n5--f0490e7ec2cc`.
- Schilling–Song–Vondraček, *Bernstein Functions*, for the Pick characterization.
