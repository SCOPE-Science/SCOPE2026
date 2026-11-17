# Integral homotopy of the three pre-stable alternating-row chessboard quotients

## Finding

Let \(\Delta_{4,n}\) be the simplicial complex of nonattacking rook placements on a board with four labeled rows and \(n\) labeled columns. Let \(A_4\) act by even permutations of the four row labels, fixing columns. For the ordinary geometric quotient \(Q_n=|\Delta_{4,n}|/A_4\), the complete homotopy types in the three widths \(n\in\{4,5,6\}\) are
\[
Q_4\simeq\bigvee^{3}S^2,\qquad
Q_5\simeq\left(\bigvee^{5}S^2\right)\vee S^3,
\]
\[
Q_6\simeq\left(\bigvee^{5}S^2\right)\vee M(\mathbb Z/3,2)\vee\left(\bigvee^{5}S^3\right).
\]
Here \(M(\mathbb Z/3,2)\) is the mapping cone of a degree-three map \(S^2\to S^2\). Thus the final pre-stable width has both free second homology and nontrivial order-three second homology:
\[
H_2(Q_6;\mathbb Z)\cong\mathbb Z^5\oplus\mathbb Z/3,\qquad H_3(Q_6;\mathbb Z)\cong\mathbb Z^5.
\]
All three spaces are simply connected, and their other reduced homology groups vanish. These are classifications of the **ordinary orbit spaces**, not the homotopy orbit spaces.

## Assumptions and scope

There are four rows; \(n\) is exactly one of \(4,5,6\). A face is a set of rooks occupying distinct rows and columns, each listed in ascending column order. Group elements act only on row labels, with no permutation of columns. The action has no inversions: a group element stabilizing a face setwise must fix each of its vertices because the columns in that face are distinct. Hence a cell orbit is a well-defined oriented cell of the ordinary quotient, with the usual signed simplicial boundary projected to cell orbits.

## Proof

**Orbit presentation.** For every \(n\ge4\), there is one zero-cell for each column and one one-cell for each unordered pair of columns because \(A_4\) is transitive on rows and on ordered pairs of distinct rows. There are two cells \(t_I^+\) and \(t_I^-\) over every three-element column set \(I\), and two cells \(u_J^+\), \(u_J^-\) over every four-element set \(J\): complete a row triple by its unique missing row, placing it last, and take the parity of the resulting permutation; a four-rook placement has the usual permutation parity. Thus the cellular ranks, in dimensions zero through three, are
\[
\left(n,\binom n2,2\binom n3,2\binom n4\right).
\]
For increasing column lists, the complete integer differential is
\[
\partial_1 e_{ij}=v_j-v_i,\quad
\partial_2t_{ijk}^{\epsilon}=e_{jk}-e_{ik}+e_{ij},
\]
\[
\partial_3u_{ijkl}^{\epsilon}=
 t_{jkl}^{-\epsilon}-t_{ikl}^{\epsilon}+t_{ijl}^{-\epsilon}-t_{ijk}^{\epsilon},
\qquad \epsilon\in\{+,-\}.
\]
The last formula follows because deleting the row in position \(a\), indexed from zero, changes the parity of the completed four-row permutation by \((-1)^{3-a}\). This explicit presentation also holds for larger widths, but no additional integral homology classification is asserted here.

**Simply connected.** The one-skeleton is the complete graph on the column labels. Every three-column cycle is attached as the boundary of \(t_{ijk}^+\), and these triangular cycles normally generate the fundamental group of the complete graph. Therefore \(\pi_1(Q_n)=1\), including at all three stated widths.

**Exact integer computation.** Substituting the column sets of cardinalities one through four into the displayed differential produces the following complete chain matrices and Smith forms. \(1^r\) means \(r\) unit diagonal factors; all omitted factors are zero.

