# Complete integral graph-metric Rips persistence of the icosidodecahedron

## Finding

Let \(D=\operatorname{GP}(10,2)\) be the dodecahedral graph and \(I=L(D)\) its thirty-vertex line graph, equivalently the icosidodecahedral graph. Equip \(V(I)\) with unit-edge shortest-path distance. For every real \(r\geq0\), let \(K_r=\operatorname{VR}_{\leq r}(V(I))\) be the simplicial complex of nonempty vertex subsets of diameter at most \(r\).

The full integral homotopy filtration is
\[
K_r\simeq\begin{cases}
\text{thirty discrete points},&0\leq r<1,\\
\bigvee^{11}S^1,&1\leq r<2,\\
S^2,&2\leq r<3,\\
S^2,&3\leq r<4,\\
S^{14},&4\leq r<5,\\
\ast,&r\geq5.
\end{cases}
\]
The inclusion \(K_2\hookrightarrow K_3\) is an **integral homology isomorphism**, of degree \(\pm1\) in degree two (using any chosen generator orientations). Hence the complete reduced integral barcode comprises twenty-nine degree-zero bars \([0,1)\), eleven degree-one bars \([1,2)\), one degree-two bar \([2,4)\), and one degree-fourteen bar \([4,5)\). There is no integral torsion at any scale. The homotopy equivalences are nonequivariant and do not assert that the inclusion of the two sphere-stage complexes is a simplicial collapse.

## Assumptions and scope

The dodecahedral graph has vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). A vertex of \(I\) is an edge of \(D\); two such vertices are adjacent when their edges in \(D\) share an endpoint. All edges of \(I\) have length one. Only the resulting **graph-vertex shortest-path metric** is used, not the ambient Euclidean chordal metric of a realization in space. Inclusivity at integer distance thresholds is essential; noninteger values give the indicated constant stages.

## Proof

**Graph geometry.** Explicit breadth-first distance calculations over the thirty edge-vertices give, among the \(\binom{30}{2}=435\) unordered pairs, exactly \(60,120,120,120,15\) pairs at distances \(1,2,3,4,5\), respectively. The fifteen distance-five pairs are pairwise disjoint and cover all vertices. Thus \(K_4\) is the join of fifteen two-point complexes, i.e. the boundary of a fifteen-dimensional cross-polytope, homeomorphic to \(S^{14}\). Since the diameter is five, \(K_5\) is the full simplex. At scale zero the vertices are isolated.

**Scale one.** The clique complex of \(I=L(D)\) has thirty vertices, sixty edges and twenty triangular faces, one triangle for each three-edge star of \(D\). Because \(D\) has no triangles, these twenty faces have mutually disjoint edge sets. Collapse each triangular face along one of its free edges; the result is a connected graph with thirty vertices and forty edges, so it is a wedge of eleven circles.

**Exact Morse certificates at scales two and three.** We construct every face of \(K_r\), for \(r\in\{2,3\}\), as an increasing-index clique in the graph connecting pairs at distance at most \(r\). The resulting face vectors, listed by cardinality, are
\[
\begin{array}{c|l}
r=2&(30,180,380,330,102)\\
r=3&(30,300,1340,3150,4374,3800,2100,720,140,12).
\end{array}
\]
For either \(r\), repeatedly pick a prescribed vertex \(v\) and pair every currently unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), whenever both remain. The vertex ordering is recorded in `verification_output.txt` and reproducibly obtained by `verify.py` from finite deterministic seeds. At radius two this produces \(510\) pairs on \(1022\) faces; at radius three it produces \(7982\) pairs on \(15966\) faces. In both cases there are exactly two critical simplices, of dimensions zero and two. The verifier checks all \(3330\) and \(83730\) covering incidences respectively and performs a complete topological sort after orienting matching edges upward and every other covering edge downward. The directed Hasse diagrams are acyclic. By discrete Morse theory, each complex is homotopy equivalent to a CW complex with exactly one cell in dimensions zero and two; that CW complex is \(S^2\) in each case. This is an integral homotopy statement, not a finite-field Betti-number inference.

