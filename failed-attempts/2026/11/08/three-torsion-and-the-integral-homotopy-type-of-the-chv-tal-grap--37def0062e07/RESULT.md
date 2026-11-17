# Three-torsion and the integral homotopy type of the Chvátal graph matching complex

## Finding
Let \(G\) be the twelve-vertex Chvátal graph specified below. Its **ordinary matching complex** \(\mathcal M(G)\), with graph edges as simplicial vertices and pairwise vertex-disjoint edge sets as faces, has the integral homotopy type
\[
\boxed{\mathcal M(G)\simeq\left(\bigvee^{28}S^3\right)\vee M(\mathbb Z/3,3),}
\]
where \(M(\mathbb Z/3,3)=S^3\cup_{\deg 3}e^4\) is the Moore space. Thus its complete reduced integral homology is
\[
\widetilde H_j(\mathcal M(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{28}\oplus\mathbb Z/3,&j=3,\\
0,&j\ne3.
\end{cases}
\]
In particular, this canonical triangle-free, four-regular, four-chromatic graph has a matching complex with nonzero integral torsion, whereas the matching complex of the eleven-vertex Grötzsch graph has previously been determined to be a torsion-free wedge of twenty-four three-spheres.

## Assumptions and scope
Take the vertex set \(V(G)=\{0,1,\ldots,11\}\). Its exactly twenty-four undirected graph edges, indexed from zero in increasing lexicographic order, are:

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

These are the edges of the standard labeled Chvátal graph; each graph vertex has degree four, and the graph has no triangles. A matching \(S\subseteq E(G)\) means that every pair of distinct edges in \(S\) has disjoint endpoints. The simplicial complex \(\mathcal M(G)\) consists of all such matchings, including the empty face. The homotopy type refers to the ordinary nonaugmented geometric realization. No assertion concerns the different independence complex \(\operatorname{Ind}(G)\), the dominance complex of \(G\), or matching complexes of all four-chromatic graphs.

## Proof
**Enumeration and discrete-Morse reduction.** Number the twenty-four graph edges as above and represent a matching face by a bit mask. The independent verifier enumerates all matchings using an edge-by-edge recursion with an occupied-vertex mask. The complete face vector, counting nonempty simplices of dimensions zero through five, is
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(24,204,752,1175,628,52),
\]
so there are \(2835\) nonempty faces. Repeatedly, for \(i=0,1,\dots,23\), pair each remaining simplex \(\sigma\) not containing edge-index \(i\) with \(\sigma\cup\{i\}\), whenever both faces remain; process the candidates by increasing cardinality and then increasing bit mask. Remove both members of a pair immediately. This deterministic partial matching consists of \(1385\) pairs, leaving one critical zero-simplex, forty-six critical three-simplices, and eighteen critical four-simplices, with no other critical faces.

Orient every face-poset covering relation downwards, except those belonging to the matching, which are oriented upwards. The verifier constructs all \(10816\) such covering incidences and topologically sorts all \(2835\) nonempty faces. All are visited, so the orientation is acyclic. Forman's discrete-Morse theorem supplies a homotopy-equivalent CW complex with one zero-cell, forty-six three-cells, and eighteen four-cells. Its three-skeleton is \(\bigvee^{46}S^3\).

**Integral attaching-degree matrix.** Orient each simplex by increasing graph-edge index, using the differential \(\partial[v_0,\ldots,v_k]=\sum_i(-1)^i[v_0,\ldots,\widehat{v_i},\ldots,v_k]\). Eliminate paired lower faces from the signed simplicial boundary by the standard finite gradient recursion. The acyclic orientation makes the recursion well-founded. For the eighteen critical four-cells, this yields the complete \(46\times18\) integral Morse boundary matrix \(B\). All entries lie in \(\{-1,0,1\}\), with \(118\) nonzero entries. The entrywise construction, including the ordered critical bases, is reproduced exactly in `verify_morse.py`.

The ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) are respectively \(18\), \(17\), and \(18\). Moreover, taking the eighteen rows with zero-based indices
\[
(0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,17,18,26)
\]
and all eighteen columns gives a square integer minor of **determinant exactly \(3\)**, computed by fraction-free Bareiss elimination with checked exact divisions. Therefore the rational rank is \(18\). Since the rank modulo three is \(17\), every maximal minor is divisible by three. The displayed minor shows that the greatest common divisor of all maximal minors is precisely three. It follows from the Smith normal form theorem that the eighteen nonzero invariant factors of \(B\) are seventeen units and one factor of three, with twenty-eight additional zero rows.

