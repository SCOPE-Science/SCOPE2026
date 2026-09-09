# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Deciding one wall for twice the (-1)-class in the Kuznetsov component of a cubic threefold
- **Round:** 2026-09-07-first-light-01
- **Lane:** 366
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Homological Algebra
- **Method:** tilt-stability wall-crossing with Bogomolov-Gieseker inequalities and Fourier-Mukai symmetry analysis

## Problem

Let Y be a smooth cubic threefold over C and Ku(Y) its Kuznetsov component with Serre-invariant Bridgeland stability conditions. Fix a (-1)-class a in N(Ku(Y)) whose sigma-stable objects are classified, and set v=2a. Decide the outermost tilt-induced wall for class v: list destabilizing sequences and determine (non)existence of sigma-stable objects of class v on each side, with a moduli-point identification where stable.

## Attempted claim

For Ku(Y) of a smooth cubic threefold and class v=2a (twice a (-1)-class), the outermost candidate tilt wall is a genuine wall: on one side there are no sigma-stable objects of class v (every object is destabilized by an explicit triangle with factors of class a), and on the other side sigma-stable objects of class v exist and M_sigma(v) is identified via extension moduli of the classified (-1)-objects.

## Research outcome

Certified one tilt wall fragment for the imprimitive class v=2a in Ku of a cubic threefold: exact wall equation a^2+(b-5/6)^2=(1/6)^2 for destabilizer type F01 with proportional-lift no-wall lemma, transverse slope-crossing certificate, and BG exclusion list, all replayable via stdlib artifacts. Fallback-grade partial theorem; tilt-to-Ku transfer explicitly excluded.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Replayed both scripts: hrr_check.py passes (HRR_OK) and tilt_wall.py wall polynomials reproduce exactly. The numerical wall polynomial for (E0,F_{0,1}) is correct: -9*A-9*b^2+15*b-6=0 i.e. A+(b-5/6)^2=(1/6)^2, real arc b in (2/3,1). Slope equality at (A,b)=(1/48,3/4) with value -1/12 and order flip at A+/-1/100 verified exactly. Proportional-lift no-wall (0,0 gives empty polynomial) verified. However essential inferences fail: (1) Delta_H(E0) is misstated as 12; exact recomputation gives d1^2-6*r*d2 = 0-6*2*(-2)=24, so Lemma/Theorem premise wrong. (2) 'Outermost within window' is false: (1,1) gives C=7/6 R^2=25/36 (max A=25/36~0.69, b-interval (1/3,2)) which strictly dominates (0,1) max A=1/36~0.028; (0,2) gives same circle as (0,1). Draft Sec.5 claims outermost certified within |m|,|n|<=2, contradicted by its own table. (3) No genuine destabilizer exhibited: only numerical equality numE*denF-numF*denE=0 plus mu_H<b slope inequality. F_{0,1}=(2,3,1/2) is only a K-theory class a0+[O(1)]; no object in Coh^b(Y) nor extension triangle A->E->B in the tilt heart is constructed. Draft Sec.5 admits triangle after [1]-shift 'not yet certified' and Ku-projection 'not carried out'. Hence 'genuine tilt destabilizer type' and 'destabilizer-versus-empty dichotomy' are unproved. (4) BG lemma as stated ('in the window these are exactly (1,2),(2,1),(2,2)') is false without rank qualifier: Delta_H<0 occurs for 8 pairs including (-2,-2),(-2,-1),(-2,0),(-1,-2),(-1,-1); the 'exactly three' holds only for r_F>0. Rank-0 real walls (0,-1),(0,-2) coincide with the headline circle but are unmentioned. (5) Fallback requires either one sigma-stable object or one proved-empty wall with destabilizing triangle becoming strictly semistable on wall; neither is delivered and tilt-to-Ku transfer plussigma-stability/moduli ID are expressly disclaimed. Numerical lemmas are proved; headline wall-verdict/chamber claim is not. value: Strongest honestly proved item is an elementary tilt numerical wall for arbitrarily chosen Db(Y) representatives: E0=2[I_l]=(2,0,-2) and F_{0,1}=a0+[O(1)]=(2,3,1/2). This does not qualify under the narrow-datum exception: (a) object not natural invariant of Ku class v=2a — depends on convenient lift and on (m,n)=(0,1) choice; same circle arises from (0,-1),(0,-2), larger circle from (1,1) in same window, and draft admits true outermost could use different lift of v; (b) value mechanically implied by textbook formula numE*denF-numF*denE=0 once representatives fixed — 3-line Fraction arithmetic, plus classical Delta>=0 and mu_H<b check; (c) no future Ku/Torelli/Ulrich/hyperkahler use possible without the disclaimed Bayer induction/restriction, Ku-projection triangle, sigma-stability on either side, or moduli ID; draft states no claim on M_sigma(2a) and consistency with Li et al nonemptiness. The |m|,|n|<=2 window is arbitrary scope with unexplained enumeration; BG list for three r>0 cases is direct textbook exclusion. Fallback of one certified…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Outermost-ness certified only within the |m|,|n|<=2 lift window and for the model lift E0=2[I_line]; different Db(Y)-lifts of v could give other walls. Destabilizer F01 has rank 2 (non-proportional lift of Ku-class a), so the wall is not a literal a+a sheaf sequence; Ku-projection/triangle and tilt-to-sigma transfer are not carried out. No claim on M_sigma(2a) (non)emptiness or full chamber decomposition; consistent with Li et al. nonemptiness.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
