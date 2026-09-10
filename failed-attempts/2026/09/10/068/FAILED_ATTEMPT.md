# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Four-point SDP closure of the tabulated 28--29 gap for equiangular lines at arccos(1/5) in R^14
- **Round:** 2026-09-07-first-light-01
- **Lane:** 665
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Combinatorics
- **Method:** Four-point semidefinite programming dual with interval enclosure plus Seidel interlacing cross-check

## Problem

Fix n=14 and alpha=1/5. Let N_1/5(14) be the maximum number of lines through the origin in R^14 with pairwise angle arccos(1/5). Greaves et al. 2016 Table 4 records N_5(14)=28--29 with a known 28-line construction, and no triaged four-point, pillar, or k-point SDP source closes the row. Produce an interval-enclosed four-point SDP dual certifying N_1/5(14)<=28 with a Seidel interlacing cross-check, plus an exact PSD replay of a 28-line Gram matrix to establish equality.

## Attempted claim

N_1/5(14)=28: an explicit interval-enclosed alternative four-point SDP dual has a logged enclosure verifying dual feasibility and certifying N_1/5(14)<=28, and an explicit 28x28 Gram matrix with unit diagonal, off-diagonal +-1/5, rank at most 14, and exact integer-LDL-verified positive semidefiniteness realizes 28 equiangular lines at angle arccos(1/5) in R^14.

## Research outcome

Target N_1/5(14)=28 and preset fallback N_1/5(14)<=28 both blocked in-lane on the same core: the <=28 certificate requires an interval-enclosed four-point SDP dual, but the lane has no SDP solver and the strongest solver-free tiers provably plateau above 28 (exact Delsarte-LP optimum 336/11 to degree 12, ceiling 31; classical closed-form floor 30). Three bounded fallback attempts logged; CLEAN_EXIT with no original increment.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No SDP solver (scipy/cvxpy/cvxopt/mosek/pyscipopt) available or installable in-lane; exact four-point dual route unrunnable', 'Kao-Yu alternative four-point block data for (14,1/5) not reconstructible in-lane on the clock', 'No exact 28x28 Gram assembled (Tremain/Lin-Yu patterns not machine-extractable from fetched HTML); tightness half unclosed in-lane']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No SDP solver (scipy/cvxpy/cvxopt/mosek/pyscipopt) available or installable in-lane; exact four-point dual route unrunnable', 'Kao-Yu alternative four-point block data for (14,1/5) not reconstructible in-lane on the clock', 'No exact 28x28 Gram assembled (Tremain/Lin-Yu patterns not machine-extractable from fetched HTML); tightness half unclosed in-lane']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
