# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Generic accessory-parameter Schwarzian triviality
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1343
- **Disposition:** AUDIT_2_REJECT
- **Domain:** functional transcendence and DCF model theory
- **Method:** Schwarzian linearisation plus Ax-Lindemann and Kovacic

## Problem

Work in a saturated differentially closed field of characteristic zero U with derivation delta and constant field C. Fix distinct a1,a2,a3 in Q and let lambda be transcendental over Q. Let R_lambda(y) be the rational function with double poles exactly at a1,a2,a3,infinity whose accessory parameter equals lambda, and let X_lambda={y in U: (y'''/y')-(3/2)(y''/y')^2+R_lambda(y)(y')^2=0, y'!=0} be the Schwarzian equation of the four-punctured sphere with generic accessory parameter. Prove or disprove that X_lambda is strongly minimal and geometrically trivial, i.e. orthogonal to C and to the Manin kernel of every simple abelian variety over acl(Q,a,lambda,t) not descending to C. A complete answer is a rigorous proof that X_lambda has Morley rank 1, plus either (a) a forking-calculus and Ax-Lindemann-type witness that any three distinct nonalgebraic solutions are independent and that no nonconstant definable correspondence to C or to any Manin kernel exists, or (b) an explicit definable witness of non-orthogonality to C or to a named Manin kernel.

## Attempted claim

Work in a saturated differentially closed field of characteristic zero U with derivation delta and constant field C. Fix distinct a1,a2,a3 in Q and let lambda be transcendental over Q. Let R_lambda(y) be the rational function with double poles exactly at a1,a2,a3,infinity whose accessory parameter equals lambda, and let X_lambda={y in U: (y'''/y')-(3/2)(y''/y')^2+R_lambda(y)(y')^2=0, y'!=0} be the Schwarzian equation of the four-punctured sphere with generic accessory parameter. Prove or disprove that X_lambda is strongly minimal and geometrically trivial, i.e. orthogonal to C and to the Manin kernel of every simple abelian variety over acl(Q,a,lambda,t) not descending to C. A complete answer is a rigorous proof that X_lambda has Morley rank 1, plus either (a) a forking-calculus and Ax-Lindemann-type witness that any three distinct nonalgebraic solutions are independent and that no nonconstant definable correspondence to C or to any Manin kernel exists, or (b) an explicit definable witness of non-orthogonality to C or to a named Manin kernel.

## Research outcome

Proved branch (a) with repaired Section 6: generic four-punctured-sphere Schwarzian X_lambda is strongly minimal, strictly disintegrated, orthogonal to constants and all Manin kernels.

## Why this attempt failed

Failed axes: correctness.

correctness: Lemma 1 normal form is correct: conditions sum c_i=0, sum c_i a_i=-1 follow from s^2 R->1/2 expansion and give a 1-dim accessory line; direction b!=0 verified. Lemma 2 Kovacic computation is correct and was re-executed green: r=-R/2 has exact order-2 poles at a1,a2,a3,oo with b=-1/4 uniformly lambda-independent, Case1 d=1/2-3/2=-1, Case2 d=(2-6)/2=-2, Case3 d=(6-18)/m<0, so no Liouvillian solutions and (via BB1) Galois group SL2; strong-minimality step via CFN criterion is then plausible. BUT the headline strict-disintegration claim is FALSE as stated: the draft's own script proves exactly 4 puncture-stabilizer maps preserve R_lambda identically for all lambda, and independent re-computation confirms the three nontrivial double-transposition Klein-4 maps (e.g. for (0,1,2): 2(y-1)/(y-2), (y-2)/(y-1), 2/y, and analogously for (0,1,7),(0,2,5),(1,2,3)) satisfy R(m(y))m'(y)^2-R(y)=0 identically, so y|->m(y) sends solutions to distinct algebraically dependent solutions, refuting 'any n distinct nonalgebraic solutions are independent' and 'any two distinct are independent'. The draft's dismissal of V4 as not giving a relation is mathematically wrong. Further, Section 6a properness proof is incomplete: F_k affine-linear in lambda is correct, but E_delta!=(0) for every discrete datum delta is asserted not proved; only quadratic phi(y)=y^2 is machine-checked, pole-count does not rule out d>1 Belyi preimages with 4 parabolic poles, and the sentence claiming fixed-delta pullbacks have constrained monodromy whereas the accessory line is monodromy-Zariski-dense by Lemma 2 is false since pullbacks of SL2 hypergeometric bases also have Zariski-dense SL2 monodromy. Hence orthogonality to C and Manin kernels is not established. ADMISSION_DEFECT: topic branch (a) literally demands any three distinct nonalgebraic solutions independent, which is impossible for this family due to the obvious fixed V4 symmetry, so the admitted success criterion was mis-specified.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Imports published black boxes with exact numbers (Kovacic Cases 1-3; CFN Thm 1.2/Cor 5.6, Prop 5.8+Fact 5.7; BFS Thm 5.6+Prop 5.7; DFN Thm 1.1-1.2) without re-proof. SymPy checks run on representative triple (0,1,2); uniformity follows from the displayed normal-form expansion. The representative triple has harmonic cross-ratio, so its puncture stabilizer is D4 of order 8 with a fixed V4 preserving R_lam identically; this finite fiber-permuting symmetry does not yield any correspondence to C or…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
