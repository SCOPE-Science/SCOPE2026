# Review of minimum maximal matching mobility in the four-dimensional cube

## Correctness
PASS. Exhaustive matching construction from vertex-first search and independent search of all \(201,376\) five-edge and \(906,192\) six-edge subsets yield the same sharp optimum \(6\) and exactly \(192\) optimizers. The bipartite independent-set bound excludes lower sizes. All \(18,336\) optimizer pairs are explicitly tested for allowed exchanges. Two independent all-source breadth-first-search computations establish connectedness and the exact diameter. All \(384\) cube automorphisms are applied in a separate check of the orbit structure. The embedded scripts and their actual outputs allow replay.

## Originality
PASS on accessible evidence, with residual historical uncertainty. The nearest classical work addresses the edge domination number or complexity without classifying minimum-solution exchanges. The 2009 hypercube paper studies extendability of matchings to perfect matchings, not mobility of six-edge maximal matchings. The accessible full-text 2014 preprint studies dominating *induced* matchings; its restrictions differ. The accessible full-text 2019 regular-graph paper proves scalar bounds and approximations; it supplies neither the optimizer census nor this reconfiguration graph. Indexed results on the four-cube concern perfect-matching difference multiplicities, matching complexes, and independence complexes. The accessible historical claim archive was compared for minimum-maximal-matching and cube-overlap wording and did not reveal this claim. Prior results do not logically imply the new degree, orbit, or diameter data. Unindexed counts and full inaccessible older texts are acknowledged limitations, not ruled out.

## Value
PASS. Minimum maximal matchings are optimal edge-dominating resources. A minimum cardinality alone does not describe whether one optimum can be converted to another while retaining the resource budget. The sharp obstruction for one-edge moves and the fully connected two-edge macro-move network reveal an exact stability-versus-flexibility boundary. The two symmetry orbits and distinct local degrees explain heterogeneous configuration mobility; radius and diameter quantify global relocation cost. This is a complete natural finite optimum-state space, not an arbitrary restricted slice.

## Sources and residual risks
Vandenbussche–West (DOI:10.1137/080732687), Horton–Kilakos (DOI:10.1137/0406030), Yannakakis–Gavril (DOI:10.1137/0138030), Hibi et al. (arXiv:1412.3881), and Baste et al. (arXiv:1905.12241) were compared by statement and parameter. The arXiv primary papers' mathematical portions were read; older paywalled material was assessed from accessible abstract/metadata only, not represented as completely read. The numerical claim concerns only the finite four-cube and does not prove an infinite-family theorem.

Self-review: passed. Independent audit: not yet performed.
