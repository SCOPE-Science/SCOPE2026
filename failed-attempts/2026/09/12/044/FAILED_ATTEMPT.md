# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Fixed log-grid near-Stahl envelope for |x|
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1156
- **Disposition:** NO_RESULT
- **Domain:** approximation theory
- **Method:** condenser-capacity lower bound versus pole-selection construction

## Problem

Prove or disprove that fixed-step log-uniform imaginary poles can match a near-Stahl exponent for f(x)=|x| on [-1,1]: let G={pm i*exp(-k): k=0,1,2,...} with fixed log-step 1 independent of n. Decide whether there exists a sequence r_n in R(n,n) (real p/q, deg<=n, q nonzero on [-1,1]) with all poles in G such that sup_{[-1,1]}||x|-r_n|<=2*exp(-2.8*sqrt(n)) for all sufficiently large n. Scope is all large n with pole locations restricted to G and no restriction on zeros or numerator. A complete answer either constructs such a sequence with proof of the envelope, or proves impossibility by a condenser-capacity or alternation lower bound showing every G-restricted sequence violates the envelope eventually.

## Attempted claim

Prove or disprove that fixed-step log-uniform imaginary poles can match a near-Stahl exponent for f(x)=|x| on [-1,1]: let G={pm i*exp(-k): k=0,1,2,...} with fixed log-step 1 independent of n. Decide whether there exists a sequence r_n in R(n,n) (real p/q, deg<=n, q nonzero on [-1,1]) with all poles in G such that sup_{[-1,1]}||x|-r_n|<=2*exp(-2.8*sqrt(n)) for all sufficiently large n. Scope is all large n with pole locations restricted to G and no restriction on zeros or numerator. A complete answer either constructs such a sequence with proof of the envelope, or proves impossibility by a condenser-capacity or alternation lower bound showing every G-restricted sequence violates the envelope eventually.

## Research outcome

No TARGET resolution: G-restricted near-Stahl envelope (2.8) neither constructed nor rigorously disproved; schedule-robust Lawson numerics suggest impossibility but prove nothing, so honest NO_RESULT via CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Double-precision Lawson upper bounds on ~3000-point grids are uncertified one-sided feasible points, not lower-bound proofs; the quantized-equilibrium cap sketch lacks explicit constants; no construction or impossibility theorem, no certified exponent estimate, and no emergent finding are claimed.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Double-precision Lawson upper bounds on ~3000-point grids are uncertified one-sided feasible points, not lower-bound proofs; the quantized-equilibrium cap sketch lacks explicit constants; no construction or impossibility theorem, no certified exponent estimate, and no emergent finding are claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
