# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Null polarity with 4x24 automorphism for (96,20,4)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1708
- **Disposition:** NO_RESULT
- **Domain:** combinatorial design theory
- **Method:** Kramer-Mesner orbit-matrix with polarity constraint

## Problem

For symmetric 2-(96,20,4) designs (v=96, k=20, lambda=4, order n=16): determine whether there exists such a design admitting a null polarity and an automorphism of order 24 whose point orbits and block orbits are each four orbits of length 24. A complete answer either exhibits a 96x96 incidence matrix satisfying the 2-(96,20,4) equations together with an explicit order-24 automorphism with the stated 24+24+24+24 orbit partition and a null polarity commuting with it up to conjugacy, verified by row/column sums, pair intersections, and absolute-point incidence, or proves by exhaustive enumeration of all Kramer-Mesner orbit matrices for that orbit partition and polarity constraint that none lifts to a full design, with the orbit-matrix list and tactical decomposition log as certificate.

## Attempted claim

For symmetric 2-(96,20,4) designs (v=96, k=20, lambda=4, order n=16): determine whether there exists such a design admitting a null polarity and an automorphism of order 24 whose point orbits and block orbits are each four orbits of length 24. A complete answer either exhibits a 96x96 incidence matrix satisfying the 2-(96,20,4) equations together with an explicit order-24 automorphism with the stated 24+24+24+24 orbit partition and a null polarity commuting with it up to conjugacy, verified by row/column sums, pair intersections, and absolute-point incidence, or proves by exhaustive enumeration of all Kramer-Mesner orbit matrices for that orbit partition and polarity constraint that none lifts to a full design, with the orbit-matrix list and tactical decomposition log as certificate.

## Research outcome

Target not completed: the 4x24 Kramer-Mesner level was fully classified (48 orbit matrices) and verified by script, but lifting to a full symmetric 2-(96,20,4) design with null polarity and order-24 automorphism proved computationally out of reach; the order-12 refinement sieve admits 49536 refinements and gives no obstruction, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No full 96x96 design, automorphism, or polarity was constructed, and no exhaustive no-lift certificate was completed. Verified pieces are limited to the 48-matrix orbit classification, one single-row difference-set witness, and H-refinement survival counts that show the subgroup sieve does not obstruct. The C12-level and full four-row searches were not exhausted, so neither existence nor nonexistence is decided.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No full 96x96 design, automorphism, or polarity was constructed, and no exhaustive no-lift certificate was completed. Verified pieces are limited to the 48-matrix orbit classification, one single-row difference-set witness, and H-refinement survival counts that show the subgroup sieve does not obstruct. The C12-level and full four-row searches were not exhausted, so neither existence nor nonexistence is decided.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
