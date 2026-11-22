# Scientific review: cycle-Mycielskian monitoring

## Correctness — PASS

The graph is \(H_n=\mu(C_n)\), with original cycle vertices \(u_i\), independent shadows \(v_i\), and apex \(w\), for every \(n\ge5\). Monitoring is defined by strict increase of distance on deleting a single edge. Every shadow is mandatory: the apex edge \(wv_i\) cannot be monitored by a pair that omits \(v_i\), because every shortest path with \(v_i\) internal admits a same-length detour. For a shadow edge \(v_{i+1}u_i\), all detecting pairs are exactly \(\{v_{i+1},u_i\}\) and \(\{v_{i+1},u_{i-1}\}\); this forces omitted originals to be independent. Conversely, the proof displays unique-shortest-path monitoring pairs for apex, shadow, and rim edges when the originals form a vertex cover. The resulting free-apex independent-set enumerator and maximal-independent-set cyclic gap count are exact, including integer coefficients and boundary orders. The minimum-state exchange graph is a cycle for odd order and two isolated states for even order. The complete algorithm in `verify.py` independently checks the original deleted-edge distance predicate and all \(698{,}368\) vertex subsets at orders five through nine, with additional local-pair tests at orders ten through fifteen. The symbolic proof, not the finite experiment, establishes the infinite quantifier.

## Originality — PASS (best-knowledge assessment)

The motivating first-public 2022 paper [arXiv:2210.03774](https://arxiv.org/abs/2210.03774) introduces monitoring edge-geodetic sets and presents different graph families; its inspected full text gives no Mycielski-cycle theorem. Haslegrave [arXiv:2210.08955](https://arxiv.org/abs/2210.08955) treats products, not this operation. The full text of [arXiv:2403.09122](https://arxiv.org/abs/2403.09122) proves a sufficient vertex-cover rule under girth at least five, whereas the graphs here have four-cycles; it neither forces all shadows nor classifies legal sets. The Mycielski-specific [arXiv:2311.13979](https://arxiv.org/abs/2311.13979) addresses locating/domination signatures, not geodesic edge-failure monitoring. Indexed comparisons with cycle, subdivided-clique, unicyclic and theta monitoring results involve different graph objects or cannot imply the all-set equivalence. Related searches for Mycielski, Mycielskian, shadow vertices and monitoring found no decisive prior implication. This does not prove absolute novelty; obscure or unindexed sources remain possible.

## Mathematical value — PASS

Mycielskians are a natural operation producing highly structured triangle-free graphs and are used in graph coloring. Here an edge-failure monitoring predicate simplifies exactly to the cycle vertex-cover complex only after the nontrivial mandatory-shadow lemma. This determines all feasible configurations, all inclusion-minimal configurations, a nonpure spectrum with the unusual pure return at order seven, and an exact parity bifurcation in optimal sensor mobility. These consequences answer natural placement, redundancy, and relocation questions across an infinite family; the value does not rest on a routine numeric invariant or a finite computer census.

## Limitations and comparisons

The graph family and the single-edge-failure sensing rule are fixed. Arbitrary Mycielskian bases, multiple edge failures, and intermediate nonmonitoring moves are not addressed. The deletion-distance program gives finite cross-checks and cannot by itself establish the universal theorem. Nearby monitoring literature and indexed result summaries have been compared at the level of object, predicate, and logical implication, but independent mathematical audit and global publication-priority clearance are outstanding.

Self-review: passed. Independent audit: not yet performed.
