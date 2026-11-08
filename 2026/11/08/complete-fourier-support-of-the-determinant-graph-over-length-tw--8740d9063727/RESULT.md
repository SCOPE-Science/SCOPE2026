# Complete Fourier support of the determinant graph over length-two odd chain rings

## Finding
Let \(R\) be any commutative finite chain ring with maximal ideal \((\pi)\), nilpotency length exactly two, and residue field \(\mathbb F_q\) of **odd** cardinality \(q\). Let \(\psi:R\to\mathbb C^\times\) be a generating additive character: its restriction to the minimal ideal \(\pi R\) is nontrivial. Set \(\Gamma_R=\{(X,\det X):X\in M_3(R)\}\). The additive Fourier multiplier of the indicator, at \((A,b)\in M_3(R)\times R\), is
\[
F(A,b)=\sum_{X\in M_3(R)}\psi\left(\sum_{i,j}A_{ij}X_{ij}+b\det X\right).
\]
All Fourier zeros are classified by the following exhaustive mutually exclusive cases.

1. For \(b=0\), the multiplier is nonzero if and only if \(A=0\).
2. For \(b\in\pi R\setminus\{0\}\), the multiplier is nonzero if and only if \(A\in\pi M_3(R)\).
3. For \(b\in R^\times\), put \(C=-\overline b^{-1}\overline A\in M_3(\mathbb F_q)\). The multiplier is nonzero if and only if either \(\operatorname{rank}C\leq1\), or \(\operatorname{rank}C=3\) and \(\det C\) is a nonzero square in \(\mathbb F_q\). In particular, every rank-two residue matrix and every invertible nonsquare-determinant residue matrix gives a Fourier zero.

Let \(N_1=(q^3-1)^2/(q-1)\) and \(N_3=(q^3-1)(q^3-q)(q^3-q^2)\). Convolution by \(\mathbf1_{\Gamma_R}\) on functions on \(M_3(R)\times R\) has exact rank
\[
\operatorname{rank}T_{\Gamma_R}=1+(q-1)q^9+(q^2-q)q^9\left(1+N_1+\frac{N_3}{2}\right).
\]
The ambient dimension is \(q^{20}\). Along odd prime-power residue sizes \(q\to\infty\), the fraction of nonzero Fourier multipliers tends to \(1/2\). The formula is independent of the presentation or characteristic of the chain ring.

## Assumptions and scope
A chain ring here is finite, commutative, and local with all ideals ordered by inclusion. Length two means \(\pi^2=0\), \(\pi\ne0\), \(|R|=q^2\), and \(|\pi R|=q\). Odd residue characteristic is essential to the square-root dichotomy and odd-order phase noncancellation. The coefficient pairing is entrywise, \(\langle A,X\rangle=\sum_{i,j}A_{ij}X_{ij}\). No normalization is used for Fourier transforms. We write \(\operatorname{cof}(X)=\operatorname{adj}(X)^{\mathsf T}\), so that \(D(\det)_X(Y)=\langle\operatorname{cof}(X),Y\rangle\). The notation \(\overline z\) means reduction modulo \(\pi\); a chosen lift of a residue is denoted \(\widetilde z\).

## Proof
**Residue-fibre orthogonality.** Every residue matrix \(X_0\in M_3(\mathbb F_q)\) has exactly \(q^9\) lifts \(X=\widetilde X_0+\pi Y\) with \(Y\in M_3(\mathbb F_q)\). Since \(\pi^2=0\),
\[
\det(\widetilde X_0+\pi Y)=\det\widetilde X_0+\pi\langle\operatorname{cof}(X_0),Y\rangle.
\]
The nontrivial character \(\psi_0(z)=\psi(\pi\widetilde z)\) is well-defined on \(\mathbb F_q\). Summing over \(Y\) gives zero unless
\[
\overline A+\overline b\operatorname{cof}(X_0)=0,
\]
and otherwise contributes \(q^9\) times the phase evaluated at \(\widetilde X_0\). If \(b\) is a unit, this becomes \(\operatorname{cof}(X_0)=C\).

**Adjugate image and invertible fibres.** On \(3\)-by-\(3\) matrices, the cofactor map has rank zero on the matrices of rank at most one, rank one on rank-two matrices, and rank three on invertible matrices. In particular it never has rank two. If \(C\) is invertible, the identities \(\operatorname{cof}(X)X^{\mathsf T}=\det X\,I_3\) and \(\det\operatorname{cof}(X)=(\det X)^2\) imply that \(\operatorname{cof}(X)=C\) has solutions precisely when \(\det C\) is a square. When \(\det C=s^2\), the only solutions are \(X=\pm s(C^{-1})^{\mathsf T}\). Opposite solutions have opposite total phases, because the linear term and the cubic determinant are odd under \(X\mapsto-X\). Thus their summed contribution is \(q^9[\psi(z)+\psi(-z)]\), which cannot vanish: both terms have odd prime-power order, whereas their ratio would have to be \(-1\). This proves the full-rank clause.

