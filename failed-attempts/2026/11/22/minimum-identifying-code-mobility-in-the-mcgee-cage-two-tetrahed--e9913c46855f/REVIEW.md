# Independent mathematical audit

## correctness

PASS

The finding fixes the LCF graph [12,7,-7]^8, ordinary closed-neighborhood identification, and moves preserving size-optimality. If k vertices identify, 4k is the total signature size and at most k of the 24 nonempty distinct signatures are singletons, so 5k >= 48. An independent direct-signature search checked all 1,961,256 ten-sets and 2,496,144 eleven-sets, giving 0 and 384 codes, respectively. It checked all 54,912 oriented one-for-one replacements. There are 208 jump components and 272 jump edges: 176 singletons, 16 isolated edges and 16 copies of the specified glued-clique graph T. For each T it checked both four-cliques, their common vertex, and the four distinct noncentral attachments, two on each clique. It expressly checked that the two slides in each T are pendant and that no jump K2 supplies a slide. There are 352 slide components and 32 slide edges, giving 320 slide-frozen codes. Diameter 4 follows from two leaves on opposite cliques. The frozen Python lines 125–126 check T and the number of slides per jump component, but not their placement on pendant edges; the new replay checks the missing assertion. This is exact on this graph only, not for larger budgets, other cages or stronger identification predicates.

## originality

PASS

The optimum cardinality, 384 masks and their 13 orbits are covered and not credited as new. No inspected source states the two exchange decompositions, the exact motif T, or the slide placements for this optimum space. This judgment is limited to the newly tabulated structural description, not to new input data, an independent theoretical result about identifying codes, or historical priority. The ease of obtaining that description mechanically from the previous data is assessed separately under value.

## value

FAIL

Optimum-preserving detector relocation is a natural question on this canonical cage, and the exact fragmentation could be useful as a benchmark. But the significant prior input is not merely the host graph or the number 384: it specifies every labelled optimum by a short orbit table. Expanding those orbits and doing at most 73,536 pairwise symmetric-difference tests, one base-graph edge lookup per jump, and ordinary component/degree traversal mechanically gives the whole reported invariant, including the glued-clique shape and pendant slides. No further mathematical property explaining or separating these exchanges is established beyond inspecting that fixed computed graph. The record independently reproduces a correct, previously unstated table-derived fact, but does not meet the nonmechanical requirement for a contribution this narrow. Better motivation or a corrected checker assertion would not change this limitation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
