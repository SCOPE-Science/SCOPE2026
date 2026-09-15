# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp outer-edge right-tail bound for fixed-beta log-gases with C^4 regular multi-cut potentials
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20201
- **Disposition:** NO_RESULT
- **Domain:** Probability Theory
- **Method:** loop equations and transport inequalities

## Problem

Fix beta>=1 independent of N. Let V in C^4(R) be confining with equilibrium measure supported on q>=2 disjoint compact intervals union_h [A_h,B_h], off-critical (positive density inside each cut, square-root vanishing at endpoints) and effective potential strictly negative outside the support. For P^N_{V,beta}(dlambda) proportional to prod_{i<j}|lambda_i-lambda_j|^beta exp(-N sum_i V(lambda_i)) dlambda and lambda_max=max_i lambda_i with outermost right endpoint B_q, prove there exist N0,s0,delta,C,c>0 depending only on (beta,V) such that for all N>=N0 and s0<=s<=delta N^{2/3}, P^N_{V,beta}(N^{2/3}(lambda_max-B_q)>s) <= C exp(-c s^{3/2}) up to a V-dependent deterministic linear rescaling of s by the square-root coefficient at B_q absorbed into c; a finite-N non-asymptotic upper-tail bound with Tracy-Widom 3/2 exponent, unconditional on any assumed edge limit.

## Attempted claim

Fix beta>=1 independent of N. Let V in C^4(R) be confining with equilibrium measure supported on q>=2 disjoint compact intervals union_h [A_h,B_h], off-critical (positive density inside each cut, square-root vanishing at endpoints) and effective potential strictly negative outside the support. For P^N_{V,beta}(dlambda) proportional to prod_{i<j}|lambda_i-lambda_j|^beta exp(-N sum_i V(lambda_i)) dlambda and lambda_max=max_i lambda_i with outermost right endpoint B_q, prove there exist N0,s0,delta,C,c>0 depending only on (beta,V) such that for all N>=N0 and s0<=s<=delta N^{2/3}, P^N_{V,beta}(N^{2/3}(lambda_max-B_q)>s) <= C exp(-c s^{3/2}) up to a V-dependent deterministic linear rescaling of s by the square-root coefficient at B_q absorbed into c; a finite-N non-asymptotic upper-tail bound with Tracy-Widom 3/2 exponent, unconditional on any assumed edge limit.

## Research outcome

Target blocked: fixed-s Tracy-Widom-scale upper tail needs O(1) log-probability precision that soft LDP (o(N) error), metastable multi-cut LSI (exp(-cN) constants), and available rigidity inputs (diverging thresholds) cannot supply; CLEAN_EXIT with no fallback and no emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proof or disproof of the target was obtained; the 3/2 rate-function scaling itself checks out, so falsity was not established either. The gap analysis rests on locally executed reasoning plus a scripted threshold model, not on an exhaustive literature survey, and does not rule out a future proof via a sharp C^4 multi-cut O(1) free-energy expansion.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proof or disproof of the target was obtained; the 3/2 rate-function scaling itself checks out, so falsity was not established either. The gap analysis rests on locally executed reasoning plus a scripted threshold model, not on an exhaustive literature survey, and does not rule out a future proof via a sharp C^4 multi-cut O(1) free-energy expansion.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
