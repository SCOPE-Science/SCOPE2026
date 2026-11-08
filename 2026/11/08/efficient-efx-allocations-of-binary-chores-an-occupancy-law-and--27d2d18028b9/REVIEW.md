# Scientific review

## Correctness — PASS

The efficiency equivalence is proved by direct transfers of any misallocated private-zero chore, and by the absolute social-cost lower bound for fractional assignments. The EFX test considers **every owned chore**, including zero-cost chores; this is necessary for the exact occupancy inequalities. Labeled-item multinomial counting, the two-agent parity bounds, fixed-dimensional Gaussian convergence, and the fixed-width Stirling estimate each have explicit proofs in `RESULT.md`. An independent brute-force enumeration of assignments checks 174 finite parameter instances and 81,620 labeled allocations with direct Pareto and EFX tests; 176 additional comparisons check the symmetric occupancy identity. The infinite and asymptotic assertions are supplied by proof, not inferred from finite computation.

## Originality — PASS, subject to stated priority risk

The closest initiating source, Tao et al. (arXiv:2308.12177v1), proves binary chore EFX/PO existence and supplies the pertinent definition, not an exact labeled allocation census. Lin et al. (arXiv:2609.13970v1) establish a stronger weighted EFX/fPO existence theorem and note the strengthening induced by owned zero-cost chores; that qualitative mechanism is prior work, but it does not state the binomial odd/even count reversal or the occupancy-probability transition. Neoh and Teh (arXiv:2504.03951v1) study counting EFX allocations for **goods** and restricted sizes, so their reported theorems do not imply the present chore count. He and Tao (arXiv:2606.08872v1) analyze existence and counterexamples outside the binary domain. Related published mathematical-record claims concern different objects or statistics. Publication-priority uncertainty remains for unindexed work and for full text not inspected outside the closest chore sources.

## Value — PASS

The result answers a natural question not resolved by an existence algorithm: what fraction, and how many, efficient binary-chore outcomes are EFX? It provides a complete exact finite census for arbitrary private-zero counts, a sharp parity-sensitive **decrease** in the count when a socially costless task is added, and a \(\sqrt{u}\)-scale prevalence threshold for symmetric populations. These are meaningful robustness and sampling facts about the strong quantifier in EFX and are not asserted as advances in probability theory. The cost model is deliberately restricted, and broader binary-cost counts remain outside scope.

Self-review: passed. Independent audit: not yet performed.
