# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Primitive automorphism-free 9+9+9+9 tactical decomposition of a (36,15,6) design
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1318
- **Disposition:** NO_RESULT
- **Domain:** symmetric block designs
- **Method:** tactical quotient enumeration and 0-1 refinement

## Problem

Does there exist a symmetric 2-(36,15,6) design, i.e. a 36-point 36-block incidence structure with every block containing 15 points and every two distinct blocks meeting in 6 points, that admits a tactical decomposition with four point classes P1,P2,P3,P4 each of size 9 and four block classes B1,B2,B3,B4 each of size 9, with quotient matrices R and K satisfying m_i R_ij = n_j K_ij, each point-class row sum 15 and each block-class column sum 15 for k=15, such that the 4x4 quotient is primitive (some positive integer power has all entries strictly positive) and the set of point classes is not preserved by any nontrivial automorphism of the design? A complete answer is either an explicit 36x36 (0,1)-incidence matrix with the four 9-sets, the verified tactical identities, a primitivity certificate, and a check that no nontrivial permutation automorphism preserves the partition, or a rigorous proof that no symmetric 2-(36,15,6) design admits such a primitive automorphism-free 9+9+9+9 tactical decomposition.

## Attempted claim

Does there exist a symmetric 2-(36,15,6) design, i.e. a 36-point 36-block incidence structure with every block containing 15 points and every two distinct blocks meeting in 6 points, that admits a tactical decomposition with four point classes P1,P2,P3,P4 each of size 9 and four block classes B1,B2,B3,B4 each of size 9, with quotient matrices R and K satisfying m_i R_ij = n_j K_ij, each point-class row sum 15 and each block-class column sum 15 for k=15, such that the 4x4 quotient is primitive (some positive integer power has all entries strictly positive) and the set of point classes is not preserved by any nontrivial automorphism of the design? A complete answer is either an explicit 36x36 (0,1)-incidence matrix with the four 9-sets, the verified tactical identities, a primitivity certificate, and a check that no nontrivial permutation automorphism preserves the partition, or a rigorous proof that no symmetric 2-(36,15,6) design admits such a primitive automorphism-free 9+9+9+9 tactical decomposition.

## Research outcome

Target blocked: stochastic refinement with fixed 9+9+9+9 tile margins for both admissible quotient types plateaued at row-pair energy E=300 (need E=0), the elite is a strict local minimum with zero improving single or double moves and strictly-worse kick basins, difference-set annealing in Z6xZ6 stalled at energy 36, and exact backtracking proved infeasible in the numpy-only toolchain; CLEAN_EXIT with no finding claimed.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No explicit 36x36 incidence matrix was constructed (best row-pair violation energy E=300 versus the required E=0), so no design, tactical decomposition, primitivity certificate, or automorphism-stabilizer analysis could be verified; the Menon difference-set route in Z6xZ6 independently stalled at difference energy 36 versus 0 across six seeds. The toolchain was numpy-only with no pip, ILP/SAT solver, or nauty, which ruled out exact cover and group-theoretic certificates in the available time. The completed quotient enumeration (120 solutions, 2 classes, automatic primitivity) is retained as a computational lemma in output/artifacts/enumerate_R.py but is routine rather than original. All elites, logs, and scripts are preserved under output/artifacts/ for reproducibility.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No explicit 36x36 incidence matrix was constructed (best row-pair violation energy E=300 versus the required E=0), so no design, tactical decomposition, primitivity certificate, or automorphism-stabilizer analysis could be verified; the Menon difference-set route in Z6xZ6 independently stalled at difference energy 36 versus 0 across six seeds. The toolchain was numpy-only with no pip, ILP/SAT solver, or nauty, which ruled out exact cover and group-theoretic certificates in the available time. T…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
