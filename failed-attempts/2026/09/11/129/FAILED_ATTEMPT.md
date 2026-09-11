# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Fixed-point-free involutory autotopism obstruction for 3-MOLS(10)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1027
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Design Theory
- **Method:** SAT-encoded OA(5,10) search with C2 orbit symmetry breaking and isotopism canonicalization

## Problem

Decide whether any triple of mutually orthogonal Latin squares of order 10 admits an involutory autotopism acting fixed-point-freely as five disjoint transpositions on rows, on columns, and on each of the three symbol sets. Deliver either a proof-logged SAT unsatisfiability certificate with a counting replay, or an explicit involution-symmetric triple with isotopism-canonical witness.

## Attempted claim

No orthogonal array OA(5,10), equivalently no set of 3-MOLS(10), admits an involutory autotopism acting fixed-point-freely as five disjoint transpositions on each of the five coordinate positions (rows, columns, and the three symbol coordinates).

## Research outcome

Proved the target: no OA(5,10) / 3-MOLS(10) admits a fixed-point-free involutory autotopism, via CRT parity-counting contradiction with machine-replayed lemmas.

## Why this attempt failed

Failed axes: originality.

originality: ADMISSION_DEFECT: Admission preflight claimed no table covers five-transposition profile, but Falcon arXiv:0709.2973 (Ars Combinatoria 103, 2012) Table 5 / Final Remarks explicitly lists cycle structure (0,5,0,0,0,0,0,0,0,0) x3 for n=10 as satisfying all Section-3 necessary conditions yet exhaustive computation proves Delta=0, i.e. no Latin square of order 10 admits autotopism (tau,tau,tau) with tau five transpositions. Any OA(5,10) with diagonal tau^5 projects on any 3 coordinates to an OA(3,10) with tau^3 (distinctness preserved because sharing 3 coords implies sharing 2 coords, forbidden by strength 2), hence a Latin square with that forbidden autotopism. Therefore published stronger triple result substantively implies the submitted 5-coordinate headline as a corollary. Headline is not new despite correct elegant parity proof. General m-odd remark does not rescue narrow headline.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: The proof decides only the fixed-point-free (five-transposition) involution profile for OA(5,10) and 3-MOLS(10); it does not rule out involutory autotopisms with fixed points, non-involutory symmetries, or asymmetric triples, and it leaves the general 3-MOLS(10) existence question open. Machine replay covers the parity/combinatorial lemmas, not automated checking of the prose normalization step.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
