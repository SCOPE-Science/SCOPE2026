# Integral dual sphere decomposition of the Clebsch ordinary four-cut complex

## Finding
Let \(C\) be the sixteen-vertex, five-regular Clebsch graph (folded five-cube), with vertices the four-bit words \(0,\ldots,15\) and edges exactly when the bitwise XOR difference is one of \(1,2,4,8,15\). Let \(\Delta_4(C)\) be the **ordinary** four-cut complex whose facets are complements of disconnected induced four-vertex sets. Its combinatorial Alexander dual \(L=\Delta_4(C)^\vee\) has the integral homotopy type
\[
\boxed{L\simeq S^4\vee\bigvee^{34}S^3.}
\]
Consequently the entire reduced integral homology of the original cut complex is
\[
\widetilde H_i(\Delta_4(C);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=9,\\
\mathbb Z^{34},&i=10,\\
0,&\text{otherwise}.
\end{cases}
\]
The ordinary cut complex is pure of dimension eleven, but is neither shellable nor Cohen–Macaulay over any field.

## Assumptions and scope
All graphs are finite simple graphs; all chains and homotopy statements are integral. The **ordinary** four-cut condition uses disconnected induced sets of size four, not necessarily independent sets of size four (the latter define a different, total four-cut complex). For the sixteen-vertex vertex set \(V\), the Alexander dual is exactly
\[
L=\{\sigma\subseteq V:\text{every four-element subset of }\sigma\text{ induces a connected graph}\}.
\]
This condition is vacuous for vertex subsets of size at most three. The theorem concerns precisely this graph and cut parameter; no generalization to all folded cubes or strongly regular graphs is asserted.

## Proof
**1. Face classification.** The graph is five-regular with forty edges, triangle-free, and any nonadjacent pair has exactly two common neighbors. Every induced connected four-vertex graph is a star, an induced path, or a square. There are \(16\binom53=160\) stars. The graph contains forty squares: eighty nonadjacent pairs each have one pair of common neighbors, and each square is counted by its two opposite pairs. There are \(16\cdot5\cdot4^2=1280\) oriented three-edge nonbacktracking walks; forty squares contribute eight noninduced oriented walks each. Dividing the remainder by two gives \((1280-320)/2=480\) induced four-vertex paths. Therefore precisely \(160+40+480=680\) four-sets are connected, and \(\binom{16}{4}-680=1140\) are disconnected.

Every five-element face of \(L\) has all four-vertex deletions connected. Its induced subgraph therefore has minimum degree at least two. A triangle-free graph on five vertices with minimum degree at least two is either a pentagon or \(K_{2,3}\). The latter cannot occur, because its two degree-three vertices have three common neighbors, while the Clebsch graph has at most two. Thus the five-element faces are precisely the induced pentagons. There are 192 such pentagons: the adjacency spectrum is \(5^1,1^{10},(-3)^5\), so \(\operatorname{tr}(A^5)/10=(5^5+10-5\cdot3^5)/10=192\); triangle-freeness ensures every closed walk of length five is a simple pentagon. No six-element set can have all five-subsets pentagons: for a fixed vertex, deletion of each other vertex would have to leave degree exactly two, which is incompatible with the presence of both neighbors and nonneighbors in any six-element set. It follows that
\[
(f_0,f_1,f_2,f_3,f_4)(L)=(16,120,560,680,192)
\]
and \(L\) has no higher-dimensional faces.

**2. Exact integral boundaries.** The full two-skeleton of a fifteen-simplex has \(\ker\partial_2\cong\mathbb Z^{\binom{15}{3}}=\mathbb Z^{455}\). An explicit integral basis is supplied by the oriented boundaries of the formal tetrahedra \([0,i,j,k]\), indexed by \(1\le i<j<k\le15\). Coordinates in this basis equal coefficients of the triangles \([i,j,k]\), avoiding vertex zero. Consequently the oriented three-boundary has a concrete integer matrix of size \(455\times680\). The attached standalone verifier constructs it directly from the 680 connected quadruples, then uses exact **unit-pivot integer column operations**. It finds 455 pivots, every one \(+1\) or \(-1\), and all 225 residual columns are exactly zero. Column operations are invertible over \(\mathbb Z\); hence \(\partial_3\) surjects onto the complete two-cycle lattice, with no hidden torsion.

The similarly constructed signed four-boundary is a \(680\times192\) matrix, built from the 192 induced pentagons. A separate exact unit-pivot reduction gives 191 pivots, every one a unit, and one identically zero residual column. The script also verifies \(\partial_3\partial_4=0\) for each of the 192 columns. Therefore \(\operatorname{im}\partial_4\) is a primitive rank-191 sublattice in the degree-three chain group, and the integral reduced homology of \(L\) is
\[
\widetilde H_3(L;\mathbb Z)\cong\mathbb Z^{680-455-191}=\mathbb Z^{34},\qquad
\widetilde H_4(L;\mathbb Z)\cong\mathbb Z^{192-191}=\mathbb Z.
\]
All other reduced groups vanish. The reduced Euler characteristic is \(-33\), agreeing with \(-34+1\). These are exact integral calculations, not ranks inferred from finite-field data.

**3. Homotopy upgrading.** The three-skeleton \(L^{(3)}\) contains the full two-skeleton of a simplex, so it is simply connected. Its vanishing integral second homology implies, by Hurewicz, that it is two-connected. As a three-dimensional CW complex with free rank-225 third homology, it is homotopy equivalent to a wedge of 225 three-spheres (Hurewicz and Whitehead). The 192 four-cells attach through \(\pi_3(L^{(3)})\cong H_3(L^{(3)};\mathbb Z)\), so their entire attaching information is the integer matrix of their boundary classes. Its rank-191 primitive image has Smith form with 191 unit entries and one zero column; integral automorphisms of the degree-three sphere wedge realize the necessary row operations. Cancelling the 191 degree-one sphere-cell pairs leaves 34 three-spheres and one unattached four-cell, proving the displayed homotopy equivalence.

**4. Original cut complex.** Integral combinatorial Alexander duality on sixteen vertices gives \(\widetilde H_i(\Delta_4(C);\mathbb Z)\cong\widetilde H^{13-i}(L;\mathbb Z)\). Since the displayed dual homology is free, the cohomology groups have the same ranks in degrees three and four, giving the asserted reduced homology in degrees ten and nine. There are 1140 disconnected quadruples, hence 1140 distinct twelve-vertex facets of \(\Delta_4(C)\); it is pure of dimension eleven. Its nonzero ninth and tenth homology groups contradict the top-degree-only homology of pure shellable or Cohen–Macaulay eleven-complexes over any field.

## Verification
Run `python3 verify_clebsch_4cut_dual.py` from the directory containing the program, using Python 3 and only its standard library. It independently enumerates all connected four-vertex sets, builds every dual face through size six, checks the absence of six-faces, checks the 192 induced pentagons, constructs the signed chain matrices and checks their composition vanishes. Two exact integer unit-pivot reductions reproduce ranks 455 and 191 and verify the primitive lattice assertions. The matching output is in `verification_output.txt`; the final line is `VERIFY_OK`. Both files are included verbatim.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced ordinary cut complexes and classified several families, but their first article does not evaluate the Clebsch ordinary four-cut complex. Their continuation studies disjoint unions, squared paths and grid graphs. A separately published calculation of the **ordinary three-cut** Clebsch complex obtains two-torsion; changing the cut parameter changes both the faces and the topology. The published **total four-cut** Clebsch calculation also has two-torsion, but total four-cut complexes use independent quadruples and are not the present object. A published ordinary four-cut computation for the four-dimensional hypercube \(Q_4\) does not imply this result: the Clebsch graph adds eight antipodal edges, changing which quadruples are connected and introducing the 192 pentagon dual faces. No inspected source provides the present dual decomposition or its consequent two-degree integral homology. Search limitations are recorded in the accompanying review.

## Limitations
The complete integral **homology** of the original cut complex is determined, but its integral **homotopy type** is not asserted to be a wedge of spheres. The homotopy classification here applies to its combinatorial Alexander dual only. The result does not identify automorphism-group representations, persistence maps, homology for higher folded cubes, or all strongly regular graphs. Absence of an indexed equivalent does not prove absolute novelty; independent mathematical audit has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public posting 2023-04-26), https://arxiv.org/abs/2304.13675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public posting 2024-07-11), https://arxiv.org/abs/2407.08158.
3. *Integral two-torsion in the Clebsch graph's ordinary three-cut complex*, public research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-integral-two-torsion-in-the-clebsch-graph-s-ordinary-three-cut-c--e8c76e05cbee/RESULT.md.
4. *The ordinary four-cut complex of the four-cube is a mixed-dimensional sphere wedge*, public research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-ordinary-four-cut-complex-of-the-four-cube-is-a-mixed-dimens--33597bc28ca6/RESULT.md.
5. *Two-torsion in the Clebsch total four-cut complex and its Alexander dual*, public research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-two-torsion-in-the-clebsch-total-four-cut-complex-and-its-alexan--b0633ca3c02c/RESULT.md.
