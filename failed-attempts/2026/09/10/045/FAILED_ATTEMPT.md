# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Integral points on y^2 = x^5 - 4x + 1 via Chabauty-Coleman and Mordell-Weil sieve
- **Round:** 2026-09-07-first-light-01
- **Lane:** 613
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Diophantine Geometry
- **Method:** Chabauty-Coleman p-adic integration with Mordell-Weil sieve and canonical-height comparison

## Problem

Determine all integral (Z) points on the affine genus-2 curve C: y^2 = x^5 - 4x + 1 (Jacobian J of Mordell-Weil rank 1 to be certified in-hour) by an explicit from-scratch Chabauty-Coleman p-adic integration at a good prime plus a Mordell-Weil sieve eliminating surplus residue disks, with canonical-height comparison; if the full list does not close, isolate a certified height-bound gap witness sharply constraining the remaining points.

## Attempted claim

The Jacobian J(Q) of C: y^2 = x^5 - 4x + 1 has rank 1 (generator to be certified by 2-descent), and the complete set of integral points on the affine model C is exactly the explicit logged list L containing (0,1) and (0,-1), proved by a from-scratch Chabauty-Coleman zero bound at a logged good prime combined with a Mordell-Weil sieve certificate eliminating all other residue classes.

## Research outcome

From-scratch arithmetic anchor for y^2=x^5-4x+1: prime discriminant -259019 with good reduction at 7; Jacobian orders #J(F3)=29 (prime), 36, 81, 237, 222 at p=3,5,7,11,13; infinite-order divisor D=[(0,1)-inf] so rank>=1; torsion in {1,Z/3}; bounded integral search to |x|<=5000 and new rational point (1/4,1/32). Full integral list and Coleman disk bound not claimed.

## Why this attempt failed

Failed axes: value.

value: EMERGENT_FINDING carries no preset-value presumption and fails the ordinary value standard. What is proved is a routine arithmetic anchor: prime discriminant, five J(Fp) orders by brute force, rank>=1 lower bound from one reduction, torsion restricted only to {1,Z/3} (not pinned), a box search to an unexplained cutoff |x|<=5000, and one small-height point (1/4,1/32). Nothing closes a residue class, determines rank, bounds any Coleman disk, or completes any list -- the admitted valuable fallback's defining feature (permanent Strassman-1 exclusion reusable as a lemma) is absent. J(Fp) orders are recomputable in milliseconds by any CAS and have negligible retrieval value; the rank-lower/torsion lemmas are textbook reduction exercises; the |x|<=5000 bound is an arbitrary scope with no mathematical interpretation (classic unexplained enumeration); (1/4,1/32) is a single denominator-4 point with no interpretation, tiny unmotivated gain. Generic 'reusable by any future determination' does not distinguish this from any intermediate computation. The exact-invariant clause does not rescue it: the invariants are mechanically implied by seconds-scale counting and the object/parameter choices (5 primes, box 5000) are not motivated before computation. Intrinsic low value + arbitrary scope + missing substantive result => value FAILS.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Rank=1 equality NOT proved (no 2-descent/Selmer upper bound available in lane); no Coleman expansion of the true annihilating differential and no Strassman bound produced; bounded search is a box certificate only, not a completeness proof; genus-2 Weil/Cantor steps assume the standard odd-degree hyperelliptic theory cited in DRAFT.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
