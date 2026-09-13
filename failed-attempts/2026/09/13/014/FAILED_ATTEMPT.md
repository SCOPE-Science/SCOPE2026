# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Generic degree-8 first-order versus finite gap witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1493
- **Disposition:** AUDIT_1_REJECT
- **Domain:** rigid origami local rigidity theory
- **Method:** rigidity Jacobian rank plus second-order obstruction

## Problem

Fix a generic flat-foldable degree-8 single-vertex crease pattern with sector angles theta1..theta8 in cyclic order summing to 2pi, alternating sum pi, each strictly between 0 and pi, all eight pairwise distinct, no two consecutive summing to pi, and no further algebraic relation among them. Consider mountain-valley assignments with |M-V|=2 that are combinatorially flat-foldable. Decide whether there exists at least one such assignment that is first-order flexibly rigid-foldable (non-trivial infinitesimal rigid folding velocity exists) but admits no finite continuous rigid folding motion from the flat state, i.e. a second-order-locked gap witness, versus proving that first-order flexibility implies finite rigid foldability for every valid assignment in this generic class. A complete answer is either an explicit angle vector plus assignment plus a rank certificate of the rigidity Jacobian and a proof of no finite branch, or a proof that the gap never occurs for this generic scope.

## Attempted claim

Fix a generic flat-foldable degree-8 single-vertex crease pattern with sector angles theta1..theta8 in cyclic order summing to 2pi, alternating sum pi, each strictly between 0 and pi, all eight pairwise distinct, no two consecutive summing to pi, and no further algebraic relation among them. Consider mountain-valley assignments with |M-V|=2 that are combinatorially flat-foldable. Decide whether there exists at least one such assignment that is first-order flexibly rigid-foldable (non-trivial infinitesimal rigid folding velocity exists) but admits no finite continuous rigid folding motion from the flat state, i.e. a second-order-locked gap witness, versus proving that first-order flexibility implies finite rigid foldability for every valid assignment in this generic class. A complete answer is either an explicit angle vector plus assignment plus a rank certificate of the rigidity Jacobian and a proof of no finite branch, or a proof that the gap never occurs for this generic scope.

## Research outcome

Proved the first-order vs finite gap exists: explicit generic degree-8 angles plus assignment (--+++++-) with certified infinitesimal flexibility but rigorously no finite rigid folding branch (gap radius 8.4e-4).

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET-route proof fails on its essential geometric inference. Independently recomputed: J rank 2 and J/B analytic formulas check out (numeric Jacobian matches; mixed-stencil gives 2B confirming the corrected B=sin/4; in-plane Hessian is zero; angle sums/genericity margins check out). But the closed sign cone C={Jw=0, s.w>=0} for s=(--+++++-) is NOT the ray R+{r}. Full vertex enumeration over all 56 five-active-bound systems (2 Jacobian + section + 5 zeros) yields 6 feasible section vertices, e.g. zero-sets (0,1,3,4,5),(0,1,3,4,7),(0,1,3,5,7),(0,1,4,5,7),(0,3,4,5,7),(1,3,4,5,7), all with |Jw|~1e-16 and s.w=1. The claimed wstar is a strict convex combination of them (coeffs ~0.14,0.16,0.20,0.14,0.17,0.19, residual ~2e-15). Facet sections are not all {0}: e.g. the (0,1,3,4,5) vertex has w0=0 and lies in the facet-0 section, so facet-0 is nonempty. Q is indefinite on C: Q/unit is -0.124 to +0.128 across vertices and attains both signs (up to +0.17 and -0.09) at interior points with strict-sign margin, versus claimed uniform Q(r)~0.0256. Hence the Lyapunov-Schmidt domination and compactness step (limit direction must be a multiple of r) is invalid. The interval certificate enumerated the wrong family (28 pin-6-coordinate systems, which indeed has 1 feasible point) instead of true polytope vertices, so its cone=ray and facet-kill claims certify nothing about C.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The 'no further algebraic relation' genericity clause is covered by openness/stability rather than by direct verification on the exhibited decimals: the certificate uses only listed open conditions plus strict inequalities, so it persists on an open angle neighborhood containing fully generic points. The gap radius 8.4e-4 is conservative (analytic remainder constant is ~4x loose vs measured third derivatives). Interval trigonometry is a from-scratch implementation (Taylor order 25 with Lipschit…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
