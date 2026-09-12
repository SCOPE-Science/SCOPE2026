# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Vol-Det inequality over twist number at most seven
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1178
- **Disposition:** NO_RESULT
- **Domain:** hyperbolic 3-manifolds
- **Method:** augmented-link parents with certified volumes and determinant counts

## Problem

Prove or disprove the Vol-Det inequality vol(S^3\L) < 2*pi*log(det(L)) for every hyperbolic alternating link L admitting a connected prime reduced alternating diagram D with twist number t(D) at most 7, excluding (2,n)-torus diagrams, where vol is the complete finite-volume hyperbolic volume and det is the link determinant equal to the spanning-tree count of a checkerboard graph of D. A complete answer is either a rigorous proof of the strict inequality for every such link, reducing via twist-region augmentation to finitely many fully augmented parents with certified Dehn-filling volume monotonicity and exact determinant counts, or one explicit prime reduced alternating diagram D with t(D)<=7 together with a certified hyperbolic volume and an exact determinant violating the inequality.

## Attempted claim

Prove or disprove the Vol-Det inequality vol(S^3\L) < 2*pi*log(det(L)) for every hyperbolic alternating link L admitting a connected prime reduced alternating diagram D with twist number t(D) at most 7, excluding (2,n)-torus diagrams, where vol is the complete finite-volume hyperbolic volume and det is the link determinant equal to the spanning-tree count of a checkerboard graph of D. A complete answer is either a rigorous proof of the strict inequality for every such link, reducing via twist-region augmentation to finitely many fully augmented parents with certified Dehn-filling volume monotonicity and exact determinant counts, or one explicit prime reduced alternating diagram D with t(D)<=7 together with a certified hyperbolic volume and an exact determinant violating the inequality.

## Research outcome

Vol-Det inequality over twist number at most 7 remains unresolved: universal volume bounds provably fail to imply it, the augmented-parent route needs unavailable certified tooling and enumeration, and the small-diagram sieve found no violating candidate, so the lane exits clean with no auditable claim.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No certified interval-volume engine (SnapPy/Sage), no network, and no exhaustive Conway-polyhedron parent enumeration were available, so neither the per-pattern tail constants nor the finite core could be rigorously certified; small-knot volumes used were published approximations, explicitly non-certificates; no counterexample candidate was found and no original structural increment emerged.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No certified interval-volume engine (SnapPy/Sage), no network, and no exhaustive Conway-polyhedron parent enumeration were available, so neither the per-pattern tail constants nor the finite core could be rigorously certified; small-knot volumes used were published approximations, explicitly non-certificates; no counterexample candidate was found and no original structural increment emerged.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
