# A mixed wedge of 28 three-spheres and three four-spheres from three disjoint triangles

## Finding

Let \(A_1=\{0,1,2\}\), \(A_2=\{3,4,5\}\), and \(A_3=\{6,7,8\}\). Put \(V=A_1\sqcup A_2\sqcup A_3\), and let \(K=\Delta(A_1)\sqcup\Delta(A_2)\sqcup\Delta(A_3)\) be the simplicial complex with exactly three facets, each a **filled** triangle. Then its two-tolerance complex satisfies

\[
\boxed{\big|\mathcal T_2(K)\big|\simeq\bigvee^{28}S^3\vee\bigvee^3S^4.}
\]

This determines the full **integral homotopy type**. In particular the complex is two-connected, and its nonzero reduced integral homology groups are \(\widetilde H_3\cong\mathbb Z^{28}\) and \(\widetilde H_4\cong\mathbb Z^3\). Both sphere dimensions occur: unlike the familiar two-facet tolerance example, the three-facet example is a genuinely mixed-dimensional sphere wedge.

## Assumptions and scope

For any finite simplicial complex \(L\) on vertex set \(V\), the tolerance complex at integer parameter \(t\ge0\) is

\[
\mathcal T_t(L)=\{\sigma\subseteq V:\text{there exists }\tau\subseteq\sigma,\ \tau\in L,\ |\sigma\setminus\tau|\le t\}.
\]

For the specified \(K\) and \(t=2\), this becomes the exact face predicate

\[
\sigma\in X\quad\Longleftrightarrow\quad
\min_{i\in\{1,2,3\}}|\sigma\setminus A_i|\le2.
\]

All vertices are labelled, though the resulting homotopy type is independent of labelling. The underlying triangles are filled two-simplices, not unfilled three-cycles. No assertion is made for four or more blocks, arbitrary facet sizes or other tolerance parameters.

## Proof

Represent a nonempty face \(\sigma\) by a nine-bit mask \(m\in\{1,\ldots,511\}\); bit positions are the vertices \(0,\ldots,8\). Let the three facet masks be \(7,56,448\). The exact predicate above selects 300 masks. Their numbers by dimension \(0,1,2,3,4\) are, respectively,

\[
(9,36,84,126,45).
\]

Construct a partial matching of their face poset by the fixed vertex order \((0,6,1,4,8,7,5,2,3)\). Starting with every nonempty face unpaired, for each vertex \(v\) in that order scan the masks in increasing numerical order. Whenever a presently unpaired face \(\sigma\) omits \(v\) and the face \(\sigma\cup\{v\}\) is also presently unpaired, match these two faces and remove both from the unpaired set.

The supplied standalone checker reproduces all resulting 134 matched covering pairs, checks that every pair consists of faces differing by one vertex, and verifies that the directed Hasse graph (reversing precisely the matched cover relations) is acyclic. This checks all 1,053 Hasse incidences by a complete topological-sort test. The unmatched faces consist of exactly one vertex, 28 three-simplices and three four-simplices. Forman's discrete-Morse theorem therefore gives a homotopy equivalent CW complex \(Y\) with exactly these cells and no cells in dimensions one or two.

It remains to compute, **over the integers**, the attaching degrees of the three four-cells against the 28 three-cells. Give every simplex the increasing-vertex orientation, so its simplicial boundary has coefficients \((-1)^j\) after deleting its \(j\)-th vertex. For each critical four-simplex, begin with its integral simplicial boundary \(b\). Whenever a matched lower three-simplex \(\sigma\) has nonzero coefficient \(c\) in \(b\) and is paired with an upper four-simplex \(\tau\), replace

\[
b\ \longleftarrow\ b-c[\sigma:\tau]\,\partial\tau,
\]

where the incidence \([\sigma:\tau]\) equals \(1\) or \(-1\). Because the reversed Hasse graph is acyclic, this procedure terminates and is exactly the signed gradient-path reduction calculating the integral Morse boundary. The checker performs these integer operations without using floating point or finite-field approximation. For **each of the three critical four-simplices**, every resulting coefficient of every critical three-simplex is zero. Consequently the integral cellular boundary \(C_4(Y;\mathbb Z)\to C_3(Y;\mathbb Z)\) is the zero \(28\)-by-\(3\) matrix.

The three-skeleton of \(Y\) is a wedge of 28 three-spheres. The Hurewicz isomorphism identifies its third homotopy group with its third integral homology, so the vanishing attaching-degree vector means each four-cell attaches by a nullhomotopic map. Therefore

\[
Y\simeq\bigvee^{28}S^3\vee\bigvee^3 S^4,
\]

proving the claimed integral homotopy type.

## Verification

Run `python checker.py` using Python 3.8 or later. The program enumerates the complete face poset, recreates the deterministic matching, checks directed acyclicity on every Hasse incidence, and evaluates the three Morse boundary columns by signed integer cancellation. Separately, it calculates the full ordinary simplicial boundary-rank profile modulo two: ranks \(8,28,56,42\) in degrees one through four. The mod-two Betti dimensions are \(1,0,0,28,3\) in degrees zero through four. These field checks are independent corroboration; the integral homotopy conclusion uses the verified integer Morse differential and the cell-attachment argument above.

## Relationship to prior work

Kim and Lew, *Leray numbers of tolerance complexes* (first publicly available 2021), introduce the same tolerance construction and exhibit two disjoint facets each containing three vertices whose two-tolerance complex is the boundary of a simplex, hence one four-sphere. The present result instead concerns **three** disjoint filled triangular facets, whose tolerance complex has homology in two degrees, and provides exact integral multiplicities and a homotopy decomposition.

Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers* (first public 10 November 2026), proves Leray/collapsibility bounds for tolerance complexes of chordal clique complexes, including the present type of chordal graph input, but does not state this exact three-triangle homotopy classification. Existing formulas for the tolerance complexes of **unfilled one-dimensional graphs** do not apply, because the input has filled triangles. Likewise, a formula for one-tolerance of disjoint simplexes concerns a different parameter.

## Limitations

This is a finite, fully enumerated nine-vertex case, not a formula for an arbitrary number of facets or general chordal graphs. Its topological proof depends on exact finite combinatorial calculations embedded in the checker and the standard discrete-Morse theorem. It does not claim independent verification, complete historical priority or a classification of all tolerance complexes. Equivalent unindexed work remains a possible priority risk.

## References

- Kim and Lew, *Leray numbers of tolerance complexes*, arXiv:2109.03030, https://arxiv.org/abs/2109.03030 (see the introduction and the two-disjoint-facets example).
- S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384, https://arxiv.org/abs/2611.14384 (version first public 10 November 2026; see Sections 1, 5, 7 and 8).
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse homotopy theorem and gradient-path differentials).
