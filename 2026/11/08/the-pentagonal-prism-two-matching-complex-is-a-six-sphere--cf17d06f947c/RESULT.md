# The pentagonal-prism two-matching complex is a six-sphere

## Finding
For the graph \(G=C_5\square K_2\), the ordinary two-matching complex has the exact integral homotopy type
\[
M_2(G)\simeq S^6.
\]
This is a single-graph classification, not an infinite-family conjecture or a finite-field homology estimate. The complex has 10,894 nonempty simplices, and its facets have cardinalities eight, nine and ten even though the only positive-dimensional critical cell has dimension six.

## Assumptions and scope
Set the vertex set of \(G\) to \(\{0,1,\ldots,9\}\). For each \(i\in\mathbb Z/5\mathbb Z\), use the two rim edges \(\{i,i+1\}\) and \(\{i+5,i+6\}\) (indices reduced cyclically within each rim), and the spoke \(\{i,i+5\}\). This graph has ten vertices, fifteen edges and degree three at every vertex. Number its fifteen unordered edges in lexicographic order, beginning with \(\{0,1\}\). A face of \(M_2(G)\) is an edge subset for which no graph vertex is incident to three selected edges. The complex contains the empty face, which is excluded from the ordinary (nonaugmented) face poset for discrete Morse matching.

## Proof
Every graph vertex has precisely three incident edges. Hence a selected edge subset is a face exactly when it avoids all ten complete three-edge vertex stars. The standalone checker evaluates this condition for every one of the \(2^{15}\) subsets, and separately checks the equivalent selected-degree condition. These independently agree and produce the face counts, by dimension from minus one to nine:
\[
(1,15,105,445,1245,2358,2985,2400,1100,230,11).
\]
The alternating sum of the positive-dimensional face-vector entries, with vertices in dimension zero, is \(2\), consistent with the claimed sphere.

To construct an acyclic matching, start with the augmented set of all faces, and for edge-index \(i=0,1,\ldots,14\) in that order pair every as-yet-unpaired face \(\sigma\) not containing edge \(i\), whenever its enlargement \(\sigma\cup\{i\}\) also remains unpaired. Remove each pair and proceed to the next index. This produces exactly \(5,447\) pairs and exactly one unpaired face: the seven-edge face with lexicographic edge indices \(1,2,4,6,8,11,14\).

The augmented matching contains \((\varnothing,\{e_0\})\). Discard only this pair and exclude the empty face. The resulting genuine face-poset matching has exactly \(5,446\) disjoint incident pairs and exactly two critical faces, namely \(\{e_0\}\) of dimension zero and the seven-edge face of dimension six.

For every remaining Hasse incidence \(\sigma\subset\tau\) of codimension one, orient the incidence from \(\sigma\) to \(\tau\) if matched, and from \(\tau\) to \(\sigma\) otherwise. The checker constructs the entire directed graph, enumerating \(64,005\) incidences, and proves it acyclic by a deterministic topological sort visiting all \(10,894\) vertices of the face-poset graph. This is a complete finite certificate, not a random or partial acyclicity test.

By the discrete Morse CW theorem, the complex is homotopy equivalent to a CW complex with one zero-cell and one six-cell, with no other cells. The attaching map of the six-cell has target a point and is unique up to homotopy. The resulting CW complex is \(S^6\), completing the proof.

## Verification
Run `python verify.py` with Python 3.9 or later, using only the standard library. The program reconstructs all graph edges, enumerates all \(2^{15}\) edge subsets in two independent ways, checks the exact f-vector, verifies every matching pair is an incidence and every face is paired at most once, and performs a full directed-acyclicity check. Its expected exact output is recorded in `verification_output.txt`. The checker uses no input tables or previously computed mathematical certificates.

## Relationship to prior work
Vega (2019) formalizes two-matching/bounded-degree complexes and develops discrete-Morse results for clawed graphs, wheels and caterpillars, none of which covers this cyclic cubic prism. Singh (2020) proves higher-matching results for complete and complete bipartite graphs, not this graph. Agarwal and Basak (2026) determine the independence and perfect-matching complexes of circular ladders, not the two-matching complex. Their source hypotheses and face conditions do not imply the present result. A known ordinary one-matching computation for the pentagonal prism is a different simplicial complex, since \(M_1(G)\subsetneq M_2(G)\).

## Limitations
Only the stated ten-vertex pentagonal prism and its ordinary two-matching complex are classified. The result is nonequivariant; no full dihedral action, classification for every circular ladder or other graph family, shellability statement, or equivariant homotopy splitting is established. Literature discovery cannot rule out unindexed equivalent results; no independent external audit is claimed.

## References
1. J. Vega, *2-Matching Complexes*, arXiv:1909.10406, initially posted 2019-09-23. https://arxiv.org/abs/1909.10406
2. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, initially posted 2020-06-24. https://arxiv.org/abs/2006.13632
3. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, initially posted 2026-09-14. https://arxiv.org/pdf/2608.30601v2