**The nontrivial inclusion at scales two and three.** The twenty triangular faces and twelve pentagonal faces of the icosidodecahedron yield a triangulated topological sphere \(T\) within both \(K_2\) and \(K_3\): fan-triangulate each pentagon into three triangles. The construction has thirty vertices, eighty-four edges, fifty-six triangles, a connected triangle-adjacency dual, and each edge belongs to exactly two triangles. Its Euler characteristic is two. The verifier constructs coherent orientations on the fifty-six triangles, producing an integral two-cycle \(z\) on \(T\).

For each \(r\in\{2,3\}\), let \(\lambda_r\) be the integral cochain obtained by backward substitution through the matched two-/three-cell pairs, initialized as one on the unique critical two-simplex and zero on all unmatched two-simplices that are not critical. Explicitly, if a matched two-simplex \(\sigma\) has paired three-simplex \(\tau\), set
\[
\lambda_r(\sigma)=-[\tau:\sigma]^{-1}
\sum_{\substack{\sigma'\subset\tau,\ |\sigma'|=3\\\sigma'\ne\sigma}}
[\tau:\sigma']\lambda_r(\sigma'),
\]
where each incidence number \([\tau:\sigma]\) is \(\pm1\). Acyclicity ensures the recursion terminates. The verifier checks the cocycle equation \(\lambda_r(\partial\tau)=0\) for **every** three-simplex. It obtains
\[
\langle\lambda_2,z\rangle=1,\qquad
\langle\lambda_3,z\rangle=-1.
\]
Since both complexes have integral second homology \(\mathbb Z\), these unit pairings make \([z]\) a primitive generator in each. Consequently the inclusion carries a generator to a generator and induces multiplication by \(\pm1\), proving the single persistent bar \([2,4)\).

The degree-one classes at radius one vanish at radius two; the degree-two class vanishes on entering radius four; the degree-fourteen class vanishes at radius five. No other positive-degree homology can occur by the established homotopy types. All degree-zero classes except the connected component class die at radius one.

## Verification

Run `python3 verify.py` with Python 3.9 or later (standard library only). The code constructs \(\operatorname{GP}(10,2)\), its line graph, every graph distance, the full face posets at the two nontrivial scales, explicit acyclic matchings, a closed oriented surface cycle, and exact integral cocycles. It independently checks both cocycle equations on every relevant three-simplex and evaluates the shared cycle. `verification_output.txt` records the deterministic output from executing this code. The verifier reports `ALL_CHECKS_PASS`. All finite computations are exhaustive on the explicitly stated finite objects; they are not extrapolated to other Archimedean or line graphs.

## Relationship to prior work

Adamaszek's 2011 preprint [1] initiates the systematic study of clique complexes of graph powers and identifies them with graph-metric Vietoris–Rips complexes. Its Theorem 5.2 relates the ordinary clique complex of a line graph to the two-skeleton of that of the original graph; it does **not** give the scale-two and scale-three graph-power complexes of this thirty-vertex line graph. Saleh, Titz Mite and Witzel [2] classify Platonic-solid Rips filtrations and explicitly propose Archimedean solids as a future direction (p. 2), but their theorem is not about this Archimedean graph or its intrinsic edge-path metric. Reference [3] identifies the icosidodecahedron as the line graph of the dodecahedron. Searches under icosidodecahedron, rectified dodecahedron, medial graph, line graph and graph-power terminology did not uncover a covering calculation; this does not establish publication priority against all unindexed sources.

## Limitations

The graph metric and the specified thirty-vertex graph are essential. The result provides no classification of arbitrary Archimedean graphs, no integral equivariant homology representation and no assertion about Euclidean-chordal persistence. The two sphere stages are individually homotopy equivalent to \(S^2\), and their inclusion has integral degree \(\pm1\); an explicit simplicial collapse from one to the other is not claimed. The verification is reproducible but has not undergone independent mathematical audit. Publication-priority uncertainty remains.

## References

[1] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first posted 2011-04-03, https://arxiv.org/abs/1104.0433 . See Introduction and Section 5, especially Theorem 5.2.

[2] N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, first posted 2023-02-28, https://arxiv.org/abs/2302.14388 . See Introduction, Theorem, p. 2 and Section 1 for metric conventions.

[3] E. W. Weisstein, *Icosidodecahedral Graph*, MathWorld, https://mathworld.wolfram.com/IcosidodecahedralGraph.html (accessed 2026-11-01); structural identification only, not a prior topology calculation.
