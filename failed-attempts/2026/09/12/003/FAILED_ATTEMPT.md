# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Falsifiable column-exploration spectral envelope for Voronoi crossing
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1068
- **Disposition:** NO_RESULT
- **Domain:** Statistical Mechanics
- **Method:** randomized-algorithm revealment with OSSS inequality and Russo-Margulis differential inequality

## Problem

Discretize intensity-1 Voronoi box crossing on [0,n]^2 with n>=16 to an M-bit Boolean function f_n with M>=64 via block colors. Does the Schramm-Steif inequality applied to an independent column-first exploration with max-cell revealment at most 0.35 n^{-1/4} imply sum_{1<=|S|<=k} hat{f_n}(S)^2 <= 0.35 sqrt(k) n^{-1/4} for every fixed level 1<=k<=6, certifying quantitative noise sensitivity with falsifiable constants decoupled from candidate 1?

## Attempted claim

For the M-bit block discretization with M>=64 of red left-right crossing f_n on [0,n]^2 with n>=16, an independent column-first exploration with max revealment at most 0.35 n^{-1/4} fed into the Schramm-Steif inequality yields sum_{1<=|S|<=k} hat{f_n}(S)^2 <= 0.35 sqrt(k) n^{-1/4} for every 1<=k<=6. At n=16 the envelope ranges from 0.175 at k=1 to 0.429 at k=6, strictly inside total mass 1 at every level, hence falsifiable across six levels at every scale n>=16.

## Research outcome

Target blocked and cleanly exited: exact Schramm-Steif summation yields a quadratic cumulative envelope that exceeds the claimed 0.35 sqrt(k) n^{-1/4} caps at k=2..6 at n=16, and the billed revealment input is unproved.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The Schramm-Steif per-level inequality itself was verified from the published source, but its cumulative summation provably contradicts the billed sqrt(k) envelope at five of six audit levels, and the independent 0.35 n^{-1/4} column-first revealment input was found unproved in the literature; neither gap could be repaired within the one-hour pass.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The Schramm-Steif per-level inequality itself was verified from the published source, but its cumulative summation provably contradicts the billed sqrt(k) envelope at five of six audit levels, and the independent 0.35 n^{-1/4} column-first revealment input was found unproved in the literature; neither gap could be repaired within the one-hour pass.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
