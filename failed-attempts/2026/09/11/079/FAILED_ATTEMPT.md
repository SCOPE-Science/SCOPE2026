# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A dilated Capparelli-type companion at modulus 12 with a mod-7 dissection family
- **Round:** 2026-09-07-first-light-01
- **Lane:** 896
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Combinatorics
- **Method:** trinomial Bailey lemma lift with 7-dissection

## Problem

Decide whether partitions into distinct parts with gap >= 2, gap >= 4 when the larger part is even, and no part equal to 1 admit a dilated Capparelli-type product at modulus 12 with a mod-7 congruence family, or certify the obstructed residue.

## Attempted claim

Let D(n) count partitions into distinct parts with lambda_i - lambda_{i+1} >= 2, >= 4 when lambda_i is even, and no part 1. Then sum_{n>=0} D(n) q^n = (-q;q)_oo (q^12;q^12)_oo / ((q^2;q^12)_oo (q^10;q^12)_oo) up to prefactor, and d(7n+3) == 0 mod 7 for all n; otherwise the exact obstructed residue class mod 7 and its minimal failing coefficient are as logged.

## Research outcome

TARGET disproved on both legs: product identity fails at n=1 (D=0 vs P=1) and the mod-7 family fails at m=3 (D=1), with a sharp all-residue obstruction log verified by dual computation.

## Why this attempt failed

Failed axes: value.

value: Strongest headline is a negative pairing: sum D != P (fails at n=1: 0 vs 1) and d(7n+3)=0 false at m=3 (D3=1), plus all-residue witnesses m<=8. Object was motivated (Capparelli level-12 program) but the invariant is mechanically implied by definitions with no non-trivial computation: D1=0 follows directly from 'no part 1', P1=1 follows directly from (-q;q)inf factor, so mismatch is visible on inspection; D0..8 are 1,0,1,1,1,1,1,2,3 none 0 mod 7 except D1=0, so all-residue obstruction follows from first 9 hand values. Extensive dual computation to n=150/300 is certification that does not rescue the datum. No general lift lemma, no corrected product, no downstream benchmark requiring this log is provided; draft honestly limits scope to exact pairing. Under the exact-invariant test (motivated before computation, not known/mechanically implied, future need) it fails the second prong. Intrinsic trivial early-failure with no substantive replacement is REJECT, not a bounded-addition fix.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Disproof covers only the exact stated gap predicate and the exact twisted mod-12 product; it does not rule out other dilations, modified gap predicates, other prefactors beyond the tested natural binomial rescues, or congruences at moduli other than 7.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
