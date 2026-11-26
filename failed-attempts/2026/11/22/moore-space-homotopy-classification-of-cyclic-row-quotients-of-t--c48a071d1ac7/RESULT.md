# Moore-space homotopy classification of cyclic-row quotients of three-row chessboard complexes

## Finding

For every integer \(n\ge5\), consider the simplicial complex \(\Delta_{3,n}\) of nonattacking rook placements on three labeled rows and \(n\) labeled columns. The cyclic order-three group rotates the rows, leaving the columns fixed. Its ordinary geometric quotient \(Q_n=|\Delta_{3,n}|/C_3\) has homotopy type

\[
Q_n\simeq M(\mathbb Z/3,1)\vee\bigvee^{\beta_n}S^2,\qquad
\beta_n=\frac{n(n-2)(n-4)}3-1,
\]

where \(M(\mathbb Z/3,1)=S^1\cup_{3}e^2\) denotes the Moore complex obtained from a circle by a degree-three two-cell. In particular the sphere counts at widths \(n=5,6,7\) are \(4,15,34\), respectively.

## Assumptions and scope

Rows are \(\mathbb Z/3\) and columns are the ordered set \(\{0,1,\ldots,n-1\}\). A simplex is a set of board squares containing at most one square in each row and column. The group \(C_3\) adds the same element of \(\mathbb Z/3\) to each occupied row. It acts freely on the realization: no nonempty face is setwise preserved by a nonidentity row rotation, because each occupied column has one rook. The quotient therefore inherits an ordinary two-dimensional \(\Delta\)-CW decomposition from the orbits of the simplices, with no simplex self-identification. The theorem concerns geometric orbit spaces, not geometric fixed spaces or homotopy orbits. Only \(n\ge5\) is asserted.

## Proof

**Step 1: exact quotient cells and attaching words.** There is a quotient vertex \(v_i\) for each column \(i\). For every \(i<j\) there are two oriented edge orbits \(e^+_{ij}\) and \(e^-_{ij}\), distinguished by row differences \(+1\) and \(-1\) modulo three, each directed \(v_i\to v_j\). For every triple \(i<j<k\) there are exactly two triangle orbits, represented by row assignments \((0,1,2)\) and \((0,2,1)\). With orientations induced by the increasing column order, their boundary words in the one-skeleton are

\[
T^+_{ijk}:\ e^+_{ij}e^+_{jk}(e^-_{ik})^{-1},\qquad
T^-_{ijk}:\ e^-_{ij}e^-_{jk}(e^+_{ik})^{-1}.
\]

These words retain the nonabelian attaching information, rather than merely cellular boundary coefficients. The quotient has exactly \(n\) vertices, \(2\binom n2\) edges, and \(2\binom n3\) two-cells.

**Step 2: eliminate the ordinary one-skeleton.** The edges \(e^+_{0j}\), for \(1\le j\le n-1\), form a spanning tree and can be contracted. Set \(x_j=e^-_{0j}\) for the remaining distinguished loops. For each \(0<i<j\), the two triangle boundary words with first column zero respectively contain the edge generators \(e^+_{ij}\) and \(e^-_{ij}\) exactly once; hence they can be eliminated by homotopy-preserving one-cell/two-cell moves. Their relations become

\[
e^+_{ij}=x_j,\qquad e^-_{ij}=x_i^{-1}.
\]

Thus the reduced CW complex has one zero-cell, \(n-1\) one-cells \(x_1,\ldots,x_{n-1}\), and for each \(1\le i<j<k\le n-1\) exactly two remaining two-cells with attaching words

\[
a_{ijk}=x_jx_kx_i,\qquad b_{ijk}=x_i^{-1}x_j^{-1}x_k^{-1}.
\]

**Step 3: cancel all but one generator, uniformly in \(n\).** Because \(n\ge5\), the indices \(1,2,3,4\) exist. The relation \(a_{123}\) eliminates \(x_1\), giving \(x_1=x_3^{-1}x_2^{-1}\). The relation \(a_{124}\) then eliminates \(x_4\), giving \(x_4=x_3\). The relation \(a_{134}\) eliminates \(x_2\), giving \(x_2=x_3\). For each \(t=5,\ldots,n-1\), the relation \(a_{12t}\) eliminates \(x_t\), giving \(x_t=x_3\). Each chosen two-cell contains its eliminated generator once at the moment of elimination; these are valid cellular Tietze eliminations (equivalently one/two-cell slides followed by elementary cancellations). Writing \(x=x_3\), we obtain

\[
x_1=x^{-2},\qquad x_2=x_3=\cdots=x_{n-1}=x.
\]

All remaining words involving index \(1\) are freely trivial after these substitutions. Every remaining triple with indices at least \(2\) has attaching word \(x^3\) or \(x^{-3}\). Since the triple \((2,3,4)\) exists, at least one such degree-three attachment remains. Select one to form \(M(\mathbb Z/3,1)\). All further degree-three attachments are nullhomotopic in this Moore complex (and the freely trivial attachments already are), so they split off two-spheres. Indeed attaching maps of two-cells are homotopy classes of loops; a degree-three loop is nullhomotopic after the first Moore attachment.

**Step 4: count spheres exactly.** The reduced presentation initially has \(2\binom{n-1}{3}\) two-cells, and the described cancellations remove exactly \(n-2\) of them, leaving one Moore two-cell and

\[
\beta_n=2\binom{n-1}{3}-(n-2)-1=\frac{n(n-2)(n-4)}3-1
\]

trivially attached two-cells. This proves the asserted complete homotopy equivalence for every integer \(n\ge5\).

## Verification

The accompanying standard-library program `verify.py` independently reconstructs the quotient cell orbits, checks every triangle's signed cellular boundary and that its boundary is a cycle, replays the specified generator eliminations on free-group words, and checks the sphere counts and Euler characteristic for each \(3\le n\le11\). The delivered program prints `VERIFY_OK` upon success. These finite checks supplement, but do not replace, the uniform symbolic proof above.

## Relationship to prior work

The foundational 1994 chessboard-complex work establishes connectivity and small-board properties of the *unquotiented* complexes. Later work develops equivariant uses of chessboard complexes in colored Tverberg theory. Recent complete classifications for generalized chessboard complexes with at most three rows likewise concern the unquotiented spaces, not their cyclic-row geometric orbit spaces. Previously established calculations of the cyclic-row orbit spaces determine their fundamental groups and integral homology; the present result upgrades those invariants to a full explicit nonabelian attaching-map and homotopy decomposition. The latter does not follow from those invariants alone for a non-simply-connected two-complex.

## Limitations

The theorem is confined to the geometric quotient by the row-rotation subgroup \(C_3\), with \(n\ge5\). It does not extend to other permutation groups, larger row counts, equivariant stable homotopy, or homotopy orbit spaces. The proof is mathematical and finite combinatorial; no independent external mathematical audit has been performed. Non-indexed equivalent publications may exist despite the literature comparisons.

## References

1. A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard complexes and matching complexes*, Journal of the London Mathematical Society 49 (1994), 25–39, https://doi.org/10.1112/jlms/49.1.25.
2. S. T. Vrećica and R. T. Živaljević, *Chessboard complexes indomitable* (2009 preprint), https://arxiv.org/abs/0911.3512.
3. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827 (2026), https://arxiv.org/abs/2610.37827.
