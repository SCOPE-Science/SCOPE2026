# Complete graph-metric Vietoris–Rips filtration of the Möbius–Kantor graph

## Finding

For the sixteen-vertex Möbius–Kantor graph \(G=\operatorname{GP}(8,3)\), endowed with its shortest-path distance and the **inclusive graph-vertex** Vietoris–Rips complex \(R_r(G)\), the full homotopy filtration at nonnegative integer thresholds is

\[
\begin{aligned}
R_0(G)&\simeq\bigvee^{15}S^0,\\
R_1(G)&\simeq\bigvee^9 S^1,\\
R_2(G)&\simeq\left(\bigvee^9 S^2\right)\vee\left(\bigvee^2 S^3\right),\\
R_3(G)&\cong S^7,\\
R_r(G)&\simeq * \quad(r\ge4).
\end{aligned}
\]

At scale three, the complex is *combinatorially* the boundary of an eight-dimensional cross-polytope. For a nonnegative real parameter the complex is constant between successive integer thresholds. Consequently the entire **reduced integral persistence barcode** consists of fifteen degree-zero intervals \([0,1)\), nine degree-one intervals \([1,2)\), nine degree-two intervals \([2,3)\), two degree-three intervals \([2,3)\), and one degree-seven interval \([3,4)\), with no other positive-multiplicity intervals.

## Assumptions and scope

Write indices modulo eight. The vertex set is \(\{u_i,v_i:i\in\mathbb Z/8\mathbb Z\}\), with edges
\[
\{u_i,u_{i+1}\},\quad \{u_i,v_i\},\quad \{v_i,v_{i+3}\},\qquad i\in\mathbb Z/8\mathbb Z.
\]
Every edge has length one. Let \(d_G\) denote the shortest-path distance on **vertices**, not the metric graph containing interiors of edges. For \(r\ge0\), a nonempty vertex subset \(\sigma\) belongs to \(R_r(G)\) precisely when \(d_G(x,y)\le r\) for all \(x,y\in\sigma\). Empty simplex bookkeeping is used only for augmented chains. All asserted equivalences are nonequivariant integral homotopy equivalences; no functorial sphere basis is claimed.

This graph is also the Levi incidence graph of the eight-point/eight-line Möbius–Kantor configuration. The standalone verifier checks an explicit bijection between the two edge descriptions, so the graph nomenclature does not rely on a drawing.

## Proof

**Radius zero and one.** The graph has sixteen distinct vertices, is connected and has twenty-four undirected edges, and its girth is six. Thus the radius-zero complex is sixteen isolated points, homotopy equivalent (in the pointed convention) to a wedge of fifteen zero-spheres. At radius one the flag complex is exactly the triangle-free graph \(G\). Its cycle rank is \(24-16+1=9\), giving a wedge of nine circles.

**Exhaustiveness of the radius-two face list.** Define the graph on the same sixteen vertices by adjacent pairs at graph distance at most two; its clique complex is \(R_2(G)\). The standalone `verify.py` independently enumerates its cliques by increasing-face extension and by maximal-clique closure. Both agree, and an additional exhaustive pairwise-distance predicate agrees on **every one of the \(2^{16}=65536\) vertex subsets**. The counts of nonempty simplices in dimensions zero through three are \((16,72,112,48)\), plus the empty face, so there are exactly 249 faces and the complex has dimension three.

**An integral radius-two homotopy certificate.** For an explicitly fixed vertex permutation the verifier applies iterative matching by a vertex toggle: at each step an unmatched simplex without the toggle vertex is paired with the simplex containing that vertex when both are still unmatched. It constructs **119 disjoint pairs**, including the empty-face pair. Across all 688 augmented Hasse incidences, reverse the incidence arrows of matched pairs and retain the others in the opposite orientation; the script checks acyclicity by a complete topological sort of the directed Hasse graph. Its critical augmented faces are exactly nine triangles and two tetrahedra. A distinct second toggle order produces another complete acyclic matching with the same critical-dimensional pattern; both are checked, not inferred from one another.

The signed augmented simplicial chain boundary is then reduced by the elementary integral cancellation rule: if a paired \((k-1)\)-face \(a\) and \(k\)-face \(b\) have boundary coefficient \(\varepsilon=\pm1\), eliminate the two generators by subtracting \(\varepsilon\) times the appropriate multiple of \(\partial b\) from all other dimension-\(k\) boundaries. Every pivot is tested to be a unit *at the time of cancellation*. The surviving differential from the two critical tetrahedra to the nine critical triangles is the **zero** \(9\times2\) integer matrix for both toggle orders and for both forward and reverse pivot-elimination orders. This is an exact integer computation, not an inference from finite-field ranks.

After reinstating the usual unaugmented zero-cell, the acyclic matching gives a Morse CW model with a single zero-cell, no one-cells, nine two-cells and two three-cells. The two-skeleton is therefore \(\bigvee^9 S^2\). By the degree-two Hurewicz isomorphism \(\pi_2(\bigvee^9 S^2)\cong H_2(\bigvee^9 S^2;\mathbb Z)\cong\mathbb Z^9\), each three-cell attaching map is determined by its nine integer attaching degrees, which are zero. Both attachments are nullhomotopic, yielding the asserted wedge of nine two-spheres and two three-spheres. The computed integral homology is therefore torsion-free; the reduced Euler characteristic \(9-2=7\) agrees with \(16-72+112-48-1=7\).

