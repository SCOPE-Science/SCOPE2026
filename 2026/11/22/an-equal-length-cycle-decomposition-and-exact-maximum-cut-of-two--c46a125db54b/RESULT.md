# An equal-length cycle decomposition and exact maximum cut of two-token cycle graphs

## Finding

**Theorem.** For each integer \(n\ge3\), the two-token graph \(F_2(C_n)\) has an explicit edge partition into \(n-2\) simple cycles, each of length \(n\). With all edges of unit weight, its maximum cut has size

\[
\operatorname{MaxCut}(F_2(C_n))=
\begin{cases}
n(n-2),&n\text{ even},\\
(n-1)(n-2),&n\text{ odd}.
\end{cases}
\]

Thus \(F_2(C_n)\) is bipartite exactly when \(n\) is even. At every odd \(n\), the minimum number of edges whose deletion makes \(F_2(C_n)\) bipartite is exactly \(n-2\). An explicit optimal bipartition is given by the parity of the number of tokens on even-indexed base vertices.

## Assumptions and scope

Fix \(n\ge3\). The base graph \(C_n\) has labeled vertices \(0,\ldots,n-1\) and edges \(\{i,i+1\}\) for \(0\le i<n-1\), together with the closing edge \(\{0,n-1\}\). The graph \(F_2(C_n)\) has vertices the unordered pairs \(\{a,b\}\) with \(a\ne b\), and adjacent vertices exactly when their symmetric difference is a base edge. We write \((a,b)\) for the pair \(\{a,b\}\) when \(a<b\). All graphs are simple and all graph edges carry unit weight. A maximum cut is a bipartition maximizing the number of edges with endpoints in opposite parts. Edge bipartization means deleting the minimum number of graph edges to obtain a bipartite graph.

## Proof

**1. Remove the closing base edge.** Consider \(F_2(P_n)\), where \(P_n\) is the path \(0,1,\ldots,n-1\). Each edge in this token graph changes one of the two strictly ordered coordinates by one. The difference between the edge sets of \(F_2(C_n)\) and \(F_2(P_n)\) consists precisely of the \(n-2\) edges

\[
w_j=\bigl\{(0,j),(j,n-1)\bigr\},\qquad 1\le j\le n-2,
\]

where the outer braces indicate an edge between the displayed token configurations.

**2. Partition the path-token edges into long paths.** For each \(1\le j\le n-2\), take the following vertex sequence, with integer indices decreasing by one in each indicated run:

\[
Q_j:\quad (j,n-1),(j-1,n-1),(j-1,n-2),\ldots,(j-1,j),
(j-2,j),\ldots,(0,j).
\]

An empty descending run is omitted. Every successive pair of configurations is joined by a legal path-token move. The sequence has exactly \(n\) distinct vertices: its first run fixes the larger coordinate at \(n-1\), its middle run fixes the smaller coordinate at \(j-1\), and its final run fixes the larger coordinate at \(j\); the two successive runs intersect only at their common displayed endpoint. Consequently \(Q_j\) is a simple path with \(n-1\) edges and endpoints \((j,n-1)\) and \((0,j)\).

Every edge of \(F_2(P_n)\) belongs to exactly one \(Q_j\), by the following exhaustive classification. An edge increasing the larger coordinate, \((a,b)(a,b+1)\), is in \(Q_{a+1}\). An edge increasing the smaller coordinate, \((a,b)(a+1,b)\), is in \(Q_b\) if \(b\le n-2\), and is the first edge of \(Q_{a+1}\) if \(b=n-1\). The indicated membership is unique in each case: the three kinds of edges use disjoint traversals within the sequences. Thus the \(Q_j\) form an edge partition of \(F_2(P_n)\). Adding the distinctive closing edge \(w_j\) to \(Q_j\) creates a simple \(n\)-cycle, and these cycles partition all edges of \(F_2(C_n)\).

**3. Upper bound on the cut.** A cut crosses at most \(n\) edges of an even \(n\)-cycle, and at most \(n-1\) edges of an odd \(n\)-cycle. Summing these bounds over the edge-disjoint cycles gives the stated cut upper bound, and gives at least \(n-2\) edges outside every cut when \(n\) is odd.

