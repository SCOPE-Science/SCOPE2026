# Independent Audit — 2026/09/11/016

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `b310d9ae648e89744a283d2197c96b9ea8044b39`  
**Disposition:** **FAILED**

## Correctness

**Verdict:** FAIL

The integer mutation replay and the final labeled-seed permutation are correct, but the headline conclusion 'a nontrivial 7-cycle in the exchange graph' is not. After the first mutation mu_3, the 1-2 entry has absolute value 1. The middle word mu_1 mu_2 mu_1 mu_2 mu_1 is exactly the standard A2 pentagon relation: it returns that seed up to transposition (12). Consequently the exchange-graph vertex after step 6 is the same as after step 1 (up to the labeling convention already used by the record), and the final mu_3 traverses the initial stem edge back. The seven-step sequence is therefore a closed walk consisting of a stem, the ordinary A2 pentagon, and the same stem in reverse—not a simple 7-cycle or a new wild-quiver cycle.

## Originality

**Verdict:** FAIL

The decisive five-mutation core is the classical type-A2 pentagon relation. Fomin–Zelevinsky's rank-2 exchange graph has a pentagon in type A2 and the variables are switched after the five-cycle. Conjugating that universal relation by mu_3 does not create an original mutation-cycle phenomenon for the (3,2,2) seed.

## Scientific value

**Verdict:** FAIL

Exact replay of a standard pentagon relation inside a larger seed is a useful software sanity check, but it does not establish the claimed new length-7 exchange-graph cycle and does not materially advance the mutation-cycle problem as packaged.

## Limitations

- The seven mutations do give a correct labeled-seed closure up to (12).
- That closure should be described as a conjugated A2-pentagon closed walk, not a 7-cycle.
- No minimality or new wild mutation-class phenomenon survives the audit.

## Independent checks

- Independently replayed the exchange-matrix/c-matrix mutations and reproduced the record's final B and C.
- Compared step 6 with step 1 and found they differ only by the stated transposition (12), proving the repeated exchange-graph vertex.
- Verified the assigned tree is unchanged through current main for the target path.

## Literature and comparison

- [Fomin–Zelevinsky, Cluster Algebras I: Foundations](https://doi.org/10.1090/S0894-0347-01-00385-X): The type-A2 exchange graph is a pentagon, with the two variables switched after a full five-cycle; this is exactly the middle five-mutation relation used here.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at the assigned tree. Git history comparison found no changes to this record between the assignment inventory, the dispatcher checked commit, and current `main`. No repository writes were made by this audit.
