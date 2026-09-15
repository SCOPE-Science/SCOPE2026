# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Positive-proportion small gaps between low-lying zeros of Dirichlet L-functions to a fixed prime modulus
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20232
- **Disposition:** NO_RESULT
- **Domain:** Analytic Number Theory
- **Method:** mollified moment and ratio-conjecture analysis

## Problem

Assume GRH for all primitive Dirichlet L(s,chi). Let q be a large prime, sum^* over primitive chi mod q, {gamma_chi} the ordinates of zeros 1/2+i gamma_chi of L(s,chi) counted with multiplicity, N_chi(1) the count with |gamma_chi|<=1, and gamma_chi^+ the successor ordinate for that chi. With mean low-lying spacing 2pi/log q define D_q(lambda) = [sum^* #{-1<=gamma_chi<=1, 0<gamma_chi^+-gamma_chi<=lambda*2pi/log q}] / [sum^* N_chi(1)]. Prove there exist explicit constants lambda_0<1 and c>0 such that liminf_{q->infinity, q prime} D_q(lambda_0)>=c>0, via an optimized mollified shifted second moment of length q^theta calibrated by the ratios-conjecture prediction, combined with a fixed-modulus pair-correlation-to-density conversion.

## Attempted claim

Assume GRH for all primitive Dirichlet L(s,chi). Let q be a large prime, sum^* over primitive chi mod q, {gamma_chi} the ordinates of zeros 1/2+i gamma_chi of L(s,chi) counted with multiplicity, N_chi(1) the count with |gamma_chi|<=1, and gamma_chi^+ the successor ordinate for that chi. With mean low-lying spacing 2pi/log q define D_q(lambda) = [sum^* #{-1<=gamma_chi<=1, 0<gamma_chi^+-gamma_chi<=lambda*2pi/log q}] / [sum^* N_chi(1)]. Prove there exist explicit constants lambda_0<1 and c>0 such that liminf_{q->infinity, q prime} D_q(lambda_0)>=c>0, via an optimized mollified shifted second moment of length q^theta calibrated by the ratios-conjecture prediction, combined with a fixed-modulus pair-correlation-to-density conversion.

## Research outcome

Target blocked on three jointly necessary links (diagonal/off-diagonal threshold at theta=1, bandlimited tails swamping the small GUE signal, pair-to-consecutive-gap conversion refuted by a 57.9x cluster counterexample). Decision-phase alternatives assessed as circular or too weak. CLEAN_EXIT with NO_RESULT; reproducible diagnostics retained in WORKLOG and output/artifacts/pair_gap_ledger.py.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No TARGET or EMERGENT_FINDING result is claimed. The evidentiary basis is a reproducible numpy ledger plus scale analysis, which documents blockage rather than proving any positive theorem; it does not establish impossibility of the target, only that the prescribed GRH-only mollified-moment route is not currently viable. Originality searches were not needed since nothing is submitted.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No TARGET or EMERGENT_FINDING result is claimed. The evidentiary basis is a reproducible numpy ledger plus scale analysis, which documents blockage rather than proving any positive theorem; it does not establish impossibility of the target, only that the prescribed GRH-only mollified-moment route is not currently viable. Originality searches were not needed since nothing is submitted.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
