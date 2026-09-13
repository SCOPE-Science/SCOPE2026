# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Graph balancing configuration-LP polytime rounding to 1.65
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1635
- **Disposition:** NO_RESULT
- **Domain:** scheduling approximation
- **Method:** configuration LP rounding and orientation search

## Problem

For restricted graph balancing (each job j is an undirected edge with a single weight w_j > 0 eligible for exactly its two endpoint machines, an integral schedule being an orientation; guess T normalized to T=1 with the configuration LP defined over feasible machine configurations of total incident weight at most 1): does a polynomial-time rounding procedure exist that, starting from any feasible configuration-LP solution at T=1 (exact, or to within 1+epsilon for arbitrary fixed epsilon > 0 with factor 1.65+epsilon allowed), always produces an integral orientation of makespan at most 1.65? The scope is all finite multigraphs and all positive edge weights. A complete answer either gives the polynomial-time algorithm with a full runtime and makespan analysis, or exhibits one explicit instance with a verified feasible configuration-LP solution at T=1 whose every integral orientation has makespan strictly greater than 1.65, thereby refuting the claimed rounding guarantee.

## Attempted claim

For restricted graph balancing (each job j is an undirected edge with a single weight w_j > 0 eligible for exactly its two endpoint machines, an integral schedule being an orientation; guess T normalized to T=1 with the configuration LP defined over feasible machine configurations of total incident weight at most 1): does a polynomial-time rounding procedure exist that, starting from any feasible configuration-LP solution at T=1 (exact, or to within 1+epsilon for arbitrary fixed epsilon > 0 with factor 1.65+epsilon allowed), always produces an integral orientation of makespan at most 1.65? The scope is all finite multigraphs and all positive edge weights. A complete answer either gives the polynomial-time algorithm with a full runtime and makespan analysis, or exhibits one explicit instance with a verified feasible configuration-LP solution at T=1 whose every integral orientation has makespan strictly greater than 1.65, thereby refuting the claimed rounding guarantee.

## Research outcome

Target blocked: theory-guided computational witness search over roughly 2000 boundary-scaled instances plateaued at feasible optimum about 1.47, far below 1.65; no algorithm chain or independently valuable finding emerged, so the lane exits cleanly with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No gap witness above 1.65 was found and no rounding algorithm was constructed; computational search used a PuLP/CBC floating-point feasibility oracle with exact rational re-verification only for the final incumbent optimum, and explored instances only up to 7 nodes and 10 edges, so the negative result is bounded evidence of difficulty rather than a proof of impossibility.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No gap witness above 1.65 was found and no rounding algorithm was constructed; computational search used a PuLP/CBC floating-point feasibility oracle with exact rational re-verification only for the final incumbent optimum, and explored instances only up to 7 nodes and 10 edges, so the negative result is bounded evidence of difficulty rather than a proof of impossibility.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
