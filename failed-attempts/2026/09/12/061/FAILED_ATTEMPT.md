# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Base-layer 29-Selmer corank for 37a1 over Q(sqrt(-7))
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1211
- **Disposition:** NO_RESULT
- **Domain:** Selmer groups over imaginary quadratic fields
- **Method:** 2-descent over class-number-1 field with 29-adic local ledger

## Problem

Let E/Q be the elliptic curve 37a1 given by y^2+y=x^3-x of conductor 37, let K=Q(sqrt(-7)) of discriminant -7, and let p=29. Preliminary gate (failure is NO_RESULT, not disproof): verify good ordinarity at 29 by point count, splitting of 37 and 29 in K, and mod-29 irreducibility. Decided claim (exact base-layer algebraic invariant feeding, but not claiming, tower mu-vanishing): decide the exact Z_29-corank of the 29-primary ordinary Selmer group Sel_{29^infty}(E/K) with explicit ordinary local conditions at the two primes above 29 and Tamagawa conditions at 37, via 2-descent over K (class number 1) combined with the 29-adic local Tate-duality ledger. A complete answer proves corank exactly 1 with an explicit point of infinite order plus a certified 29-Selmer bound killing the Sha[29] alternative, or rigorously establishes a different exact corank (0 or at least 2) with explicit Selmer cohomology witnesses and the matching Mordell-Weil-or-Sha explanation.

## Attempted claim

Let E/Q be the elliptic curve 37a1 given by y^2+y=x^3-x of conductor 37, let K=Q(sqrt(-7)) of discriminant -7, and let p=29. Preliminary gate (failure is NO_RESULT, not disproof): verify good ordinarity at 29 by point count, splitting of 37 and 29 in K, and mod-29 irreducibility. Decided claim (exact base-layer algebraic invariant feeding, but not claiming, tower mu-vanishing): decide the exact Z_29-corank of the 29-primary ordinary Selmer group Sel_{29^infty}(E/K) with explicit ordinary local conditions at the two primes above 29 and Tamagawa conditions at 37, via 2-descent over K (class number 1) combined with the 29-adic local Tate-duality ledger. A complete answer proves corank exactly 1 with an explicit point of infinite order plus a certified 29-Selmer bound killing the Sha[29] alternative, or rigorously establishes a different exact corank (0 or at least 2) with explicit Selmer cohomology witnesses and the matching Mordell-Weil-or-Sha explanation.

## Research outcome

Target blocked: gate checks and rank>=1 lower bound proved, but no certified Selmer upper bound; clean exit with no emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No CAS (sage/pari/magma) and no pip were available, so no certified 2-Selmer or 29-Selmer computation, no proven twist-rank bound, and no certified ordinary 29-adic Tate-duality ledger could be built; the exact corank 1 versus at least 2 remains undecided.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No CAS (sage/pari/magma) and no pip were available, so no certified 2-Selmer or 29-Selmer computation, no proven twist-rank bound, and no certified ordinary 29-adic Tate-duality ledger could be built; the exact corank 1 versus at least 2 remains undecided.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
