# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Extremal syzygy witness for a five-section rank-2 bundle on a general genus-7 curve
- **Round:** 2026-09-07-first-light-01
- **Lane:** 917
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Geometry
- **Method:** Koszul cohomology plus limit linear series comparison

## Problem

Attach to a general member E of the genus-7 locus B(2,L,5) with det of degree 14 an explicit projective model and determine its extremal Koszul cohomology distinguishing it from line-bundle Brill-Noether syzygies.

## Attempted claim

For C general of genus 7 and E general in B(2,L,5) with deg det E=14, the associated projective model has K_{2,1} nonzero of the stated rank r>=3 while K_{3,1}=0, giving the extremal Betti shape predicted by the rank-2 maximal-rank program; the table is certified by an explicit Macaulay2 free resolution with semicontinuity to the general member.

## Research outcome

Target blocked and cleanly exited: the genus-7 degree-14 five-section extremal Betti witness requires an explicit graded resolution that no available engine can compute; BN numerics were checked but yield no certifiable result.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No Macaulay2, Singular, Sage, Magma, GAP, or PARI engine is installed locally and no pip module is present; the single bounded remote SageCell probe returned no usable output. Without a graded-resolution engine the explicit K_{2,1}/K_{3,1} Betti certification, stability check, and semicontinuity transfer required by the audit plan cannot be grounded, and hand-computed Betti numbers would fail reproducibility.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No Macaulay2, Singular, Sage, Magma, GAP, or PARI engine is installed locally and no pip module is present; the single bounded remote SageCell probe returned no usable output. Without a graded-resolution engine the explicit K_{2,1}/K_{3,1} Betti certification, stability check, and semicontinuity transfer required by the audit plan cannot be grounded, and hand-computed Betti numbers would fail reproducibility.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
