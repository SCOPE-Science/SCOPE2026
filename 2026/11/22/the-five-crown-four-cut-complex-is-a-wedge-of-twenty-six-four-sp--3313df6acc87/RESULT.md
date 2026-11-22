# The five-crown four-cut complex is a wedge of twenty-six four-spheres

## Finding
Let \(C_5\) be the ten-vertex crown graph with bipartition \(A=\{a_0,\ldots,a_4\}\) and \(B=\{b_0,\ldots,b_4\}\), with edge \(a_i b_j\) exactly when \(i\ne j\). Its ordinary four-cut complex \(\Delta_4(C_5)\), defined by complements of disconnected induced four-vertex sets, has integral homotopy type
\[
\Delta_4(C_5)\simeq\bigvee^{26}S^4.
\]
Its combinatorial Alexander dual also has a complete type,
\[
\Delta_4(C_5)^\vee\simeq\bigvee^{26}S^3.
\]
Consequently its only nonzero reduced integral homology is \(\widetilde H_4\cong\mathbb Z^{26}\). The four-cut complex is pure of dimension five but not shellable.

## Assumptions and scope
All graphs are finite, simple, undirected. Vertices are enumerated \(a_i=i\) and \(b_i=5+i\), with \(0\le i\le4\). A four-element vertex set \(Q\) is a *disconnected quadruple* if the induced graph \(C_5[Q]\) is disconnected. The cut complex has facets \(V\setminus Q\) for every disconnected quadruple \(Q\); faces are their subsets, including the empty face. Its combinatorial Alexander dual is \(\{F\subseteq V:V\setminus F\notin\Delta_4(C_5)\}\). No claim is made for other crown orders or a filtration of cut parameters.

## Proof
**Disconnected quadruples.** There are precisely three disjoint kinds: (i) four on the same shore, with \(2\binom54=10\) choices; (ii) three on one shore and one on the other, where the isolated majority-shore vertex shares the minority vertex's index, with \(2\cdot3\binom53=60\) choices; and (iii) two vertices on each shore using the same two matched indices, with \(\binom52=10\) choices. To verify completeness, a mixed three-plus-one quartet is connected exactly when the minority vertex has an edge to all three majority vertices; a two-plus-two quartet is disconnected exactly when the two deleted diagonal edges form its only missing cross edges. This gives eighty distinct disconnected quadruples and eighty distinct six-vertex facets.

**Finite acyclic matching.** Enumerate all nonempty faces of the cut complex. In vertex order \(a_0,a_1,a_2,a_3,a_4,b_0,b_1,b_2,b_3,b_4\), for each vertex \(v\), pair every currently unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\) if that face remains unmatched. Remove both faces from further consideration. Each pair is a cover relation in the nonempty face poset. The standalone checker `verify.py` constructs the graph, enumerates all disconnected quadruples and cut faces rather than reading precomputed face data, and generates all pairs.

The exact exhaustive certificate has 697 nonempty faces, 335 paired cover relations and precisely one unmatched vertex together with 26 unmatched four-dimensional faces. Crucially, its acyclicity is *not* inferred from these counts: the checker constructs the complete 2,930-edge directed Hasse diagram, orienting a matched cover relation upwards and every other cover relation downwards. An exhaustive topological sort visits all 697 vertices. Thus the directed graph is acyclic, and the pairing is a valid discrete-Morse matching.

By the finite discrete-Morse CW theorem, the complex has a CW model with one zero-cell, 26 four-cells and no cells of other dimensions. Every attaching map of a four-cell has target the one-point three-skeleton and is null; hence this CW model is a wedge of 26 four-spheres, proving the claimed integral homotopy type. In particular there is no torsion. The original complex is pure five-dimensional because every facet has exactly six vertices, so its nonzero fourth homology rules out pure shellability.

**Dual check.** Independently constructing the Alexander dual by forbidding all eighty quadruples gives 325 nonempty faces and a separate acyclic matching with 149 pairs, one critical vertex and 26 critical three-faces. The dual is therefore a wedge of 26 three-spheres. Combinatorial Alexander duality on ten vertices relates original reduced degree-four homology to dual reduced degree-three cohomology, as expected.

## Verification
With Python 3, run `python verify.py` in the directory containing the embedded files. `verify-output.json` records the exact tested face vectors, matching sizes, Hasse-diagram sizes, unmatched dimensions, and the result `PASS`. The algorithm enumerates subsets exhaustively, tests connectedness using graph adjacency, checks a separate closed-form classification of disconnected quadruples, tests the Alexander-dual definition for every vertex subset, and independently checks acyclicity on both complexes. No probability, timeouts, external source files or assumed integer matrices enter this finite certificate. The proof is computationally exhaustive for this stated ten-vertex graph, not for all crown graphs.

## Relationship to prior work
The definition, Alexander duality and use of discrete Morse theory are standard, especially in Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue (2023). Their complete-bipartite calculation concerns the undeleted \(K_{m,n}\), and their clique-prism theorem concerns the Cartesian graph with same-shore clique edges and diagonal rungs, not the matching-deleted bipartite crown. Bayer et al. (2024) treat disjoint unions, squared paths and grids rather than the present crown-four-cut case. Previously reported four-cut topology of the eight-vertex cube applies to \(C_4\), not \(C_5\); the previously reported crown-three-cut theorem concerns the different cut parameter \(k=3\). These results motivate the precise adjacent case but do not give this 26-sphere four-cut type by a stated theorem.

## Limitations
This is an exact finite classification, not an all-order formula or a claim of independent external audit. The constructive proof uses an exhaustive acyclic-matching checker whose source and result are included. No analogous homotopy classification for \(C_n\) with \(n>5\), nor a homology map between cut parameters, follows from the statement. An unindexed equivalent prior result remains a bibliographic risk.

## References
1. M. Bayer et al., *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public 2023-04-26; especially Theorems 7.1 and 7.18. https://arxiv.org/abs/2304.13675
2. M. Bayer et al., *Topology of Cut Complexes II*, arXiv:2407.08158, first public 2024-07-11; sections on disjoint unions, squared paths and grids. https://arxiv.org/html/2407.08158v1
3. *Upper cut-complex transition of the three-cube* (published 2026), cube four-cut benchmark. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-upper-cut-complex-transition-of-the-three-cube--e19e23ee7a6b
4. *Two-degree integral homology of crown-graph three-cut complexes* (published 2026), related graph at a different cut parameter. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-two-degree-integral-homology-of-crown-graph-three-cut-complexes--9ac5fb7f228c
