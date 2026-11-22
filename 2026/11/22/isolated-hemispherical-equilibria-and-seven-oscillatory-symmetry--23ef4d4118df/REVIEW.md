# Scientific review

## Correctness — PASS

The domain is the labelled, twelve-vertex, five-regular icosahedral graph with binary synchronous open-neighbor majority threshold three. The transition formula is exact at each vertex. Two independently written exhaustive checkers inspect every one of 4096 configurations, using separate edge definitions and separate five-neighbor threshold implementations (popcount versus ten three-neighbor conjunctions). They agree on all fixed configurations, all first-entrance/period cells, 156 temporal two-cycles, individual basin sizes, and the sharp five-update bound. A full exhaustive adjacency-preserving permutation backtrack supplies all 120 automorphisms and verifies the seven spatial cycle types; the programs confirm equivariance on all configurations. The explicit trajectory starting at integer 87 witnesses the sharp cutoff. Limits: this proves only the finite stated graph; it does not prove a larger-family theorem.

## Originality — PASS with residual historical-priority risk

The strongest relevant prior general theorem (Goles–Olivos, 1980) restricts eventual periods to one and two but does not determine exact icosahedral counts. The accessible full text of Tošić–Agha (2004) addresses parallel/sequential threshold automata, mainly in one dimension. Benjamini and coauthors (arXiv:1405.2486v1, 2014) address random and infinite graph majority, and Kaaser et al. (MFCS 2016) prove general voting-time bounds, not the exact icosahedral delay. A published dodecahedral majority census treats the degree-three, twenty-vertex dual graph; it does not imply the degree-five icosahedral result. A published icosahedral three-state excitation study has a different transition. Targeted published-claim searches using icosahedron, closed neighborhoods, 14 fixed, 156 two-cycles and basin 1586 returned no claim with equivalent coverage. Exact unindexed tabulations could exist; no search proves uniqueness.

## Value — PASS

The twelve five-neighbor caps are natural geometric hemispheres of the icosahedron, yet are dynamically inaccessible from all other initial states: all nonunanimous equilibria are singleton basins. In contrast, almost 77.5% of configurations reach consensus, while 156 two-cycles exhibit four distinct exact basin sizes and seven spatial orbit types. This separates geometric stability from dynamic accessibility and quantifies the full finite phase portrait of a canonical highly symmetric five-regular network. The exact invariant is motivated by the graph's six antipodal vertex pairs and its role as the dual Platonic solid to the dodecahedron, not by an arbitrary induced subgraph or parameter slice.

## Closest literature and limitations

- Goles–Olivos (1980), DOI 10.1016/0012-365X(80)90121-1: general period restriction, not a graph-specific census.
- Tošić–Agha (2004), ACRI, accessible OA full text: general threshold automata and one-dimensional classifications, not this finite graph.
- Benjamini et al. (2014), arXiv:1405.2486v1: almost-sure and random-graph majority behavior, not the exact icosahedral numbers.
- Kaaser et al. (2016), DOI 10.4230/LIPIcs.MFCS.2016.55: structural upper bounds for convergence, not the exact sharp bound and basin census.
- Published dodecahedral majority and icosahedral excitation finite calculations: different graph and different dynamical rule respectively.

All finite counts are reproducible, but no independent external mathematical validation is asserted. Unindexed earlier calculations and incomplete historical access remain priority risks.

Self-review: passed. Independent audit: not yet performed.
