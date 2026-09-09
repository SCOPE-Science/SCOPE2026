# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A certified semigroup hole resolving the normality flag of the 4x4x4 no-three-way toric cell
- **Round:** 2026-09-07-first-light-01
- **Lane:** 439
- **Disposition:** NO_RESULT
- **Domain:** Computational Commutative Algebra
- **Method:** Normaliz saturation and hole certification with secondary-fan regular-triangulation replay

## Problem

Resolve the openly flagged normality question for the 4x4x4 no-three-way-interaction toric semigroup (MBDB no3way-04-04-04): exhibit and certify one explicit semigroup hole with a Normaliz saturation log, and explain it with a secondary-fan regular-triangulation replay identifying the covering non-unimodular simplex — without recomputing the archived 148968-move Markov table.

## Attempted claim

The toric semigroup N A_444 of the fixed 4x4x4 no-three-way-interaction design matrix A_444 (36x64, MBDB no3way-04-04-04) is NOT normal: there exists an explicitly archived integer margin vector h-star in cone(A_444) intersected with the semigroup lattice that is not in N A_444, certified by an archived Normaliz saturation log plus exact integer-infeasibility replay, together with a logged regular triangulation T-star whose covering maximal simplex has normalized volume at least 2, resolving the database UNKNOWN normality flag to NON-NORMAL.

## Research outcome

No hole in the 4x4x4 no-three-way semigroup was certified within the hour, so neither the target nor the exact preset fallback can be claimed. Verified partial obstructions are archived instead: the column lattice is saturated (minors-gcd = 1), an explicit det=-2 simplex is empty, R2/R3 margins are fully collision-free, and R3 is exhaustively midpoint-convex (129024 pairs); every Pi point tested (degrees 8-12) had a feasible fiber. Replay with: python3 output/artifacts/verify.py (expects ALL VERIFY_OK).

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No candidate margin vector jointly satisfied cone membership and semigroup non-membership, so fallback clauses (ii)+(iv) were never jointly met.', 'Exact backtracking fiber solver timed out at degree >~10, leaving the high-degree window undecided rather than cleared.', 'No Normaliz/4ti2/ILP binaries and no pip in the environment; saturation was proved by a minors-gcd route, not a Normaliz log.', 'Topic text says 36x64 but the archived matrix is 48x64 rank 37; all work used the archived 48-row matrix.', 'No triangulation T-star was logged since no hole was found to explain.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No candidate margin vector jointly satisfied cone membership and semigroup non-membership, so fallback clauses (ii)+(iv) were never jointly met.', 'Exact backtracking fiber solver timed out at degree >~10, leaving the high-degree window undecided rather than cleared.', 'No Normaliz/4ti2/ILP binaries and no pip in the environment; saturation was proved by a minors-gcd route, not a Normaliz log.', 'Topic text says 36x64 but the archived matrix is 48x64 rank 37; all work used the archived 48-row…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
