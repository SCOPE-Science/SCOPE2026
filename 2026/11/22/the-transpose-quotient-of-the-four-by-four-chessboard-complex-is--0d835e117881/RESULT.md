# The transpose quotient of the four-by-four chessboard complex is a wedge of six two-spheres

## Finding
Let \(\Delta_{4,4}\) be the ordinary chessboard complex with vertices \((i,j)\), \(0\leq i,j<4\), in which a finite set of squares is a face precisely when no two squares share a row or a column. Let \(\tau(i,j)=(j,i)\), and take the **ordinary geometric orbit space** (not homotopy orbits). Then
\[
\boxed{|\Delta_{4,4}|/\langle\tau\rangle\simeq\bigvee^{6}S^2.}
\]
In particular the quotient is simply connected, its only positive-degree integral homology is \(H_2\cong\mathbb Z^6\), and there is no integral homology torsion.

## Assumptions and scope
Here \(\Delta_{4,4}\) is the matching complex of the complete bipartite graph \(K_{4,4}\); it is **not** the matching complex of the Cartesian four-by-four square grid. The involution interchanges the two vertex classes of \(K_{4,4}\), or equivalently inverts the partial permutation represented by a rook placement. All realizations are finite CW spaces. No assertion is made for larger boards or different involutions.

A *nonempty flag* means a strictly increasing chain \(\sigma_0\subsetneq\cdots\subsetneq\sigma_d\) of nonempty rook-placement faces. An orbit flag is a pair of such flags identified under simultaneous transposition of every face. Vertex ranks strictly increase along a flag, so no nontrivial group element reverses a flag simplex; its orbit has the usual signed boundary obtained by deleting a flag member. We use the resulting regular \(\Delta\)-complex/cellular model for the geometric quotient.

## Proof
**1. Finite quotient model.** Every rook placement of size \(k\) is uniquely specified by \(k\) distinct row labels and an ordered injection into the column labels. Exhaustively enumerating these faces gives counts
\[
(f_0,f_1,f_2,f_3)=(16,72,96,24).
\]
Barycentrically subdivide and identify flags by the involution. An exhaustive orbit enumeration, including all flags rather than just flags fixed pointwise, yields
\[
(c_0,c_1,c_2,c_3)=(125,586,768,300),\qquad \chi=125-586+768-300=7.
\]
In detail, represent each rook placement by a sixteen-bit subset mask, apply \(\tau\) by transposing the four-by-four bit array, and represent each orbit flag by the lexicographically smaller of the flag and its transpose. The full signed cellular boundary is obtained by deleting each flag member and canonicalizing the resulting orbit. The program `verify.py` performs the complete construction and checks the signed boundary compositions vanish.

