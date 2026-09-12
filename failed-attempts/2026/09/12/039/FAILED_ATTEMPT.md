# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Block chromatic index of the four cyclic STS(19)s
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1133
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Design Theory
- **Method:** exact-cover block-partition search with unsatisfiability certificates

## Problem

Decide the block chromatic spectrum of the symmetric tier: test each of the four cyclic STS(19)s with published Z19 base triples for partitionability of its 57 blocks into 10 partial parallel classes, and determine whether every cyclic system is chromatic-index 10 or at least one needs 11 classes.

## Attempted claim

Let A1 through A4 be the four cyclic STS(19)s in Mathon-Phelps-Rosa notation over Z19. Then at least one of A1-A4 has block chromatic index 11, meaning its 57 blocks admit a partition into 11 partial parallel classes but no partition into 10, as certified by an explicit 11-partition together with a machine-checkable 10-partition unsatisfiability proof.

## Research outcome

Certified exact block chromatic index 12 for the fourth cyclic STS(19) A4 (explicit 12-partition plus exhaustive no-6-matching proof) with companion exact value 10 for A1; literal index-11 target blocked.

## Why this attempt failed

Failed axes: originality, value.

originality: The headline chi(A4)=12 via no-6-matching plus a 12-partition is already recorded and substantively implied by Colbourn et al., Properties of the STS(19), EJC 17:R98 (2010, DOI 10.37236/370). Theorem 6 states the chromatic-index census of all 11,084,874,829 STS(19)s is 10/11/12 in counts 11084870752/4075/2, and expressly that exactly the two STS(19)s with no almost parallel class have index 12. Section 2.7 identifies those two as A4 (cyclic system A4 in Mathon-Phelps-Rosa notation, Aut order 171, Netto system) and the unique Aut-432 design. Since an almost parallel class in STS(19) is exactly 6 pairwise-disjoint blocks, prior 'A4 has no almost parallel class and has index 12' literally covers the submitted 'A4 has no 6 disjoint blocks so 11 classes cover at most 55, and a 12-partition exists'. The new explicit partition files and stdlib verifier are a recomputation/certificate of a known stronger census fact, which under the shared STANDARD does not create originality. A timestamp or de novo computation does not establish priority. value: As an exact invariant of a natural motivated object the question is well posed, and the EMERGENT_FINDING genuinely arose from the admitted target investigation, so no evasion penalty applies. But under the shared STANDARD an exact invariant is eligible only when the exact value is not already known or mechanically implied, and certification alone does not create value. Here chi(A4)=12 and its counting obstruction (no almost parallel class) were published in the completed 2010 STS(19) census (Theorem 6 plus Section 2.7 naming A4), and chi(A1)=10 is the generic census outcome shared by 11,084,870,752 designs. A future researcher needing the precise fact would retrieve the prior census record, not a recomputation. Hence the submission is a known-database recomputation with no new boundary, datum, or downstream use, and fails the independent-retrieval value threshold.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Exact chromatic indices of A2 and A3 remain undecided (verified 11-partitions exist; bounded 10-searches — ~600k greedy tries plus ~24M simulated-annealing steps per system and a targeted 7x6+3x5 exact-cover heuristic — were negative but are heuristic evidence only, not UNSAT proofs); the A4 lower bound is counting-based and specific to A4; isomorphism classification is computational (affine-map canonical forms) rather than a hand proof.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