**Rank-zero cofactor fibre.** If \(C=0\), then \(\overline A=0\), so write \(A=\pi B\). The critical matrices \(X_0\) are exactly those of rank zero or one, and any rank-one lift can be used because its determinant is zero. Therefore
\[
F(\pi B,b)=q^9\sum_{\operatorname{rank}X\le1}\psi_0(\langle\overline B,X\rangle).
\]
For \(r=\operatorname{rank}\overline B\), representing every nonzero rank-one matrix by exactly \(q-1\) pairs \((u,v)\) with \(u,v\in\mathbb F_q^3\setminus\{0\}\), and applying character orthogonality to the bilinear form \(u^{\mathsf T}\overline Bv\), yields
\[
\sum_{\operatorname{rank}X\le1}\psi_0(\langle\overline B,X\rangle)=\frac{q^{6-r}-2q^3+q}{q-1}.
\]
For ranks \(0,1,2,3\) this is respectively \(1+(q^3-1)^2/(q-1)\), \(q(q-1)(q+1)^2\), \(q(q^2-q-1)\), and \(-q(q+1)\). All are nonzero for odd \(q\ge3\).

**Rank-one cofactor fibre.** Left and right multiplication by suitable invertible residue matrices reduces any prescribed rank-one cofactor to \(E_{33}\). The critical matrices then have the form \(\operatorname{diag}(U,0)\) with \(U\in\operatorname{SL}_2(\mathbb F_q)\). Choose lifts preserving the zero last row and column. Their determinant is zero, and because the upper-left block of the residue of \(A\) is zero, the phase becomes a nontrivial residue-field character evaluated at a \(2\)-by-\(2\) coefficient matrix \(B\). Thus, up to an irrelevant nonzero common phase and changes of linear coordinates,
\[
F(A,b)=q^9\sum_{U\in\operatorname{SL}_2(\mathbb F_q)}\psi_0(\langle B,U\rangle).
\]
The finite-field special-linear Gauss-sum identity states
\[
\sum_{U\in\operatorname{SL}_2(\mathbb F_q)}\psi_0(\langle B,U\rangle)=q^3\mathbf1_{B=0}+q\sum_{t\in\mathbb F_q^\times}\psi_0(t+\det B/t).
\]
For completeness, if \(B\) is invertible, substitute \(V=B^{\mathsf T}U\) and group matrices \(V\) with fixed nonzero upper-left entry \(s\). The determinant fixes the lower-right entry, and the sum over the two off-diagonal entries is \(q\); upper-left entry zero contributes nothing after summing the lower-right entry. This yields the displayed Kloosterman identity for \(B\) invertible. If \(B\) is nonzero singular, row/column changes reduce it to \(E_{11}\), and orthogonality gives \(-q\). At \(B=0\), the sum is \(|\operatorname{SL}_2(\mathbb F_q)|=q^3-q\). The Kloosterman sum on the right never vanishes: its \(q-1\) summands are powers of a primitive \(p\)-th root, and modulo the cyclotomic prime \(1-\zeta_p\) their sum is congruent to \(q-1\equiv-1\pmod p\). Hence the displayed sum is nonzero both when \(B=0\) (where it equals \(q^3-q\)) and when \(B\ne0\). This proves the rank-one clause. The argument does not assume that \(\det B\ne0\).

**Nonunit determinant frequency.** If \(b=0\), ordinary additive character orthogonality yields \(F(A,0)=q^{18}\mathbf1_{A=0}\). If \(b=\pi b_1\ne0\), the residue-fibre sum vanishes unless \(A=\pi B\); in the latter case
\[
F(\pi B,\pi b_1)=q^9 S(\overline B,\overline{b_1}),\qquad
S(B,\lambda)=\sum_{X\in M_3(\mathbb F_q)}\psi_0(\langle B,X\rangle+\lambda\det X).
\]
Here \(\lambda\ne0\). For \(r=\operatorname{rank}B\) this field sum is
\[
S(B,\lambda)=
\begin{cases}
q^7+q^6-q^4,&r=0,\\
q^6-q^4,&r=1,\\
-q^4,&r=2,\\
q^4\sum_{t\in\mathbb F_q^\times}\psi_0(t-\det B/(\lambda t)),&r=3.
\end{cases}
\]
One elementary derivation fixes the first two matrix rows and sums the third: the third-row character sum is \(q^3\) exactly when its frequency vector equals minus \(\lambda\) times the cross-product of the first two rows. For rank at most two, a row/column change of variables makes the last-row frequency zero and reduces the remaining double sum to a rank-one bilinear-cone transform. For full-rank frequency, substitute \(Z=B^{\mathsf T}X\) to make the linear phase \(\operatorname{tr}Z\) and the cubic phase \((\lambda/\det B)\det Z\). The last-row orthogonality forces the first two rows into the coordinate plane and their upper-left \(2\)-by-\(2\) determinant to equal \(-\det B/\lambda\). The remaining sum is \(q^3\) times the fixed-determinant trace sum, which is \(q\) times the displayed Kloosterman sum by the same upper-left-entry computation. These field identities are also specializations of published finite-field general/special linear matrix Gauss sums. The Kloosterman congruence just proved ensures all four values are nonzero.

