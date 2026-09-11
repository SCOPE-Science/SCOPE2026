# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Closing one rank-1 sextic genus-2 curve with two infinities via Coleman bound at p=13
- **Round:** 2026-09-07-first-light-01
- **Lane:** 800
- **Disposition:** NO_RESULT
- **Domain:** Arithmetic Geometry
- **Method:** Chabauty-Coleman p-adic integration at p=13 with Mordell-Weil sieving (two-infinities model)

## Problem

Let C2: y^2 = x^6 - 3x^5 + x^4 + 3x^2 - x + 1 over Q (smooth, genus 2, leading coefficient a square, two points at infinity infinity-plus and infinity-minus). Naively visible affine points include (0,+/-1). With Jacobian rank 1 and p=13 a good Chabauty prime, prove via Coleman zero bound (including infinity disks) and Mordell-Weil sieve at 17 and 31 that C2(Q) equals exactly the naive finite set {infinity-plus, infinity-minus, (0,1), (0,-1)}.

## Attempted claim

C2(Q) = {infinity-plus, infinity-minus, (0,1), (0,-1)} with Coleman bound at p=13 and Mordell-Weil sieve elimination at 17 and 31 as witness.

## Research outcome

Target C2(Q) 4-point closure blocked: lane stack (python3.12+sympy only) cannot compute the required rank-1 certificate, p=13 Coleman integrals/infinity-disk bound, or 17/31 sieve images; Stoll ceiling 20 leaves 16 classes unkilled. Revealed partial target (proved Coleman bound + one elimination) attempted and likewise blocked (ATTEMPTED_AND_BLOCKED). No independently valuable emergent increment; clean exit.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No certified Jacobian rank, generator, Coleman integrals/zero bound, or sieve images (no Sage/Magma/PARI/mwrank in lane). Logged counts and torsion divisor are conditional on script replay, not a census proof; completeness of C2(Q) remains open.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No certified Jacobian rank, generator, Coleman integrals/zero bound, or sieve images (no Sage/Magma/PARI/mwrank in lane). Logged counts and torsion divisor are conditional on script replay, not a census proof; completeness of C2(Q) remains open.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