| \(n\) | Cell counts \((c_0,c_1,c_2,c_3)\) | Smith form of \(\partial_1\) | Smith form of \(\partial_2\) | Smith form of \(\partial_3\) |
|---|---|---|---|---|
| 4 | \((4,6,8,2)\) | \(1^3\) | \(1^3\) | \(1^2\) |
| 5 | \((5,10,20,10)\) | \(1^4\) | \(1^6\) | \(1^9\) |
| 6 | \((6,15,40,30)\) | \(1^5\) | \(1^{10}\) | \(1^{24},3\) |

The explicit integer matrices are generated and reduced by the standalone program `verify.py`. Its second, separately constructed set of matrices enumerates all ordered row injections and the \(12\) even permutations rather than using the parity incidence formula. Both constructions have the displayed forms and satisfy \(\partial_1\partial_2=\partial_2\partial_3=0\). Since image and kernel of successive boundaries are integral sublattices and the previous differentials have only unit Smith factors, these forms give \(\widetilde H_2(Q_4)=\mathbb Z^3\); \(\widetilde H_2(Q_5)=\mathbb Z^5\), \(\widetilde H_3(Q_5)=\mathbb Z\); and \(\widetilde H_2(Q_6)=\mathbb Z^5\oplus\mathbb Z/3\), \(\widetilde H_3(Q_6)=\mathbb Z^5\). There are no other positive-degree homology groups.

**Homotopy type.** Each \(Q_n\) is a simply connected CW complex of dimension three. Its two-skeleton, also simply connected, is homotopy equivalent to a wedge of two-spheres by the Hurewicz and Whitehead theorems. The three-cell attaching maps are then elements of the free group \(\pi_2\) of that wedge. Elementary basis changes of these two- and three-cells reduce the attaching-map integer matrix to Smith normal form. Unit columns cancel, an integer factor \(3\) gives the Moore summand, and zero columns give free two- and three-sphere summands. The homotopy equivalences displayed in the finding follow. This reduction uses the fact that a three-cell attaches to the two-skeleton via \(\pi_2\), not merely the homological ranks.

## Verification

Run `python verify.py` with the exact dependency `sympy==1.14.0` from `requirements.txt`. The program independently constructs orbit boundary matrices by two descriptions, checks both cellular chain identities, and computes integer Smith forms using integer arithmetic. Its complete deterministic output is `verification_output.txt`. The domain is exhausted because the program generates every column subset of sizes one through four and every allowed ordered injection of rows; no sampling is involved. The table and homotopy deduction are valid only for the three stated finite widths. No inference from computational checking to infinitely many widths is made.

## Relationship to prior work

Björner, Lovász, Vrećica and Živaljević established the classical chessboard-complex framework and connectivity bounds (1994). Shareshian and Wachs studied integral torsion and symmetric-group representations of the **unquotiented** chessboard complex (first preprint 2004). Both results concern the original complex and do not supply the integral orbit-cell boundaries above; taking rational representation invariants cannot detect the quotient's order-three torsion. The later generalized-chessboard classification by Limonchenko and Yu likewise concerns ordinary/multiple chessboard spaces rather than this even-row orbit quotient. The present classification is deliberately restricted to the natural pre-stable row-four widths, just before the Cohen–Macaulay/shellability range begins at seven columns.

## Limitations

There is no claim of novelty for classical chessboard-complex connectivity, nor any asserted uniform homology theorem for arbitrarily many columns. Published and unindexed equivalent quotient calculations may exist; independent comparison and audit have not been performed. The exact computations rely on the stated deterministic integer algorithms and require the specified Python dependency. The result concerns the ordinary topological quotient and cannot be transferred automatically to homotopy quotients or equivariant cohomology.

## References

1. A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society **49** (1994), 25–39; first published 1994-02-01, DOI: https://doi.org/10.1112/jlms/49.1.25 . Author-uploaded full text: https://www.researchgate.net/publication/245653497_Chessboard_Complexes_and_Matching_Complexes .
2. J. Shareshian, M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, first public preprint 2004-09-03, https://arxiv.org/abs/math/0409054 .
3. I. Limonchenko, S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, first public 2026-10-27, https://arxiv.org/abs/2610.37827 . This is comparison literature, not the dated historical basis.
