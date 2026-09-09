# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Defect-eleven inversion monotonicity and a refined staircase-cell upper bound below 13.5 for 1324-avoiders
- **Round:** 2026-09-07-first-light-01
- **Lane:** 370
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Combinatorics
- **Method:** analytic combinatorics of generating functions with singularity transfer and insertion-encoding / staircase-decomposition structural analysis

## Problem

Let a(n,k) be the number of 1324-avoiding permutations of length n with k inversions. Using the Linusson-Verkama injection f sqcup g and Meng's residual/skeleton framework (defect d=k-2n+7, skeleton length<=8d+25, quadratic block-size equation), decide the inversion-monotonicity inequality at the next open layer k=2n+4 (defect 11) and convert any proved step, together with a refined splittable-vs-simple staircase/domino cell decomposition, into a proved exponential upper bound on |Av_n(1324)| strictly below 13.5.

## Attempted claim

Prove a(n,k)<=a(n+1,k) for all k<=2n+4 (defect d<=11) by classifying R_{11,n} via the skeleton reduction, and derive from the refined staircase/domino decomposition an explicit proved exponential upper bound gr(Av(1324))<=13.49 (audit threshold: any explicit constant strictly below 13.5 with certified rounding counts as success).

## Research outcome

Consolidated the strongest verifiable fragment: a dual-engine exact inversion-refined census of Av(1324) to n=12 with LV-transfer audit and sharpness certificates (VERIFY_OK). The defect-11/sub-13.5 target remains open; claimed only the certified finite census plus window checks, sharply separated from conjecture.

## Why this attempt failed

Failed axes: value.

value: Target claim (defect-11 k<=2n+4 monotonicity + proved gr<=13.49) admittedly not proved; none of the predefined valuable fallbacks achieved (DRAFT p.44: F1 |R3| polynomial NOT derived, no R11 classification, no sub-13.5 bound, needs Meng skeleton theory beyond budget). Remaining headline is a finite-window census to arbitrary cutoff n<=12: V3 window monotonicity (231 cells) proves no infinite statement; V4 re-checks the known LV identity on 52 cells; V5 re-certifies the published LV sharpness example; full rows extend LV k<=12 print to k<=66 but without skeleton-sum closed form, cell equation, singularity bound, or downstream use. Table supplies raw residual data but not the motivated invariant (F1 polynomial / F2 cell singularity / F3 simple gridded obstruction). This is an unexplained enumeration / arbitrary scope with missing substantive result under the shared standard: a future researcher testing defect-11 needs arbitrarily large n, not a(12,k) spot values. Certification alone does not rescue it. No bounded value-only addition can supply the missing R3 formula or defect-11 proof without new research direction, so not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Finite-window census only: proves no infinite-family statement. Defect-11 monotonicity (k<=2n+4), R_{11,n} classification, any sub-13.5 growth bound, and the exact |R_3| polynomial (fallback F1 closed form) are NOT proved; the table supplies residual data but not the skeleton-sum formula. Full n<=12 rows extend LV printed slices (k<=12) but overlap OEIS marginals by design (used as anchors, not claimed novel).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
