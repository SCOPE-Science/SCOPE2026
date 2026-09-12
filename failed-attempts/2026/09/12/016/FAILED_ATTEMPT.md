# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Scaling-independent archimedean optimum 96 for S={2,3,5,11,50033}
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1070
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Transcendental Number Theory
- **Method:** archimedean Baker-Wustholz with dual-scaling de Weger LLL optimum

## Problem

Certify the scaling-independent archimedean optimum for open S2={2,3,5,11,50033}: from explicit Baker-Wustholz B0 build de Weger lattices at Ca=10^40 and Cb=10^80, run LLL, and prove the optimal reduced bound B*=96 with matching certificates, or log the quantified divergence; the bound is consumed by the Thue-Mahler equation x^3-2y^3=+-z with S2-smooth z.

## Attempted claim

With explicit Baker-Wustholz constants giving initial bound B0 for S2={2,3,5,11,50033}, the de Weger lattices at Ca=10^40 and Cb=10^80 with LLL delta=0.99 both certify max exponent <=96 and no smaller uniform bound follows from the pair, i.e. the scaling-independent optimum is B*=96 with logged dual Gram certificates, directly imported by the stated Thue-Mahler sieve.

## Research outcome

Certified first dual de Weger LLL transcripts for open S2 with two-sided shortest-vector brackets, proved one-step stall thresholds blocking the B*=96 route, and unconditional B=96 linear-form bounds, all replayable via verify.py with VERIFY_OK.

## Why this attempt failed

Failed axes: value.

value: Even though correct and new, the headline is not independently worth retrieving under the shared STANDARD. The TARGET's C-independent optimum B*=96 is explicitly NOT claimed; what remains is C-dependent log data for two Topic-chosen round scalings (Ca=10^40, Cb=10^80): two short-vector lengths, quality ratios L/C^{1/6}, tiny C-scaled linear-form lower bounds at B=96, and the arithmetic restatement T=L/kappa (~9.07e5, ~4.99e12). The one-step stall 'theorem' is the generic de Weger necessary condition instantiated at those L values and stalls for every lattice whenever B>>L, so without a computed explicit Baker-Wustholz B0 or any multi-step iteration it only records that the chosen C values lie far below any astronomical B0 -- an arbitrary-parameter mismatch, not a structural obstruction that resets the named x^3-2y^3 Thue-Mahler consumer (no import is shown). No reduced exponent upper bound, census, classification, improved cutoff, or reusable canonical invariant is established; certification and VERIFY_OK replay strengthen evidence but do not create value for an arbitrary C-pair and an evasively large-prime set. No bounded motivation-only addition can supply the missing substantive result without a new research direction, so this is intrinsic low value, not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The TARGET claim B*=96 (from explicit Baker-Wustholz B0 with minimality over the pair plus the Thue-Mahler sieve import) is not established here; the stall theorem covers only single-step de Weger reduction and does not rule out a future multi-step iteration with sharp validated BW/Matveev constants; high-precision logarithm rounding margins rely on 120-digit mpmath interval discipline (with >=0.03 slack) while all lattice certificates R2-R5 and R7 are exact integer/rational facts; quality fact…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
