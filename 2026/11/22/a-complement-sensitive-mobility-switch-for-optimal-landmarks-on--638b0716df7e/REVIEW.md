# Independent mathematical audit

## correctness

PASS

The five generators have one dependence, using all five; consequently differences are uniquely singletons or pairs of generator labels. This gives exactly zero common neighbors if adjacent and two if nonadjacent, diameter two, and independence of each neighborhood. In the complement, an edge uv of G has six other vertices adjacent to neither in G (each endpoint has four other neighbors and they are disjoint); these are common complement neighbors. Thus both distances 1 and 2 really swap, while a landmark is singled out by a zero. Three landmarks cannot distinguish thirteen outside vertices with eight signatures. For four landmarks at least nineteen ones are needed across twelve distinct four-bit outside signatures, obtained by filling the weights 0,1,2 and one weight-3 word. The incidence total is 20−2e; hence a resolving four-set must have no internal edge. Translating a member to 0 reduces independence to three distinct pair-labels that pairwise intersect; they are a star or triangle. In the triangle case the two unused singletons each see only the landmark 0 and have identical signatures. The star case is four neighbors of a common center. Its center, omitted neighbor and ten nonneighbors have respectively the all-one, all-zero and distinct one-/two-bit adjacency signatures. Distinct centers share at most two neighbors, so every jump lies inside the appropriate K5, and every removed/inserted pair is nonadjacent in G and adjacent in its complement. Independent replay: `python3 /workspace/reviews/4-check.py`. It uses even subsets of five labels with distance-four symmetric-difference adjacency, Floyd–Warshall, pair-separation masks and three-landmark overlap buckets. It checked all sizes 0–4 in both graphs, exact equality of the 80 bases, unique centers, sixteen 5-cliques and the 160, 0, 160 jump/original slide/complement slide counts. Frozen scripts were inspected, not executed.

## originality

PASS

Best of knowledge, novelty is confined to the exhaustiveness of the basis form and its reconfiguration consequences. The dimension, agreement for complementary diameter-two graphs, and even sufficiency of the proposed four-of-five placements are covered by earlier work or its direct implications; this does not establish that no other bases occur. The 2019 folded-cube paper and the 2014 hypercube symmetry paper are bounded full-text access risks, not grounds for claiming negative full-text evidence.

## value

PASS

This supplies a natural finite benchmark for exact optimal-landmark reconfiguration on complementary diameter-two graphs. Identical optimal states and feasible jumps do not entail identical locality: all 160 jumps are disabled as slides in one graph and retained in the other, with an exact obstruction to changing centers. That information is structurally useful and strictly richer than the known metric dimension or construction of some bases. No broader folded-cube claim is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
