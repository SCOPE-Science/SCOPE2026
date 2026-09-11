# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Closing the C_5^{(3)} Turan-density window: flag-algebra certificate toward 2sqrt(3)-3 with blow-up stability
- **Round:** 2026-09-07-first-light-01
- **Lane:** 747
- **Disposition:** NO_RESULT
- **Domain:** Extremal Combinatorics
- **Method:** flag-algebra semidefinite certificates with blow-up stability analysis

## Problem

Determine the ordinary Turan density pi(C_5^{(3)}) of the 3-uniform tight 5-cycle, conjectured (Mubayi-Rodl) to equal 2sqrt(3)-3, via a new flag-algebra SDP certificate with blow-up stability rounding; failing exact determination, bank a certified strict upper-bound improvement with a stability fragment describing near-extremal structure around the iterated blow-up.

## Attempted claim

pi(C_5^{(3)}) = 2sqrt(3) - 3 (≈ 0.4641): the ordinary Turan density of the 3-uniform tight 5-cycle equals the Mubayi-Rodl iterated blow-up value.

## Research outcome

TARGET pi(C5^(3))=2sqrt3-3 blocked: upper leg needs novel SDP/theoretical breakthrough with no execution engine in lane; SDP-free substitutes stall at ~0.60+. Preset fallback (SDP certificate B<=0.4663) attempted via same engine probe and certified elementary caps (best 22/35=0.6286, gap 0.1623) and is blocked. No independently valuable original increment. CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No SDP solver in lane (scipy/cvxpy/cvxopt/ecos/clarabel/mosek/sdpa all missing); no flag-algebra certificate built. ex(7)=22 branch-and-bound max verified by two independent scripts but is a finite census with no asymptotic implication; not claimed as emergent finding. Lower-leg derivation reproduces known MR bound.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No SDP solver in lane (scipy/cvxpy/cvxopt/ecos/clarabel/mosek/sdpa all missing); no flag-algebra certificate built. ex(7)=22 branch-and-bound max verified by two independent scripts but is a finite census with no asymptotic implication; not claimed as emergent finding. Lower-leg derivation reproduces known MR bound.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
