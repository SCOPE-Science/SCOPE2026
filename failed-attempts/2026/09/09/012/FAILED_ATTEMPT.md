# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified integral-spectrum census of connected cubic graphs to 14 vertices with minimal cospectral witness and Hoffman gaps
- **Round:** 2026-09-07-first-light-01
- **Lane:** 307
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Spectral Graph Theory
- **Method:** exact integer characteristic-polynomial computation with equitable-partition cospectrality check and Cauchy-interlacing replay

## Problem

Produce a certified integral-spectrum census of all connected cubic graphs with even n<=14: exact adjacency characteristic polynomials and integral/non-integral verdicts, the smallest-order non-isomorphic cospectral pair in the slice with an equitable-partition certificate, and a Hoffman-ratio-bound gap table, all replayable from committed adjacency matrices in exact integer arithmetic with Cauchy-interlacing checks.

## Attempted claim

The complete connected-cubic n<=14 census (even n=4..14) has exact characteristic-polynomial logs and integral verdicts reproducing exactly the known 13 cubic integral graphs in-slice, identifies the explicit smallest-order non-isomorphic cospectral pair in the slice with an equitable-partition certificate, and tabulates Hoffman-bound residuals from extreme eigenvalues.

## Research outcome

Certified exact integral-spectrum census of all 8 connected cubic graphs n<=8 with Hoffman residuals and interlacing replay (VERIFY_OK), proving no cospectral pair at n<=8, plus Petersen/Heawood benchmark rows; full n<=14 census explicitly out of scope.

## Why this attempt failed

Failed axes: value.

value: Strongest self-contained headline actually delivered is an 8-class n<=8 census (not the admitted 621-class n<=14 census with smallest cospectral pair and Hoffman-gap table). Six of ten rows are textbook restatements: K4, K3,3, triangular prism, Q3, Petersen {3,1^5,(-2)^4}, Heawood (x-3)(x+3)(x^2-2)^6 spectra and their Hoffman tightness are classical. Only four n=8 non-integral polynomials are non-textbook, each an 8x8 integer determinant instantly reproducible by any CAS from the edge list. Scope n<=8 is explicitly tool-limited (n=10 timed out without nauty/geng) rather than the natural historic <=14 boundary; it captures only 4 of the 13 integral cubics so cannot cross-check the classification, and the fallback's smallest-pair witness is missing (proved absent <=8, minimum if any at n>=10 undelivered). The negative no-pair-at-n<=8 observation with 8 graphs is trivial once polynomials are computed and is already implied by broader cospectral enumerations (general graphs to 12 vertices; smallest regular pairs quartic). As a Ramanujan/integral benchmark or ratio-bound sharpness check the n<=8 table is too small to be reasonably needed later (cf. larger certified censuses at n=10-18). Certification is correct but does not rescue arbitrary truncation and missing substantive result. Hence independently not worth retrieving.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Scope n<=8 only, not the n<=14 (621-class) target -- n=10 run timed out (~9 min) without geng/nauty; no smallest cospectral pair exhibited (proved absent at n<=8, minimum if any is at n>=10); numeric eigenvalues auxiliary only; isomorphism by exact backtracking valid at n<=8.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
