# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Admissible 28-set in one class mod 30
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1762
- **Disposition:** AUDIT_1_REJECT
- **Domain:** analytic number theory
- **Method:** residue covering and subset search in one class mod 30

## Problem

Does there exist an integer residue r with gcd(r,30)=1 and an integer set H={h_1,...,h_28} with 0<=h_1<h_2<...<h_28<=1000 such that (i) every h_i is congruent to r modulo 30, and (ii) H is admissible, meaning for every prime p<=28 the residues {h_i mod p} omit at least one class modulo p? A complete answer is either the explicit r and list H together with, for each prime p<=28, an omitted residue class, or a complete proof that no 28-element subset of any coprime residue class modulo 30 inside an interval of length 1000 is admissible.

## Attempted claim

Does there exist an integer residue r with gcd(r,30)=1 and an integer set H={h_1,...,h_28} with 0<=h_1<h_2<...<h_28<=1000 such that (i) every h_i is congruent to r modulo 30, and (ii) H is admissible, meaning for every prime p<=28 the residues {h_i mod p} omit at least one class modulo p? A complete answer is either the explicit r and list H together with, for each prime p<=28, an omitted residue class, or a complete proof that no 28-element subset of any coprime residue class modulo 30 inside an interval of length 1000 is admissible.

## Research outcome

TARGET resolved: proved by exhaustive enumeration over all 4113824 candidate subsets that no admissible 28-set exists in any coprime residue class mod 30 within [0,1000]; answer is NO.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: although the exhaustive NO formally resolves the literal TARGET, the resolved fact is an arbitrary parameter slice under STANDARD: 28 elements, single coprime class mod 30, interval [0,1000] with no pre-computation motivation, classification boundary, benchmark, or downstream use stated in DRAFT or report. Limitations admit no generalization. A future researcher has no reason to retrieve this precise nonexistence datum. It is unexplained enumeration over an arbitrary finite slice, not a motivated exact invariant of a natural object; certification and replayability do not create value. Hence value FAILS despite correctness and novelty.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The proof is computational rather than structural: it establishes nonexistence by exhaustive enumeration of 4113824 subsets instead of a closed-form covering argument, and it is specific to the stated bounds (28 elements, interval length 1000, modulus 30) and does not generalize to other parameters.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
