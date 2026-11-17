# Ninety-one three-spheres and the full symmetry character of the Nauru non-matching complex

## Finding
Let \(G\) be the Nauru graph, equivalently the arrangement graph \(A_{4,3}\) of injections from a three-element set into a four-element set, with two injections adjacent when exactly one image coordinate changes to the unique unused value. Let \(\operatorname{NM}_3(G)\) be the abstract simplicial complex on the 36 edges of \(G\) whose faces contain no three pairwise vertex-disjoint edges. There is an integral homotopy equivalence
\[
\operatorname{NM}_3(G)\simeq\bigvee^{91}S^3.
\]
The entire graph-automorphism group is \(\mathfrak S_4\times\mathfrak S_3\), acting by permuting the four values and three coordinate positions. Its rational third-homology character has the following values, with rows indexed by \(\mathfrak S_4\)-cycle types \((1^4),(2,1^2),(2^2),(3,1),(4)\), and columns by \(\mathfrak S_3\)-cycle types \((1^3),(2,1),(3)\):
\[
\begin{pmatrix}
91&7&1\\
19&7&1\\
7&11&1\\
1&1&1\\
1&1&1
\end{pmatrix}.
\]
In particular, the space of rational third-homology classes fixed by every graph automorphism has dimension four.

Writing \(V_\lambda\) for the irreducible rational symmetric-group representation indexed by partition \(\lambda\), the complete irreducible decomposition is
\[
\begin{aligned}
\widetilde H_3(\operatorname{NM}_3(G);\mathbb Q)\cong{}&
4(V_{(4)}\boxtimes V_{(3)})\oplus3(V_{(4)}\boxtimes V_{(2,1)})\\
&\oplus3(V_{(3,1)}\boxtimes V_{(3)})\oplus5(V_{(3,1)}\boxtimes V_{(2,1)})\\
&\oplus2(V_{(3,1)}\boxtimes V_{(1,1,1)})\oplus3(V_{(2,2)}\boxtimes V_{(3)})\\
&\oplus3(V_{(2,2)}\boxtimes V_{(2,1)})\oplus2(V_{(2,1,1)}\boxtimes V_{(2,1)})\\
&\oplus2(V_{(2,1,1)}\boxtimes V_{(1,1,1)}).
\end{aligned}
\]

## Assumptions and scope
The vertex set consists of all 24 distinct-coordinate triples from \(\{0,1,2,3\}\). The 36 undirected edges connect triples differing in exactly one coordinate. The explicit isomorphism with \(\operatorname{GP}(12,5)\) is independently checked using the permutation given in `verify_nauru.py`. Faces of \(\operatorname{NM}_3(G)\) are arbitrary subsets of those 36 graph edges, including the empty face, subject only to the forbidden three-edge-matching condition. There are no assumptions on coefficients for the asserted homotopy equivalence; the representation statement uses rational coefficients.

## Proof
**Face reconstruction.** The arrangement graph has bipartition sizes 12 and 12. By the bipartite matching–vertex-cover theorem, a set of edges avoids a three-edge matching if and only if its edge subgraph admits a vertex cover of cardinality at most two. Therefore every face is a subset of the union of the incident-edge stars of some pair of graph vertices. This finite description enumerates exactly 7,627 faces when the empty face is included. As an independent finite check, exhaustive increasing-index recursion constructs each edge subset unless adding its newest edge creates three disjoint edges; the two complete face sets agree. The numbers of faces with respectively 0, 1, 2, 3, 4, 5 and 6 edges are \(1,36,630,2256,2988,1476,240\); no face has more than six edges.

**Acyclic collapse certificate.** Number the graph edges lexicographically, from 0 to 35. Process these edge indices in ascending order. At step \(j\), pair every currently unpaired face \(F\) that omits edge \(j\) with \(F\cup\{j\}\), provided both are still unpaired faces. The resulting 3,768 pairs form a partial matching of the augmented face poset. For every cover relation, orient it upward if matched and downward otherwise. Exhaustive topological sorting of all 28,836 directed covers visits each of the 7,627 faces and finds no directed cycle. Precisely 91 critical faces remain, all with four graph edges (dimension three); the empty face is paired. By the augmented discrete-Morse theorem, the realization admits a reduced CW model with 91 cells of dimension three and no other reduced cells. Since there are no possible positive-dimensional attaching targets below dimension three, this is a wedge of 91 three-spheres. This argument determines the integral homotopy type, not just Betti numbers.

**Symmetry.** The two symmetric groups act on the 24 injections, preserve adjacency, and produce 144 different graph automorphisms. An exhaustive adjacency-preserving backtracking enumeration, partitioned by the image of one vertex and the permutation of its three neighbors, also produces exactly 144 automorphisms, proving completeness. For each of those 144 actions, calculate the trace on an oriented simplicial chain group as the sum over setwise fixed faces of the sign of the induced edge-vertex permutation. As the only nonzero ordinary rational homology groups are \(H_0=\mathbb Q\) and \(H_3=\mathbb Q^{91}\), the alternating simplicial trace equals \(1-\operatorname{tr}(g|H_3)\). This gives the displayed five-by-three character matrix. Character orthogonality with the symmetric-group character tables gives the displayed nine irreducible multiplicities, each a nonnegative integer whose dimension-weighted sum is 91. Averaging the 144 character values gives \(576/144=4\) invariant classes.

## Verification
Execute `python3 verify_nauru.py` in the directory containing the standalone files. It requires only the Python standard library, independently constructs faces by two methods, replays every matching pair, verifies all oriented Hasse covers and group automorphisms, evaluates all signed cellular traces and checks the irreducible decomposition. The expected machine-readable output is `verification_output.json`; the program compares all critical values internally. This finite exhaustive certificate is part of the proof, not an extrapolation from sampled instances.

## Relationship to prior work
Shan and Wang (initial public version September 2, 2026) prove injectivity of top non-matching homology under bipartite edge additions and derive nonvanishing and algebraic regularity consequences. Their general results do not specify the Nauru graph's integer homotopy type, multiplicity or symmetry character. Holmsen and Lee prove Leray and link-vanishing bounds for arbitrary graphs and their bipartite subgraphs, not this exact 91-sphere decomposition. Linusson, Shareshian and Welker compute complete-graph and complete-bipartite-graph non-matching complexes; the Nauru graph is a proper sparse bipartite graph, and restriction to its edges does not inherit the complete-bipartite formula. The precise calculation and the full symmetry character are independent additional statements. The exact comparison of source hypotheses is more informative than a negative title search.

## Limitations
This is a complete finite theorem about the one named 24-vertex graph at matching threshold three. It does not establish a universal formula for all high-girth or cubic bipartite graphs, does not classify different matching thresholds and does not identify an integral equivariant lattice decomposition. The group-character decomposition is over \(\mathbb Q\). Literature-search coverage cannot exclude unindexed or differently titled prior calculations, and no independent mathematical audit has been performed.

## References
- J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, arXiv:2609.02621 (first public September 2, 2026). https://arxiv.org/abs/2609.02621
- A. F. Holmsen and S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270 (2020); *Journal of Combinatorial Theory, Series A* (2022). https://arxiv.org/abs/2003.11270
- S. Linusson, J. Shareshian and V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345 (2004); *Journal of Algebraic Combinatorics* 27 (2008), 331–349. https://arxiv.org/abs/math/0410345
