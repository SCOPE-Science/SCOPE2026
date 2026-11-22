# Scientific review

## Correctness — PASS
The three-block event has probability \(6/[n(n-1)]\) for each specified value triplet. The three classes of pairs of triplets have exact probabilities derived from block contractions; their summed overlap is \(O(n^{-2})\), establishing rarity and asymptotic uniqueness. Given one event, its six internal orders are independent of the contracted uniform permutation. Mixed factorial moments of nonboundary positive and negative adjacencies converge to those of two independent mean-one Poisson variables. The boundary error is uniformly \(O(n^{-1})\). Transferring from a specified block to the union event introduces only a relative \(O(n^{-1})\) error on bounded test functions. Exhaustive exact-rational checks support all finite combinatorial steps. A proof, not finite computation, supplies the limit.

## Originality — PASS, with historical priority risk
Corteel–Louchard–Pemantle (2006), particularly Section 2, gives the unconditional Poisson limit for common adjacencies and separate exact/asymptotic information about the *number* of three-label common intervals. Xu–Alain–Sankoff (2008) establishes marginal Poisson adjacency laws and their use for genomic testing. Neither the inspected Section 2 of the first article nor the accessible substantive sections of the second establishes a conditional joint signed adjacency limit when at least one rare three-block occurs. The result is not implied by their marginal limits or triplet expectations: conditioning on an event of probability \(\Theta(n^{-1})\) can change the limit while leaving all unconditional limits untouched. Relevant semantic database searches did not reveal the same theorem. Historical equivalent formulations, especially within older runs/genome literature, remain a bounded priority risk; a failed search alone is not evidence of uniqueness.

## Value — PASS
An observed conserved three-gene block necessarily forces at least one common adjacency, and its internal orientation creates one of four dependent signed marks. Using an unconditional Poisson baseline after selecting for a common three-block therefore miscalibrates the count distribution. The full conditional marked law gives a natural asymptotic null model for such selected comparisons, distinguishing increasing/decreasing orientations; this is an exact structural relationship, rather than recomputing a known marginal or selecting arbitrary numerical parameters.

## Scope and limitations
Only independent uniform linear gene-order permutations are covered, with the first order normalized to identity. The event is rare, asymptotic to \(6/n\). No evolutionary mechanism, explicit total-variation convergence rate, or signed/circular extension is claimed. Finite checking does not replace the proof. No independent audit has been performed.

## Primary literature
- S. Corteel, G. Louchard, R. Pemantle, *Common Intervals in Permutations*, DMTCS 8 (2006), 189–214, https://doi.org/10.46298/dmtcs.362.
- W. Xu, B. Alain, D. Sankoff, *Poisson adjacency distributions in genome comparison*, Bioinformatics 24 (2008), i146–i152, https://doi.org/10.1093/bioinformatics/btn295.
- F. de Montgolfier, M. Raffinot, I. Rusu, *Easy Identification of Generalized Common and Conserved Nested Intervals*, J. Comput. Biol. 21 (2014), 520–533, https://doi.org/10.1089/cmb.2013.0146 (background on interval definitions and detection rather than probability).

Self-review: passed. Independent audit: not yet performed.
