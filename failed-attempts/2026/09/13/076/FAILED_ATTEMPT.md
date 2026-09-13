# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Two-valued restricted assignment configuration-LP gap at most 8/5
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1637
- **Disposition:** NO_RESULT
- **Domain:** scheduling approximation
- **Method:** configuration LP two-size case analysis

## Problem

For two-valued restricted assignment (each job j has an eligible machine set E_j and all finite processing times take only two distinct positive values across the whole instance, i.e. after scaling p_{ij} in {a, b} union {infinity} for some 0 < a <= b that may depend on the instance; guess T normalized to T=1 with the configuration LP over per-machine configurations of total size at most 1): is the worst-case ratio OPT/T over all such instances with feasible configuration LP at T=1, ranging over all finite machine and job counts, all value pairs (a,b) and all eligible sets, at most 8/5? A complete answer either proves that every such instance admits an integral schedule of makespan at most 8/5, or exhibits one explicit two-valued instance with a verified feasible configuration-LP solution at T=1 and a proof that every integral assignment has makespan strictly greater than 8/5.

## Attempted claim

For two-valued restricted assignment (each job j has an eligible machine set E_j and all finite processing times take only two distinct positive values across the whole instance, i.e. after scaling p_{ij} in {a, b} union {infinity} for some 0 < a <= b that may depend on the instance; guess T normalized to T=1 with the configuration LP over per-machine configurations of total size at most 1): is the worst-case ratio OPT/T over all such instances with feasible configuration LP at T=1, ranging over all finite machine and job counts, all value pairs (a,b) and all eligible sets, at most 8/5? A complete answer either proves that every such instance admits an integral schedule of makespan at most 8/5, or exhibits one explicit two-valued instance with a verified feasible configuration-LP solution at T=1 and a proof that every integral assignment has makespan strictly greater than 8/5.

## Research outcome

Target blocked: proof closes all regimes except the two-size mixing subcase and ~90k-instance adversarial search found no witness (best gap 1.23); clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No complete TARGET resolution was achieved: neither a full proof of the 8/5 upper bound (the mixing subcase {alpha<=1/2, beta in (3/5,1]} lacks a closing rounding inequality) nor an explicit verified gap witness (best observed gap 1.23 across ~90k trap instances plus exhaustive m=2 coverage) could be produced. Computational evidence favors the bound but proves nothing; the partial case reductions use only standard tools and carry no independent originality claim.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No complete TARGET resolution was achieved: neither a full proof of the 8/5 upper bound (the mixing subcase {alpha<=1/2, beta in (3/5,1]} lacks a closing rounding inequality) nor an explicit verified gap witness (best observed gap 1.23 across ~90k trap instances plus exhaustive m=2 coverage) could be produced. Computational evidence favors the bound but proves nothing; the partial case reductions use only standard tools and carry no independent originality claim.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
