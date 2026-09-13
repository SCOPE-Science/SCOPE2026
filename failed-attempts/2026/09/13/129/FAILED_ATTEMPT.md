# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Polynomial revealment-decay family for critical FK q=3 crossings
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1776
- **Disposition:** NO_RESULT
- **Domain:** decision trees / FK percolation
- **Method:** OSSS interface exploration plus one-arm revealment bound

## Problem

Prove or disprove the following polynomial revealment-decay family for critical FK q=3 crossings: for each integer n>=64 let B_n=[0,n]x[0,n] intersected with Z^2 with nearest-neighbour edges and free boundary, and let Cross_n be the left-right open crossing event in B_n under the critical random-cluster measure at p_c(3)=sqrt(3)/(1+sqrt(3)), q=3. Consider randomized adaptive decision trees that query edges of B_n one by one (queries may depend on previously revealed states and independent auxiliary randomness), stop almost surely, and output the correct indicator of Cross_n; the maximum revealment is the supremum over edges of the query probability. For every n>=64 there exists such a decision tree T_n for Cross_n with maximum revealment at most n^{-0.10}. A complete answer is an explicit family description with proofs that each T_n determines Cross_n a.s. and meets the stated decay bound, yielding an OSSS-driven noise-sensitivity/threshold consequence across growing boxes, or a rigorous proof that for some explicit n>=64 every admissible randomized tree has maximum revealment exceeding n^{-0.10}. Scope: q=3, growing square-box family, free boundary. Any rigorous argument is allowed.

## Attempted claim

Prove or disprove the following polynomial revealment-decay family for critical FK q=3 crossings: for each integer n>=64 let B_n=[0,n]x[0,n] intersected with Z^2 with nearest-neighbour edges and free boundary, and let Cross_n be the left-right open crossing event in B_n under the critical random-cluster measure at p_c(3)=sqrt(3)/(1+sqrt(3)), q=3. Consider randomized adaptive decision trees that query edges of B_n one by one (queries may depend on previously revealed states and independent auxiliary randomness), stop almost surely, and output the correct indicator of Cross_n; the maximum revealment is the supremum over edges of the query probability. For every n>=64 there exists such a decision tree T_n for Cross_n with maximum revealment at most n^{-0.10}. A complete answer is an explicit family description with proofs that each T_n determines Cross_n a.s. and meets the stated decay bound, yielding an OSSS-driven noise-sensitivity/threshold consequence across growing boxes, or a rigorous proof that for some explicit n>=64 every admissible randomized tree has maximum revealment exceeding n^{-0.10}. Scope: q=3, growing square-box family, free boundary. Any rigorous argument is allowed.

## Research outcome

Target blocked: both proof and disproof of the n^{-0.10} revealment-decay family for critical FK q=3 reduce to a missing explicit one-arm/circuit estimate (c>=0.067 per dyadic scale) that cannot be derived in-session; clean exit with no claim.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No unconditional theorem about critical FK q=3 crossings was proved: the exploration-to-one-arm reduction is conditional on a missing explicit one-arm/circuit estimate, published RSW gives only non-explicit constants, and exhaustive verification at n>=64 is infeasible; the recovery computation is illustrative arithmetic, not a proof of any crossing estimate.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No unconditional theorem about critical FK q=3 crossings was proved: the exploration-to-one-arm reduction is conditional on a missing explicit one-arm/circuit estimate, published RSW gives only non-explicit constants, and exhaustive verification at n>=64 is infeasible; the recovery computation is illustrative arithmetic, not a proof of any crossing estimate.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
