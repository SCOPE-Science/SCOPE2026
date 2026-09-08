# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp Ehrhart-positivity threshold along the White p=2 diagonal of empty 3-simplices
- **Round:** 2026-09-07-first-light-01
- **Lane:** 261
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Discrete Geometry
- **Method:** signed-triangulation lattice-point enumeration with Ehrhart-reciprocity and floor-sum coefficient analysis

## Problem

For the White p=2 diagonal W_k = conv{(0,0,0),(1,0,0),(0,0,1),(2,2k+1,1)}, k >= 1 (empty, normalized volume 2k+1), establish the exact sharp Ehrhart-positivity cutoff: prove the linear Ehrhart coefficient c1(k) is strictly decreasing in k and identify the unique integer K* such that c1(k) > 0 for k < K* and c1(k) <= 0 for k >= K*, with full Ehrhart/h* rows and width-1 certificates replayed from committed vertices.

## Attempted claim

Over the infinite White diagonal W_k defined above, the linear Ehrhart coefficient c1(k) admits a closed floor-sum form, is strictly decreasing, and changes sign exactly once at a run-determined integer K*, giving a sharp Ehrhart-positivity/non-positivity threshold for this natural empty-simplex class, supported by reciprocity-checked Ehrhart/h* rows and width-1 witnesses replayed from committed vertices.

## Research outcome

Proved exact Ehrhart polynomial for the infinite White p=2 diagonal W_k, giving strictly decreasing linear coefficient c1(k)=(11-2k)/6 with unique positivity cutoff K*=6, with emptiness, width-1, and h* corollaries and a replayable stdlib verifier.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline closed form and K*=6 are substantively identical to long-known empty-tetrahedron facts, not a new diagonal-specific boundary. Ferroni-Higashitani survey arXiv:2307.10852 Example 2.4 gives the Reeve Ehrhart polynomial with linear coefficient (11-q)/6 and flags negativity at q=12; Remark 2.6 states 3D empty simplices all have h* of the form 1+qx^2 (empty iff h1=hd=0). Via the standard identity E(x)=sum h_j C(x+3-j,3), stated in the same survey, this mechanically implies L(t)=C(t+3,3)+(q-1)C(t+1,3) and c1=(12-q)/6 for ANY empty tetrahedron of normalized volume q. White 1964 (via Iglesias-Santos background) already gives emptiness and width-1 for W_k. Independent check by the auditor: brute lattice counts for apex (p,q,1) with p=1 vs p=2 at the same q coincide for q=3..13, t=1..3, confirming the Ehrhart polynomial sees only q, so the p=2 diagonal adds no Ehrhart content over the classical Reeve ladder. Solving (12-(2k+1))/6<=0 to get K*=6 is elementary algebra on the known volume-determined coefficient, i.e. parameter substitution to the odd subsequence q=2k+1. No prior source prints the integer label K*=6, but a label/timestamp absence does not establish priority; the substance is implied. The nearest HNF, sign-pattern, and multi-width sources are disjoint, but the Reeve/White general facts cover the claim. value: Textbook restatement plus mere parameter substitution with no independently retrievable delta. The result is a corollary of the known volume-determinacy of empty-tetrahedron Ehrhart polynomials: once h*=(1,0,q-1,0) is known, c1(k), the monotonicity step -1/3, and the cutoff K*=6 follow by expanding binomials and solving a linear inequality. The object (p=2 diagonal) is natural as an empty class and the positivity program is genuinely motivating, but the invariant value IS mechanically implied by published formulas, so it fails the narrow-datum exception which requires the value to be not known or mechanically implied. A future researcher needing c1 for any empty tetrahedron of volume q would use the general formula, not a p=2-diagonal table. Certification (9900-point agreement, brute recounts, reciprocity) does not rescue a volume-forced number. Falls under reject categories: textbook restatement, parameter substitution (odd-volume subsequence), and relabeling of the classical Reeve q-around-11/12 zero-crossing as K*=6.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Threshold is for the linear coefficient c1 along this specific White p=2 diagonal only; says nothing about other coefficients, other White classes, or higher dimensions. Proof is elementary enumeration, not a new method.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
