# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Hessian-rank WLP failure at the compressed codimension-4 socle-7 Gorenstein boundary
- **Round:** 2026-09-07-first-light-01
- **Lane:** 595
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** Macaulay inverse-system duality with Hessian-rank criteria and Jordan-type decomposition

## Problem

Decide a weak-Lefschetz boundary cell for standard-graded Artinian Gorenstein algebras of codimension 4 and socle degree 7 over a characteristic-zero field: settle WLP for the compressed Hilbert-function cell via an explicit Macaulay dual generator and its Hessian-rank/Jordan-type certificate.

## Attempted claim

There exists a standard-graded Artinian Gorenstein k-algebra A=R/Ann(F) with R=k[x1,x2,x3,x4], k a characteristic-zero field, F in k[y1,y2,y3,y4]_7 homogeneous of degree 7, such that: (i) A has Hilbert function (1,4,10,20,20,10,4,1); (ii) the third Hessian determinant hess^3(F) vanishes identically; (iii) for the explicitly logged linear form l, the multiplication map x l : A_3 -> A_4 has rank at most 19 < 20; hence A fails the Weak Lefschetz Property in middle degree.

## Research outcome

Target blocked on the built route: on the bigraded (3,4) ansatz, every verified det(B30)=0 solution (30 one-row linear solves + 29 spread-pattern nsolve points + exact relation rechecks; artifacts/det_verify3.log) collapses to N-rank 3 with catalecticant ranks (4,10,19), never the compressed (4,10,20). Bounded fallback probe for H'=(1,4,7,10,10,7,4,1) also blocked (4/4 trials give (4,8,12), no A0). CLEAN_EXIT per 45-minute directive; no emergent finding claimed.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

det(B30)=0 => N-rank<=3 collapse is a 62-point sampled conjecture, not a theorem; det(B21)=0 block and mixed-ansatz routes unbuilt; fallback family probe covers only one G+L family with 4 trials; computations exact over QQ via sympy differentiation-rank linear algebra.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: det(B30)=0 => N-rank<=3 collapse is a 62-point sampled conjecture, not a theorem; det(B21)=0 block and mixed-ansatz routes unbuilt; fallback family probe covers only one G+L family with 4 trials; computations exact over QQ via sympy differentiation-rank linear algebra.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