**Radius three and above.** The all-pairs breadth-first searches establish that the graph diameter is exactly four. The **only** unordered vertex pairs farther than three are the eight disjoint pairs \(\{u_i,u_{i+4}\}\) and \(\{v_i,v_{i+4}\}\), where \(i\in\{0,1,2,3\}\). A radius-three simplex is consequently a subset selecting at most one vertex from each of eight disjoint antipodal pairs. This is precisely the boundary complex of the eight-dimensional cross-polytope, giving a seven-sphere. Radius four includes all subsets and is a simplex.

**Barcode consequence.** At radius one only reduced homology degree one survives, at radius two only degrees two and three, at radius three only degree seven, and at radius four none. Therefore no nonzero class in these degrees can survive beyond its displayed next threshold. All changes occur at integers, so the stated intervals and multiplicities follow; there are no undetermined extension or torsion issues.

## Verification

Run `python3 verify.py` using Python 3's standard library. It checks both graph presentations, all shortest-path distances, two independent clique enumerations, all 65,536 vertex subsets, both augmented face matchings, complete acyclicity of each matching, all signed unit pivots and exact zero residual matrices. A second unreduced boundary computation independently obtains boundary ranks \((15,57,46)\) over each of the coefficient fields of orders two, three and five. It also identifies all eight scale-three forbidden pairs and checks diameter four. The embedded `verification-output.txt` is the literal output of this standalone verifier, ending with `MK_RIPS_COMPLETE_FILTRATION_INTEGRAL_HOMOTOPY_VERIFIED`.

The graph has twenty-four distinct unoriented six-cycles; as many as six of these traverse a common edge. Thus the published edge-disjoint-hexagon classification cannot be applied to infer the scale-two result here. This is checked in the verifier. The two independent exact reductions, not the finite-field computations alone, certify the integral homotopy statement.

## Relationship to prior work

Adamaszek and Adams, *On Vietoris–Rips complexes of hypercube graphs* (arXiv:2103.01040), establish sphere-wedge results for the **hypercube with the Hamming metric**. Our graph has the same number of vertices as a four-cube but is cubic rather than four-regular and has a different graph metric. Their result therefore does not determine the present radius-two mixed-dimensional wedge or barcode. It motivates analyzing a comparably symmetric graph metric at an integral scale.

Adamaszek, *Clique complexes and graph powers* (arXiv:1104.0433), treats square-graph clique complexes under hypotheses such as girth at least seven, while the present graph has girth six. The published *A hexagon-packing classification of scale-two graph Rips complexes* assumes that all six-cycles are pairwise edge-disjoint; the present graph's 24 hexagons share edges, so its all-graph theorem does not apply. Results about incidence graphs of **finite projective or affine planes** likewise have different incidence axioms and vertex counts; the Möbius–Kantor \((8_3)\) configuration is neither such plane.

Feng and Nukala, *On Vietoris–Rips complexes of Finite Metric Spaces with Scale 2* (arXiv:2302.14664), analyze particular layers of the Boolean cube under symmetric-difference distance, not this graph's shortest-path metric. Knill, *Remarks about the Moebius–Kantor graph* (arXiv:2605.30799), discusses the graph's symmetries, torus embedding, geodesic flow and Lefschetz numbers, but does not supply this Rips classification in the inspected text. Published same-graph computations of the intrinsic Čech nerve, independence complex and matching complex concern other filtrations or simplicial constructions and do not imply this one. Public research-record searches using the alternate \(\operatorname{GP}(8,3)\), Möbius–Kantor, incidence-graph, square-graph and Rips descriptions did not identify an equivalent claim; this does not prove absolute bibliographic uniqueness.

## Limitations

The classification is for this sixteen-vertex graph and **its vertex-shortest-path metric only**. No result is asserted for metric graph realizations, arbitrary generalized Petersen graphs, all symmetric cubic graphs, equivariant homotopy or canonical sphere generators. The proof is exact but computer-assisted at radius two: its integrity depends on the complete face enumeration, acyclicity and integral chain-cancellation implementation supplied. A stronger equivalent result in unindexed literature remains possible; no independent external scientific audit is claimed.

## References

1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, first public 2021-03-01. Full preprint, particularly Theorem 1.
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public 2011-04-03. Full preprint, Proposition 2.2 and graph-square hypotheses.
3. Z. Feng and N. C. P. Nukala, *On Vietoris–Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664, first public 2023-02-28, Sections 1 and 6.
4. O. Knill, *Remarks about the Moebius–Kantor graph*, arXiv:2605.30799, 2026-05-29, accessible complete HTML, Sections 1–5.
5. *A hexagon-packing classification of scale-two graph Rips complexes*, published mathematical result at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-hexagon-packing-classification-of-scale-two-graph-rips-complex--70b9bc9b3abb, particularly the hypotheses and Finding/Proof sections of `RESULT.md`.
