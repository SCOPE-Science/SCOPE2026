# Scientific review

## Correctness

**PASS.** The theorem uses a completely specified finite-state majority-update process. Following the first active group, the other group is the sole possible active group, so the update sequence is forced until consensus or a closed two-state alternating class. Private-group majority inequalities yield the exact condition \(2s<\min(a,b)\) for a closed polarized class. Exact first-event weighting correctly handles cases with one or two initially active groups. The unbiased-initialization formula follows by conditioning on a strict majority in a group's private part and correcting for initially inactive groups. An extracted exact-rational verifier independently checks \(18{,}544\) profiles and \(46\) complete fair-average cases. Risk: the claim does not extend automatically to a third hyperedge or to even-sized majority ties.

## Originality

**PASS under current accessible-source comparison, with residual priority uncertainty.** The closest directly related 3-uniform two-group loose-hyperstar subcase already establishes the \(1/4\) polarization probability for two triplets sharing one vertex and is explicitly excluded from the novelty claim. It does not imply the arbitrary odd sizes, general overlap sizes, exact conditional probabilities, sharp large-overlap consensus cutoff, or the all-size binomial-tail law. Golovin–Mölter–Kuehn describe an adaptive majority-propagation model and simulations, not these two-group exact formulas; Noonan–Lambiotte study mean-field and modular collections of triplets; Papanikolaou et al. use a different group-update mechanism; Lanchier–Neufer consider a lattice of overlapping blocks. Current search cannot exclude all unindexed mathematically equivalent results, particularly general finite hypergraph interacting-particle arguments that might implicitly encompass this configuration.

## Value

**PASS.** Pairwise intersecting social groups are the simplest nontrivial test of whether group majority influence enforces global agreement. The theorem completely classifies the all-size two-group case, identifies a topology-only boundary between inevitable finite consensus and feasible endless polarization, and computes the exact ex ante risk from natural independent initial opinions. The finite 3-uniform result is substantially generalized; the criterion distinguishes small and large overlaps and supplies canonical counterexamples to claims that connected finite hypergraphs necessarily reach consensus under majority updates.

## Closest literature and restrictions

The motivating paper is arXiv:2308.03640, first released 2023-08-07. For the classical hypergraph majority rule see Noonan–Lambiotte (2021) and Lanchier–Neufer (2013); the 2022 group-adaptive voter study uses a different update. The theorem applies only to precisely two intersecting odd hyperedges, no rewiring, and equal event rates. Computation checks finitely many structures, not all size pairs; the analytic proof carries universal quantifiers. Missing or unindexed exact results remain a priority risk. Independent external review is outstanding.

Self-review: passed. Independent audit: not yet performed.
