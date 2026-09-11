# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Subpolynomial counting and toric unlikely-intersection finiteness on an explicit restricted-exponential Pfaffian leaf
- **Round:** 2026-09-07-first-light-01
- **Lane:** 781
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Mathematical Logic
- **Method:** Pila-Wilkie counting transfer with Ax-Schanuel for exp

## Problem

Fix the restricted exponential Pfaffian leaf L_exp = {(x,y,exp(x),exp(x*y)) : (x,y) in (0,1)^2} in R_exp. Prove a subpolynomial transcendental count and deduce a toric Manin-Mumford-type finiteness fragment for its atypical intersections via Ax-Schanuel for exp.

## Attempted claim

For T>=1, N(L_exp^{trans},T) <= C0 * T^{1/8} with C0 logged explicitly from Pfaffian complexity (order 2, degree (2,1)), and L_exp contains only finitely many maximal atypical points lying on proper algebraic-subgroup translates of G_m^2 outside the weakly special locus {x=0} union {rational-linear relations identified in proof}.

## Research outcome

Proved the full target on L_exp={(x,y,exp(x),exp(xy))}: order-2 degree-(2,1) Pfaffian chain logged, effective Pila-Wilkie instantiated at eps=1/8 with pedigree C0=max(1,C_BJST), sharp vanishing N=0 via Hermite-Lindemann, weakly special locus {x=0} U rational horizontal lines via elementary real solve, 0 (hence finite) maximal atypical points off locus with Ax-Schanuel cited for completeness. Replay script VERIFY_OK.

## Why this attempt failed

Failed axes: value.

value: FAIL: textbook restatement + mere parameter substitution with vacuous threshold and arbitrary scope, even though correct and literally new. Load-bearing content is: (i) N=0 from Hermite-Lindemann (nonzero rational x => exp(x) transcendental, hence irrational) — undergraduate textbook corollary, mechanically implied for any similar leaf, strictly stronger than the claimed T^{1/8} bound; (ii) locus y=-a/b from real e^t=1 iff t=0 and x>0 — elementary algebra; (iii) torsion avoidance from positivity — elementary. The framed machinery is decorative: effective Pila-Wilkie invoked but never needed (any C0 works once N=0; numeral of C_BJST explicitly not computed by design); Ax-Schanuel cited only to certify completeness already proved elementarily; Dobrowolski explicitly confirmatory only. eps=1/8 is arbitrary (any eps>0 holds with same proof); leaf (exp(x),exp(xy)) has no pre-computation literature identity or recognized-question necessity beyond being constructed as a convenient vanishing example — (0,1)^2 and rational-line locus are intrinsic only after the arbitrary leaf choice. No complexity-explicit numeral, no non-vanishing counting, no height-comparison finiteness, no census, no downstream theorem uses the threshold; claimed reusable threshold lemma saves only differentiation (format logging) and does not transfer to adjacent non-vanishing leaves where work would actually be needed. This is exactly the excluded class: textbook implication + arbitrary single-leaf parameter instantiation + unexplained narrow datum whose value is already superseded by N=0. Narrow-datum allowance does not rescue it: object was not motivated before computation in the literature, value was mechanically implied by LW/real-exp facts, and no future researcher needs C0*T^{1/8} when N=0 is proved in the same draft. Intrinsic low value / arbitrary scope, not a presentation gap.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: C0's numeral is not recomputed: existence/effectivity is by citation of BJST at the logged format; inequality replay uses sharp value N=0 with witness C0=1. Ax-Schanuel, Lindemann-Weierstrass, Dobrowolski-type bound are cited black boxes (exact references in DRAFT), not reproved. Dobrowolski comparison is confirmatory only; load-bearing finiteness is the exact count 0. No numeric search beyond replay script.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
