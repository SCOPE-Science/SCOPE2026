# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Maximal volume and h*-unimodality census for reflexive 3-polytopes with at most 14 lattice points
- **Round:** 2026-09-07-first-light-01
- **Lane:** 146
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Discrete Geometry
- **Method:** lattice-point enumeration with regular-triangulation h*-vector computation and Ehrhart-series cross-check

## Problem

Survey the class C = {reflexive lattice 3-polytopes P with |P cap Z^3| <= 14} up to unimodular equivalence: produce a certified complete list with committed vertex lists, compute every h*-vector by regular triangulation cross-checked against Ehrhart counts to dilation 6, record a per-polytope unimodality-gap table, and identify one maximal normalized-volume witness.

## Attempted claim

Over the class C of reflexive lattice 3-polytopes with at most 14 lattice points (up to GL(3,Z)-equivalence), the maximum normalized volume equals an explicit integer V* attained at an explicit vertex matrix P*, and every other P in C satisfies Vol(P) <= V* - g for a committed integer gap g >= 1, with each h*-vector verified by regular triangulation and Ehrhart-series agreement to dilation 6.

## Research outcome

Complete certified census of the <=14-point reflexive 3-polytope window: 1943 classes, closed form V=2n-6 and h*=(1,n-4,n-4,1), all unimodal, max volume V*=22 (413-fold, witness KS-167) with gap g=2, Ehrhart cross-checked to dilation 6 with independent stdlib replay passing.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: the entire headline closed form is mechanically implied by textbook prior theory plus KS headers already containing M. Derivation: for any 3D lattice polytope L(k)=sum_{i=0..3} h*_i C(k+3-i,3) with h*_0=1, so at k=1, L(1)=4*1+h*_1, i.e. h*_1=n-4 where n=|P cap Z^3|, with no computation. Hibi's theorem for reflexive/Gorenstein polytopes gives h* palindromic (h*=(1,a,a,1)), so h*_2=h*_1=n-4 automatically. Hence h*=(1,n-4,n-4,1), V=sum(h*)=2n-6, L(k) rows, palindromicity and unimodality of (1,a,a,1) with a=n-4>=1 (1<=a>=1) are all forced. V is strictly increasing in n, so max on n<=14 is at n=14 (V*=22), runner-up n=13 (V=20), gap g=2, and 413-way tie = exactly the 413 headers with M=14. Verified empirically that V=2n-6 and h*=(1,n-4,n-4,1) hold for all 4319 KS records (0 failures), confirming generality. KS hep-th/9805190 supplies the M-headers/baseline; Braun-Davis 1403.5378 (unimodality open in general) and Bruns-Roemer math/0508392 (conditional g-theorem) plus Hibi palindromicity supply the theory. The per-n window counts are a direct count of KS M-headers, not a new window-completeness proof. Admission claim that palindromicity 'does not mechanically imply V*/g' is false for the reasons above. No prior search or timestamp establishes priority; substantive comparison shows database repackaging + textbook corollary. value: FAIL: even if correct, the result is a textbook restatement and arbitrary finite slice with no independently retrievable new invariant. Because V=2n-6 and h*=(1,n-4,n-4,1) follow from Hibi + L(1) formula for every reflexive 3-polytope (confirmed on all 4319), restricting to n<=14 adds no new extremal or census insight; the general fact covers the window. The 'maximal witness' is not an extremal discovery: volume is a strictly monotone function of n, so V* just restates '14 is the largest n in the window' and the 413-way tie (all n=14 polytopes share V=22) dissolves headline strength. The ten L-rows are mechanically generated from n via the closed form (recomputed in seconds). No motivated downstream researcher needs this precise table beyond reading KS M-headers + applying Hibi; no new criterion, benchmark separation, or toric-Fano/mirror-symmetry use depends on the 1943-row enumeration. Certification (recount==header, dilation-6 agreement) alone does not rescue an arbitrary cutoff or unexplained number per the standard. The valuable general theorem (Hibi) already exists; this is its parameter substitution.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Regular-triangulation h* leg failed (291/1943) and is excluded; h* evidence is Ehrhart-series route only.', 'Maximal volume ties 413 ways; witness committed but uniqueness not claimed.', 'Rigidity proved by exhaustive replay, not general theory.', 'Completeness relative to published KS archive (recount-anchored), no new proof of 4319.', 'Prior work/all4319.json voided (truncated source + wrong volume formula).']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
