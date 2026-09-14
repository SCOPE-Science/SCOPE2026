# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Existence of a monochromatic-K5-free 2-coloring of K43
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1792
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Ramsey theory / extremal combinatorics
- **Method:** SAT encoding with DRAT unsatisfiability certification and heuristic search with exhaustive 5-set verification

## Problem

Does there exist a red-blue coloring of the edges of the complete graph K43 containing no monochromatic complete subgraph K5? A complete answer either exhibits such a coloring as an explicit 43-by-43 symmetric binary adjacency matrix together with a self-contained verification program that checks all C(43,5) = 962598 five-vertex subsets and confirms none is monochromatic, thereby establishing R(5,5) >= 44, or gives a machine-checkable unsatisfiability certificate proving that every red-blue coloring of K43 contains a monochromatic K5, thereby establishing R(5,5) <= 43.

## Attempted claim

Does there exist a red-blue coloring of the edges of the complete graph K43 containing no monochromatic complete subgraph K5? A complete answer either exhibits such a coloring as an explicit 43-by-43 symmetric binary adjacency matrix together with a self-contained verification program that checks all C(43,5) = 962598 five-vertex subsets and confirms none is monochromatic, thereby establishing R(5,5) >= 44, or gives a machine-checkable unsatisfiability certificate proving that every red-blue coloring of K43 contains a monochromatic K5, thereby establishing R(5,5) <= 43.

## Research outcome

Full K43 target blocked (best 120 monos over 32 heuristic runs; UNSAT infeasible); proved emergent lemma: no cyclic 2-coloring of K43 is K5-free, by exhaustive 2^20 enumeration verified by two independent programs.

## Why this attempt failed

Failed axes: correctness, originality.

correctness: EMERGENT_FINDING genuinely arose from symmetric-first K43 witness search, so scope is legitimate. Proof fails: cyc.c, cyc_verify.c and verify_cyclic.py all use d[k]=(mask>>(k-1)) for k=2..21, so bit20 is always 0 and bit0 unused; only 2^19 distinct d-vectors are visited (direct check: 524288 distinct, d21 identically 0), not the claimed 2^20. Complement-fixing and translation-to-vertex-0 reductions are valid and C(42,4)=111930, C(43,5)=962598 are correct, and a fresh recompile reproduces the logs, but logs count loop iterations not distinct colorings; the two C programs share the identical mapping bug so agreement gives no independence. Exhaustion is therefore unproved. originality: Normalized headline into literal, equivalent (circulant/cyclic/difference-set/Cayley on Z43), and dominance (exhaustive census/classification/database) queries in one fused search with full provider coverage. Prior Ivanov Zenodo v2 (2026-09-03) Theorem 3 states no S subset of {1..21} makes C(43,S) Ramsey(5,5;43)-valid, proved by exhaustive 1,048,575-representative check. Full-text theorem-scope comparison shows identical object, parameters, and conclusion to the submitted headline. Prior substantively covers the claim verbatim, so the submission is a recomputation; originality FAILS.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; address the recorded limitation: The lemma covers only cyclic (difference) colorings of K43, not arbitrary colorings, so it does not decide the admitted target (existence of any K5-free coloring of K43 / R(5,5) bounds). The independent Python verifier was timing-sampled (2000 masks in ~2.8 s, ~0.4 h projected full run) and stopped after the two compiled runs agreed, so its committed log is empty and it serves as archived source, not as a third completed run; verification rests on the two agreeing compiled logs. The literature-…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
