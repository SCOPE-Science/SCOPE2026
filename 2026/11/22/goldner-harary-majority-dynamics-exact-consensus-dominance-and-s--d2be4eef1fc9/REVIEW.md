# Scientific evaluation

## Correctness

PASS. The 27 labelled edges correspond exactly to the named Sage Goldner–Harary construction. The binary update is unambiguous even at degrees six and eight because tie retention is explicit. One program evaluates all \(2^{11}\) states by integer bit-count comparisons and proves the whole functional graph classification by indegree peeling. A second independently builds the graph from all individual edges, uses signed-neighbor sums, and traces every orbit until repetition. Their separately constructed cycle identities, exact basin catalog, and entrance distributions agree on all 2,048 inputs. A third program verifies all degree-compatible graph automorphisms and their recurrent orbit classes. The depth-four witness is \(179\to119\to51\to49\to0\).

## Originality

PASS within the checked literature, with historical-priority risk. The graph-specific numerical and geometric census is not implied by the classical period-two theorem (Goles–Olivos, 1981; Benjamini et al., arXiv:1405.2486v1). Lima, Moreira and Araújo (arXiv:1205.5297v1) study stochastic majority-vote critical behavior on larger Apollonian networks, not finite deterministic synchronous attraction basins. The Sage source provides only the exact graph. Published exact majority basins on other named graphs do not imply the Goldner–Harary values. Searches for aliases, exact counts, the same graph and equivalent models found no dominating prior result. An unindexed enumeration could exist.

## Value

PASS. The Goldner–Harary graph is the canonical smallest non-Hamiltonian maximal planar graph, and a planar 3-tree. The full finite census determines a natural, previously non-implied invariant: \(935/1024\) initial states reach consensus even though the network supports 47 oscillating attractors, all with extraordinarily small individual basins. The distinction between attractor quantity and basin weight, and the exact four-step cutoff, are directly informative for deterministic opinion dynamics on a natural dense planar network. No broader planar-graph law is asserted.

## Closest work and limitations

Most pertinent sources are the full-text 2012 Apollonian majority-vote preprint and the 2014 majority-dynamics preprint, together with the explicit Sage graph construction. Only the specified finite deterministic model is classified; global novelty against unindexed computations and independent reproducibility remain unresolved.

Self-review: passed. Independent audit: not yet performed.
