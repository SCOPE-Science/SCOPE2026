# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A parity-shifted Gollnitz-Gordon companion at modulus 8 with a mod-11 dissection family
- **Round:** 2026-09-07-first-light-01
- **Lane:** 897
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Combinatorics
- **Method:** Bailey-chain lift with 11-dissection via quintuple product

## Problem

Decide whether the parity-shifted Gollnitz-Gordon condition (minimal difference 2, gap >= 4 between evens, smallest part >= 2, no part 2) yields a new mod-8 product with a mod-11 congruence family, or certify the obstructing residue.

## Attempted claim

Let G(n) count partitions with lambda_i - lambda_{i+1} >= 2, >= 4 when both parts are even, smallest part >= 2, and no part equal to 2. Then sum_{n>=0} G(n) q^n = (q^8;q^8)_oo / ((q^2;q^8)_oo (q^3;q^8)_oo (q^6;q^8)_oo) up to prefactor, and g(11n+6) == 0 mod 11 for all n; otherwise the exact obstructed residue class mod 11 with minimal witness is as logged.

## Research outcome

Target disproved at minimal indices: G(2)=0 vs P(2)=1 kills the product; G(6)=1 kills the 11-family; all 11 residue classes certified obstructed.

## Why this attempt failed

Failed axes: originality, value.

originality: The combinatorial predicate G (gaps >=2, >=4 between evens, smallest >=2 with no 2, i.e. all parts >2) is literally the classical second Gollnitz-Gordon class, whose generating function is 1/((q3;q8)(q4;q8)(q5;q8)) per MathWorld/Slater/Andrews. The submitted product with residues {2,3,6} is disjoint from classical {1,4,7} and {3,4,5}. Live fused search retrieved classical statements and He-Zhao 2023 companions but no {2,3,6} identity. Crucially, the classical second identity already implies the headline's first half: it fixes G's series (0 at q^2) while P_{2,3,6} has 1 at q^2, so G!=P is a direct corollary/recomputation of a known stronger theorem, not a new companion. The mod-11 non-vanishing census (all witnesses <=13 with values <=4 <11) is mechanically implied by small values and was never a stated prior gap. Hence the headline is covered as corollary/repackaging and fails adversarial coverage. value: TARGET route audited normally with no preset presumption. The headline falsification fails at the first checkable coefficient (n=2: [2] counted by P, excluded by G) and the congruence fails at its first term (G(6)=1 from [6]); both are visible without any Bailey-chain or 11-dissection work claimed in the topic. The 11-class census is automatic because all cited G-values are 0-4, so non-zero implies non-zero mod 11; residue 0 is trivially obstructed by G(0)=1. The object G is not new: it is the classical second Gollnitz-Gordon sequence (OEIS A036015), so comparing it to a different known product {2,3,6} and logging small-value non-vanishing provides no benchmark, classification datum, or downstream fact a future researcher would need to retrieve. Short proof is not the issue; mechanical immediacy plus pre-classified object with no new method or insight is intrinsic low value.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Disproof is specific to the stated residue triple {2,3,6} at level 8 with the exact shifted predicate, and to mod-11 residue families for this G; it does not exclude companions with different residue sets, repaired initial conditions, or congruences at other moduli, and the N=200 divergence census beyond n=13 rests on the DP-plus-series computation replayed by the verifier.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