**4. Matching lower bound.** Two-color the base vertices by the parity of their index. Every edge of the path \(P_n\) joins opposite colors, and the closing base edge does so if and only if \(n\) is even. Partition the token configurations by the parity of the number of their tokens on even-indexed vertices. Moving a token toggles this parity exactly when it crosses a bichromatic base edge. Each base edge has \(n-2\) possible placements of the other token, so this parity-lifted cut contains all \(n(n-2)\) token edges if \(n\) is even, and exactly \((n-1)(n-2)\) token edges if \(n\) is odd. This attains the upper bound.

Finally, for any finite graph, the smallest number of edges whose removal makes it bipartite equals its edge count minus its maximum cut: the surviving graph has a bipartition, and conversely retaining all crossing edges of a maximum cut creates a bipartite graph. Here the token graph has exactly \(n(n-2)\) edges. Therefore the edge-bipartization number is \(0\) for even \(n\) and \(n-2\) for odd \(n\). This completes the proof, including \(n=3\).

## Verification

A standalone checker in `verify.py` independently constructs token edges from legal moves, checks all paths/cycles and edge partitions for \(3\le n\le150\), and compares the parity-lift count with the derived formula. It also independently enumerates all cuts of \(F_2(C_n)\) for \(3\le n\le7\), fixing one configuration's side to eliminate global complement symmetry. The computations corroborate but are not needed for the unrestricted proof.

## Relationship to prior work

Rivera's preprint *An improved lower bound for the packing number of the 2-token graph of the cycle* (first public 2026-09-25, arXiv:2609.31991) motivates the same token graph but concerns its vertex-packing number, not edge-cycle decompositions or maximum cuts. Alejandro-Soto and collaborators' *Max-Cut on Token Graphs* (arXiv:2611.25153v1, 2026-11-18) proves the general parity-lift **lower bound** \(\operatorname{MaxCut}(F_k(G))\ge\binom{|V(G)|-2}{k-1}\operatorname{MaxCut}(G)\). For a cycle and two tokens, this yields the lower bound attained in the theorem, but not its matching upper bound or its edge-cycle decomposition; their studied exact families are different. Rivera's *Independent sets in the 2-token graph of a cycle and kings on the torus* (arXiv:2611.22830v1, 2026-11-17) classifies maximum independent vertex sets, not maximum edge cuts. The earlier open-access *On the spectra and spectral radii of token graphs* (DOI:10.1007/s40590-023-00583-3, 2024) treats spectral information for the same graph, not the edge-decomposition theorem. The work of Aberle, Gold, Moshe and Offner on cycle decompositions of Cartesian products of cycles (DOI:10.1007/s00373-025-02953-2, 2025) concerns a different graph construction. These distinctions are statements about inspected material and do not claim an exhaustive historical novelty proof.

## Limitations

The exact formula concerns **unweighted** two-token graphs of simple cycles. It does not determine weighted maximum cuts, maximum cuts for arbitrary base graphs, or maximum cuts of higher-token cycle graphs. The cycle decomposition is an edge partition, not a partition of token configurations. Historical priority remains provisional because older literature may contain a nonidentically titled equivalent decomposition or cut computation; the full text of the motivating packing preprint was inaccessible, although its public abstract distinctly concerns packing.

## References

1. L. M. Rivera, *An improved lower bound for the packing number of the 2-token graph of the cycle*, arXiv:2609.31991, first publicly posted 2026-09-25. https://arxiv.org/abs/2609.31991
2. J. A. Alejandro-Soto et al., *Max-Cut on Token Graphs*, arXiv:2611.25153v1, posted 2026-11-18. https://arxiv.org/html/2611.25153v1
3. L. M. Rivera, *Independent sets in the 2-token graph of a cycle and kings on the torus*, arXiv:2611.22830v1, posted 2026-11-17. https://arxiv.org/html/2611.22830v1
4. *On the spectra and spectral radii of token graphs*, Boletín de la Sociedad Matemática Mexicana, 2024. https://doi.org/10.1007/s40590-023-00583-3
5. M. Aberle, S. Gold, R. Moshe and D. Offner, *Cycle Decompositions of Cartesian Products of Two Cycles*, Graphs and Combinatorics 41, 84 (2025). https://doi.org/10.1007/s00373-025-02953-2
