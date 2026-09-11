# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** List-recovery beyond the recovery Johnson bound for Reed-Solomon codes at fixed input list size
- **Round:** 2026-09-07-first-light-01
- **Lane:** 842
- **Disposition:** NO_RESULT
- **Domain:** Coding Theory
- **Method:** algebraic list-recovery interpolation with set-membership constraints and Johnson-bound comparison

## Problem

Prove one explicit rate-1/4 Reed-Solomon code is list-recoverable beyond the recovery Johnson bound at fixed input list size with an explicit output-list bound.

## Attempted claim

The Reed-Solomon code [n=48,k=12] over F_97 (rate 1/4) is (rho=0.33, l=2, L<=8)-list-recoverable: for every choice of input lists S_i of size at most 2, at most 8 codewords agree with the lists on at least (1-rho)n=32 coordinates, certified by an explicit recovery interpolation log. The radius 0.33 exceeds the recovery Johnson value 1-sqrt(l*R)=1-sqrt(0.5)~0.293.

## Research outcome

Target blocked: the admitted uniform-multiplicity interpolation count is provably infeasible at agreement T=32 for every multiplicity (exact all-m deficit, machine-checked), no published beyond-Johnson theorem applies to the fixed F_97 window, and disproof search plateaued at min-agreement 20 vs required 32. Bounded fallback also attempted and blocked: T=33/L<=16 infeasible for all m<=500, L<=8 certifies at best T>=37 (below Johnson), and the sole feasible corner (T=33,L=64,m=22) needs an intractable 24k dense solve. No preset fallback existed; no emergent claim met the bar.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Target truth (recoverable or not at T=32) remains undecided: the search plateau at min-agreement 20 does not disprove, and the GS-count deficit blocks only the uniform-multiplicity interpolation route, not all conceivable proofs. Fallback scans covered m<=500 and L in {8,12,16,32,64}; exotic non-uniform-multiplicity or non-GS certificates were not explored. The negative count artifacts are routine checks, claimed as nothing more.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Target truth (recoverable or not at T=32) remains undecided: the search plateau at min-agreement 20 does not disprove, and the GS-count deficit blocks only the uniform-multiplicity interpolation route, not all conceivable proofs. Fallback scans covered m<=500 and L in {8,12,16,32,64}; exotic non-uniform-multiplicity or non-GS certificates were not explored. The negative count artifacts are routine checks, claimed as nothing more.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
