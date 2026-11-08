# Homotopy and tetrahedral symmetry of a subdivided-complete-graph matching complex

## Finding
Let \(G\) be the graph with vertex set
\[
V(G)=\{(i,j):i,j\in\{0,1,2,3\},\ i\ne j\},
\]
where distinct arcs \((i,j)\) and \((a,b)\) are adjacent precisely when \(i=a\), or \((a,b)=(j,i)\). This is the twelve-vertex truncated-tetrahedral graph. Equivalently, \(G\) is the line graph of the once-subdivided tetrahedral graph \(\operatorname{sd}(K_4)\). Set \(X=\operatorname{Ind}(G)=\mathcal M(\operatorname{sd}(K_4))\), its ordinary independence or matching complex.

**Theorem.** There is an integral homotopy equivalence
\[
X\simeq\bigvee^{5}S^2.
\]
The natural group \(S_4\) permuting the original four vertices acts on rational second homology by
\[
\widetilde H_2(X;\mathbb Q)\cong_{\mathbb Q[S_4]}
\mathbf1\oplus (\operatorname{sgn}\otimes\mathbb Q^{4}),
\]
where \(\mathbb Q^4\) is the four-label permutation representation. Equivalently, it is the direct sum of the trivial, sign, and sign-twisted standard representations. Its character on \(g\in S_4\) is
\[
\chi(g)=1+\operatorname{sgn}(g)\,\#\operatorname{Fix}_{\{0,1,2,3\}}(g).
\]
For **every subgroup** \(H\le S_4\), the geometric quotient \(|X|/H\) is simply connected and has reduced rational homology concentrated in degree two, of dimension
\[
\dim_{\mathbb Q}\widetilde H_2(|X|/H;\mathbb Q)
=1+\frac{1}{|H|}\sum_{h\in H}\operatorname{sgn}(h)
\,\#\operatorname{Fix}_{\{0,1,2,3\}}(h).
\]
In particular, the full symmetric quotient has second rational Betti number one, and the alternating quotient has second rational Betti number two.

## Assumptions and scope
The graph is simple and undirected. A simplex is any set of arcs with no repeated first coordinate and no pair of mutually reversed arcs. The symmetric group acts by \((i,j)\mapsto(g(i),g(j))\); the word quotient means the orbit space of the geometric realization, not a Borel construction. The homotopy equivalence is **ordinary**, not asserted equivariant. The character and quotient homology statements use rational coefficients; no integral identification of quotient homology is claimed. The conclusions concern this exact graph, not the arbitrary-order family of subdivided complete graphs.

The line-graph identification follows directly: each edge of \(K_4\) is split at its midpoint; its two half-edges are indexed by their original endpoint and the other original endpoint. Half-edges meet at an original vertex exactly when their first indices coincide, and the two halves of one original edge meet at its new midpoint exactly when the corresponding arcs reverse.

## Proof
**1. Complete finite simplicial model.** Order the twelve graph vertices lexicographically as
\[
(0,1),(0,2),(0,3),(1,0),(1,2),(1,3),
(2,0),(2,1),(2,3),(3,0),(3,1),(3,2).
\]
Encode a simplex by the twelve-bit integer with the corresponding bit set. Starting from the empty simplex, add each vertex to every existing face containing no adjacent vertex. This produces exactly \(163\) faces including the empty face, with face counts \(12,48,72,30\) in dimensions \(0,1,2,3\). Both the construction and counts are recomputed by the standalone verifier.

**2. An exact acyclic discrete Morse matching.** On the nonempty face poset, successively use the pivot-bit order
\[
1,9,8,5,10,2,3,7,4,0,11,6.
\]
For a pivot \(i\), in ascending numerical order, match each currently unmatched face \(F\) that omits \(i\) with \(F\cup\{i\}\), whenever the latter remains unmatched. At the end there are precisely \(78\) disjoint pairs and six critical faces: one vertex and five two-simplices. To verify acyclicity, orient every covering relation of the nonempty face poset downward except matched relations, which are oriented upward. The exact directed graph has \(162\) nodes and \(432\) arcs. A complete topological-sort elimination visits all \(162\) nodes, proving it has no directed cycle. Thus there is no closed discrete gradient path. The included self-contained code constructs every face and incidence, executes the prescribed matching, and checks these assertions exhaustively; no numerical rank or partial enumeration is being promoted into an infinite proof.

Forman's discrete Morse theorem gives a CW complex with one zero-cell, no one-cells, five two-cells and no higher cells. Each two-cell is attached to the unique zero-cell, since there is no one-skeleton beyond that point. Consequently the CW model is exactly a wedge of five two-spheres. This proves the integral homotopy type and implies that integral reduced homology is free of rank five in dimension two and zero elsewhere.

