# Self-review

## Correctness — PASS

The exact domain contains 4096 labelled binary configurations of the simple 5-regular icosahedral graph. An explicit 30-edge construction and its independent hard-coded edge-list implementation yield matching update tables and full attraction counts. An additional direct neighborhood-sum argument proves every cap equilibrium has only itself as a predecessor, independent of any enumeration. The first program proves \(F^{7}=F^{5}\) by checking every input and exhaustively counts fixed states, unordered two-cycles, all basins, cap states and sharp entrance times. The independent implementation checks graph isomorphism, all 120 automorphisms, the seven geometric classes and each orbit's basin. The delivered 82-row quotient certificate sums to 4096. Every claimed finite quantifier is checked, with no inference from sampling.

Residual correctness risks: the executable verification and proofs have not received independent expert validation; users should rerun both scripts and inspect the finite certificate. This is a complete finite proof, not an infinite generalization.

## Originality — PASS, qualified

The strongest classical implication checked is eventual period at most two for every finite symmetric threshold system (Goles–Olivos); it does not determine exact multiplicities, basin counts, isolated stable fixed states, a first-entry bound or an icosahedral group-orbit census. The complete Agur–Fraenkel–Klein (1988) fixed-point paper was inspected and concerns cyclic self-inclusive three-bit majority, not the icosahedral five-neighbor rule. The directly inspected Benjamini et al. arXiv:1405.2486v1 preprint analyzes unimodular and random graph behavior, not the fixed 12-vertex graph. The published dodecahedral majority result uses the 20-vertex dual graph; duality does not conjugate majority updates. Published icosahedral excitation counts use a different three-state update. Directed searches of mathematical records, icosahedral-majority phrases and OEIS did not find the stated census. An inaccessible original 1980 full text and unindexed literature leave genuine priority risk.

## Mathematical value — PASS

The icosahedral graph is the unique planar 5-regular 12-vertex Platonic graph, making it a canonical finite testbed for odd-degree, tie-free majority dynamics. The exact atlas reveals a nontrivial basin decomposition, with 12 strictly stable but isolated balanced equilibria, two very large consensus basins and seven geometrically inequivalent classes of oscillation. These structural features are not consequences of a universal period-two bound and permit exact benchmarking of convergence, initial-vote sensitivity and symmetry reduction. The task is a natural complete classification, not an arbitrarily sliced or merely numerical invariant; its limited finite scope is stated plainly.

Self-review: passed. Independent audit: not yet performed.
