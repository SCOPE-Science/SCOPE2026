# A Moore-space summand in the ordinary three-cut complex of the Clebsch graph

## Finding

Let \(C\) be the five-regular Clebsch graph (the folded five-cube), and let \(\Delta_3(C)\) be its **ordinary** three-cut complex: its facets are complements of three-vertex subsets inducing disconnected subgraphs. Then
\[
\boxed{\Delta_3(C)\simeq M(\mathbb Z/2\mathbb Z,11)\vee\bigvee^{15}S^{11}.}
\]
Here \(M(\mathbb Z/2\mathbb Z,11)=S^{11}\cup_{2}e^{12}\) denotes the Moore space with a twelve-cell attached by a map of degree two. In particular,
\[
\widetilde H_j(\Delta_3(C);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{15}\oplus\mathbb Z/2\mathbb Z,&j=11,\\
0,&j\ne11.
\end{cases}
\]
The complex is pure of dimension twelve and is not shellable. Its natural torsion is not implied by torsion-free classifications for triangle-free graphs whose four-cycles have disjoint edge sets.

## Assumptions and scope

The vertex set is \(V=\mathbb F_2^4\), coded by integers \(0,\dots,15\). Two distinct vertices \(a,b\) are adjacent precisely when their bitwise exclusive-or lies in \(\{1,2,4,8,15\}\). The graph has sixteen vertices and forty edges, is triangle-free, and is strongly regular with parameters \((16,5,0,2)\). It has forty induced four-cycles; every edge belongs to four such cycles.

For a triple \(T\subseteq V\), define \(T\) to be *disconnected* if the graph induced on its three vertices is disconnected. A facet of \(\Delta_3(C)\) is \(V\setminus T\) for every such triple \(T\); all subsets of these facets are faces. This is the ordinary cut complex, not the total cut complex or an independence, matching, Čech, or neighborhood complex. The theorem concerns this graph and this cut parameter only.

## Proof

**1. Exact combinatorics.** Enumerating the \(\binom{16}{3}=560\) triples gives \(160\) connected triples (each an induced path of length two) and \(400\) disconnected triples. The latter yield exactly \(400\) distinct twelve-dimensional facets of the ordinary three-cut complex. The numbers of nonempty faces in dimensions zero through twelve are
\[
(16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1780,400).
\]
Including the empty face gives \(65{,}199\) faces. The supplied `verify_cut.py` independently constructs each of these faces by iterating over all submasks of the \(400\) facets; the enumeration is exhaustive for the displayed sixteen-vertex graph.

**2. An explicit acyclic matching.** Represent each face by a sixteen-bit integer mask. Start with the set of all faces, including the empty face. Process vertex labels in the fixed order

`9, 15, 12, 0, 7, 11, 10, 14, 1, 8, 6, 3, 4, 5, 2, 13`.

For each label \(v\), simultaneously pair every currently remaining face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) when both remain; remove both. Such pairs at the same stage are disjoint, since one member contains \(v\) and the other does not. The algorithm produces exactly \(32{,}591\) pairs and leaves precisely sixteen faces of dimension eleven and one of dimension twelve. One pair is the empty face with a vertex. Remove this augmented pair to obtain an ordinary acyclic matching with one critical vertex, sixteen critical eleven-cells and one critical twelve-cell.

A complete check of the augmented directed face-incidence graph orients each unmatched cover downward and each matched cover upward. Kahn's topological sorting visits all \(65{,}199\) faces along all \(519{,}792\) incidences without a cycle. Removing the empty-face matching leaves the empty face a sink and cannot introduce a directed cycle. Hence Forman's discrete Morse theorem gives a CW homotopy model with the specified critical cells.

**3. Exact top-cell attaching degrees.** Orient simplices by increasing vertex labels. For each matched dimension-eleven face \(\tau\) paired with a dimension-twelve simplex \(\eta\), eliminate \(\tau\) using the signed boundary relation of \(\eta\), whose pivot coefficient is \(\pm1\). Recursing along the acyclic matching projects boundaries to the sixteen critical eleven-cells. In ascending critical-mask order, the boundary of the unique critical twelve-cell is
\[
(0,0,0,0,-2,2,2,-2,-2,2,-2,0,0,0,0,-2).
\]
The attached verification program constructs this vector using exact integers; its nonzero coefficients have greatest common divisor \(2\). The unit-pivot elimination is the cellular Morse differential, not merely a finite-field boundary rank.

