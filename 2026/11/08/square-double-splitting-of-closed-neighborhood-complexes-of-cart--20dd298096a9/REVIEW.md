# Self-review

## Correctness — PASS

The object is the simplicial complex of vertex subsets contained in closed graph neighborhoods of the Cartesian product of two connected graphs, each without cycles of length three or four. The proof separates length-two pairs by the number of common neighbors: uniqueness permits explicit elementary deletion, while pairs having two common neighbors are precisely diagonals of Cartesian product squares. Every face with at least three neighbors of one center has that center uniquely and is eliminated by a free-face pair in decreasing cardinality. This leaves the double-triangulation of each product square. One triangulation per square realizes the topological product; the second is a disc with nullhomotopic attaching loop, providing one integral two-sphere. Every attaching map, dimension and factor hypothesis has been checked. A self-contained program confirms all proposed collapses on ten finite test products and computes mod-two boundary ranks independently. These finite tests are supporting evidence, not an infinite-family proof.

## Originality — PASS, with stated risks

Matsushita (arXiv:2511.12608, first public November 16, 2025) provides the motivating closed-neighborhood framework and a Cartesian example where both factors are complete graphs; that result does not imply this two-high-girth-factor splitting. Adams–Shukla–Singh (arXiv:2212.05871) classify binary hypercube scale-two Čech nerves; they do not obtain nontrivial product fundamental groups such as that of two pentagons. The earlier high-girth prism result is subsumed when one factor is an edge and is explicitly excluded from the originality claim. Clique-fiber constructions with a complete-graph second factor and toroidal **open**-neighborhood complexes are distinct objects. Statement-level and alternative-terminology published-finding corpus searches found no covering formula for two factors without triangles and four-cycles. Residual risk is a more general unindexed theorem about graph-square filling complexes or closed-neighborhood functorial products; the search evidence alone cannot rule this out.

## Mathematical value — PASS

The result identifies a natural and widely studied finite-vertex Čech construction on Cartesian graph products with a complete integral homotopy splitting for every pair of high-girth factors. Unlike the known prism special case, both factors may contain independent cycles, making the fundamental group a product of nontrivial free groups (in particular, \(\mathbb Z^2\) for toroidal grids) while the nerve acquires exactly one *additional* two-sphere per product square. The explicit simple-homotopy collapse and exact sphere multiplicity explain how local neighborhood fillings interact with product two-cells. This is structural information not supplied by homology ranks or the special-case prism alone.

## Limitations

No claim is made for factors with triangles/four-cycles, equivariant splittings, additional filtration scales, or higher Cartesian products. The all-family theorem is proved symbolically; the ten-case computational check is nonexhaustive and cannot substitute for the proof. The literature comparison cannot exclude unindexed equivalent results.

Self-review: passed. Independent audit: not yet performed.
