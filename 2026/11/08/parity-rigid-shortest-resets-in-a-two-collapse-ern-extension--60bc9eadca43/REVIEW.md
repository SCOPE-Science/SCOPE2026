# Scientific review

## Correctness: PASS
The precise transition table, all integers \(n\ge2\), and unit letter costs are stated in `RESULT.md`. Set-theoretic inverse images preserve inclusion. In a shortest reset path, deleting any nonexpanding, nonrotating reverse letter would still yield full preimage, so every reverse step is either a one-step inverse rotation or a one-state interval expansion. These expansions can occur only at two adjacent endpoint residues. Exactly \(n-1\) expansions are required, and the alternating one-step / \(n-1\)-step spacing forces the length and parity-specific unique or two shortest words. The boundary case \(n=2\) is explicit. The provided standalone program confirms the shortest distance for \(2\le n\le15\), all optimal words for \(2\le n\le12\), and independent expansion-span arithmetic for \(2\le n\le50\). These are finite checks, not an infinite proof.

## Originality: PASS (qualified)
The closest primary sources are Zhu, *A quadratic upper bound on the reset thresholds of synchronizing automata containing a transitive permutation group* (arXiv:2407.08135v1, Theorems 1.4 and 2.7), whose class-wide bound is far weaker and does not determine uniqueness; de Bondt–Don–Zantema, *Slowly synchronizing automata with fixed alphabet size* (arXiv:1609.06853, Sections 3, 5), which discusses extensions but not this labeled three-letter exact formula; and Gonze et al., *On the interplay between Babai and Černý's conjectures* (arXiv:1704.04047v2, Section 2.1), in which the added adjacent generator is a transposition rather than a nonbijective rank-\(n-1\) letter. Semantic searches for neighboring simple idempotents, two adjacent collapses, exact threshold and optimal-word multiplicity found no equivalent covering statement. Prior published two-letter deficiency and avoidance formulas are not the same automaton. Residual risk: an unindexed equivalent formulation may exist, so this is not a universal priority assertion.

## Mathematical value: PASS
The result completely classifies the optimal reset length and all shortest reset words for an infinite, naturally motivated extension of a classical extremal family. It quantifies a substantial effect of an added adjacent collapse (approximately halving the quadratic threshold) and reveals parity-rigid optimal-word multiplicity. The classification is an exact object-level theorem, not a parameter substitution or small-instance enumeration.

## Limitations
The theorem is for unit-cost letters and the given labeled automata only. It does not classify arbitrary two-collapse placements or all weights; no external expert or independent audit has been performed. Its scientific originality is assessed against the inspected texts and recovered indexed records, not every conceivable publication.

Self-review: passed. Independent audit: not yet performed.
