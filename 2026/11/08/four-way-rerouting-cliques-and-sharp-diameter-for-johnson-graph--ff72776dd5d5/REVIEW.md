# Review of the Johnson-geodesic rerouting theorem

## Correctness — PASS
A shortest path of length \(d=|A\setminus B|\) must increase its intersection with \(B\) on every step. Hence the two independent permutations encode all and only geodesics. Fixing the vertices immediately before and after a rerouting rank produces exactly four intermediate choices, which establishes adjacency and all clique counts. A common comparator schedule sorts two arbitrary permutations in at most \(\binom d2\) steps; the reverse-order inversion obstruction gives equality. Vertex transitivity supplies the radius. Independent complete enumeration of paths through \(d=4\) and Cayley BFS through \(d=5\) confirms the key finite identities, without being treated as an infinite proof.

## Originality — PASS (qualified)
The closest model is Bonsma (arXiv `1009.3217v1`, 2010). Zara (2003, DOI `10.37236/1683`) classifies constrained *relevant ascending* Johnson paths, not all shortest-path reroutings. Asplund et al. (arXiv `1705.09385v1`) and Gajjar et al. (2024, DOI `10.1007/s00453-024-01263-y`) establish the single-permutation hypercube analogy, but their reviewed results do not determine the paired-synchronous-generator graph, its unique four-cliques, or the exact Johnson diameter. Searches covering Johnson geodesics, paired permutations, and synchronized adjacent swaps found no exact same-claim record. Unindexed equivalent work is an unresolved historical-priority risk; a failed search is not proof of novelty.

## Value — PASS
This classifies all one-vertex reroutings of shortest paths between *every pair* of vertices in the classical Johnson family, not an arbitrary finite instance. The simultaneous-removal/insertion constraint creates local \(K_4\) geometry instead of the hypercube's ordinary permutohedral edges; yet the sharp global diameter remains \(\binom d2\), despite the quadratic-order increase from \(d!\) to \((d!)^2\) states. A single fixed sorting network supplies uniform constructive rerouting. Individual all-pairs distances and shortest-sequence counts remain outside the theorem.

Self-review: passed. Independent audit: not yet performed.
