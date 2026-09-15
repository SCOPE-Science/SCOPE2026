# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** What is the asymptotic symmetric subrank of the F_2 corner tensor, and is it below 4?
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20203
- **Disposition:** NO_RESULT
- **Domain:** Additive Combinatorics
- **Method:** polynomial method and slice-rank bounds

## Problem

Let H_{cor,F_2} be the directed 3-uniform corner hypergraph on vertex set V=F_2 x F_2 (|V|=4) with edge set E={((x,y),(x+lambda,y),(x,y+lambda)): x,y in F_2, lambda != 0}, and let H_{cor,F_2}^{\boxtimes n} be its n-th strong power, whose independent sets are exactly the corner-free subsets of F_2^n x F_2^n. Let f_cor in (C^4)^{\otimes 3} be its adjacency tensor: (f_cor)_{i,j,k}=1 if i=j=k or (i,j,k) in E, 0 otherwise. Let Q_s denote symmetric subrank (same linear map on all three legs) and \widetilde{Q}_s(f_cor)=lim_{n\to\infty} Q_s(f_cor^{\otimes n})^{1/n} the asymptotic symmetric subrank. Determine \widetilde{Q}_s(f_cor); in particular, is \widetilde{Q}_s(f_cor)<4? Equivalently, does the symmetric-subrank tensor method yield a fixed exponent c<4 with r_{\angle}(F_2^n) <= c^{n+o(n)}, where r_{\angle}(F_2^n) is the largest corner-free subset of F_2^n x F_2^n? Only the proved direction Q_s >= \alpha / \widetilde{Q}_s >= \Theta is claimed.

## Attempted claim

Let H_{cor,F_2} be the directed 3-uniform corner hypergraph on vertex set V=F_2 x F_2 (|V|=4) with edge set E={((x,y),(x+lambda,y),(x,y+lambda)): x,y in F_2, lambda != 0}, and let H_{cor,F_2}^{\boxtimes n} be its n-th strong power, whose independent sets are exactly the corner-free subsets of F_2^n x F_2^n. Let f_cor in (C^4)^{\otimes 3} be its adjacency tensor: (f_cor)_{i,j,k}=1 if i=j=k or (i,j,k) in E, 0 otherwise. Let Q_s denote symmetric subrank (same linear map on all three legs) and \widetilde{Q}_s(f_cor)=lim_{n\to\infty} Q_s(f_cor^{\otimes n})^{1/n} the asymptotic symmetric subrank. Determine \widetilde{Q}_s(f_cor); in particular, is \widetilde{Q}_s(f_cor)<4? Equivalently, does the symmetric-subrank tensor method yield a fixed exponent c<4 with r_{\angle}(F_2^n) <= c^{n+o(n)}, where r_{\angle}(F_2^n) is the largest corner-free subset of F_2^n x F_2^n? Only the proved direction Q_s >= \alpha / \widetilde{Q}_s >= \Theta is claimed.

## Research outcome

Target blocked: asymptotic symmetric subrank of the F2 corner tensor could not be determined; all support functionals provably trivialize at 4 and remaining certificates reproduce published bounds, so a CLEAN_EXIT is filed.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Only bounded computation was available (exact exhaustion to n=2, heuristic to n=3, numeric restriction search at r=2); the upper-bound half (<4 vs =4) is obstructed by proved support-functional trivialization plus the published induced-matching barrier, and lower-bound certificates obtained (Theta>=2.88, Q_s>=2) reproduce or trail the literature and carry no originality claim.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Only bounded computation was available (exact exhaustion to n=2, heuristic to n=3, numeric restriction search at r=2); the upper-bound half (<4 vs =4) is obstructed by proved support-functional trivialization plus the published induced-matching barrier, and lower-bound certificates obtained (Theta>=2.88, Q_s>=2) reproduce or trail the literature and carry no originality claim.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
