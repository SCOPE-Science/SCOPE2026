# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Support-restricted L2 stability at short-root zonotopes
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1485
- **Disposition:** NO_RESULT
- **Domain:** convex geometry
- **Method:** mixed volumes and mixed area measures

## Problem

Prove or disprove the following support-restricted L2 stability bound for the Alexandrov-Fenchel deficit at short-root zonotopes. For each n in {4,5,6}, let Z_n in R^n be the short-root zonotope of type C_n in standard Bourbaki coordinates, defined as the Minkowski sum of the segments [-g,g] over all positive short roots g = e_i - e_j and e_i + e_j (1 <= i < j <= n); for n=4 also allow the F4 short-root zonotope defined analogously from its 24 short roots. Fix the reference tuple C=(Z_n,...,Z_n) with n-2 copies and let S(C,.) be its mixed area measure on S^{n-1}. Claim: there exists an explicit constant c(n) > 0 depending only on n such that for every origin-symmetric convex body K in R^n normalized by Vol_n(K)=Vol_n(Z_n)=1, the Alexandrov-Fenchel deficit Delta(K) = V(K,Z_n,C)^2 - V(K,K,C)*V(Z_n,Z_n,C) satisfies Delta(K) >= c(n) * min_{a>0, v in R^n} integral over S^{n-1} of (h_K(u) - a*h_{Z_n}(u) - <v,u>)^2 dS(C,.)(u), where h denotes support functions, so the distance is measured in L2(S(C,.)) and hence only on the support of S(C,.). A complete answer either proves this bound with a stated explicit c(n) in ranks 4, 5 and 6, or gives a rigorous counterexample (a body K or sequence with positive support-restricted distance violating the bound for every positive c(n)).

## Attempted claim

Prove or disprove the following support-restricted L2 stability bound for the Alexandrov-Fenchel deficit at short-root zonotopes. For each n in {4,5,6}, let Z_n in R^n be the short-root zonotope of type C_n in standard Bourbaki coordinates, defined as the Minkowski sum of the segments [-g,g] over all positive short roots g = e_i - e_j and e_i + e_j (1 <= i < j <= n); for n=4 also allow the F4 short-root zonotope defined analogously from its 24 short roots. Fix the reference tuple C=(Z_n,...,Z_n) with n-2 copies and let S(C,.) be its mixed area measure on S^{n-1}. Claim: there exists an explicit constant c(n) > 0 depending only on n such that for every origin-symmetric convex body K in R^n normalized by Vol_n(K)=Vol_n(Z_n)=1, the Alexandrov-Fenchel deficit Delta(K) = V(K,Z_n,C)^2 - V(K,K,C)*V(Z_n,Z_n,C) satisfies Delta(K) >= c(n) * min_{a>0, v in R^n} integral over S^{n-1} of (h_K(u) - a*h_{Z_n}(u) - <v,u>)^2 dS(C,.)(u), where h denotes support functions, so the distance is measured in L2(S(C,.)) and hence only on the support of S(C,.). A complete answer either proves this bound with a stated explicit c(n) in ranks 4, 5 and 6, or gives a rigorous counterexample (a body K or sequence with positive support-restricted distance violating the bound for every positive c(n)).

## Research outcome

Target blocked in both directions at n=4: exact zonotope computation across rays, dense scans, extreme shapes, and a 24-mode tangent Hessian found no counterexample (ratio floor ~434, local gap ~861), but a proved explicit constant needs quantitative global stability machinery beyond session reach; clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proved bound or counterexample is claimed: all gap figures (scan floor ~434, Hessian floor ~861) are numerical evidence without chamber certification or interval arithmetic, the K-subset-P(y) reduction sketch relies on a cited AF equality characterization rather than a self-contained proof, and ranks 5 and 6 plus the F4 variant were not computationally explored; the positive finding is only that exact computation strongly suggests the claimed stability bound is true with an explicit constant of order 0.04 under volume-1 normalization.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proved bound or counterexample is claimed: all gap figures (scan floor ~434, Hessian floor ~861) are numerical evidence without chamber certification or interval arithmetic, the K-subset-P(y) reduction sketch relies on a cited AF equality characterization rather than a self-contained proof, and ranks 5 and 6 plus the F4 variant were not computationally explored; the positive finding is only that exact computation strongly suggests the claimed stability bound is true with an explicit constant…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
