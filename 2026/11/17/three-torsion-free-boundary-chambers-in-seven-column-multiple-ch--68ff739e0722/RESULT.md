# Three torsion-free boundary chambers in seven-column multiple chessboard complexes

## Finding
Let \(\Delta_{[7]}^{\boldsymbol c}\) be the simplicial complex of rook placements in four labeled rows and seven labeled columns, with at most one rook per column and at most \(c_i\) rooks in row \(i\). For the three positive row-capacity vectors (up to row permutation)
\[
\boldsymbol c=(1,1,1,5),\quad (1,1,2,4),\quad (1,1,3,3),
\]
the **integral homotopy types** are, respectively,
\[
\Delta_{[7]}^{(1,1,1,5)}\simeq\bigvee^{15}S^5,\qquad
\Delta_{[7]}^{(1,1,2,4)}\simeq\bigvee^{57}S^5,\qquad
\Delta_{[7]}^{(1,1,3,3)}\simeq\bigvee^{57}S^5.
\]
Each complex is pure of dimension six but has nonzero fifth homology, and hence is not shellable. These three cases complete the previously unclassified positive four-row capacity patterns with total capacity eight on seven columns: the two other patterns are \((1,2,2,3)\) and \((2,2,2,2)\), treated separately in earlier work. The last pattern is distinguished by integral two-torsion, while the three types proved here are torsion-free.

## Assumptions and scope
Rows and columns are labeled; column capacities are all one, and each row capacity is positive. A face is an arbitrary subset of the 28 row-column squares obeying the constraints. The empty face is included in enumeration but excluded from the nonempty face-poset matching. The assertion concerns exactly the three specified capacity vectors, equivalently their permutations. The homotopy equivalence is an integral, nonequivariant statement. The relevant source was first publicly posted on October 27, 2026.

## Proof
Fix column-major order on the 28 board squares, with row varying fastest. Enumerate every face by processing the seven columns in order, and for each existing face either leave the next column empty or place one rook in any row below its capacity. At the end identify faces by their 28-bit characteristic masks. This gives, including the empty face, exactly 8,835, 15,933, and 18,873 faces for the three respective capacity vectors.

Construct a discrete-Morse matching by scanning the 28 squares in that fixed order. At each square \(v\), pair every still-unmatched nonempty face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), **only when** the latter is a legal, still-unmatched face. Each face is used at most once. For acyclicity orient every cover of the nonempty face-poset downward except paired covers, which point upward. A complete topological sort of every vertex and cover in the resulting directed Hasse diagram succeeds. The exhaustive counts are:

| Capacities | Nonempty face-poset covers | Matched pairs | Critical dimensions and multiplicities |
|---|---:|---:|---|
| \((1,1,1,5)\) | 40,544 | 4,406 | one in 0, three in 4, eighteen in 5 |
| \((1,1,2,4)\) | 76,958 | 7,901 | one in 0, one in 3, thirty-six in 4, ninety-two in 5 |
| \((1,1,3,3)\) | 92,848 | 9,312 | one in 0, two in 3, ninety-five in 4, one hundred fifty in 5 |

Obtain the exact integer Morse differentials using signed gradient paths. For each oriented \((k-1)\)-simplex \(\tau\), define its reduction \(F_k(\tau)\) in the free group on critical \((k-1)\)-simplices: a critical cell reduces to its own basis generator; an upper cell paired downward reduces to zero; if \(\tau\) is paired upward with \(\eta\), replace it by the signed negative sum of all other facets of \(\eta\), divided by its incidence coefficient \(\pm1\), and reduce recursively. The acyclic matching makes this recursion terminate. For each critical \(k\)-simplex, sum the reductions of its ordinary oriented facets to obtain its Morse boundary. This is the integral algebraic Morse boundary, not a field-only calculation.

For the first pattern, the Morse differential from critical dimension five to four is a \(3\times18\) integer matrix admitting **three** successive integer unit pivots. For the second, the differential from four to three is \(1\times36\) with **one** unit pivot, while the differential from five to four is \(36\times92\) with **35** unit pivots. For the third, the respective differentials are \(2\times95\) with **two** unit pivots and \(95\times150\) with **93** unit pivots. A unit pivot is an entry equal to \(1\) or \(-1\), with all subsequent row/column eliminations performed over the integers; no division by a nonunit is used. In each pattern, the exact chain-complex identity \(\partial_4\partial_5=0\) is checked.

These unit cancellations leave, in each case, only one zero-cell and respectively 15, 57, 57 critical five-cells. The Morse CW complexes have no cells in dimensions one or two, so the degree-one attachments in the relevant homotopy groups permit homotopy-preserving cancellation of the three/four-dimensional and four/five-dimensional cell pairs. The final five-cells attach to a point and thus give the asserted wedges of five-spheres. This proves integral homotopy types, not merely Euler characteristics or homology ranks.

Every legal face can be extended to seven rooks: a face of size at most six leaves an empty column and at least two unused units of row capacity (total row capacity eight), so a rook can be added. Thus every facet has seven rooks and dimension six. Nonzero homology in dimension five obstructs pure shellability.

## Verification
Run `python3 verify_chessboard.py` with Python 3 standard library. Its deterministic output is supplied in `verification_output.txt`. The program independently reconstructs all legal faces, builds the complete gradient matching, topologically sorts every directed face-poset cover, computes the signed integer Morse differentials, verifies their composition is zero, and performs integer-only unit-pivot elimination to recover all three sphere multiplicities. Counts, boundary dimensions, unit ranks, and final assertions are checked from the complete finite input, not sampled faces.

## Relationship to prior work
Limonchenko and Yu (arXiv:2610.37827v1, posted October 27, 2026) classify complexes with at most three rows and give a four-row torsion family \(\Delta_{[m]}^{(2,2,2,m-5)}\). Their Theorem 5.5 gives, at seven columns, \(\Sigma^3\mathbb{R}P^2\) together with free sphere summands for capacity \((2,2,2,2)\). Their other explicit four-row reduction for a row of capacity \(m\) or \(m-1\) does not cover the vectors here, whose largest capacities are five, four, and three. Their capacity-redistribution torsion criterion requires at least four row capacities at least two, which none of these three patterns has. Earlier computations address \((1,2,2,3)\) separately. Rational rank descriptions for general chessboard complexes do not by themselves establish the integral homotopy wedges proved here.

## Limitations
This is a complete exact finite calculation for three capacity patterns, not a theorem for all board sizes or all row capacities. The discrete-Morse proof establishes neither equivariant decompositions nor functorial naturality. It does not independently re-establish other existing cases, and no independent mathematical review has yet been performed. An unindexed equivalent earlier homotopy classification cannot be excluded absolutely.

## References
1. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827v1 (2026-10-27), https://arxiv.org/html/2610.37827v1; especially Theorems 1.1–1.3, 5.5, and Proposition 3.4.
2. V. Reiner and J. Roberts, work on Segre modules and generalized chessboard complexes, as cited in Limonchenko and Yu, reference [19]; rational and algebraic context only.
