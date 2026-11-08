# The heptagonal prism is the first spherical second-independence circular ladder

## Finding
For the circular-ladder graphs \(L_n=C_n\square K_2\), with integers \(n\ge3\), the smallest \(n\) such that the second-independence complex \(\operatorname{Ind}_2(L_n)\) is homotopy equivalent to a sphere is \(n=7\). At that first occurrence,
\[
\operatorname{Ind}_2(L_7)\simeq S^5.
\]
In particular, this is an integral homotopy statement, not only a calculation of homology with field coefficients. No assertion is made for \(n>7\).

## Assumptions and scope
Here \(C_n\) is the simple cycle on \(n\ge3\) vertices and \(K_2\) is one edge. The graph \(L_n\) has vertices \((i,j)\), with \(0\le i<n\) and \(j\in\{0,1\}\); its edges are \((i,j)(i+1\bmod n,j)\) and \((i,0)(i,1)\). The complex \(\operatorname{Ind}_2(G)\) has as faces exactly those vertex subsets \(S\) for which every connected component of the induced graph \(G[S]\) has at most two vertices. Its empty face is included in the complex but excluded from the nonempty-face Morse matching and all stated face-vector counts.

A set fails this condition if and only if it contains three distinct vertices \(a,v,b\) with edges \(av\) and \(vb\). Therefore a complete enumeration can check the finite collection of forbidden triples consisting of a vertex and an unordered pair of its neighbors. In \(L_7\) there are \(42\) such distinct triples.

## Proof
**Smaller circular ladders.** Exhaustively enumerate every subset of the \(2n\) labeled vertices for \(3\le n\le6\), retaining just the subsets containing no forbidden connected triple. The resulting nonempty face vectors \((f_0,f_1,\ldots)\) are, in order:

- \(n=3\): \((6,15,6)\), hence \(\widetilde\chi=-4\).
- \(n=4\): \((8,28,32,8)\), hence \(\widetilde\chi=3\).
- \(n=5\): \((10,45,90,75,10)\), hence \(\widetilde\chi=-11\).
- \(n=6\): \((12,66,184,261,144,22)\), hence \(\widetilde\chi=-10\).

The formula is \(\widetilde\chi=\sum_{d\ge0}(-1)^d f_d-1\). A sphere of any nonnegative dimension has reduced Euler characteristic \(\pm1\), so none of these four complexes is homotopy equivalent to a sphere.

**The heptagonal prism.** Identify vertex \((i,j)\) with integer \(i+7j\), and a face \(S\) with its fourteen-bit mask \(m(S)=\sum_{v\in S}2^v\). Direct forbidden-triple enumeration gives \(2044\) nonempty faces and face vector
\[
(f_0,\ldots,f_6)=(14,91,322,644,658,287,28).
\]

Apply successive element matchings using the following vertex order, recording a pair \((S,S\cup\{v\})\) precisely if both faces remain unmatched before processing \(v\):

`(11, 4, 0, 8, 9, 1, 2, 7, 3, 12, 13, 6, 10, 5)`.

This is an explicit algorithm specifying all \(1021\) matched face pairs (no external certificate is required). An exhaustive directed-Hasse test checks all \(8932\) codimension-one incidences: direct the matched edges upward and all other edges downward; a topological sort visits all \(2044\) faces. The matching is therefore acyclic. The only critical faces have masks \(2048\) and \(1258\), corresponding to the vertex \(\{11\}\) and the six-vertex face \(\{1,3,5,6,7,10\}\). Thus there is one critical zero-cell and one critical five-cell, with no cells in dimensions one through four. Forman's discrete Morse theorem yields a CW complex with one zero-cell and one five-cell; its attaching map from \(S^4\) to a point is unique, giving \(S^5\). Combining this with the preceding reduced-Euler-characteristic obstructions proves minimality.

## Verification
The standalone program `prism_certify.py` uses two separate face tests: (a) exclusion of all connected triples and (b) explicit graph-component search for every induced subset. The programs agree on every subset for \(3\le n\le7\). It also checks matching disjointness, every Hasse incidence, absence of directed cycles, the exact critical masks and the claimed Euler characteristics. Finally, independent mod-two boundary reduction in the original (unmatched) simplicial chain complex gives boundary ranks \((13,78,244,400,258,28)\) in positive degrees one through six and Betti numbers \((1,0,0,0,0,1,0)\). These checks are finite and exhaustive for the stated finite graphs, and they provide a reproducible proof certificate rather than an inference from sampling.

Run `python3 prism_certify.py` using ordinary Python 3. No third-party packages are required. The claimed homotopy equivalence follows from the verified acyclic matching and the standard discrete Morse theorem; the mod-two calculation alone would not prove it.

## Relationship to prior work
An earlier calculation for well-covered cubic polyhedral graphs already identifies the second-independence homotopy types of the triangular and pentagonal prisms (at \(n=3\) and \(n=5\)), so those smaller cases are used only as boundary comparisons, not claimed as original. That finite classification does not cover the heptagonal prism. Taylan's arXiv preprint dated January 27, 2015 develops forbidden-subgraph/devoid complexes and matching trees, and determines homotopy types for paths, cycles, and forests; it supplies the archival starting point, not a classification of circular ladders. Deshpande and Singh classify higher-independence complexes of complete multipartite graphs, fully whiskered graphs, paths, cycles and certain trees, and explain discrete Morse methods. Abdelmalek and collaborators study chordal graphs and related higher-independence complexes; \(L_7\) has induced four-cycles and is not chordal. Work on ordinary independence complexes of other graph products studies a different invariant. Existing public results on circular-ladder Rips, Čech, ordinary independence, and cut complexes also concern different face conditions. A matching of the graph name, or a separate sphere of the same dimension, does not imply the stated second-independence homotopy type.

## Limitations
The result identifies the first spherical member of this family, not an infinite homotopy-classification formula or a classification of all larger members. It does not determine equivariant homotopy types, a preferred homeomorphism, or inclusion-induced maps between members of different sizes. Literature comparisons cannot rule out equivalent unindexed work; independent audit has not been performed.

## References
1. D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754 (first publicly posted 2015-01-27), Sections 3–5.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first posted 2020-01-15), Sections 3–5.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863 (first posted 2021-06-21), Sections 2–4.
4. A. Carnero Bravo, *On Independence Complexes of Graph Products*, arXiv:2505.06457 (first posted 2025-05-09), Sections 2–5.
5. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145.
