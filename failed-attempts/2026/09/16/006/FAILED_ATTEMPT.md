# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Are stacked cross-polytopal spheres extremal for the linear strand of balanced normal pseudomanifolds?
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20445
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** local-cohomology and squarefree Grobner degeneration analysis

## Problem

Let d >= 4, k >= 2, and let Delta be a (d-1)-dimensional balanced normal pseudomanifold over a field F with f_0(Delta) = kd vertices. Let Gamma be any stacked cross-polytopal (d-1)-sphere in ST^x(kd,d). Is it true that for every i >= 0, beta_{i,i+1}(F[Delta]) <= beta_{i,i+1}(F[Gamma]), where beta_{i,i+1}(F[Gamma]) = (k-2)*C(d(k-1),i+1) - (k-1)*C(d(k-2),i+1) + d(k-1)*C(d(k-2),i-1) ?

## Attempted claim

Let d >= 4, k >= 2, and let Delta be a (d-1)-dimensional balanced normal pseudomanifold over a field F with f_0(Delta) = kd vertices. Let Gamma be any stacked cross-polytopal (d-1)-sphere in ST^x(kd,d). Is it true that for every i >= 0, beta_{i,i+1}(F[Delta]) <= beta_{i,i+1}(F[Gamma]), where beta_{i,i+1}(F[Gamma]) = (k-2)*C(d(k-1),i+1) - (k-1)*C(d(k-2),i+1) + d(k-1)*C(d(k-2),i-1) ?

## Research outcome

Target blocked and cleanly exited: the stacked cross-polytopal extremality claim for the full linear strand could be neither proved nor disproved within bounds; Gamma formula verified computationally and no target-adjacent alternative passed the independent Audit bar.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The investigation could not close the uniform higher-slice upper bound the target requires: general missing-edge bounds are too weak by factors of 3-9 on the extremal example itself, partition bounds point the wrong way, and deletion induction fails on non-pure deletions. All computational searches and rival constructions are retained in output/artifacts for future work with stronger machinery.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The investigation could not close the uniform higher-slice upper bound the target requires: general missing-edge bounds are too weak by factors of 3-9 on the extremal example itself, partition bounds point the wrong way, and deletion induction fails on non-pure deletions. All computational searches and rival constructions are retained in output/artifacts for future work with stronger machinery.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
