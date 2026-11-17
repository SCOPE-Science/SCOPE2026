# Scientific review

## Correctness — PASS

The graph and update rule are fully specified by the self-contained source programs. The first algorithm enumerates all \(2^{19}\) states for the original graph and every one of its 38 deletions, computes the entire functional digraph through deterministic successor arrays, checks first entry into period at most two, and separately counts consensus-reaching states. The independent implementation reproduces the original and one representative from each class, computes the 24 graph automorphisms, verifies that their orbits cover all 38 edges with sizes \(2,12,12,12\), and confirms matching values. The displayed inequalities follow directly. The only asserted universe is the finite family, not untested graph orders.

## Originality — PASS (qualified)

Robertson's original two-page construction proves the graph and enumerates its four edge types; it does not analyze binary majority attraction. The accessible Goles–Olivos abstract proves only an eventual period restriction for symmetric threshold networks. The first two pages of the full Agur–Fraenkel–Klein paper establish that it treats a cyclic three-site majority automaton, not this graph. The closest identified Chvátal-graph single-edge census has *opposite* behavior for the two-cycle orbit count: those counts decrease for every deletion whereas here they increase for every deletion. A separate complete-bipartite edge-defect result has different graph structure and cannot imply the quartic-girth-five all-edge result. Semantic mathematical-record queries found no claim with these same graph, rule, parameters and edge-wise effects. Searches are not proof of absolute priority; relevant unindexed historical work could exist.

## Value — PASS

The Robertson graph is a canonical minimum-order quartic girth-five cage, with a small number of graph-inequivalent edge perturbations fixed in its original structural description. Its one-edge removals are therefore a mathematically natural complete test, not arbitrary sampled edges. The strict simultaneous gain in unanimity attraction **and** period-two orbit diversity, paired with loss of fixed states, separates three natural dynamical observables and contrasts with the previously documented Chvátal case. The four-class exact census and sharp transient time make the distinction reproducible and potentially useful in threshold-network perturbation studies. The value is the concrete finite structural classification, not a claim of a general monotonicity principle.

## Limits and closely related literature

The existence of two-periodic attractors in symmetric threshold dynamics is classical, and no novelty is claimed for that theorem. This assessment does not assert comprehensive historical priority or certify independent validation. Classical papers inaccessible in full were assessed only to the extent of available abstracts, with that limitation explicitly recorded.

Self-review: passed. Independent audit: not yet performed.
