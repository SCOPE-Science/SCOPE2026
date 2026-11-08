# Sixteen six-spheres in the four-robust clique complex of the two-subset Kneser graph

## Finding
Let \(G=\operatorname{KG}(6,2)\), whose fifteen vertices are the two-element subsets of \(\{1,2,3,4,5,6\}\), with two vertices adjacent precisely when the represented subsets are disjoint. The four-robust clique complex \(\mathcal R_4(G)\) consists of those collections of vertices that contain no four-element independent set in \(G\). Then
\[
 \mathcal R_4(\operatorname{KG}(6,2))\simeq\bigvee^{16}S^6.
\]
Equivalently, with \(K_6\) the complete simple graph and \(M_3(K_6)\) the simplicial complex of edge sets of maximum degree at most three,
\[
 M_3(K_6)\simeq\bigvee^{16}S^6.
\]
All reduced integral homology therefore vanishes except \(\widetilde H_6\cong\mathbb Z^{16}\). No independent equivariant or simple-homotopy classification is asserted.

## Assumptions and scope
Every edge of \(K_6\) is a vertex of the simplicial complex. The fifteen edge-vertices are ordered lexicographically: \(\{0,1\},\{0,2\},\dots,\{4,5\}\), with graph vertices indexed from zero in the executable. A face is any nonempty subset of these edges whose degree at each of the six underlying graph vertices is at most three; the empty face is added for reduced chains. An edge set of size \(q\) determines a face of dimension \(q-1\). The assertion applies to the specified two-subset Kneser graph and no other parameters.

## Proof
**Identification.** A set of four vertices of \(\operatorname{KG}(6,2)\) is independent exactly when it is a four-edge pairwise-intersecting family of \(K_6\). Such a family must be contained in a vertex star. To see this, choose distinct intersecting edges \(ab,ac\). Any edge avoiding \(a\) while meeting both must be \(bc\); then an edge meeting \(ab,ac,bc\) has to be among the three edges of the triangle, so no family of four can contain an edge avoiding \(a\). Thus a set of Kneser vertices avoids all independent fours exactly when its associated edges have degree at most three. This identifies the two complexes simplicially.

**Exhaustive acyclic matching.** Index the fifteen edges of \(K_6\) lexicographically and represent an edge subset by its fifteen-bit mask. Enumerate every nonempty mask with vertex degrees bounded by three. In lexicographic edge order, for each mask that has not been matched and lacks the current pivot edge, match it to the mask obtained by adding that pivot, provided this mask is also still unmatched and admissible. These are precisely the pairing rules in `verify.py`; no hidden selection data are necessary. Exhaustive construction gives 12,067 nonempty faces, 6,021 matching pairs, and 25 unmatched faces in dimensions \(0,5,6,7\), respectively \(1,1,20,3\). To check acyclicity, orient all face-poset covers downward, except the matched incidences upward. A Kahn topological sort visits every one of the 12,067 faces, proving the absence of directed cycles. Therefore the discrete Morse theorem gives a CW model with the stated critical cells.

**Signed integral differential.** Give each face the increasing-edge orientation. If a codimension-one face is the lower member of a matched pair, recursively replace it using the signed boundary relation of its matched upper simplex. Ignore faces which are upper members of lower-dimensional matched pairs. Acyclicity makes this recursion terminate; `verify.py` independently derives every contribution rather than taking a saved matrix on trust. In the resulting integral Morse chain complex, the differential from \(C_6\cong\mathbb Z^{20}\) to \(C_5\cong\mathbb Z\) is the row vector (on the lexicographically sorted critical six-cells)
\[
 (0,-1,0,0,0,0,0,0,-1,0,-1,0,0,0,0,0,1,0,0,0 ).
\]
The differential \(C_7\cong\mathbb Z^3\longrightarrow C_6\) has its three columns given by the transposes of the following three row vectors:
\[
\begin{aligned}
&(0,0,0,0,-1,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0),\\
&(0,0,-1,-1,0,-1,0,1,-1,0,0,0,0,0,0,0,-1,1,-1,0),\\
&(-1,1,0,0,0,0,0,0,0,-1,-1,1,0,0,0,1,0,0,0,0).
\end{aligned}
\]
Their compositions with \(C_6\to C_5\) are zero. Stack the \(C_6\to C_5\) row with these three rows and select columns of zero-based indices \(0,2,4,10\). The resulting \(4\)-by-\(4\) integer minor has determinant \(+1\). Consequently the outgoing map \(C_6\to C_5\) is onto, the incoming map \(C_7\to C_6\) is injective and primitive in its kernel, and
\[
\widetilde H_6\cong\mathbb Z^{20-1-3}=\mathbb Z^{16},\qquad\widetilde H_i=0\ (i\ne6).
\]
All conclusions are integral; no field-only inference is used.

**Homotopy rather than homology.** The Morse CW complex has one vertex and no cells in dimensions one through four. Thus it is simply connected. Its reduced integral homology vanishes below dimension six. Repeated use of the first-nonvanishing-homotopy form of the Hurewicz theorem gives five-connectivity and \(\pi_6\cong\widetilde H_6\cong\mathbb Z^{16}\). Maps from sixteen six-spheres representing a basis induce an integral homology isomorphism from their wedge, hence a homotopy equivalence by the homological Whitehead theorem for simply connected CW complexes.

## Verification
Run `python3 verify.py` with the standard Python library. It exhaustively checks the Kneser independent-four characterization, all 12,067 faces, each of 6,021 paired incidences, acyclicity of the oriented Hasse graph, both signed integral Morse differentials, their zero composition, and the unimodular minor. The exact output appears in `verification_output.txt`, finishing `ALL_VERIFY_OK`. The finite computation here is an exhaustive proof for one explicitly finite graph; it is not being extrapolated to an infinite graph family.

## Relationship to prior work
Filakovský (first posted February 11, 2026) introduced four-robust clique complexes within a general \(k\)-robust framework and proved wedge classifications for bipartite square-sequence graphs, including grids. The nonbipartite Kneser graph \(\operatorname{KG}(6,2)\) is not covered by those graph hypotheses. Singh's theorem determines \(M_{n-2}(K_n)\) for complete graphs, which for \(K_6\) is \(M_4(K_6)\), not the \(M_3(K_6)\) considered here. Jonsson studied bounded-degree complexes and proved torsion-existence results, especially for versions with loops, without establishing this particular loop-free integral homotopy type. The four-intersecting-edges/star observation is elementary and is not claimed as an independent new extremal result; the claimed contribution is the exact topological decomposition for the first submaximal complete-graph case.

## Limitations
The result is restricted to \(M_3(K_6)\), equivalently the four-robust complex of \(\operatorname{KG}(6,2)\). It gives neither an all-order formula for \(M_{n-3}(K_n)\) nor an equivariant decomposition of its \(\mathfrak S_6\) action. Finite exhaustive checking and mathematical replay are not an independent review.

## References
Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (first public version 2026-02-11), https://arxiv.org/abs/2602.11365.

Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, https://arxiv.org/abs/2006.13632.

Jonsson, *3-torsion in the Homology of Complexes of Graphs of Bounded Degree*, Canadian Journal of Mathematics 65 (2013), 843–862, https://doi.org/10.4153/CJM-2013-008-4.
