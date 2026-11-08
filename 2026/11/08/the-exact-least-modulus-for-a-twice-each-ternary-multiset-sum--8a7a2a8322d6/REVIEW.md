# Scientific review: twice-each ternary modulus

## Correctness — PASS
The exact statement requires a single multiplicity vector of total \(2n\) to share the target sum modulo the least modulus. The proof reduces that assertion to the minimal number of ternary coins and a parity condition. For the proposed odd modulus, negative differences are excluded by the minimum size of the target, and positive differences force more than \(2n\) coins. Every smaller modulus is defeated by an explicit permitted difference; the final odd-modulus case uses digit-sum and a maximal ternary-power parity constraint. The argument includes all \(n\ge2\) and does not infer infinitude from tests. Independent finite algorithms enumerate compositions and reachable powers and agree for \(n=2,\ldots,8\).

## Originality — PASS, qualified
Fonollosa's July 2026 theorem evaluates the minimum modulus for binary powers with **one** copy of each element and \(n\) total summands. Its precise result, including the greedy binary-coin argument, does not state or imply the present formula for ternary powers with **two** copies each and \(2n\) summands. The author's listed related finite-abelian-group generalization also concerns the original all-ones problem. Published research-record searches did not identify an implication or equivalent theorem. The related permanent companion was inspected at abstract level only: there is a residual risk from its inaccessible full text. Earlier unindexed equivalent work is possible. No covering equivalent theorem was identified in the scientific comparisons.

## Mathematical value — PASS
The recent modular-uniqueness problem motivates exact transform moduli and explicitly identifies variations of its target multiplicities as a natural direction. The result solves a whole infinite-parameter family and exhibits a parity-sensitive ternary cutoff. It is not simply evaluating a few numerical instances; the proof gives the exact optimum and all smaller-modulus obstructions.

## Scope and limitations
This fixes both the radix and the multiplicity profile; it makes no universality assertion over all residue sets. Arithmetic experiments are a reproducibility check only. Priority is not certified and an inaccessible relevant companion source leaves a limited comparison risk.

Self-review: passed. Independent audit: not yet performed.
