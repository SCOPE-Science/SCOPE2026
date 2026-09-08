# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified trapping annulus and period-amplitude enclosure for the Van der Pol limit cycle at mu=1
- **Round:** 2026-09-07-first-light-01
- **Lane:** 171
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Ordinary Differential Equations
- **Method:** validated Taylor-model ODE integration with Poincare-return annulus verification

## Problem

Certify the Van der Pol limit cycle at mu=1 with an explicit forward-invariant annulus and validated two-sided period/amplitude bounds that strictly improve on the harmonic approximation.

## Attempted claim

For x'' - (1-x^2)x' + x = 0 (mu=1), i.e. x' = y-(x^3/3-x), y' = -x: there exists a logged polygonal annulus A (vertices listed) proved forward-invariant by interval sign checks of field-dot-normal on every edge, containing exactly one periodic orbit; its period T satisfies a two-sided interval [L,U] with U-L <= 0.05 and its x-amplitude satisfies a two-sided interval of width <= 0.1 that is disjoint from the harmonic predictions (amplitude 2, period 2pi) by a logged positive margin, all replayable from the validated Taylor-model integrator remainders.

## Research outcome

Certified forward-invariant rational octagonal annulus for VdP mu=1 enclosing the unique limit cycle, with rigorous transit-time upper bound T<106.16; full-chain exact stdlib verifier passes. Two-sided period/amplitude enclosure deferred.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Replayed inputs/artifacts/verify_annulus.py in Python 3.12.3: exit 0 ALL PASS. Outer sups [-4.6919,-0.1611,-0.0522,-0.2620]x2 <0 (N=40 Lipschitz grid, exact Fractions, L=3|h3|+2|h2|+|h1| valid); inner infs [0.01722,0.01111,0.00246,0.01053]x2 >0 (N=60); O convex CCW, I convex CCW, origin strictly in I, all I verts strictly in O — all pass. Hence strict transversality/nesting/forward-invariance/existence (Poincare-Bendixson, equilibrium-free since unique equilibrium (0,0) in hole) are computationally sound, corner cases implicitly covered because bounds are over closed edges. Two essential defects remain. (1) Uniqueness proof note is false as written: with F(x)=x^3/3-x, F(1)=-2/3, not 0; positive zero is sqrt(3)~1.732, not a=1; claim 'F<0 on (0,1), F>0 increasing for x>1' is false (e.g. F(1.5)=-0.375). True Liénard conclusion (at most one cycle, a=sqrt(3)) still holds but stated derivation is wrong. (2) Item 5 (every closed trajectory T<=530779/5000) proof is invalid: 'A closed curve in a convex body is no longer than its perimeter' is false in general — a wiggly/simple-indented closed curve inside a convex body can be arbitrarily longer than the body perimeter (perimeter monotonicity gives perim(hull)<=perim(O), while length(gamma)>=perim(hull), yielding no upper bound on length(gamma)). No convexity of the limit cycle is proved. Hence the 106.16 transit bound is asserted without valid proof (numerically true since true T~6.6, but proof != truth). Minor gaps: gap(x)<=1 used for Lg=2(Sm+1) not logged (provable: |h|<=0.481, |y|<=0.41 so gap<1); continuum h(x) in [L(x),U(x)] for |x|<0.2 needed for |F|^2>=max(x^2,gap^2) only checked on grid, not propagated by explicit Lipschitz margin. Because an essential claimed inequality lacks valid proof and a proof note is false, correctness FAILS. originality: The strong target (two-sided period U-L<=0.05 plus amplitude width<=0.1 disjoint from harmonic predictions with logged margin via validated Taylor-model integrator) would be substantively new, but DRAFT explicitly disclaims it: 'No two-sided period/amplitude enclosure and no harmonic-separation witness: the validated-integrator leg was not completed.' What is actually proved is the fallback: existence of an explicit forward-invariant octagonal annulus enclosing the unique VdP mu=1 cycle plus a coarse one-sided transit bound. That existence is textbook Lienard theory (Lienard 1928; e.g. Perko/Strogatz/Guckenheimer-Holmes construction of a trapping annulus for Van der Pol to apply Poincare-Bendixson, plus uniqueness). Logging one specific rational octagon (outer ~2.87x3.47, inner ~0.4) whose inward/outward pointing follows from dominant-cubic-at-infinity and unstable-focus-linear-part estimates is an arbitrary instantiation of that textbook construction, not a substantive new object or method. Cited nearest works (Lopez et al. 0806.1634 non-rigorous homotopy amplitude; Gimeno et al. 2111.06391 DDE perturbation assuming ODE cycle; Szczelina-Zgl…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Fallback-level claim only: no two-sided period/amplitude intervals (U-L<=0.05 target unmet), no harmonic-separation witness; transit bound T<106.16 is one-sided and weak; uniqueness via analytic Lienard theorem, not validated contraction.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
