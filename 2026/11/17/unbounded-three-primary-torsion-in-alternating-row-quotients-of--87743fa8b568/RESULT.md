# Unbounded three-primary torsion in alternating-row quotients of four-row chessboard complexes

## Finding
For every integer \(n\ge7\), let \(Q_n=|\Delta_{4,n}|/A_4\), where \(A_4\) acts by even row permutations and leaves the \(n\) column labels fixed. For the **ordinary geometric quotient**, not a homotopy quotient,
\[
\pi_1(Q_n)=1,\qquad H_2(Q_n;\mathbb Z)\cong\mathbb Z/6\mathbb Z\oplus(\mathbb Z/3\mathbb Z)^{n-2},
\]
and
\[
H_0(Q_n;\mathbb Z)\cong\mathbb Z,\quad H_1(Q_n;\mathbb Z)=0,\quad
H_3(Q_n;\mathbb Z)\cong\mathbb Z^{r_n},\quad H_j(Q_n;\mathbb Z)=0\ (j\ge4),
\]
where \(r_n=1-n+\binom n2-2\binom n3+2\binom n4\). Thus the three-primary torsion rank is exactly \(n-1\) for every \(n\ge7\). This determines integral homology, **not** a full homotopy decomposition.

## Assumptions and scope
The simplicial complex \(\Delta_{4,n}\) has vertices \((r,c)\) with \(r\in\{1,2,3,4\}\), \(c\in\{0,\dots,n-1\}\). A face is a set of such vertices with pairwise distinct rows and columns. \(A_4\) permutes row labels, leaving all columns fixed. Quotient cells are the orbits of **open** simplices with increasing column order; the stabilizer of a face acts trivially on its vertices, because each occupied column has precisely one rook. Therefore the orbit space has an honest regular-orbit cellular chain model and no orientation-twisting identification of a face with itself.

## Proof
Write column indices \(0,1,\ldots,n-1\). The alternating group is transitive on ordered injections of one or two rows; its ordered injections of three or four rows have exactly two orbits distinguished by the parity of the unique completion to a permutation of four rows. Thus the quotient has cell counts
\[
(c_0,c_1,c_2,c_3)=\left(n,\binom n2,2\binom n3,2\binom n4\right).
\]
Its one-skeleton is the complete graph on the columns. Each of the two triangular cells over \(a<b<c\) has precisely the same oriented boundary \([b,c]-[a,c]+[a,b]\). Hence the quotient's two-skeleton contains the usual two-skeleton of the simplex on its column set. In particular \(\pi_1(Q_n)=1\), and the cellular first homology vanishes.

Let \(T^+_{abc}\) and \(T^-_{abc}\) denote the two triangle orbits, with their orientations induced by increasing columns, and put \(\delta_{abc}=T^-_{abc}-T^+_{abc}\). For each \(0<i<j<k\), let
\[
w_{0ijk}=T^+_{ijk}-T^+_{0jk}+T^+_{0ik}-T^+_{0ij}.
\]
The cycles \(\delta_{abc}\), for all triples, together with \(w_{0ijk}\), for triples avoiding column zero, form an **integral basis** of \(\ker\partial_2\). This follows because the positive triangles comprise a copy of the full simplex two-skeleton, whose cycle lattice has the displayed standard basis of tetrahedral boundaries, and the negative-positive differences are independent free summands.

For every \(a<b<c<d\), let \(F^+_{abcd}\) and \(F^-_{abcd}\) be the two oriented three-cell orbits. In the above cycle lattice, direct deletion of each rook gives
\[
\partial_3F^+_{abcd}=w_{abcd}+\delta_{bcd}+\delta_{abd},\qquad
\partial_3F^-_{abcd}=w_{abcd}-\delta_{acd}-\delta_{abc},
\]
where \(w_{abcd}=T^+_{bcd}-T^+_{acd}+T^+_{abd}-T^+_{abc}\), equal to \(w_{0bcd}\) if \(a=0\), and to \(w_{0bcd}-w_{0acd}+w_{0abd}-w_{0abc}\) otherwise.

