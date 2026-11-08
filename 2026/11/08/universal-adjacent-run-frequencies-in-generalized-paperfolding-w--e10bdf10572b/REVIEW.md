# Review of the universal generalized-paperfolding adjacent-run law

## Correctness

**PASS.** The word is explicitly normalized by its 2-adic valuation formula for arbitrary instructions. Opposite signs at successive odd positions bound run length by three. A complete adjacent pair is a local factor of length at most eight. Exactly one position of such a window is divisible by eight; conditional on the starting residue modulo sixteen, its sign is asymptotically balanced for all instruction tails. The other seven positions are fixed by the first three instructions. An exhaustive finite \(32\)-template enumeration for each normalized triple gives the claimed integer matrix, with direct checker replay. Converting position density to run-index density uses the independently established total pair density \(1/2\). The mutual information is a direct exact calculation.

## Originality

**PASS, with residual priority risk.** Madill–Rampersad (2012) studies abelian factor complexity, not run-pair frequencies. Shallit (arXiv 2024) provides a finite-automaton description, the possible run lengths and run-factor support, but the inspected full text does not calculate an all-instruction invariant pair-frequency matrix or the mutual information. Bunder–Bates–Arnold (2024) addresses the regular word and its continued fractions. The later automaton work could in principle be used for an independent derivation, and the inaccessible full 1994 canonical-position study remains a historical priority risk. The claim is not that allowed pairs, the run-length bound, or automata are new.

## Value

**PASS.** The exact two-point law provides a natural quantitative statistic beyond known support and subword complexity, and its striking invariance across all folding instructions makes it relevant to the large class of paperfolding words rather than just a single numerical example. It separates the deterministic transition restrictions from statistical independence, yielding a nonzero exact information measure.

## Limits

The result covers only ordered pairs of successive run lengths, not longer correlations. The direct-prefix checks are not substitutes for the 2-adic proof. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
