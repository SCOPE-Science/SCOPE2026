# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quadratic Mahler stability around the 4-simplex
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1173
- **Disposition:** NO_RESULT
- **Domain:** Mahler conjecture stability
- **Method:** volume-product and polar-volume estimates

## Problem

Prove or disprove that the following explicit Mahler volume-product stability fragment holds for non-symmetric polytopes in R^4. Let S subset R^4 be a regular simplex with centroid at the origin and volume |S| = 1, and let P range over convex polytopes in R^4 with centroid at the origin, at most 8 vertices, volume |P| = 1, with polar P^circ = {y : sup_{x in P} <x,y> <= 1}. Let d(P,S) = inf_{A in GL(4), z in R^4} d_H(P, A(S)+z) with d_H Hausdorff distance. Then |P||P^circ| >= |S||S^circ| + (1/10)*d(P,S)^2 whenever d(P,S) <= 1/2. A complete answer is either a rigorous proof of this inequality with the stated constant 1/10 and threshold 1/2, or an explicit polytope P in the stated class with verified volumes |P|,|P^circ| and distance d(P,S) violating the inequality.

## Attempted claim

Prove or disprove that the following explicit Mahler volume-product stability fragment holds for non-symmetric polytopes in R^4. Let S subset R^4 be a regular simplex with centroid at the origin and volume |S| = 1, and let P range over convex polytopes in R^4 with centroid at the origin, at most 8 vertices, volume |P| = 1, with polar P^circ = {y : sup_{x in P} <x,y> <= 1}. Let d(P,S) = inf_{A in GL(4), z in R^4} d_H(P, A(S)+z) with d_H Hausdorff distance. Then |P||P^circ| >= |S||S^circ| + (1/10)*d(P,S)^2 whenever d(P,S) <= 1/2. A complete answer is either a rigorous proof of this inequality with the stated constant 1/10 and threshold 1/2, or an explicit polytope P in the stated class with verified volumes |P|,|P^circ| and distance d(P,S) violating the inequality.

## Research outcome

Target blocked: 2000-body search found no volume-product violator, and the remaining explicit quadratic stability proof needs open-level R^4 Mahler machinery beyond this pass. Clean exit with no claim.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proof or disproof of the target inequality was obtained. The disproof search covered only 2000 sampled bodies, and the computational pipeline provably overcounts non-simplicial facets (cube volume 37.33 versus exact 16), so even the one-sided survey signal is partially unreliable. No independently valuable emergent result was produced.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proof or disproof of the target inequality was obtained. The disproof search covered only 2000 sampled bodies, and the computational pipeline provably overcounts non-simplicial facets (cube volume 37.33 versus exact 16), so even the one-sided survey signal is partially unreliable. No independently valuable emergent result was produced.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
