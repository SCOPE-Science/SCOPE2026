# Review of the exact finite-level Kolakoski Schreier distance census

## Correctness
**PASS.** The finite claim is supported by the published two-permutation block recurrence (Mitchell--Walton--Whittaker, arXiv:2611.06878v1, Corollary 4.8), whose base and level-two cases were checked. Every one of the \(2^n\) starting vertices was traversed by directed breadth-first search at all fifteen levels. Each graph was confirmed strongly connected and each all-pairs histogram summed to \(2^{2n}\). A second C++ program independently reconstructs the permutations and explores all reversed arrows, recovering the same diameters and ordered diametral-pair multiplicities. A Python tuple-state implementation independently confirms the first nine levels. The equality \(D_n=n+4\) is asserted only for the seven stated finite levels; it is not extended by extrapolation.

## Originality
**PASS within inspected evidence.** The source graph recurrence and its all-level strong connectivity are established prior results, and not independently claimed. Material read in the relevant sections of Mitchell--Walton--Whittaker, especially Corollary 4.8, Figure 6 and Theorem 5.3, disclosed no evaluated directed diameter or all-pairs metric census. MacAulay's 2026 full text concerns the closely related run-length permutation automaton, group orders through twelve levels and lengths of cycles of single permutation products, not the minimum number of arbitrary generator steps between all ordered pairs. The closest identified Kolakoski finding in published mathematical records and accessible local claim history gives shortest **symbolic shift orbit periods** for finite derivative-depth systems; this is a different dynamical invariant and does not imply these accelerated-graph directed distances. Residual risk: a specialized historical graph-distance table could be unindexed or named differently.

## Value
**PASS.** After a qualitative strong-connectivity theorem, the minimum number of accelerated moves needed to connect arbitrary directive states is a natural quantitative invariant. A complete exact metric census of the first fifteen canonical graphs, reaching 32,768 states and more than a billion ordered pairs, demonstrates an empirically sharp finite near-Moore regime and supplies a reproducible quantitative benchmark. The exact finite cutoff is useful independently of a future general formula; no general formula is claimed.

## Uncertainty and limits
The first public paper is from 4 November 2026. The graph recurrence is not novel and is explicitly credited. Computational exhaustive proof covers only levels one to fifteen, with a separate algebraic two-outdegree Moore lower bound. Directed accelerated distances must not be interpreted as unaccelerated shift durations. Historical priority remains provisional; the record is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
