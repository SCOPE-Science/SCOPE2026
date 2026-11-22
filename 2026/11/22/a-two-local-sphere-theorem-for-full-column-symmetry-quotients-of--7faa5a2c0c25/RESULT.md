# A two-local sphere theorem for full column-symmetry quotients of three-row two-matching complexes

## Finding
For every integer \(n\ge4\), let \(X_n=M_2(K_{3,n})\) be the simplicial complex on the \(3n\) edges of a complete bipartite graph, in which a face uses at most two edges incident to every vertex. The symmetric group \(\mathfrak S_n\) acts by permuting the columns. Write \(Q_n=|X_n|/\mathfrak S_n\) for the *geometric* orbit space, and write \((-)_{(2)}\) for localization of a simply connected space at the prime two. Then

\[
\boxed{(Q_n)_{(2)}\simeq (S^5)_{(2)}\quad\text{for every }n\ge4.}
\]

More explicitly, \(Q_n\) is simply connected and has \(H_*(Q_n;\mathbb F_2)\cong H_*(S^5;\mathbb F_2)\). Its integral fifth homology is \(\mathbb Z\), and no integral homology group has nonzero two-primary torsion. The canonical barycentric orbit-cell models of \(Q_n\) are identical for every \(n\ge6\); hence those orbit spaces are canonically PL-homeomorphic via the cell models. No claim is made that the *integral* homotopy type is a sphere.

## Assumptions and scope
The complex is the bounded-degree **edge-set** complex \(M_2(K_{3,n})\), not the ordinary matching complex or the complex forbidding a three-edge matching. Each of the three row vertices has capacity two and each of the \(n\) column vertices has capacity two. The group acts on columns alone. The orbit space is the quotient of the geometric realization, not the abstract complex formed by identifying vertices of the same orbit. All reduced homology is taken with the indicated coefficients; two-local homotopy equivalence need not be an integral equivalence.

## Proof
**1. Connectivity and simple connectivity of the quotient.** The generalized chessboard connectivity theorem of Jojić–Panina–Vrećica–Živaljević (Theorem 6.1 of the cited paper) gives \((\sum k_i-2)\)-connectivity if \(\sum l_j\ge\sum k_i+3-1\). Here the three row capacities are \(k_i=2\) and the column capacities are \(l_j=2\), so \(2n\ge8\) for \(n\ge4\) and \(X_n\) is four-connected. Under the finite \(\mathfrak S_n\) action, every transposition fixes a nonempty geometric point (indeed, an original vertex in a column outside its swapped pair). Transpositions generate \(\mathfrak S_n\). Armstrong's theorem on the fundamental group of a finite-group orbit space of a simply connected polyhedron therefore gives \(\pi_1(Q_n)=1\).

**2. A complete quotient cellular model.** Take the barycentric subdivision of \(X_n\). Its vertices are the nonempty faces of \(X_n\), and its simplices are strictly nested flags \(F_1\subset\cdots\subset F_k\). The \(\mathfrak S_n\) action never reverses a flag simplex, since the cardinality of its \(j\)-th face distinguishes every vertex. Its quotient is therefore a finite regular cell model whose \((k-1)\)-cells correspond exactly to flag orbits.

To specify a flag orbit, assign to each occupied cell \((r,c)\) the tag \((r,t)\), where \(t\in\{1,\ldots,k\}\) is the first flag stage containing the cell. Each occupied column gives a type consisting of one or two distinct-row tags. The whole orbit is uniquely represented by the sorted multiset of nonempty column types subject to each row occurring at most twice and all \(k\) stages occurring. Two flags have the same type multiset if and only if they differ by a permutation of the column labels. To delete the \(j\)-th flag face, if \(j<k\) merge birth stages \(j,j+1\) and decrement higher stages; if \(j=k\), discard the cells born at stage \(k\). Remove resulting empty columns and sort. Over \(\mathbb F_2\), the quotient cellular differential is the sum of these \(k\) face operations, one per flag position. This description explicitly includes all possible stabilizers; it does not assume a free group action.

**3. Finite exact computation and uniform reduction.** The attached dependency-free `verify.py` enumerates *all* flag orbits with these rules, constructs the quotient cellular boundaries, verifies their successive compositions vanish, and computes their exact binary ranks. Its results are:

