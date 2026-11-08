# Forty four-spheres and the full symmetry character of the icosahedral induced-forest complex

## Finding
Let \(I\) be the graph of the regular icosahedron, and let
\[
\mathcal F(I)=\{S\subseteq V(I):I[S]\text{ is acyclic}\}
\]
be its **vertex-induced forest complex**, not its edge-set graphic-matroid complex. Then its **integral homotopy type** is
\[
\boxed{\mathcal F(I)\simeq\bigvee^{40} S^4.}
\]
The complex has sixty facets of dimension four and sixty facets of dimension five. Its full graph automorphism group is \(G\cong A_5\times C_2\), and the rational fourth-homology character \(\chi\) takes the following values on **all ten conjugacy classes**:

| Class | Cardinality | Element order | \(\chi\) |
|---|---:|---:|---:|
| identity | 1 | 1 | 40 |
| central antipode | 1 | 2 | -10 |
| rotational involutions | 15 | 2 | -4 |
| antipode times rotational involutions | 15 | 2 | 2 |
| rotational elements of order three | 20 | 3 | 1 |
| antipode times order-three rotations | 20 | 6 | -1 |
| either rotational order-five class | 12 each | 5 | 0 |
| antipode times either order-five class | 12 each | 10 | 0 |

Let \(V_3,V_{3'},V_4,V_5\) denote the complex irreducible \(A_5\)-modules of dimensions three, three, four and five, and \(\varepsilon\) the nontrivial \(C_2\)-character. The resulting **complexified** symmetry representation is
\[
\boxed{\begin{aligned}
\widetilde H_4(\mathcal F(I);\mathbb C)\cong
&(V_3\oplus V_{3'}\oplus V_4\oplus V_5)\boxtimes\mathbf1\\
&\oplus(2V_3\oplus2V_{3'}\oplus2V_4\oplus V_5)\boxtimes\varepsilon.
\end{aligned}}
\]
In particular, the central antipode has \(15\) invariant and \(25\) anti-invariant dimensions, while
\[
\dim_{\mathbb Q}\widetilde H_4(\mathcal F(I);\mathbb Q)^G=0,
\qquad\langle\chi,\chi\rangle_G=17.
\]

## Assumptions and scope
The labeled vertex set is \(\{0,1,\ldots,11\}\). The edge list, in this order-independent encoding, is

```text
(0,1) (0,5) (0,7) (0,8) (0,11)
(1,2) (1,5) (1,6) (1,8)
(2,3) (2,6) (2,8) (2,9)
(3,4) (3,6) (3,9) (3,10)
(4,5) (4,6) (4,10) (4,11)
(5,6) (5,11)
(7,8) (7,9) (7,10) (7,11)
(8,9) (9,10) (10,11)
```

This is the twelve-vertex, thirty-edge, degree-five graph of the regular icosahedron, with twenty triangles. A face is a vertex subset \(S\) for which the **induced** graph \(I[S]\), including all edges with both ends in \(S\), has no cycle of any length. Empty face is included. A vertex subset \(S\) is encoded by the integer \(\sum_{v\in S}2^v\) in the computational certificate. All homotopy and homology assertions concern this one explicitly defined finite graph; the character is the action on homology induced by vertex permutation.

## Proof
**1. Exact face determination.** For each of the \(2^{12}=4096\) vertex masks, perform a disjoint-set cycle test on all thirty edges, retaining a mask if and only if inserting every induced edge joins two previously separate components. This is an equivalent definition of a forest. A separately coded component search confirms the criterion by checking that the induced edge count is \(|S|-c(I[S])\). All \(4096\) results agree. There are \(984\) faces including the empty face, with the dimension counts
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5)=(1,12,66,200,345,300,60).
\]
Facet tests yield \(60\) four-dimensional and \(60\) five-dimensional facets.

**2. Exact acyclic discrete-Morse matching.** Work in the poset of **nonempty** faces. In stages \(v=0,1,\ldots,11\), pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both faces are still unmatched, and remove paired faces before moving to the next pivot. Within a stage the pairs are disjoint because each pair toggles the same bit. This produces \(471\) pairs. The unmatched cells consist of the vertex \(\{0\}\) and precisely \(40\) four-dimensional simplices. Their vertex-mask encodings are

```text
316 488 682 714 740 744 818 824 872 1166
1226 1234 1256 1444 1476 1488 1586 1826 1840 1858
2078 2332 2388 2408 2452 2500 2512 2642 2664 2724
2756 2784 2834 3086 3116 3146 3340 3590 3620 3680
```

For an independently checkable acyclicity certificate, orient every unmatched covering relation in the face poset from the larger face to the smaller face, and every matched covering relation from the smaller face to the larger. The complete oriented Hasse graph has \(983\) vertices and \(3972\) covering relations; an exhaustive topological sort visits **every** vertex. Hence the matching is acyclic. Forman's discrete-Morse theorem gives a CW complex having one zero-cell and forty four-cells and no other cells. Every attaching map of a four-cell to the one-point zero-skeleton is constant, so this CW complex is a wedge of forty four-spheres. The homotopy equivalence is over the integers, not a consequence inferred merely from ranks over a field.

**3. Complete group and homology character.** Enumerate all bijections of the twelve vertices satisfying adjacency and nonadjacency constraints. Incremental exhaustive backtracking finds exactly \(120\) permutations and verifies group closure and inverses. The center consists of the identity and a unique antipodal involution \(c\); the commutator subgroup has order \(60\), with trivial intersection with \(\langle c\rangle\). As is standard for the regular icosahedron, this subgroup is the rotational \(A_5\), yielding \(G\cong A_5\times C_2\). Direct conjugation splits \(G\) into ten classes with the sizes shown above.

Since reduced rational homology is concentrated in even dimension four, the reduced Hopf--Lefschetz trace equals \(\chi(g)\) for every graph automorphism \(g\). If \(g\) permutes the vertices in cycles \(C_1,\ldots,C_r\), and \(U_T=\bigcup_{j\in T}C_j\), a setwise invariant simplex is exactly a union of these cycles. Its oriented-chain sign is \((-1)^{|U_T|-|T|}\); thus, after including the empty-face term, the exact finite formula is
\[
\boxed{\chi(g)=-\sum_{T\subseteq\{1,\ldots,r\}\,\colon\, I[U_T]\text{ forest}}(-1)^{|T|}.}
\]
This is evaluated exhaustively for each of the \(120\) automorphisms, and independently compared to signed simplicial chain traces. The two calculations agree for **every** element, giving the table. In particular, summing the characters yields \(0\), and summing squared characters yields \(120\cdot17\); character orthogonality proves the two displayed consequences.

**4. Complex irreducible decomposition.** Project to the \(\pm1\)-eigenspaces of the central antipode. On rotational elements of respective orders \(1,2,3,5\), the two \(A_5\)-characters are
\[
\chi_+=(15,-1,0,0),\qquad\chi_-=(25,-3,1,0),
\]
with the same last value on both order-five conjugacy classes. Using the standard \(A_5\) character table (complex irreducible degrees \(1,3,3,4,5\)) gives the stated direct-sum decomposition. Maschke's theorem justifies the decomposition over \(\mathbb C\). No integral splitting into these irreducibles is claimed.

## Verification
Run `python3 icosa_forest_verify.py` using Python 3.9 or later, with no third-party packages. The source implements both exact forest predicates, the full matching, the entire directed face-poset cycle test, independent mod-two boundary ranks, exhaustive graph automorphism backtracking, closure and conjugacy checks, and **two independent exact classwise Lefschetz calculations**. The program asserts every key figure and finishes with `ICOSAHEDRAL_FOREST_FULL_CERTIFICATE_PASS` on success. Its precise output is reproduced in `icosa_forest_verify.out`. The verification does not use random sampling, probabilistic group identification or incomplete enumeration.

## Relationship to prior work
Taylan's general matching-tree and devoid-complex framework [1] supplies the early mathematical setting for vertex-subset constraints, but its named graph classifications concern paths, cycles and forests; it does not state this icosahedral induced-forest result. Carnero Bravo [2] studies the same vertex-induced forest construction in a systematic filtration, calculating homotopy types for paths, cycles, double stars, cactus graphs, wheels, multipartite graphs and certain graph products. Its displayed formulas and families do not give the icosahedral induced-forest homotopy type or symmetry action.

Previously published computations of the icosahedral **open-neighborhood** complex [3] and its **three-cut** complex [4] also use this graph and, in [3], the same automorphism group. They have different defining face conditions: respectively subsets of a vertex's open neighborhood and complements of disconnected triples, not all vertex subsets inducing forests. In particular, the complexes' face counts, homology dimensions and chain representations differ. Neither inspected result contains an implication determining the present forest complex. The present computation gives a complete integral homotopy type **and** a full group character rather than claiming these other calculations.

## Limitations
This is a theorem about the single regular-icosahedron graph, not a classification of all polyhedral graphs or all forest filtrations. The representation decomposition is over \(\mathbb C\), and the full integral \(G\)-lattice and an equivariant homotopy splitting are not determined. The finite computation is exhaustive for the explicitly specified graph and group, but cannot establish a universal family theorem. Targeted published-source and indexed comparisons do not logically exclude unindexed or differently phrased prior computations; publication priority remains a residual risk. Independent mathematical audit has not been performed.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754, first public 2015-01-27. https://arxiv.org/abs/1501.06754
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first public 2023-07-25. https://arxiv.org/abs/2307.13271
3. *Rational icosahedral symmetry on the neighborhood complex*, published mathematical result, identifier `5d7e0af98d39` (2026).
4. *The icosahedral three-cut complex is a mixed-dimensional sphere wedge*, published mathematical result, identifier `fb104995d472` (2026).
