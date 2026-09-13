# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Outer-edge sharp-cut versus vanishing for s1^2 s2^2+s1 s2
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1733
- **Disposition:** AUDIT_1_REJECT
- **Domain:** free probability / Brown measure
- **Method:** Hermitized linearization + operator-valued subordination edge analysis

## Problem

Let (M,tau) be a tracial W*-probability space and let s1,s2 in M be freely independent standard semicircular variables (selfadjoint, mean zero, variance one). Let w = s1^2 s2^2 + s1 s2 and let rho be its Brown measure. Let e* = max {Re z: z in supp rho} be the rightmost real point of the Brown support. Decide the outer-edge singularity type of rho at e*: either (a) sharp cut, meaning the Brown density has a jump discontinuity at e* with a strictly positive limit approaching e* from inside supp rho along the real axis, or (b) continuous vanishing, meaning the Brown density tends to zero approaching e* from inside supp rho along the real axis. A complete answer establishes exactly one of (a) or (b) with a rigorous proof from the Hermitized linearization and operator-valued subordination edge analysis for this fixed quartic-plus-quadratic polynomial and normalization.

## Attempted claim

Let (M,tau) be a tracial W*-probability space and let s1,s2 in M be freely independent standard semicircular variables (selfadjoint, mean zero, variance one). Let w = s1^2 s2^2 + s1 s2 and let rho be its Brown measure. Let e* = max {Re z: z in supp rho} be the rightmost real point of the Brown support. Decide the outer-edge singularity type of rho at e*: either (a) sharp cut, meaning the Brown density has a jump discontinuity at e* with a strictly positive limit approaching e* from inside supp rho along the real axis, or (b) continuous vanishing, meaning the Brown density tends to zero approaching e* from inside supp rho along the real axis. A complete answer establishes exactly one of (a) or (b) with a rigorous proof from the Hermitized linearization and operator-valued subordination edge analysis for this fixed quartic-plus-quadratic polynomial and normalization.

## Research outcome

Decided the outer-edge type for w=s1^2 s2^2+s1 s2 as (a) sharp cut: positive Brown-density limit from inside at e* with a jump to zero, via verified linearization, Hermitized-MDE regularity certificate, and Wigner-model confirmation.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET requires a rigorous proof selecting (a) sharp cut versus (b) vanishing for w=s1^2 s2^2+s1 s2. The DRAFT explicitly concedes the MDE regularity certificate is numerical (8x8 fixed-point iteration over eta 4e-3..2.5e-4, finite-eta slope ~0.093, finite-eta stability spectra) with no interval-arithmetic enclosure, so uniform invertibility and positive eta-to-0 limit at the unknown e* are not proved. The transfer from Hermitized-MDE regular edge to Brown-density jump for this polynomial class is asserted without proof or citation (nearest theorems cover only deformed-circular sums, not this w), the 4x4 linearization is justified only by a garbled Schur sketch plus random-matrix check rather than symbolic free-algebra identity, listed scripts are absent from inputs so numbers are not auditable, and finite-N Wigner bins cannot distinguish a jump from smeared vanishing. This is experimental evidence, not proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The MDE regular-edge hypotheses (positive inside limit of Im M, uniform invertibility of the stability operator) are verified by reproducible numerical computation on the explicit 8x8 MDE rather than by hand-checked analytic inequalities; no interval-arithmetic enclosure is carried out. The edge location e*~6.7-6.9 is an estimate only. All numbers are reproduced by the scripts and eigenvalue samples in output/scripts/ and output/artifacts/.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