All four-cell attaching maps are maps from three-spheres into the wedge of forty-six three-spheres. By the degree classification \(\pi_3(\bigvee^{46}S^3)\cong\mathbb Z^{46}\), their homotopy classes are completely captured by \(B\). Unimodular changes of the domain and target wedge bases realize the integer Smith operations; seventeen unit-degree pairs then cancel. The resulting CW complex is homotopy equivalent to twenty-eight free three-spheres wedged with the Moore space having degree-three four-cell attaching map. This proves the stated integral **homotopy type**, not merely a field-valued Betti-vector computation.

## Verification
The complete standard-library Python code `verify_morse.py` reconstructs the graph, all matchings, the full acyclic Hasse orientation, every signed Morse gradient reduction, ranks over three prime fields, and the nonzero determinant-three maximal minor. Independently, `verify_simplicial.py` enumerates faces by a separate combinations-based algorithm and computes ranks of the complete *simplicial* boundary operators over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). The direct reduced Betti vectors (dimensions zero through five) are respectively
\[
(0,0,0,28,0,0),\qquad(0,0,0,29,1,0),\qquad(0,0,0,28,0,0).
\]
The characteristic-three discrepancy independently corroborates the torsion pattern by the universal coefficient theorem; it does not replace the integer-minor proof. Run both programs with Python 3, without external packages. `verify_output.txt` records their actual stdout.

## Relationship to prior work
Shareshian and Wachs' *Torsion in the Matching Complex and Chessboard Complex* (first public September 3, 2004) establishes torsion for matching complexes of complete graphs and for chessboard complexes, notably their Theorem 1.6 and Table 1.1. Those conclusions do not calculate the matching complex of the sparse, specific Chvátal graph. Engström's *Independence complexes of claw-free graphs* (first public December 17, 2005) yields general connectivity results: a matching complex is the independence complex of its graph's line graph, but his theorems do not determine this graph's integral attaching degrees.

A published exact homotopy calculation for the **icosahedral** matching complex also produces one order-three Moore summand, but has sixty-four free three-spheres and concerns a different graph; no implication yields the Chvátal computation. A separate published calculation for the **Grötzsch** graph gives \(\bigvee^{24}S^3\) and no torsion. In particular, the present Chvátal example distinguishes the matching-complex torsion behavior of two canonical triangle-free four-chromatic graphs, rather than asserting that matching-complex torsion is unprecedented. Bayer, Jelić Milutinović, and Vega's theorem for outerplanar graphs does not apply: the Chvátal graph has twenty-four edges, exceeding the twenty-one-edge bound for simple outerplanar graphs on twelve vertices.

## Limitations
This is an explicit finite graph calculation. The proof establishes neither a classification for all regular or four-chromatic graphs nor a minimal-torsion theorem. It does not give a graph-equivariant homotopy decomposition or integral symmetry representation. All numerical certificates arise from recomputable, exhaustive finite algorithms rather than a separate formal proof assistant. The inspected primary and indexed results do not exclude mathematically equivalent work in unindexed or inaccessible literature; publication priority and independent mathematical validation remain unresolved.

## References
1. John Shareshian and Michelle L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1, first public 2004-09-03, https://arxiv.org/html/math/0409054v1 .
2. Alexander Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, first public 2005-12-17, https://arxiv.org/html/math/0512420v1 .
3. Jakob Jonsson, *3-torsion in the Homology of Complexes of Graphs of Bounded Degree*, Canadian Journal of Mathematics 65 (2013), 843–862, doi:10.4153/CJM-2013-008-4 (background on matching complexes of complete graphs).
4. Margaret Bayer, Zorana Jelić Milutinović, and Julianne Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, first public 2024-11-07 (theorem for outerplanar graphs only).
5. *Three-torsion in the icosahedral matching complex: a planar counterexample*, published published-finding corpus mathematical record, identifier `28565ad1ea1a`.
6. *The Grötzsch graph matching complex is a wedge of twenty-four three-spheres*, published published-finding corpus mathematical record, identifier `514850eb507b`.
7. *Chvátal graph*, MathWorld, https://mathworld.wolfram.com/ChvatalGraph.html (standard graph identification).