**4. Identify the homotopy type.** The eleven-skeleton of the Morse CW model is \(\bigvee^{16}S^{11}\), because no cells of dimensions one through ten remain. For this wedge, the Hurewicz map identifies \(\pi_{11}\) with \(H_{11}\cong\mathbb Z^{16}\), so the attaching map of the twelve-cell is determined completely by its displayed degree vector. Integral elementary basis changes of the wedge are realized by homotopy self-equivalences and reduce that vector to \((2,0,\ldots,0)\). Thus the attachment is the degree-two Moore space wedged with fifteen eleven-spheres. This proves the claimed integral homotopy equivalence, including the torsion summand, without relying solely on field homology. As a pure twelve-dimensional shellable complex has free homology concentrated in top degree, the identified eleventh-degree torsion also obstructs shellability.

**5. Independent Alexander-dual check.** The combinatorial Alexander dual \(Q=\Delta_3(C)^\vee\) has all sixteen vertices, all \(120\) edges, the \(160\) connected path triples as triangles and the \(40\) induced four-cycles as tetrahedra. No larger dual simplex exists: on five vertices, requiring every one of ten triples to induce at least two edges forces at least seven graph edges (each lies in exactly three triples), exceeding the six-edge maximum for a triangle-free graph. Likewise on four vertices, requiring every triple connected forces at least four edges; the only triangle-free four-edge graph on four vertices is a four-cycle. Its first homology is controlled by the triangle-boundary map in the integral cycle lattice of the complete one-skeleton. Using the star at vertex zero as a spanning tree, `verify_dual_smith.py` constructs the resulting exact \(105\times160\) integer matrix and computes its Smith diagonal: \(104\) unit factors and one factor \(2\). Therefore \(H_1(Q;\mathbb Z)\cong\mathbb Z/2\mathbb Z\). This independent calculation confirms the torsion detected by the full cut-complex Morse differential. The Alexander dual is explicitly \(Q\), not a graph Čech nerve.

## Verification

Run `python3 verify_cut.py` (Python standard library only) and `python3 verify_dual_smith.py` (Python plus SymPy; tested with SymPy 1.14.0). Their complete outputs are in `verification_output.txt`. The first constructs all facets, subfaces, matching pairs and incidence arrows, proves finite acyclicity exhaustively, and derives the signed integral top Morse differential. The second constructs the Alexander-dual connected-triple boundary independently and computes its integral Smith form. The expected terminal markers are `VERIFY_OK` and `INDEPENDENT_VERIFY_OK` respectively. A calculation over a finite field alone would not detect the integral degree or establish the homotopy type; the proof uses integral coefficients and the stated topological theorems.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and investigated ordinary cut complexes in [1]; the sequel [2] treats further graph families. The torsion example obtained by realizing a projective plane using a purposely constructed graph and a much higher cut parameter is not an instance of the present natural Clebsch three-cut complex. Their shellability and torsion-freeness conditions do not include the claimed object.

The published triangle-free, edge-disjoint-four-cycle classification [3] gives a torsion-free sphere wedge for graphs satisfying its disjointness condition. The Clebsch graph has forty four-cycles, with **each edge lying in four four-cycles**, so the essential premise fails; its degree-two torsion demonstrates a sharp structural obstacle to dropping that hypothesis. The same graph's intrinsic scale-two Čech complex was separately found to have a projective-plane summand [4], but that is a different complex: its sixteen facets have six vertices, versus the \(400\) thirteen-vertex facets here. No Alexander-dual identity or stronger classification of the present ordinary cut complex follows from [4]. Other published Clebsch independence and open-neighborhood results concern distinct functors.

## Limitations

The result is for the standard Clebsch graph and the ordinary three-cut complex only, not a universal characterization of torsion in three-cut complexes. The displayed decomposition is an **ordinary integral homotopy** equivalence, not an equivariant decomposition. It does not classify other cut parameters, all strongly regular graphs or persistence maps. Independent mathematical audit is not claimed; unindexed equivalent prior work remains a risk despite the comparisons described here.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public April 26, 2023. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public July 11, 2024. https://arxiv.org/abs/2407.08158
3. *Three-cut complexes of triangle-free graphs with edge-disjoint squares*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-cut-complexes-of-triangle-free-graphs-with-edge-disjoint-s--8ca830284420
4. *A projective-plane summand in the scale-two Čech nerve of the Clebsch graph*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-projective-plane-summand-in-the-scale-two-ech-nerve-of-the-cle--4f10424a46be
