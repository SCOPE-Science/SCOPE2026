# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Extremal transference constant for cyclotomic ideals
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1695
- **Disposition:** NO_RESULT
- **Domain:** geometry of numbers
- **Method:** transference bounds and small-ideal minima enumeration

## Problem

Prove or disprove the following extremal transference claim. With notation as in (1), let F be the family of all nonzero integral ideals a of Z[zeta_m] over all m=2^k, k>=3, embedded as L=sigma(a) with the same trace norm, and L^* its Euclidean dual. Claim: sup_{L in F} lambda_1(L)*lambda_1(L^*)/n <= 1/(2*pi*e)+o(1) as n->infinity, i.e. no cyclotomic ideal family attains Banaszczyk order n/(2*pi), and the optimal universal constant for this structured family is at most half the general-lattice constant. Scope is all integral ideals in the 2-power tower. A complete answer is a proof of the uniform upper bound with an explicit constant strictly below 1/(2*pi) for all large n, or an explicit infinite ideal subfamily with computed minima violating it and approaching the general bound.

## Attempted claim

Prove or disprove the following extremal transference claim. With notation as in (1), let F be the family of all nonzero integral ideals a of Z[zeta_m] over all m=2^k, k>=3, embedded as L=sigma(a) with the same trace norm, and L^* its Euclidean dual. Claim: sup_{L in F} lambda_1(L)*lambda_1(L^*)/n <= 1/(2*pi*e)+o(1) as n->infinity, i.e. no cyclotomic ideal family attains Banaszczyk order n/(2*pi), and the optimal universal constant for this structured family is at most half the general-lattice constant. Scope is all integral ideals in the 2-power tower. A complete answer is a proof of the uniform upper bound with an explicit constant strictly below 1/(2*pi) for all large n, or an explicit infinite ideal subfamily with computed minima violating it and approaching the general bound.

## Research outcome

Target blocked: uniform transference bound over all 2-power cyclotomic ideals could be neither proved nor disproved within the pass; enumeration timed out, analytic bounds overshoot by a factor of 2, and the normalization was ambiguous, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The result is limited by the missing equation-(1) normalization, the exponential cost of unreduced shortest-vector enumeration which already timed out at dimension 8, and the lack of a uniform ideal-theoretic lemma closing the factor-2 gap between naive Hermite bounds and the claimed constant; no statement is made about the truth or falsity of the extremal transference claim itself.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The result is limited by the missing equation-(1) normalization, the exponential cost of unreduced shortest-vector enumeration which already timed out at dimension 8, and the lack of a uniform ideal-theoretic lemma closing the factor-2 gap between naive Hermite bounds and the claimed constant; no statement is made about the truth or falsity of the extremal transference claim itself.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