**2. A two-dimensional deformation retract.** Number the orbit cells of each dimension by lexicographically sorted orbit flags, beginning at zero. The 300 pairs \((i,j)\) stored in `certificate.json` mean: delete the currently active two-cell with index \(i\) together with its unique active three-dimensional coface with index \(j\). For each pair, `verify.py` checks that the face appears with coefficient \(\pm1\) and occurs in **exactly one** remaining three-cell. It then removes the pair. This is a legal elementary cellular collapse, because the quotient flag model is regular and the selected two-cell is a free face. After all 300 certified collapses no three-cells remain and the two-dimensional deformation retract has
\[
(c_0',c_1',c_2')=(125,586,468),\qquad \chi=7.
\]
These statements are exact enumerations with an independently replayable list of all free-face pairs, rather than an inference from numerical homology alone.

**3. Trivial fundamental group.** The verifier independently applies van Kampen to the original quotient's two-skeleton. It constructs a spanning tree in the 125-vertex one-skeleton, leaving \(586-(125-1)=462\) generators. The 768 two-cell boundaries provide 768 signed triangular relators. In each of **462 deterministic Tietze eliminations**, a generator occurring exactly once in one relator is solved for, substituted into every other relator, and the defining relator and generator are discarded. Cyclic conjugation and free reduction are performed explicitly. The verifier checks the unique-occurrence hypothesis at each step and verifies that all surviving relators are the empty word after all 462 generators have disappeared. Hence
\[
\pi_1(|\Delta_{4,4}|/\langle\tau\rangle)=1.
\]
As an independent conceptual check, the theorem of Björner–Lovász–Vrećica–Živaljević states that \(\Delta_{m,n}\) is \((\nu-2)\)-connected for \(\nu=\min\{m,n,\lfloor(m+n+1)/3\rfloor\}\); for \(m=n=4\), this gives simple connectivity of the original space. Armstrong's orbit-space theorem then gives simple connectivity of the quotient because the involution fixes each diagonal-square vertex \((i,i)\).

**4. Integral homology and homotopy.** The resulting connected, simply connected two-dimensional finite CW complex \(Y\) has \(H_1(Y;\mathbb Z)=0\), no homology above degree two, and Euler characteristic seven. Its second homology is a subgroup of a free cellular chain group, hence free abelian, and therefore
\[
H_2(Y;\mathbb Z)\cong\mathbb Z^6.
\]
By Hurewicz, choose six two-sphere maps whose images form an integral basis of \(H_2(Y;\mathbb Z)\). The induced map \(\bigvee^6 S^2\to Y\) is an integral homology equivalence between simply connected CW complexes, hence a homotopy equivalence by the homological Whitehead theorem.

## Verification
Place `verify.py` and `certificate.json` in the same directory, then run `python3 verify.py` with the Python standard library. The verifier reconstructs every rook face and quotient orbit flag from definitions; checks their cardinalities; recomputes and verifies signed cellular boundary compositions; checks each of the 300 prescribed free-face collapses and final two-dimensional cell counts; constructs the exact fundamental-group presentation and replays all 462 Tietze elimination steps. Its terminal marker is `CHESSBOARD_TRANSPOSE_4X4_WEDGE6_OK`; it additionally prints all three cell-count vectors and the count of eliminated fundamental-group generators. No external saved tables, calculation logs or unstated dependencies are used. The cited connectivity/orbit theorem supplies an alternative proof of simple connectivity, not an indispensable computational assumption.

## Relationship to prior work
Björner, Lovász, Vrećica and Živaljević established the connectivity of ordinary chessboard complexes in 1994, which supplies a classical structural comparison but does not classify this geometric involution quotient. The fixed-point classification for symmetric rook boards shows that the **fixed locus** of this involution on the four-by-four board has homotopy type \(\bigvee^3 S^1\); this is not the **orbit space** calculated here. A published five-by-five result proves a **three-local** classification of that larger board's transpose quotient, not an integral four-by-four homotopy classification. Other known chessboard orbit results concern row/column actions, diagonal simultaneous label permutations, or different board dimensions. Neither numerical data for the original space nor the separate fixed-locus computation directly establishes the 300 collapses, trivial orbit fundamental group, and six-sphere wedge asserted here.

## Limitations
This is one geometrically distinguished finite board, not a uniform classification of transpose quotients in every size. The computer-assisted part of the proof is an exhaustive, exactly replayable finite construction; it does not claim broader asymptotic behavior or independent third-party validation. Publication priority remains conditional on the inspected literature and targeted searches: an equivalent unindexed or differently named calculation may exist. The conclusion identifies the ordinary geometric quotient, not its Borel construction or the fixed-point space.

## References
1. A. Björner, L. Lovász, S. T. Vrećica and R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society 49 (1994), 25–39, first published February 1, 1994; https://doi.org/10.1112/jlms/49.1.25 .
2. M. A. Armstrong, *On the fundamental group of an orbit space*, Proceedings of the Cambridge Philosophical Society 61 (1965), 639–646; https://doi.org/10.1017/S0305004100038974 .
3. *Perfect matchings classify transpose-fixed graph-board chessboard complexes*, public 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-perfect-matchings-classify-transpose-fixed-graph-board-chessboar--6329661ec23a .
4. *Three-local torsion cancellation in the transpose quotient of the five-by-five chessboard complex*, public 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-three-local-torsion-cancellation-in-the-transpose-quotient-of-th--62667cf31b8c .
