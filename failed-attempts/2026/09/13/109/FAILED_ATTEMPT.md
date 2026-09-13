# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Connectedness of Brown support for s1^2-s2^2+s1 s2
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1732
- **Disposition:** NO_RESULT
- **Domain:** free probability / Brown measure
- **Method:** Hermitized linearization + operator-valued subordination

## Problem

Let (M,tau) be a tracial W*-probability space and let s1,s2 in M be freely independent standard semicircular variables (selfadjoint, mean zero, variance one). Let r = s1^2 - s2^2 + s1 s2 and let nu be its Brown measure. Decide whether the support of nu is connected. A complete answer either proves supp nu has exactly one connected component or proves supp nu has at least two connected components separated by a positive distance, with a rigorous proof from the Hermitized linearization and operator-valued subordination equations for this fixed indefinite-quadratic polynomial and normalization.

## Attempted claim

Let (M,tau) be a tracial W*-probability space and let s1,s2 in M be freely independent standard semicircular variables (selfadjoint, mean zero, variance one). Let r = s1^2 - s2^2 + s1 s2 and let nu be its Brown measure. Decide whether the support of nu is connected. A complete answer either proves supp nu has exactly one connected component or proves supp nu has at least two connected components separated by a positive distance, with a rigorous proof from the Hermitized linearization and operator-valued subordination equations for this fixed indefinite-quadratic polynomial and normalization.

## Research outcome

Target blocked: corrected linearization and extensive Dyson/GUE numerics suggest one connected Brown-support component, but no rigorous proof route survives, so clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Finite-eps floating-point Dyson scans and a finite-size GUE surrogate suggest connected support but do not constitute a proof: no validated enclosure, no certified eps-to-zero limit, a failed crude contraction bound, and unproved edge exclusion. These limits prevent any CLAIMED result under Audit.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Finite-eps floating-point Dyson scans and a finite-size GUE surrogate suggest connected support but do not constitute a proof: no validated enclosure, no certified eps-to-zero limit, a failed crude contraction bound, and unproved edge exclusion. These limits prevent any CLAIMED result under Audit.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
