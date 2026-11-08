# Integral two-torsion in the Clebsch graph's ordinary three-cut complex

## Finding
Let \(C\) be the 5-regular Clebsch graph, equivalently the folded five-cube, specified below. Its ordinary three-cut complex has integral homotopy type
\[
\Delta_3(C)\simeq\bigvee^{15}S^{11}\vee M(\mathbb Z/2\mathbb Z,11),
\]
where \(M(\mathbb Z/2\mathbb Z,11)=S^{11}\cup_{2}e^{12}\) is the degree-two Moore space. Thus
\[
\widetilde H_j(\Delta_3(C);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{15}\oplus\mathbb Z/2\mathbb Z,&j=11,\\
0,&j\ne11.
\end{cases}
\]
The complex is pure of dimension twelve and is not shellable.

## Assumptions and scope
Use the 16 even-Hamming-weight binary words of length five as vertices, ordered increasingly by their five-bit integer values. Join two distinct words when their Hamming distance is four. This is the 5-regular Clebsch graph with parameters \((16,5,0,2)\), not the complementary 10-regular graph sometimes called by the same name. The set \(\Delta_3(C)\) contains exactly the subsets \(\sigma\) for which the complementary vertex set contains a three-subset inducing a disconnected graph. Equivalently, its facets are the complements of disconnected induced triples. Homotopy and homology are integral unless explicitly qualified.

## Proof
**Enumeration and duality.** There are 40 edges. Since the graph is triangle-free and 5-regular, precisely \(16\binom{5}{2}=160\) induced triples are connected (they are two-edge paths), out of \(\binom{16}{3}=560\) triples. Hence the other 400 triples index distinct thirteen-vertex facets. Their downward closure has 65,199 faces including the empty face, with face numbers in dimensions zero through twelve:
\[
(16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1780,400).
\]
In particular the complex is pure twelve-dimensional, but lacks forty possible eleven-dimensional faces.

**Explicit acyclic matching.** Number vertices zero through fifteen by the increasing binary-word ordering. Process toggles in the sequence
`12,5,6,10,1,2,7,8,9,13,3,15,0,11,14,4`.
For each processed vertex, pair every currently unmatched face not containing it with the face obtained by adjoining it, provided that the latter is a face and is still unmatched. The first such construction also pairs the empty face to a vertex; remove this one pair and keep that vertex critical. The resulting matching on ordinary nonempty faces has 32,590 pairs. Orient each matched covering relation upward and every other covering relation downward. The accompanying checker constructs all 519,776 covering incidences and confirms that this entire directed graph is acyclic by topological sorting all 65,198 nonempty faces. The only critical cells are one vertex, sixteen eleven-cells and one twelve-cell. The finite verification is exhaustive, not a sample.

**Integral attaching map.** Orient each simplex by the increasing order on its vertices, so the coefficient of a codimension-one face obtained by deleting position \(j\) is \((-1)^j\). On a matched pair \(s\subset u\) with \(\dim s=11\) and \(\dim u=12\), eliminate the coefficient of \(s\) using the signed identity \(\partial u=0\) in the cellular Morse reduction. The complete recursive gradient-path calculation produces the boundary of the unique critical twelve-cell in the increasing-mask basis of critical eleven-cells:
\[
D=(0,0,2,-2,-2,2,-2,0,0,0,0,-2,-2,0,-2,0)^{\mathsf T}.
\]
The greatest common divisor of these sixteen entries is exactly two, and the rank is one. Thus its Smith normal form has exactly one nonunit invariant, equal to two. The discrete-Morse CW complex has a single zero-cell and no cells in dimensions one through ten. Its eleven-skeleton is a wedge of sixteen eleven-spheres. The attaching class of its twelve-cell lies in
\[\pi_{11}\!\left(\bigvee^{16}S^{11}\right)\cong\mathbb Z^{16},\]
by the Hurewicz theorem in this dimension; the displayed vector represents that attaching class. An invertible integral change of basis on the wedge of eleven-spheres carries this vector to \((2,0,\ldots,0)\) and is realized by a self-homotopy equivalence. Consequently the CW complex, and hence \(\Delta_3(C)\), is the stated wedge of a degree-two Moore space and fifteen spheres. The integral homology formula follows.

**Nonshellability.** A pure shellable twelve-dimensional complex has the homotopy type of a wedge of twelve-spheres, hence no torsion in degree eleven. The proven \(\mathbb Z/2\mathbb Z\) summand rules out shellability.

## Verification
Run `python3 verify_clebsch_cut.py` with Python 3.10 or later, using only the standard library. It reconstructs the entire graph and all faces, independently checks the face condition against the disconnected-triple definition, constructs the specified matching, checks every oriented Hasse edge for directed cycles, and computes the signed integral Morse differential via complete recursive elimination. The recorded output is `verification_output.txt`.

An independent small-complex check constructs the combinatorial Alexander dual \(L=\{\sigma:\text{every three-subset of }\sigma\text{ induces a connected graph}\}\). Its face vector is \((16,120,160,40)\); there are no larger faces. Exact boundary ranks \((\operatorname{rk}\partial_1,\operatorname{rk}\partial_2,\operatorname{rk}\partial_3)\) are \((15,104,40)\) in characteristic two and \((15,105,40)\) in characteristics three, five, seven and eleven. These confirm the expected mod-two torsion signature and free Betti rank. The integral conclusion is established by the signed Morse differential, not by finite-field extrapolation.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced the ordinary cut-complex framework and proved homotopy classifications for several graph families. Their relevant skeleton-based torsion-freeness criterion does not apply: this Clebsch complex lacks forty eleven-faces, so its eleven-skeleton is not complete. Their triangle-free classification concerns the two-cut, not the three-cut, complex. The continuation studies disjoint unions, squared paths and grids, not the five-folded cube. The strongly regular graph parameters and folded-cube description are classical and are not claimed as new.

The contribution here is the **exact integral homotopy type** for the ordinary three-cut complex of this particular graph, including both fifteen free sphere summands and genuine two-torsion. Previously known torsion examples for other cut complexes do not imply this graph-specific homotopy classification. No claim of a universal classification of triangle-free or strongly regular graphs is made.

## Limitations
The result concerns only the 5-regular version of the sixteen-vertex Clebsch graph and the ordinary three-cut construction; it does not address the complementary graph, total cut complexes, other cut parameters or full equivariant homotopy. The exhaustive computations establish a finite statement but do not generalize automatically to larger graphs. An equivalent result in inaccessible or unindexed literature remains possible. Independent external mathematical audit has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted 2023-04-26), later SIAM J. Discrete Math. 38 (2024), DOI 10.1137/23M1569034. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first posted 2024-07-11). https://arxiv.org/abs/2407.08158
3. A. E. Brouwer, *Clebsch graph* (strongly regular graph information and complement-name convention). https://aeb.win.tue.nl/drg/graphs/Clebsch.html
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
