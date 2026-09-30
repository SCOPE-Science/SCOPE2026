# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/11/016`  
Independent audit date: 2026-09-28 (UTC)  
Task: `65b419b9c1230ba286453b0c84691e86`

The computation closes, but the claimed 7-cycle is a stem-conjugated classical A2 pentagon and repeats an exchange-graph vertex; it is neither a simple 7-cycle nor an original wild-quiver cycle.

## Audit basis

**Correctness:** The integer mutation replay and the final labeled-seed permutation are correct, but the headline conclusion 'a nontrivial 7-cycle in the exchange graph' is not. After the first mutation mu_3, the 1-2 entry has absolute value 1. The middle word mu_1 mu_2 mu_1 mu_2 mu_1 is exactly the standard A2 pentagon relation: it returns that seed up to transposition (12). Consequently the exchange-graph vertex after step 6 is the same as after step 1 (up to the labeling convention already used by the record), and the final mu_3 traverses the initial stem edge back. The seven-step sequence is therefore a closed walk consisting of a stem, the ordinary A2 pentagon, and the same stem in reverse—not a simple 7-cycle or a new wild-quiver cycle.

**Originality:** The decisive five-mutation core is the classical type-A2 pentagon relation. Fomin–Zelevinsky's rank-2 exchange graph has a pentagon in type A2 and the variables are switched after the five-cycle. Conjugating that universal relation by mu_3 does not create an original mutation-cycle phenomenon for the (3,2,2) seed.

**Scientific value:** Exact replay of a standard pentagon relation inside a larger seed is a useful software sanity check, but it does not establish the claimed new length-7 exchange-graph cycle and does not materially advance the mutation-cycle problem as packaged.

## Consequence

This package is preserved as a failed research attempt rather than silently deleted. The importer should relocate the complete original package atomically to the designated failed path together with this audit material.

## Literature

- [Fomin–Zelevinsky, Cluster Algebras I: Foundations](https://doi.org/10.1090/S0894-0347-01-00385-X): The type-A2 exchange graph is a pentagon, with the two variables switched after a full five-cycle; this is exactly the middle five-mutation relation used here.
