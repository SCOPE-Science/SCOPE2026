# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Triconfluent-Heun transport Galois-Stokes dichotomy
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1363
- **Disposition:** NO_RESULT
- **Domain:** differential Galois theory
- **Method:** SL2 normal form plus Stokes and Kovacic reduction

## Problem

Let T_{s,t} be T_{s,t}(y) = y'' - (3*x^2 + s)*y' + (t*x)*y = 0 over C(x) with constants C, with parameters (s,t) in all of C^2 (triconfluent-Heun transport slice with fixed zero constant term; polynomial coefficients so the sole singularity is an unramified irregular point at infinity of rank 3 with 6 Stokes directions and generally nontrivial formal exponents). Put T_{s,t} in SL(2) normal form, compute the formal fundamental matrix at infinity (exponential parts, exponents of formal monodromy, exponential torus), the six Stokes matrices, and run the Kovacic reduction over C(x). Decide with proof for every (s,t) in C^2 the connected differential Galois group G^0(T_{s,t}): either G^0 = SL(2,C) or a named proper connected subgroup (Borel/torus/additive), giving the exact exceptional locus in the (s,t)-plane (including polynomial-solution/reducibility curves) and the Stokes-matrix witness pattern generating G^0 with the formal monodromy. A complete answer is the explicit Stokes-matrix list plus a theorem proving this SL(2,C)-versus-exceptional dichotomy with no further exceptions.

## Attempted claim

Let T_{s,t} be T_{s,t}(y) = y'' - (3*x^2 + s)*y' + (t*x)*y = 0 over C(x) with constants C, with parameters (s,t) in all of C^2 (triconfluent-Heun transport slice with fixed zero constant term; polynomial coefficients so the sole singularity is an unramified irregular point at infinity of rank 3 with 6 Stokes directions and generally nontrivial formal exponents). Put T_{s,t} in SL(2) normal form, compute the formal fundamental matrix at infinity (exponential parts, exponents of formal monodromy, exponential torus), the six Stokes matrices, and run the Kovacic reduction over C(x). Decide with proof for every (s,t) in C^2 the connected differential Galois group G^0(T_{s,t}): either G^0 = SL(2,C) or a named proper connected subgroup (Borel/torus/additive), giving the exact exceptional locus in the (s,t)-plane (including polynomial-solution/reducibility curves) and the Stokes-matrix witness pattern generating G^0 with the formal monodromy. A complete answer is the explicit Stokes-matrix list plus a theorem proving this SL(2,C)-versus-exceptional dichotomy with no further exceptions.

## Research outcome

Target blocked: full (s,t)-plane SL2-versus-exceptional Galois-Stokes dichotomy not established; partial normal-form data and one-family D_m tables only. Clean exit with obstruction preserved.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No complete Stokes-matrix list, no Kovacic case-2/case-3 elimination certificate, no dual polynomial family, and no G^0-identification proof were established; the verification script crashes before the degree-count stage and no DRAFT proof exists. The partial normal-form and one-family determinant tables are preserved in the worklog and compute.py but do not support any auditable claim.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No complete Stokes-matrix list, no Kovacic case-2/case-3 elimination certificate, no dual polynomial family, and no G^0-identification proof were established; the verification script crashes before the degree-count stage and no DRAFT proof exists. The partial normal-form and one-family determinant tables are preserved in the worklog and compute.py but do not support any auditable claim.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
