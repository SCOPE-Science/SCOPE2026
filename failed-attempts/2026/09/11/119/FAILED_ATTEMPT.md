# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Twisted badly approximable witness for a fixed shift via affine Dani flow
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1004
- **Disposition:** NO_RESULT
- **Domain:** Diophantine Approximation
- **Method:** inhomogeneous affine Dani correspondence shifted-minima ledger

## Problem

Decide whether the explicit twisted pair beta*=(sqrt(2),sqrt(3)) with shift gamma*=(1/4,1/9) is inhomogeneously badly approximable with constant c1=1/800: for every integer q>=1 and p in Z^2, max(|q sqrt2-p1-1/4|,|q sqrt3-p2-1/9|) >= (1/800) q^{-1/2}, equivalently the affine Dani orbit of the shifted lattice stays at shifted-minimum distance >= delta(c1) from the cusp.

## Attempted claim

For beta*=(sqrt2,sqrt3) and gamma*=(1/4,1/9), max_i||q beta*_i - gamma*_i|| >= (1/800) q^{-1/2} for all q>=1, equivalently the lifted affine Dani trajectory has shifted first minimum bounded below, certifying an inhomogeneous badly approximable gap.

## Research outcome

Target blocked on both sides: every proof route caps at exponent 1 or a finite head (q<=312), convergent forcing reverses, and refutation needs Q~exp(160000). The decision-phase exact alternative (head plus weak global bound) runs correctly but is a routine fragment that cannot pass Audit, so the lane exits clean with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The infinite tail q>312 with exponent 1/2 is unresolved: norm routes provably cap at exponent 1, convergent forcing provably reverses, and search-based refutation would need Q~exp(160000). The Q=2x10^7 computation is finite uncertified numerical evidence only, and the exact q<=312 head lemma plus max>=1/(54q) global bound are routine Liouville-type fragments that cannot pass Audit as independent results.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The infinite tail q>312 with exponent 1/2 is unresolved: norm routes provably cap at exponent 1, convergent forcing provably reverses, and search-based refutation would need Q~exp(160000). The Q=2x10^7 computation is finite uncertified numerical evidence only, and the exact q<=312 head lemma plus max>=1/(54q) global bound are routine Liouville-type fragments that cannot pass Audit as independent results.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