Set \(z_{ij}=\delta_{0ij}\) for \(1\le i<j\le n-1\). The relations for \(0<b<c<d\) eliminate both other kinds of generators integrally, without division:
\[
w_{0bcd}=z_{bc}+z_{cd},\qquad
\delta_{bcd}=-(z_{bc}+z_{bd}+z_{cd}).
\]
For a four-subset \(a<b<c<d\) of \(\{1,\dots,n-1\}\), each remaining three-cell relation reduces, up to sign, to the **same single relation**
\[
z_{ab}+z_{ac}+z_{ad}+z_{bc}+z_{bd}+z_{cd}=0.
\]
Consequently
\[
H_2(Q_n;\mathbb Z)\cong\operatorname{coker}\left(W_{2,4}(n-1):\mathbb Z^{\binom{n-1}4}\longrightarrow\mathbb Z^{\binom{n-1}2}\right),
\]
where \(W_{2,4}(v)\) has entry one if its indexed two-subset lies inside its indexed four-subset, zero otherwise. These are exact integer-presentation transformations, not just rational equivalences.

For \(v=n-1\ge6\), Wilson's inclusion-matrix diagonal-form theorem, as proved in Ghorbani–Khosrovshahi–Maysoori–Mohammad-Noori (2007, Corollary 3), gives diagonal entries \(\binom42=6\) once, \(\binom31=3\) with multiplicity \(v-1=n-2\), and \(\binom20=1\) in all remaining slots. It applies in the range \(2\le4\le v-2\), exactly \(n\ge7\). Therefore the displayed torsion decomposition holds with no free second homology.

The quotient is three-dimensional, so \(H_3=\ker\partial_3\) is free. The Euler characteristic computed from the cell counts above and the established lower homology yields \(\operatorname{rank}H_3=1-n+\binom n2-2\binom n3+2\binom n4\). No cells exist above dimension three. This completes the infinite-family proof.

## Verification
The standalone `verify_a4.py` reconstructs the exact integer cycle-lattice presentation from the two three-cell boundary formulae. It computes Smith forms for \(n=5,6,7,8\). The stable cases give diagonal nonunit factors \((3,3,3,3,3,6)\) at seven columns and \((3,3,3,3,3,3,6)\) at eight columns, exactly as predicted; the earlier cases have a free rank-five second homology and demonstrate why the stable range is necessary. The finite computations corroborate the derivation but do not substitute for the cited all-size inclusion-matrix diagonal theorem. Run with Python 3 and SymPy: `python verify_a4.py`. The recorded output is `verify_a4.out`.

## Relationship to prior work
Björner–Lovász–Vrećica–Živaljević (1994) introduces chessboard complexes and their topology. Wilson (1990) and the full-text 2007 reproof of his diagonal-form theorem establish the independent subset-inclusion matrix theorem used **after** the new quotient-cellular reduction. Neither states that the second homology of the ordinary alternating-row geometric quotient is this incidence cokernel. Earlier finite-case calculations cover specific small widths, including width seven, but do not imply the unbounded formula or the uniform identification with a Wilson matrix. The new contribution is the structural reduction of the topological quotient to that established arithmetic matrix and the resulting all-size torsion theorem; the matrix theorem itself is not new.

## Limitations
The result concerns ordinary geometric quotients and the row action of \(A_4\), only for \(n\ge7\). It does not classify unstable smaller widths, the integral homotopy type, third-stage attaching maps or cohomology products. External indexed literature might contain an unrecognized equivalent formulation; no independent external audit has been performed.

## References
1. A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, J. London Math. Soc. 49 (1994), 25–39. https://doi.org/10.1112/jlms/49.1.25
2. R. M. Wilson, *A Diagonal Form for the Incidence Matrices of t-Subsets vs. k-Subsets*, European J. Combin. 11 (1990), 609–615. https://doi.org/10.1016/S0195-6698(13)80046-7
3. E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori, M. Mohammad-Noori, *Inclusion Matrices and Chains*, arXiv:0709.3144, 20 September 2007, especially Corollary 3. https://arxiv.org/pdf/0709.3144
