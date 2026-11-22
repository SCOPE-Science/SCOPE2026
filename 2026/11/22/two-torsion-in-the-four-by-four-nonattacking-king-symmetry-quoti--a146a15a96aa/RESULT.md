# Two-torsion in the four-by-four nonattacking-king symmetry quotient

## Finding

Let \(K\) be the simplicial complex of all nonattacking placements of kings on an ordinary \(4\times4\) board. The eight elements of the square-dihedral group \(D_4\) act by rotating and reflecting board coordinates. Let \(Y=|K|/D_4\) denote the **ordinary geometric orbit space**, rather than a Borel construction or an orbit set of faces. Then

\[
\widetilde H_i(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z, & i=2,\\
0, & i\ne2.
\end{cases}
\]

In particular \(Y\) is connected, its integral first and third homology vanish, and its second integral homology is a single group of order two. No assertion about \(\pi_1(Y)\) or its complete homotopy type is made.

## Assumptions and scope

Index the board squares by \((r,c)\in\{0,1,2,3\}^2\). Two squares attack one another exactly when they are distinct and \(\max(|r-r'|,|c-c'|)=1\). The complex \(K\) has one vertex per square and a simplex for every set of pairwise nonattacking squares. It is finite, of dimension three, and has nonempty face numbers \((16,78,140,79)\). The group \(D_4\) has order eight and consists of ordinary rigid rotations/reflections. Homology is ordinary reduced singular homology with integral coefficients, equivalently the simplicial homology of the quotient of the barycentric subdivision.

## Proof

First enumerate all \(313\) nonempty faces by recursively choosing or omitting each of the \(16\) board squares, excluding choices that attack a previously chosen square. The enumeration returns the stated face counts.

Barycentrically subdivide \(K\). Each new simplex is a nonempty chain of strict face inclusions. Every group element sends such a chain to a chain and preserves each vertex's face cardinality. Thus it cannot permute the vertices of a simplex nontrivially, so the ordinary quotient of this subdivision is a regular \(\Delta\)-complex; its cells are exactly the \(D_4\)-orbits of these chains. Order each chain by increasing cardinality. Each oriented face deletion has sign \((-1)^j\), and faces in the same orbit are identified with no extra orientation sign because cardinalities are preserved.

Exhaustive enumeration of all chains, canonicalization under the eight symmetries, and an independent Burnside fixed-chain count give quotient cell numbers
\[
(c_0,c_1,c_2,c_3)=(50,283,471,237).
\]
The signed boundary columns satisfy \(\partial_1\circ\partial_2=0\) and \(\partial_2\circ\partial_3=0\). Explicit integer row/column elimination by \(\pm1\)-pivots gives \(49\) units for \(\partial_1\), \(234\) for \(\partial_2\), and \(236\) for \(\partial_3\), with zero residual for the first two. For \(\partial_3\), one column remains, whose nonzero entries have greatest common divisor exactly \(2\); its Smith normal form therefore has \(236\) unit factors followed by a single factor \(2\). All pivot steps are unimodular and preserve the Smith invariants. The boundary ranks are respectively \(49,234,237\).

The chain dimensions then give \(H_0(Y;\mathbb Z)\cong\mathbb Z\), zero free homology in all positive degrees, and one torsion summand \(\mathbb Z/2\mathbb Z\) in degree two arising from the final Smith factor of \(\partial_3\). No other torsion is possible because all other nonzero Smith factors are units. Since the quotient is three-dimensional, there are no higher homology groups. Its Euler characteristic equals \(50-283+471-237=1\), independently consistent with the result.

## Verification

Run the included standalone `verify_king4_d4.py` using Python 3; it requires no external packages. It enumerates each ordinary face and barycentric flag, verifies all eight group elements, checks the flag-orbit count against Burnside's lemma, constructs both signed boundary compositions and verifies they vanish, and performs explicit integral unimodular eliminations. Independent finite-field elimination checks the ranks in characteristics two and three: degree-three boundary ranks are \(236\) and \(237\), respectively. The output terminates with `KING4_D4_QUOTIENT_INTEGRAL_HOMOLOGY_OK`.

## Relationship to prior work

Calkin and collaborators studied enumeration of nonattacking king configurations on chessboards, supplying the canonical placement problem; its inspected abstract and introduction do not state an integral orbit-space homology claim. The earlier complete integral homology computation for the *unquotiented* nonattacking-king complexes through size six establishes torsion-freeness of the underlying complexes, but does not imply the integral homology of their geometric symmetry quotients. Earlier rational representations on the \(5\times5\) king complex concern a different board and cannot detect this \(2\)-torsion. Other small dihedral chessboard quotients use different attack graphs. The present claim is specifically about the \(4\times4\) **king** attack relation and the full dihedral geometric quotient.

## Limitations

This is a finite computer-assisted integral homology theorem. The included complete algorithm supplies a reproducible exact calculation, not an independent mathematical audit. It does not establish simple connectivity, an exact Moore-space homotopy type, a formula for general board sizes, or priority over any unindexed equivalent calculation. Using integer Smith factors is essential: rational homology alone is acyclic here.

## References

- N. J. Calkin, K. James, S. Purvis, S. Race, K. Schneider and M. Yancey, *Counting kings: explicit formulas, recurrence relations, and generating functions! Oh my!*, Congr. Numer. 182 (2006), 41–51. Public full text: https://www.researchgate.net/publication/239804979_Counting_Kings_Explicit_Formulas_Recurrence_Relations_and_Generating_Functions_Oh_My (visible upload date 20 May 2014).
- Prior integral calculation of king-configuration complexes through size six: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-integral-homology-of-the-first-six-king-configuration-complexes--4f5da28787e8 .
- Prior rational dihedral character on the distinct five-by-five board: https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-full-dihedral-homology-character-of-five-by-five-nonattackin--4bd13ce494df .