| \(n\) | Cell numbers in dimensions \(0,\ldots,5\) | Boundary ranks from dimensions \(1,\ldots,5\) |
|---|---|---|
| 4 | 77, 1160, 5577, 11334, 10260, 3420 | 76, 1084, 4493, 6841, 3419 |
| 5 | 83, 1346, 6783, 14250, 13230, 4500 | 82, 1264, 5519, 8731, 4499 |
| 6 | 84, 1371, 6921, 14544, 13500, 4590 | 83, 1288, 5633, 8911, 4589 |

Consequently, in each case the quotient has one zero-dimensional mod-two class, one fifth-dimensional class, and no others. Every face of \(X_n\) has at most six cells, hence uses at most six occupied columns. Therefore all column-type multisets and every flag incidence relation stabilize exactly once \(n\ge6\). The model for \(n=6\) consequently proves the same mod-two result for **every** larger \(n\), not merely a finite tested range. The same isomorphism of barycentric quotient cell models gives the asserted PL homeomorphism across these widths.

**4. Two-local homotopy conclusion.** The quotient is a finite simply connected CW complex of dimension five. Its mod-two homology is that of \(S^5\), so its homology with \(\mathbb Z_{(2)}\) coefficients is also that of \(S^5\): the universal coefficient theorem and finite generation remove all two-primary torsion and all lower two-local free homology. In top dimension its integral group is free (a subgroup of its cellular five-chains), hence \(H_5(Q_n;\mathbb Z)\cong\mathbb Z\). The localized Hurewicz theorem supplies a class in \(\pi_5((Q_n)_{(2)})\) mapping to the generator of \(H_5(-;\mathbb Z_{(2)})\). The induced map from the two-local five-sphere is a two-local homology equivalence and, by the simply connected localized Whitehead theorem, a homotopy equivalence. This proves the finding.

## Verification
Run `python3 verify.py` in the same directory as this document. The program has no external package dependencies and exhaustively enumerates the orbit flags at widths four, five and six. Its exact \(\mathbb F_2\)-boundary ranks, face counts, boundary-square tests, and saturation checks are recorded in `verification_output.txt`. This is a finite exhaustive *proof component*: the preceding combinatorial stabilization argument is what extends it to all widths. The calculation does not determine odd-primary integral torsion or the global integral homotopy type.

## Relationship to prior work
The generalized chessboard connectivity bound is due to Jojić et al. Reiner–Roberts and subsequent papers determine rational representation or nonequivariant homotopy information for multiple chessboard complexes; rational representation formulas alone do not determine the mod-two homology of a geometric quotient with stabilizers. An existing analysis of *cyclic* column quotients of this exact three-row two-matching family exhibits torsion in odd-width cyclic quotients, but its group is \(C_n\), not \(\mathfrak S_n\), and does not imply the present two-local full-symmetric quotient theorem. The 2026 three-row homotopy classification concerns the covering complexes, not their full column-symmetry orbit spaces. The contribution here is the exact mod-two quotient-chain computation coupled with a sharp finite-cell stabilization and the corresponding two-local homotopy classification.

## Limitations
The conclusion is **two-local**, not integral. Possible odd-primary homology torsion, integral homotopy type, and finer group actions on other invariants are not determined. The canonical cell stabilization at six occupied columns does not assert that widths four and five have different underlying homeomorphism types. This statement does not claim new connectivity, a new nonequivariant wedge-of-spheres theorem, or a new rational representation decomposition. As with any literature comparison, unindexed equivalent results remain a bibliographic risk.

## References
1. D. Jojić, G. Panina, S. T. Vrećica, R. T. Živaljević, *Generalized chessboard complexes and discrete Morse theory*, first arXiv posting 2020-03-09, arXiv:2003.04018, Theorem 6.1, https://arxiv.org/abs/2003.04018.
2. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, first posted 2026-10-27, arXiv:2610.37827, https://arxiv.org/abs/2610.37827.
3. V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, J. Algebraic Combin. 11 (2000), Theorem 3.3, https://www-users.cse.umn.edu/~rober005/chessmatch.pdf.
4. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Proc. Cambridge Philos. Soc. 64 (1968), 299–301, https://doi.org/10.1017/S0305004100042845.
5. *Cyclic quotient torsion and the parity threshold for three-row two-matching complexes*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-cyclic-quotient-torsion-and-the-parity-threshold-for-three-row-t--e5952a573c96.