**3. Complete rational symmetry character.** For \(g\in S_4\), transport the corresponding twelve graph vertices and calculate the signed simplicial trace. A face fixed setwise contributes its orientation sign multiplied by \((-1)^{\dim F}\) to the *augmented* Lefschetz number. As homology is supported only in even dimension two, the augmented Lefschetz number equals \(\chi(g)\). A complete enumeration of all twenty-four label permutations, all \(163\) faces, and each induced permutation of oriented faces gives the following traces indexed by cycle type:
\[
\begin{array}{c|ccccc}
\text{type}&1^4&2\,1^2&2^2&3\,1&4\\\hline
\chi&5&-1&1&2&1.
\end{array}
\]
These equal \(1+\operatorname{sgn}(g)\#\operatorname{Fix}(g)\) in every conjugacy class. The class functions of \(\mathbf1\oplus(\operatorname{sgn}\otimes\mathbb Q^4)\) have those same values. Character equality and semisimplicity over \(\mathbb Q\) imply the representation isomorphism; the permutation module splits as trivial plus the three-dimensional standard module.

**4. Quotient topology for all subgroups.** Every element of \(S_4\) fixes a point of \(|X|\): a transposition fixes an arc between the other two labels; a double transposition preserves a pair of independent arcs joining corresponding elements of its two two-cycles; a three- or four-cycle preserves the independent set of arcs going around that directed cycle. The barycenter of any such invariant simplex is geometrically fixed. (The trivial element fixes everything.) Since \(|X|\) is simply connected, Armstrong's fundamental-group theorem for orbit spaces gives
\(\pi_1(|X|/H)\cong H/N_H=1\) for every subgroup \(H\), where \(N_H\) is normally generated by elements with fixed points. For rational homology, first pass to the barycentric subdivision to remove simplex inversions and apply finite-group cellular transfer: \(\widetilde H_*(|X|/H;\mathbb Q)\cong \widetilde H_*(X;\mathbb Q)^H\). Character averaging gives the formula above and shows every other reduced rational homology group vanishes. For \(H=S_4\) the invariant dimension is one, and for \(H=A_4\) it is two.

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. It reconstructs the graph, all \(163\) faces, all \(78\) specified Morse pairs, the full \(432\)-incidence oriented Hasse diagram, and its acyclicity via an exhaustive topological sort. An independent augmented \(\mathbb F_2\) boundary-rank calculation has ranks \((1,11,37,30)\) in degrees zero through three, giving reduced Betti vector \((0,0,5,0)\). The verifier additionally tests the signed character of every one of the \(24\) group elements and checks the existence of an invariant nonempty face for each element. The recorded output in `verification_output.txt` ends in the complete `ALL_VERIFY_OK` success marker and is reproduced from the standalone package. The exact discrete Morse matching, not field homology alone, proves the integral homotopy statement.

## Relationship to prior work
Barik, Mondal and Mukherjee's preprint dated 2026-04-14 develops recursive acyclic Morse matchings when a graph has a simplicial vertex and proves consequences for chordal graphs and specified comparability-graph blowups. In the present graph, each vertex has two mutually adjacent same-source neighbors and a reversed-arc neighbor not adjacent to them, so **no vertex is simplicial**. The cited recursion's initial hypothesis fails; its family theorems do not imply this homotopy calculation.

The published *Edge-orbit matching-complex homotopy of the truncated tetrahedron* computes the matching complex **of the truncated-tetrahedral graph itself**, which is a different simplicial complex: its simplicial vertices correspond to that graph's eighteen edges, whereas the present independence complex has twelve vertices and is the matching complex of the *once-subdivided* tetrahedral graph. The former paper proves \(\mathcal M(G)\simeq\bigvee^{22}S^3\), not the present five-sphere result or the symmetry and subgroup-quotient statements. Its description of the line-graph identification was checked, not silently ignored.

General results of Engström on claw-free graph independence complexes and Bayer, Jelić Milutinović and Vega on polygonal line tilings supply context but not the precise integral sphere count or complete tetrahedral symmetry character. Searches under the polyhedron, line graph, subdivided complete graph, partial-function and representation descriptions did not identify a mathematically covering claim. This is a best-knowledge comparison, not a proof of absolute publication priority.

## Limitations
The finite computation establishes the stated object and its natural \(S_4\)-action only, with no extension to larger subdivided complete graphs. The quotient result gives a simply connected space and its **rational** homology, not a complete integral homotopy classification of the quotients. No independent audit has been performed. Equivalent calculations in unindexed or inaccessible sources may exist.

## References
1. S. Barik, A. Mondal and S. Mukherjee, *A recursive construction of an acyclic matching on the independence complex of a graph with a simplicial vertex*, arXiv:2604.12606v1 (first public 2026-04-14), https://arxiv.org/abs/2604.12606.
2. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-edge-orbit-matching-complex-homotopy-of-the-truncated-tetrahedro--f5ae4a359c83.
3. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420 (2005), https://arxiv.org/abs/math/0512420.
4. M. Bayer, M. Jelić Milutinović and J. Vega, *General polygonal line tilings and their matching complexes*, Discrete Mathematics 346 (2023), 113428, https://doi.org/10.1016/j.disc.2023.113428.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, https://doi.org/10.1006/aima.1997.1650.
6. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Mathematical Proceedings of the Cambridge Philosophical Society 64 (1968), 299–301, https://doi.org/10.1017/S0305004100042845.
