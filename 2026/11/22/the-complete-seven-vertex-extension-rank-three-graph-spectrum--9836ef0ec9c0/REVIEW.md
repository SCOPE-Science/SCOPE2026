# Scientific review of the seven-vertex extension-rank spectrum

## Correctness — PASS

The claimed invariant is the original one-point-extension game rank, not graph adjacency-matrix rank or first-order quantifier rank. Unrolling three extension steps gives the full-pair criterion; on exactly seven vertices it forces a degree-three root and the two local degree/mixed-neighbourhood tests, and the converse is immediate from the four patterns. Every rank-four graph needs at least eleven vertices. The fifteen integer-partition classes exhaust all permutations of seven vertices. For each class, enumerating unions of its induced edge orbits exhausts all fixed graphs, and Burnside's lemma then yields the complete labelled and unlabelled edge polynomials. A separate standard-library recursion over the graph atlas agrees. The replays are reproducible from the supplied source and data.

## Originality — PASS within inspected evidence

The primary 2026 rank paper introduces the invariant and proves broad existence, without this seven-vertex census. The closest published seven-vertex graph result proves the sharp onset and the unique six-edge extremizer; its full `RESULT.md` was inspected, and its explicit limitations do not give any count for the entire seven-vertex layer. The Read–Wilson graph atlas lists all small graph types but not their rank filter. published-finding corpus queries for the exact numbers, full-pair aliases and unrestricted edge spectrum found no covering census. Neither title matching nor absence of a result alone is taken as a novelty proof; the statement-implication comparison is decisive within the inspected sources. Database incompleteness and unsearched older literature remain risks.

## Value — PASS

The first possible rank-three order is a canonical, previously determined boundary, not an arbitrarily chosen graph slice. The present finite theorem replaces knowledge of only the sparsest witness with the complete distribution at every allowed edge count, including isomorphism orbits and exact labelled probabilities. Its concise root criterion explains the entire admissible family and its complement symmetry; the Burnside certificate makes the natural exact invariant reproducible and useful for subsequent sharper rank and graph-forcing investigations. No asymptotic significance or new six-edge theorem is claimed.

## Sources and limitations

Primary rank definition: López-Callejas and Navarro-Castillo, arXiv:2604.14461v1 (2026-04-15), https://arxiv.org/html/2604.14461v1. Closest quantitative theorem: *Sharp rank-three onset and six-edge extremum for finite graphs* (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-rank-three-onset-and-six-edge-extremum-for-finite-graphs--a3c35b6162f1. Graph-atlas source: Read and Wilson, *An Atlas of Graphs* (1998), https://r.igraph.org/reference/graph_from_atlas.html. The result is exact only at order seven; historical priority is provisional, and no independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
