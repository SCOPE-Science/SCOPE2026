# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Unbounded Seifert-versus-slice gap with ribbon witnesses in a single-twist extension family of 8_20
- **Round:** 2026-09-07-first-light-01
- **Lane:** 267
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Low-Dimensional Topology
- **Method:** Parameterized Seifert-matrix block induction with SNF/Alexander-degree growth plus propagating ribbon-band slice certificate

## Problem

Let D_m be the single-twist-region full-twist extension family built from the frozen 8_20 seed diagram by a fixed explicit insertion rule (m>=0, D_0 = 8_20). Prove Seifert genus g(D_m) = 2+m by parameterized Seifert-matrix block SNF-rank plus Alexander-degree induction, and prove smooth slice genus g_4(D_m) = 0 for all m by one propagating ribbon-band certificate (signature identically 0), establishing unbounded Seifert-minus-slice gap with ribbon witnesses.

## Attempted claim

For the frozen single-twist-region extension family D_m of the 8_20 seed (DT insertion rule fixed at Research start, D_0 = 8_20 = 4 8 -12 2 -14 -6 -16 -10, crossings 8+2m), Seifert genus g(D_m) = 2+m for all m>=0 by block Seifert-matrix SNF-rank plus Alexander-degree induction, while smooth slice genus g_4(D_m) = 0 for all m by an explicit propagating ribbon-band construction with identically vanishing Murasugi signature — hence Seifert-minus-slice gap m+2 diverging to infinity with ribbon witnesses.

## Research outcome

Partial finite-family theorem salvaged after computation refuted the infinite slice half: exact Alexander-span growth (4+2m), genus lower bounds (2+m), determinants (10m+9) for m=0..4, with Fox-Milnor nonslice witnesses for m=1,2,3.

## Why this attempt failed

Failed axes: value.

value: Strongest headline is a finite enumeration: Alexander polynomials/spans/dets for five explicitly frozen 3-braid words (m=0..4) + textbook lower bounds g>=2+m + determinant-nonsquare nonslice for m=1,2,3. This is intrinsic low value: (a) No exact genus (only 2g>=span lower bound), no slice genus, no ribbon, no infinite theorem; admitted infinite divergence (g=2+m vs g4=0 with ribbon) is explicitly disclaimed and refuted by the same data (19,29,39 nonsquare => not slice). Admitted fallback (Seifert genera 3,4,5 with slice 0 and DT/SNF/ribbon) is not delivered; a different weaker fallback is substituted, so admission value case does not transfer. (b) Mere parameter substitution + unexplained enumeration: objects are ad hoc braid words where the insertion site was selected after a 36-case scan to produce growth (post-hoc), not motivated before computation; no knot names, DT codes, primeness, minimality, or above-range-as-knot-type proof; c(m) is diagram length. Exhibiting three more nonsquare-det nonslice knots (infinitely many exist) and four Burau evaluations does not advance the recognized Seifert-vs-slice gap question, which required large gap WITH sliceness. Pattern beyond m=4 is stated conjecture only. (c) Narrow-datum rescue fails: object/invariant were not motivated before computation independent of the refuted gap, values are mechanically produced by the standard Burau formula, and a future researcher has no reason to retrieve the precise Alexander of these unidentified words. Certification alone does not rescue an arbitrary object. Hence correct and new but independently not worth finding later.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Finite family m<=4 only; genus equality not proved (lower bounds only); sliceness of K_4 undecided; pattern beyond m=4 is conjecture; no DT/Seifert-matrix/ribbon-band/signature certificates; seed row values known from KnotAtlas.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
