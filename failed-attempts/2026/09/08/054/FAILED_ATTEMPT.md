# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Eliahou-number formula under numerical-semigroup gluing with a certified negative-Eliahou glued family beyond the genus-100 Wilf-verified frontier
- **Round:** 2026-09-07-first-light-01
- **Lane:** 154
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Semigroup Theory
- **Method:** gluing arithmetic with exact Eliahou-number and Wilf-function evaluation

## Problem

For a gluing C = k1*A join k2*B of numerical semigroups A, B (coprime multipliers k1 in B\G(B), k2 in A\G(A) with gcd(k1,k2)=1 in the Delorme-Rosales sense), derive and certify an exact closed formula for the Eliahou number E(C) in terms of the Wilf functions, conductors, genera and Eliahou numbers of A and B plus (k1,k2); instantiate it on a fixed catalog of small base pairs (A0,B0) over all admissible coprime multiplier pairs with k1<=K1, k2<=K2 (bounds committed by Research, e.g. K1,K2 in [20,60]) and certify an explicit parametric subfamily whose members have E(C)<0 and genus g(C)>100, with the least-genus member above 100 exhibited as the beyond-frontier witness with full generator, gap, and invariant logs.

## Attempted claim

A proved exact gluing formula E(k1*A join k2*B) = F(E(A),E(B),W_A,W_B,c,g,k1,k2) (closed integer expression in base Wilf-function values, conductors, genera and multipliers), machine-checked on the committed base-pair catalog, plus at least one explicit infinite parametric glued subfamily (fixed A0,B0, one multiplier fixed, the other varying over an arithmetic progression preserving the gluing conditions) all of whose members satisfy E<0 with genus growing unboundedly past 100, and one fully certified least member with g>100 given by minimal generators, Frobenius number, genus, multiplicity, embedding dimension, concentration, Wilf ratio and negative Eliahou number with exact-integer replay logs.

## Research outcome

Proved + machine-checked (345/345) closed Eliahou-number gluing formula; proved fixed-base both-growing rays with e_A+e_B>=3 drive E to +infinity (refuting the target infinite negative ray as stated except the A=B=N ray with E=0 constant); delivered 255-row certified glued table all beyond genus 100 (g<=2438) with reusable auditor.

## Why this attempt failed

Failed axes: value.

value: Admitted headline required a proved E-gluing propagation formula plus an infinite parametric E<0 glued family past genus 100 with a certified least witness g>100. Delivered is the opposite: both-growing fixed-base rays provably drive E->+infinity (refuting the target ray as stated except the trivial A=B=N E=0 ray), ~10,500 evaluations find zero E<0 (min +612), and the 255-row 'beyond-frontier' table is all-positive (E 1056-8417) with zero flagged negatives. Remaining assets: (a) Theorem 1 is definitional substitution (apply E-definition to known gluing generators + known Rosales data; does not express E(C) in E(A),E(B) as promised, still needs base generator lists) derivable in minutes by anyone knowing both inputs; (b) Theorem 2 is a 5-line quadratic-dominance corollary of (a), unsurprising large-gluing positivity, ruling out one search direction but proving no general E>=0 criterion (explicitly conjectural) and no single-ray result; (c) 255-row sampled (non-exhaustive, k<=40, five arbitrary small bases) all-positive table whose precise entries (e.g. g=2438,E=8417 at <8,11,13>x<9,13,14>,37,39) are arbitrary pairs no future researcher would need as distinguished data, with no negative near-miss test cases for concentration/highly-dense/Farey programs. This is a missing substantive result (no witness, no general positivity proof) plus arbitrary-scope enumeration, not a retrievable exact invariant of a pre-motivated distinguished object. Certification alone does not rescue it.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Target infinite negative-E ray NOT delivered: disproved for both-multipliers-growing for all fixed bases except A=B=N (E=0 constant ray, verified E=0 e.g. <5,7>,<6,11>,<37,39>); single-ray case conjectural (evidence-only). E>=0 for all gluings conjectured, not proved. Catalog is a sampled multiplier window (k<=40), not exhaustive; all-positive table (no E<0 witness). Corrected topic Jq endpoint prose [c,c+m]->[c,c+m-1].

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