**Counting supported frequencies.** There is one supported frequency with \(b=0\). There are \(q-1\) nonzero \(b\) in \(\pi R\), each permitting \(q^9\) coefficient matrices \(A\). There are \(q^2-q\) unit values of \(b\); for each, the allowable \(C\) consists of one zero matrix, the \(N_1\) rank-one matrices, and half of the \(N_3\) invertible matrices. Each such residue \(C\) admits \(q^9\) lifts \(A\). Diagonalization of convolution by additive characters makes its rank the number of nonzero Fourier multipliers, giving the formula in the Finding. Since \(N_3=q^9(1+O(q^{-1}))\), the limiting rank fraction is \(1/2\).

## Verification
The reproducible scripts `check_field.py`, `check_cyclic.py`, and `check_split.py` require Python 3 and NumPy. The field checker exhaustively compares the claimed field-frequency formula with a nine-dimensional discrete Fourier transform for fields of sizes two and three. The cyclic-ring checker independently eliminates one matrix row over \(\mathbb Z/9\mathbb Z\), then checks the remaining six-dimensional Fourier transform against the rank/square criterion for representative unit, nonunit, and zero determinant frequencies. The split-ring checker independently performs the analogous six-dimensional Fourier test over \(\mathbb F_3[t]/(t^2)\). The executed scripts reported respectively `p 2 max_err 2.06e-14`, `p 3 max_err 2.26e-12`, `ALL_DETERMINANT_CHAIN_CHECKS_OK`, and `SPLIT_CHAIN_EXACT_SUPPORT_CHECKS_OK`. Their floating FFT values are numerical corroboration, not exact certificates or substitutes for the algebraic proof.

The rank formula gives \(703312957\) supported frequencies for \(q=3\) out of \(3486784401\) and \(29212703125001\) for \(q=5\) out of \(95367431640625\). These are symbolic evaluations of the proven count, not exhaustive enumerations of the ambient Fourier space.

## Relationship to prior work
Li and Hu's 2011 finite-field matrix Gauss-sum formulas (arXiv:1105.4513) give known ingredients for the \(\operatorname{SL}_2\) and \(\mathbb F_q\) determinant-phase calculations; the stand-alone finite-field formulas are *not* asserted as new. Choosuwan, Jitman and Udomkavanich (arXiv:1605.06826) count determinant-value fibres of matrices over finite chain rings, corresponding to matrix-frequency zero rather than the full twisted Fourier support. Hu, He, Meng and Li (arXiv:1805.09729) calculate special-linear and general-linear Gauss sums over cyclic rings; these are related but not directly the additive Fourier multiplier of the complete determinant graph over all length-two finite chain rings. Lapkova and Xiao (arXiv:2002.11657) develop prime-square stationary-phase stratification for exponential sums, a methodological antecedent rather than a pointwise graph-support classification. The result here isolates the full length-two Fourier-zero locus and its exact convolution-rank count, including singular matrix-frequency strata.

## Limitations
The proof assumes odd residue characteristic and nilpotency length exactly two; no assertion is made in even residue characteristic or higher lengths. The arguments prove exact nonvanishing/support and rank, not a complete magnitude distribution for all frequencies. The result's scientific novelty is subject to the possibility that a broader local-ring matrix Gauss-sum or prehomogeneous-vector-space theorem already implies it. Reproducible finite computations support but cannot replace the universal proof. Independent mathematical validation has not been performed.

## References
- Yan Li and Su Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513v1 (first posted 2011-05-23), https://arxiv.org/abs/1105.4513.
- P. Choosuwan, S. Jitman and S. Udomkavanich, *Determinants of Matrices over Commutative Finite Principal Ideal Rings*, arXiv:1605.06826v1 (first posted 2016-05-22), https://arxiv.org/abs/1605.06826.
- K. Lapkova and S. Xiao, *A stratification result for an exponential sum modulo \(p^2\)*, arXiv:2002.11657v1 (first posted 2020-02-26), https://arxiv.org/abs/2002.11657.
- S. Hu, G. He, Y. Meng and Y. Li, *Gauss sums of some matrix groups over \(\mathbb Z/n\mathbb Z\)*, arXiv:1805.09729v1 (first posted 2018-05-24), https://arxiv.org/abs/1805.09729.
