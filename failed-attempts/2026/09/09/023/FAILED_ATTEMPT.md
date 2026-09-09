# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Minimal-cardinality distinct covering with minimum modulus 7 inside the minimal-LCM universe 10080
- **Round:** 2026-09-07-first-light-01
- **Lane:** 331
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Number Theory
- **Method:** density-pruned orderly backtracking with Chinese-remainder covering replay

## Problem

Let L0=10080 and D={d : d divides L0, d>=7}. Among distinct-modulus systems C={(a_i mod m_i)} with all m_i in D, min m_i=7, whose union is Z (equivalently covering all residues mod L0), determine C*=min |C| and exhibit one attaining system with a minimality certificate.

## Attempted claim

C* = the minimal cardinality of a distinct-modulus covering of Z with minimum modulus 7 and all moduli dividing L0=10080 is determined exactly; an explicit residue system {(a_i,m_i)} with |C|=C* covering all 10080 residues is exhibited, with a density-plus-exhaustive-search certificate that no distinct covering with min modulus 7 in D uses fewer than C* congruences (overlap sum>1 per Mirsky-Newman necessity checked).

## Research outcome

Certified partial theorem on minimal cardinality for min-modulus-7 distinct coverings in the minimal-LCM universe 10080: C* in [14,65] with an explicit verified irredundant 65-class witness improving the published 66-class upper bound by one, plus an exact reciprocal-sum proof that k<=13 is impossible.

## Why this attempt failed

Failed axes: value.

value: Strongest headline actually delivered is C* in [14,65] with an irredundant 65-cover; exact C* and promised fallback complete minimal-size table over divisors of 2520 are both admittedly undelivered (draft Sec.3: gap 14..65 open, no 64-impossibility). Lower bound 14 is textbook density arithmetic over fixed divisors, mechanically reproducible. Upper bound 65 is a one-class deletion from the published Zhang 66-system (missing modulus exactly 1120); testing all 66 single deletions by CRT replay over 10080 residues is milliseconds and mechanically discoverable by anyone holding the published system, verified here in one replay run. Gap width 51 leaves no exact invariant: C* undetermined, no minimality certificate, no census, no located gaps. Irredundancy proved is inclusion-minimality for fixed residues (each class owns a private residue), explicitly not global cardinality minimality, so not the promised cheapest-cover benchmark. Heuristic trials after dropping large moduli are admitted non-proofs. A future researcher already possessing Zhang's 66-system gains only 66->65 saving with no closure toward C*, reusable only as a marginally smaller feasible example, not a citable extremal optimum or atlas anchor. Certification (VERIFY_OK) alone does not rescue a tiny incremental tweak plus textbook bound. This is a missing substantive result / tiny unmotivated gain, not a narrow-but-exact motivated invariant whose value was unknown and non-mechanical.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Exact C* is NOT closed; gap 14..65 remains open. No proof that 64 classes are impossible; irredundancy holds only for the stated residue choices, not global minimality. The 65-witness is derived from the published Zhang et al. construction (credited), with the new verified finding being the single-class redundancy plus irredundant 65-subsystem. Heuristic re-optimization trials are supporting evidence only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
