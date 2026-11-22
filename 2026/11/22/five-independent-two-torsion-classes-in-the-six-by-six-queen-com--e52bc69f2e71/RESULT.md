# Five independent two-torsion classes in the six-by-six queen-complex symmetry quotient

## Finding
Let \(Q_6\) be the graph on the \(36\) squares of the ordinary (nonperiodic) \(6\times6\) chessboard, with two different squares adjacent exactly when queens placed there attack along a common row, column, or diagonal. Let \(K=\operatorname{Ind}(Q_6)\) be the abstract simplicial complex of all mutually nonattacking queen placements, including the empty placement. The geometric symmetries of the square act on \(K\) as the dihedral group \(D_4\) of order eight. For the **ordinary geometric orbit space** \(Y=|K|/D_4\), its complete reduced integral homology is
\[
\widetilde H_i(Y;\mathbb Z)\cong
\begin{cases}
(\mathbb Z/2\mathbb Z)^5,&i=2,\\
\mathbb Z,&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, \(Y\) is connected, has five independent order-two degree-two homology classes, and has exactly one free degree-three class. The geometric quotient creates more order-two classes than occur in the original complex, whose previously determined reduced degree-two integral homology has one \(\mathbb Z/2\mathbb Z\) summand.

## Assumptions and scope
Squares have coordinates \((r,c)\), with \(0\leq r,c\leq5\). Distinct squares attack when \(r=r'\), \(c=c'\), or \(|r-r'|=|c-c'|\). A placement is a subset of pairwise nonattacking squares. The group \(D_4\) consists of four rotations and four reflections of the square, acting simultaneously on all squares. The quotient is a quotient of geometric realizations, **not** the independence complex of an orbit graph, the quotient of the face poset by forgetting stabilizers, or a homotopy-orbit construction. There are no periodic edge identifications. The assertion is for this board and this full group only; it makes no claim about the fundamental group, full homotopy type, or other board sizes.

## Proof
Every nonempty face is enumerated uniquely by increasing square index \(6r+c\), extending a placement only by a square that attacks none of its selected squares. The number of faces of cardinalities \(1,\ldots,6\) is respectively
\[
(36,340,1024,982,248,4).
\]
There are no larger faces because at most one queen can occupy any row.

Take the barycentric subdivision, whose vertices are nonempty faces of \(K\) and whose simplices are nonempty strict inclusion chains (flags). The group preserves the cardinalities of the faces in a flag, so no nonidentity element can invert a flag simplex: every simplex stabilizer fixes its vertices separately. Moreover, the different facets of one flag have different missing cardinality sets and are not identified with one another in its group orbit. Thus flag orbits give an exact finite regular cellular model of \(Y\). Choose representatives by lexicographically minimizing the image of each whole flag over all eight group elements. Orient flags by increasing inclusion. Boundary coefficients are the usual alternating deletion signs, with each deleted flag reduced to its canonical group-orbit representative. This yields the following numbers of cells in dimensions \(0\) through \(5\):
\[
(337,3541,10110,11166,4620,360).
\]
The signed cellular differential squares to zero in every dimension, as checked by the exact verifier. The Euler characteristic is zero.

Remove a pair of cells only when the lower cell has precisely one surviving codimension-one coface, occurring once, and the upper cell is that coface. The checker makes \(11{,}550\) such genuine elementary collapses, leaving a subcomplex with cell counts \((227,1751,3290,1766)\) in dimensions \(0\) through \(3\). These are homotopy-preserving cellular collapses; they do not assume that an arbitrary unit boundary coefficient implies a free face.

For the remaining finite *integral cellular chain complex*, apply exact unit-pivot chain contractions (which preserve integral homology, not necessarily homotopy type). For a unit coefficient \(a=\pm1\) in row \(i\), column \(j\), modify each other boundary column \(k\) by subtracting \(\partial_{ik}a\) times column \(j\); remove basis cells \(i,j\) and their coordinates in adjacent differentials. The verifier implements these basis changes with full signed integers and executes respectively \(1760\), \(1525\), and \(226\) cancellations in degrees three, two, and one. Only one zero-cell, five two-cells, and six three-cells survive. The only nonzero differential is a \(5\times6\) matrix:
\[
\partial_3=2
\begin{pmatrix}
0&1&-1&0&0&0\\
0&0&1&0&0&0\\
0&0&0&-1&-1&0\\
-1&0&0&0&0&0\\
0&0&-1&0&1&-1
\end{pmatrix}.
\]
The first five columns of the displayed matrix **after dividing by two** have determinant \(-1\). Consequently its integral Smith invariants are exactly five copies of \(2\), and its rational rank is five. Its cokernel is \((\mathbb Z/2\mathbb Z)^5\), while its kernel is free of rank one. All other positive-dimensional differentials in the contracted chain complex vanish, establishing the homology assertion.

## Verification
Run `python3 verify_quotient.py` using a standard Python interpreter. This program reconstructs the face-poset quotient from the board coordinates, checks all cellular chain-square identities, verifies actual free-face conditions before collapses, replays every integer unit-pivot contraction, and checks the final matrix and unimodular minor; it emits `QUEENS6_D4_INTEGRAL_QUOTIENT_OK`. The independent `python3 check_burnside.py` instead enumerates placements by choosing occupied rows and injective columns, counts flags fixed by each individual square symmetry, and applies Burnside averaging. It emits `BURNSIDE_QUEENS6_D4_OK` and independently recovers all six quotient-cell counts. Both checks were executed successfully from their included program paths. No external data or downloaded mathematical files are required for the computations.

## Relationship to prior work
Chaiken, Hanusa, and Zaslavsky developed the classical enumerative theory of nonattacking riders and square-board queen configurations; counting placements does not determine the cellular topology of their geometric symmetry quotient. The published calculation *A Moore-space summand in the six-by-six queen-placement complex* determines \(K\simeq M(\mathbb Z/2,2)\vee\bigvee^{19}S^3\) and the rational dihedral degree-three character, so the **one-dimensional rational degree-three invariant is already known and is not claimed as new**. That character is consistent with the free \(\mathbb Z\) in \(H_3(Y;\mathbb Z)\), but it cannot determine the five integral order-two summands. The earlier five-by-five square-symmetry quotient calculation concerns a different original board with no such torsion group. The present claim is exactly the integral homology of the six-by-six full geometric quotient, not a claim to a novel homotopy classification of the original complex.

## Limitations
This is a complete finite computational proof for a specific natural quotient, without a general formula for arbitrary board sizes. Chain contractions on the final matrix establish homology only: no homotopy equivalence to a wedge of Moore spaces or spheres follows from the asserted computations. Searches and inspection of the named closest sources did not reveal a prior determination of these five torsion summands, but cannot exclude unindexed or privately circulated equivalent computations. No independent mathematical audit of this result has been performed.

## References
1. S. Chaiken, C. R. H. Hanusa, T. Zaslavsky, *A q-Queens Problem. I. General Theory*, first public version 2013-03-08, https://arxiv.org/abs/1303.1879.
2. S. Chaiken, C. R. H. Hanusa, T. Zaslavsky, *A q-Queens Problem. II. The Square Board*, first public version 2014-02-20, https://arxiv.org/abs/1402.4880.
3. *A Moore-space summand in the six-by-six queen-placement complex*, publicly available 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-moore-space-summand-in-the-six-by-six-queen-placement-complex--709883c6625b. Cited exclusively for the previously established unquotiented homology and rational symmetry action.
