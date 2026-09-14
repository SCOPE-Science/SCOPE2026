# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact chromatic threshold for the next binary projective space
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20040
- **Disposition:** NO_RESULT
- **Domain:** Additive Combinatorics
- **Method:** Fourier-analytic density increment and slice-rank comparison

## Problem

Let χ₂(n) be the least number of sum-free subsets needed to partition 𝔽₂ⁿ∖{0}. Determine whether χ₂(8)=5; equivalently, determine whether 𝔽₂⁸∖{0} can be partitioned into five sum-free sets and prove that it cannot be partitioned into four.

## Attempted claim

Let χ₂(n) be the least number of sum-free subsets needed to partition 𝔽₂ⁿ∖{0}. Determine whether χ₂(8)=5; equivalently, determine whether 𝔽₂⁸∖{0} can be partitioned into five sum-free sets and prove that it cannot be partitioned into four.

## Research outcome

Target chi_2(8)=5 unresolved: verified chi(4)=3, chi(5)=4, chi(6)>=4 calibration plus solver-failure diagnosis; no auditable n=8 result, so honest NO_RESULT with CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Native SAT-solver bridge in this worker wedges on every solve() call at n>=6 across all backends (environmental, not hardness); only n<=5 SAT legs plus the n=6 k=3 UNSAT leg completed. Heuristic search reached bad=1 on n=6 k=4 but no verified coloring at n>=6. The n=8 upper and lower legs are therefore unresolved.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Native SAT-solver bridge in this worker wedges on every solve() call at n>=6 across all backends (environmental, not hardness); only n<=5 SAT legs plus the n=6 k=3 UNSAT leg completed. Heuristic search reached bad=1 on n=6 k=4 but no verified coloring at n>=6. The n=8 upper and lower legs are therefore unresolved.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
