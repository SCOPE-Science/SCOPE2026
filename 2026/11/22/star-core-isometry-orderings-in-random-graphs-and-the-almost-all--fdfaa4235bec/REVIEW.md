# Review: star-core isometry orderings in random graphs

## Correctness — PASS

The deterministic statement quantifies over every finite simple graph, center, and internal ordering of its neighbor and nonneighbor blocks. A star prefix preserves distance one/two, while any later prefix contains the entire closed neighborhood serving as a common-neighbor witness for *every* nonedge. This verifies the ordering criterion without assuming connectivity beforehand. For a fixed center, witness failure has exactly two types: nonedges incident to the center, with probability \((1-p)(1-p^2)^{n-2}\), and nonedges away from the center, with probability \((1-p)(1-p^2)(1-p^3)^{n-3}\). Disjoint edge sets justify the independent products; only a union bound is applied across distinct pairs. The stipulated sparse-density limit makes the every-center union bound vanish. For uniform labelled graphs, the exact Burnside argument bounds all nonidentity automorphism contributions by \(o(1)\) relative to the identity, and a component-union bound removes disconnected graphs. This proves the unlabelled connected assertion rather than assuming asymmetry. Two independently programmed finite verifiers corroborate the certificate, not the asymptotics.

## Originality — PASS, with residual historical priority risk

Nussbaum and Esfahanian's earlier paper poses the almost-all-graphs distance-preservation conjecture and already uses a star in its *different* large-minimum-degree construction; neither this idea nor the weaker conjecture is presented as new. Zahedi's 2015 paper repeats the random-graph question; Smith and Zahedi's subsequent work characterizes sequential orderings and proves results for four-chordal graphs. A later degree-based theorem requires minimum degree above half the graph order, which is not satisfied by \(G(n,p)\) at fixed \(p<1/2\). The 2025 open-access article still introduces the almost-all assertion as a conjecture. Searches for random-graph, almost-all, isometric-induced, sequential-ordering, and weakly-four-simplicial equivalent formulations, including published mathematical findings, did not locate a statement implying the explicit probability estimate or the unlabelled connected conclusion. Unindexed independent resolutions and inaccessible auxiliary proofs cannot be excluded.

## Value — PASS

The theorem answers an explicitly published almost-all distance-preservation conjecture for the intended connected unlabelled graph population, proves the *stronger* nested sequential property, and gives an explicit finite-size probability bound and a structurally transparent universal-order certificate. These are motivated natural quantities, not arbitrary finite slices, and the theorem includes a sparse-density regime; the threshold is expressly not claimed sharp.

## Prior work and limitations

Primary papers: Nussbaum–Esfahanian, *Preliminary Results on Distance-Preserving Graphs* (2013), Conjecture 6 and large-minimum-degree proof; Zahedi, arXiv:1507.03615, Question 5.7; Smith–Zahedi, arXiv:1701.06404, Proposition 3.4 and Theorem 3.5; Khalifeh–Zahedi, DOI 10.1002/jgt.22521; Smith–Zahedi, DOI 10.26493/2590-9770.1813.5ce (2025). The open primary text was inspected where available; the degree-theorem comparison is restricted to its publicly available statement. This is best-knowledge originality, not a guarantee that no prior proof exists. The density criterion is only sufficient, and no connectivity-threshold characterization is asserted.

Self-review: passed. Independent audit: not yet performed.
