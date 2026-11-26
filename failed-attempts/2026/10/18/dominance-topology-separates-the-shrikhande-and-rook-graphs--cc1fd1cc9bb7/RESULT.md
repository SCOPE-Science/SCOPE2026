# Dominance topology separates the Shrikhande and rook graphs

## Finding
For the Shrikhande graph \(S\) and the \(4\times4\) rook graph \(R\), with the precise definitions below, the dominance complexes have distinct integral homological signatures:
\[
\mathcal D(S)\simeq\bigvee^{11}S^9,
\qquad
\widetilde H_j(\mathcal D(R);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=9,\\
\mathbb Z^2,&j=11,\\
0,&\text{otherwise}.
\end{cases}
\]
Both graphs have strongly regular parameters \((16,6,2,2)\). Moreover, for translation \(t=(a,b)\in(\mathbb Z/4\mathbb Z)^2\) of the Shrikhande graph, its action on \(\widetilde H_9(\mathcal D(S);\mathbb Q)\) has character
\[
\chi(t)=
\begin{cases}
11,&(a,b)=(0,0),\\
3,&(a,b)\ne(0,0)\text{ and }(a=0\text{ or }b=0\text{ or }a=b),\\
-1,&\text{otherwise},
\end{cases}
\]
with coordinates understood modulo four. Equivalently, over the complex numbers the character contains the trivial character twice and each of the nine characters indexed by
\[
(0,1),(0,2),(0,3),(1,0),(1,3),(2,0),(2,2),(3,0),(3,1)
\]
once, when a character indexed by \((u,v)\) sends translation \((a,b)\) to \(i^{ua+vb}\).

## Assumptions and scope
Both graphs are finite, undirected, simple graphs on the vertex set \(V=(\mathbb Z/4\mathbb Z)^2\), identified with integer masks by \((x,y)\mapsto4y+x\) for coordinate representatives \(0,1,2,3\). In \(S\), two distinct vertices are adjacent if and only if their difference belongs to
\[
\{\pm(1,0),\pm(0,1),\pm(1,1)\}.
\]
In \(R\), two distinct vertices are adjacent if and only if they have one equal coordinate. Each vertex has six neighbors and every pair of distinct vertices has exactly two common neighbors; this is directly tested in the verification program. The graphs are nonisomorphic: a vertex's open neighborhood induces a six-cycle in \(S\), versus two disjoint triangles in \(R\).

For any such graph \(G\), a vertex set \(D\) dominates when every vertex belongs to \(D\) or is adjacent to a vertex of \(D\). Its dominance complex is
\[
\mathcal D(G)=\{A\subseteq V(G):V(G)\setminus A\text{ is dominating}\}
=\{A\subseteq V(G):\nexists v,\;N_G[v]\subseteq A\}.
\]
The empty face is included for combinatorial calculations; reduced homology and geometric realization use the standard conventions. The claim is solely about these two sixteen-vertex graphs and the translations specified above. It does not classify all strongly regular graphs, assert a full homotopy type for the rook dominance complex, or assert that the rook eleven-cells attach trivially in homotopy.

## Proof
**Exact finite face presentation.** Each graph has sixteen closed neighborhoods \(N_G[v]\), each containing seven vertices. For any mask \(A\in\{0,1,\ldots,65535\}\), define it to be an admissible face precisely when it contains none of these neighborhoods. Exhausting all masks determines every face without truncation. The resulting complexes have 59,819 and 59,747 faces, respectively, including the empty face. For \(S\), the nonempty face vector in increasing simplex dimension is
\[
(16,120,560,1820,4368,8008,11424,12726,10864,6712,2640,528,32).
\]
For \(R\), it is
\[
(16,120,560,1820,4368,8008,11424,12726,10864,6712,2640,488).
\]

**A complete discrete-Morse matching.** Starting with all faces available, visit vertex labels \(v=0,1,\ldots,15\) in order. At step \(v\), visit all available faces \(A\) not containing \(v\) in increasing integer-mask order. If both \(A\) and \(A\cup\{v\}\) are still available, pair them and remove both from availability. This deterministic prescription specifies all pairs, without requiring an external matching table.

For \(S\), 29,904 pairs leave eleven unmatched nine-simplices; for \(R\), 29,872 pairs leave one unmatched nine-simplex and two unmatched eleven-simplices. In both cases the pair \((\varnothing,\{(0,0)\})\) occurs. Removing just that pair from the matching on the ordinary nonempty face poset leaves the indicated higher critical simplices together with one critical zero-simplex.

**Acyclicity.** Orient each face-poset covering incidence from the larger face to the smaller face except for matched pairs, which point from smaller to larger. The attached checker explicitly inspects all 461,568 covering incidences of \(S\) and 460,672 of \(R\), then performs a complete topological sort of each directed Hasse graph. Every one of the 59,819 or 59,747 faces, respectively, is visited exactly once. Thus no directed cycle exists. Deleting the empty face and its incident edges preserves acyclicity and leaves the ordinary matching specified above.

**Topological consequences.** Forman's discrete Morse theorem supplies a CW model having exactly one zero-cell and eleven nine-cells for \(\mathcal D(S)\), so every nine-cell attaches to the basepoint and the CW model is \(\bigvee^{11}S^9\). For \(\mathcal D(R)\), the Morse CW model has one zero-cell, one nine-cell and two eleven-cells. There are no ten-cells, so every cellular boundary is zero, and the stated reduced *integral homology groups* follow. The possible unstable attaching maps from eleven-cells to the nine-skeleton are not calculated or assumed null.

**Translation representation.** Every translation of \(V\) preserves \(S\) and its closed-neighborhood forbidden-set complex. For a translation \(t\), an invariant face is a union of orbits of the permutation it induces on the sixteen vertices. If it occupies \(c\) orbits, the product of its simplicial chain sign and its alternating-degree sign is \(-(-1)^c\), including the reduced empty-face term. Therefore the reduced Lefschetz number is the negative of the sum of \((-1)^c\) over all invariant faces. As the only reduced homology of \(\mathcal D(S)\) is in odd degree nine, the trace on that group is precisely this face sum. The checker evaluates it for all sixteen translations and obtains the displayed character. Exact Fourier inversion over \((\mathbb Z/4\mathbb Z)^2\) yields the ten nonzero character multiplicities listed above (the trivial character twice).

## Verification
Run `python verify.py` with Python 3.10 or later, from the directory containing this document. No external packages, prior files, database, random choices, or network access are required. The program reconstructs both graphs and all 65,536 masks; checks symmetry, degree six, two common neighbors for every distinct vertex pair, and equivalence of two face predicates; checks downward closure; builds all matching pairs; verifies total coverage and reduced Euler counts; and constructs and topologically sorts every oriented Hasse incidence. For \(S\), it also evaluates the full translation character and performs exact integral Fourier-inversion checks. The supplied `verification_output.txt` is one replay result; the proof uses the executable exhaustive construction and finite acyclicity criterion, not the log alone.

## Relationship to prior work
Matsushita and Wakatsuki, arXiv:2312.02639v1 (December 5, 2023), establish the Alexander-dual relationship \(\mathcal D(G)=\mathcal N(\overline G)^\vee\), and compute families involving cycles and Cartesian path strips; those theorems do not give the Shrikhande or four-by-four rook dominance homology. Matsushita, arXiv:2009.04145v1, gives general connectivity restrictions from vertex-cover numbers, not these exact homotopy types. Taylan, arXiv:1501.06754v1, computes dominance complexes for chordal graphs; neither graph here is chordal.

Related indexed calculations of \(\operatorname{Ind}(S)\) and \(\operatorname{Ind}(R)\), their intrinsic radius-one Čech nerves, and their ordinary open-neighborhood complexes involve different simplicial complexes. A dominance complex is combinatorially dual to the *open-neighborhood complex of the graph complement*, not automatically to the open-neighborhood complex of the same graph, its independence complex, or its graph-metric Čech complex. None of the inspected exact indexed results determines the critical-cell counts, full homotopy statement, or translation character here. Earlier results distinguish the two graphs by other invariants, so the claim is not that this is the first topological distinction of these graphs.

## Limitations
The calculations are exhaustive but finite and restricted to the two defined graphs. The rook result determines integral homology, not its full unstable homotopy type. The character calculation concerns only the natural translation subgroup and rational ninth homology of the Shrikhande dominance complex, not the entire graph automorphism group. Searches and inspected primary literature cannot eliminate unindexed prior computations; no independent external mathematical audit has been performed.

## References
Matsushita, T., and Wakatsuki, S., *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (first public date 2023-12-05), https://arxiv.org/abs/2312.02639.

Matsushita, T., *Dominance complexes and vertex cover numbers of graphs*, arXiv:2009.04145v1 (2020-09-09), https://arxiv.org/abs/2009.04145.

Taylan, D., *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1 (2015-01-27), https://arxiv.org/abs/1501.06754.
