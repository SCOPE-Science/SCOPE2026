# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Weak-glueing smoothability gap for a rank-1 series on a 3-edge genus-6 metrized complex
- **Round:** 2026-09-07-first-light-01
- **Lane:** 489
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Tropical Geometry
- **Method:** tropical Weierstrass slope-weight calculus with Amini-Baker weak-glueing smoothability test and Demazure-permutation vertex gluing

## Problem

Decide smoothability of a symmetric rank-1 degree-4 pre-limit linear series on the minimal genus-6 metrized complex with rational vertex curves attaining exactly 3 parallel edges, via the weak-glueing condition with tropical Weierstrass slope-weight logs.

## Attempted claim

Let M* be the genus-6 metrized complex with vertex curves C_a=C_b=P1 joined by exactly 3 parallel unit edges plus 2 loops at each vertex. The named symmetric rank-1 degree-4 Amini-Baker pre-limit series S* on M* either satisfies the He weak-glueing condition and hence smooths to a smooth projective genus-6 curve carrying a rank-1 degree-4 linear series (algebraic gonality at most 4), or provably violates weak glueing at a named joint edge, in which case the logged tropical Weierstrass slope-weight excess is a proved non-smoothability (realizability-gap) obstruction for this gonality cell.

## Research outcome

Binary PASS verdict: S* satisfies He weak glueing at the 3-edge joint (per-edge checks, torus-pattern match, regular sections), with tropical rank 1 and vertex Weierstrass weights 1,1 in total 9; replayable; no smoothing claimed.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Headline binary PASS itself recomputes: twisting b=0, D0=0/D1=P1+P2+P3, multivanishing (0,0), V(-D1)=0, identical 2-plane evaluation matrix B=[[1,1,1],[1,1/2,0]] on both sides so torus-support match ({{0,1},{0,2},{1,2},{0,1,2}}, no singletons verified by hand) gives He Def 3.3/Remark 3.4 PASS; replay prints VERIFY_TARGET_OK. BUT essential supporting certification is false: report claims 'tropical Baker-Norine rank of D_Gamma is exactly 1' because 'D-(a)-(m1) a-reduced (1,2,-1,0,0) unwinnable'. This is mathematically false on the modeled loopless core (vertices a,b,m1,m2,m3, E=6, V=5, g=2). By Baker-Norine Riemann-Roch any degree-4 divisor on a genus-2 graph has rank deg-g=2 (K-D has degree -2). Explicitly D-(a)-(m1)=[1,2,-1,0,0] is linearly equivalent to effective [0,1,1,0,0] via Laplacian firing f=(0,0,-1,0,0) (borrow at m1), so it IS winnable; auditor brute-force confirms all sampled degree-2 subtractions winnable. The vector [1,2,-1,0,0] is not a-reduced in the effective-away-from-root sense (negative at m1 != root), so 'uniqueness of reduced representatives implies unwinnable' is invalid. Hence vertex weights mu=D_x(x)-r=1 (which assume r=1) are wrong on the core (true r=2 gives 0), and the 'complete log verifying d-r+r*g=9' is not established: only vertex (1,1) pointwise logged, total 9 cited from AGR conditional on r=1,g=6 which is unproved for the loop-augmented object (loops omitted from chip-firing model). The exact fallback claim's certification clause therefore fails. value: Route is explicit PRESET_FALLBACK, so preset-fallback policy applies. The exact_success_criterion's binary mechanics (lengths, vanishing orders, per-edge checks, single verdict, replay) are present, but Admission's conditional value approval cannot be retained: ADMISSION_DEFECT. Admission fallback_value promised that PASS 'smooths by He/Osserman to genus-6 g^1_4 (gonality<=4)' and FAIL gives a 'proved non-smoothability obstruction via He Thm 4.7'. The draft's own Section 4 honestly proves the opposite for this (M*,S*): with n=(1,1,1), witness x=(1,-1,0) gives floor-sum 3, so d'<3 i.e. d'<=2, while d=4 violates d<=d'; He Thm 4.8/Cor 4.10 cannot be invoked and 'no smoothing or gonality claim is made'. Hence a PASS here carries no smoothability consequence (necessity without sufficiency), and no FAIL obstruction was found. What remains is a bare necessary-condition check on a symmetrically chosen identical-both-sides 2-plane (PASS automatic by construction) plus a weight log whose rank/sum-9 core is false/incomplete as above, with SBN-general hypothesis assumed and interiors unlogged. This is an isolated combinatorial datum with no proved algebraic-geometric transfer, no obstruction, no smoothing template, and no completed Weierstrass census. Under ordinary value standard it is not independently worth retrieving later; certification does not rescue it. Reopening value is not re-litigation of narrowness but correction of a materially false qualification.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Loops as vertex-genus augmentation (g=2 each) with general loop markings; joint computation on 3-edge core. SBN-general hypothesis admitted/assumed. Only vertex weights machine-certified pointwise; total 9 via cited AGR identity. No smoothing/lifting/gonality claim: He Thm 4.3(II) with n=(1,1,1) caps d'<=2 (witness x=(1,-1,0) gives floor-sum 3), so d=4 violates d<=d' and Thm 4.8/Cor 4.10 are not invoked.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
