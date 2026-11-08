# Quadratic singular-number decay for commutators of the Cesàro operator with powers of the shift

## Finding
Let \(C\) denote the classical discrete Cesàro operator on \(\ell^2(\mathbb N_0)\), and \(S\) the unilateral forward shift. For each integer \(m\geq1\), set \(D_m=CS^m-S^mC\). There are positive constants \(c_m,C_m\), independent of the singular-value index \(n\), such that
\[
\boxed{\qquad c_m n^{-2}\leq s_n(D_m)\leq C_m n^{-2}\quad(n\geq1).\qquad}
\]
Consequently, for every \(m\geq1\) and every real \(p>0\),
\[
\boxed{\quad D_m\in\mathcal S_p\ \Longleftrightarrow\ p>\tfrac12,\qquad
D_m\in\mathcal S_{1/2,\infty}\setminus\mathcal S_{1/2}.\quad}
\]
Here \(\mathcal S_{1/2,\infty}\) is the weak Schatten ideal defined by \(\sup_{n\geq1}n^2s_n(T)<\infty\). In addition, writing \(H_m=\sum_{r=1}^m r^{-1}\) and \(H_m^{(2)}=\sum_{r=1}^m r^{-2}\), the Hilbert–Schmidt norm is exactly
\[
\boxed{\quad \|D_m\|_{\mathcal S_2}^2=H_m+mH_m^{(2)}-m\zeta(2).\quad}
\]
The quadratic singular-number exponent is therefore sharp for every nonzero monomial power of the shift. The theorem does **not** assert an exact limit for \(n^2s_n(D_m)\).

## Assumptions and scope
Work on the complex Hilbert space \(\ell^2(\mathbb N_0)\) with orthonormal basis \((e_j)_{j\geq0}\), and write \(Se_j=e_{j+1}\). The Cesàro operator is the bounded operator
\[
(Cx)_n=\frac1{n+1}\sum_{j=0}^n x_j,\quad n\geq0.
\]
Its boundedness on \(\ell^2\) is the classical Hardy inequality. Singular values \(s_n(T)\) are decreasing, with indices beginning at \(n=1\); for a compact operator they equal its approximation numbers. Schatten ideals with exponents less than one are interpreted as quasi-Banach operator ideals. All constants in the statement may depend on the fixed integer \(m\) but never on \(n\).

## Proof
**1. Exact reduction to a factorable matrix.** Directly on basis vectors, for \(n\geq j+m\),
\[
\langle D_me_j,e_n\rangle=\frac1{n+1}-\frac1{n-m+1}=-\frac{m}{(n+1)(n-m+1)},
\]
and all other entries vanish. Thus \(D_m=-S^mB_m\), where \(B_m\) is the lower triangular matrix
\[
(B_m)_{ij}=a_i\mathbf1_{j\leq i},\qquad a_i=\frac{m}{(i+1)(i+m+1)}\quad (i,j\geq0).
\]
Since \(S^m\) is an isometry, \(s_n(D_m)=s_n(B_m)\) for every \(n\). Also,
\[
\frac{m}{m+1}(i+1)^{-2}\leq a_i\leq m(i+1)^{-2}.
\]
We prove the more general two-sided estimate \(s_n(B)\asymp n^{-2}\) for every matrix \(B_{ij}=a_i\mathbf1_{j\le i}\) with \(0<c(i+1)^{-2}\le a_i\le C(i+1)^{-2}\).

**2. A dyadic upper approximation bound.** Partition \(\mathbb N_0\) into blocks
\[
I_r=\{2^r-1,\dots,2^{r+1}-2\},\qquad N_r=|I_r|=2^r\quad(r\geq0).
\]
Write \(B=G+F\), where \(G\) is the direct sum of the diagonal blocks of \(B\) and \(F\) contains the strictly earlier-block interactions. On \(I_r\), the block of \(G\) is \(\operatorname{diag}(a_i)J_{N_r}\), where \(J_N\) is the \(N\)-by-\(N\) matrix of ones on and below its diagonal.

For \(1\le k\le N\), one has \(s_k(J_N)\le 2N/k\). Indeed, cut \(\{1,\dots,N\}\) into \(k\) consecutive groups of length at most \(\lceil N/k\rceil\). Replace \(J_N\) by its strictly below-block part: this has rank at most \(k-1\), while the error is a direct sum of triangular zero-one blocks, each of norm at most \(\lceil N/k\rceil\le 2N/k\). Consequently
\[
 s_k(G|_{I_r})\le \frac{2C}{N_r k}\quad (1\le k\le N_r).
\]
For \(t>0\), the number of singular values of \(G\) exceeding \(t\) is therefore bounded by
\[
\sum_{r\ge0}\min\left(N_r,\frac{2C}{N_r t}\right)\le A_Ct^{-1/2},
\]
using the two geometric sums on either side of \(N_r\asymp t^{-1/2}\). Hence \(s_n(G)\le K_C n^{-2}\).

For every \(r\ge1\), the part \(F_r\) with output supported on \(I_r\) has rank one: its range vector is \((a_i)_{i\in I_r}\), while its input functional is summation over indices preceding \(I_r\). Hence
\[
\|F_r\|\le \sqrt{N_r}(CN_r^{-2})\sqrt{N_r}=C2^{-r}.
\]
The rank of \(\sum_{r<R}F_r\) is at most \(R\) and the operator-norm tail is at most \(2C2^{-R}\). Thus \(s_{R+1}(F)\le2C2^{-R}\). The elementary singular-number sum inequality \(s_{j+k-1}(G+F)\le s_j(G)+s_k(F)\) now gives \(s_n(B)\le K'_C n^{-2}\).

**3. A matching lower bound.** For each \(r\ge1\), consider the subspace
\[
E_r=\{x:\operatorname{supp}(x)\subset I_r,\ \sum_{j\in I_r}x_j=0\},\qquad \dim E_r=N_r-1.
\]
For \(x\in E_r\), all rows of \(Bx\) outside \(I_r\) vanish: earlier rows see no input, and later rows see the zero total sum. On \(I_r\), \(Bx=\operatorname{diag}(a_i)J_{N_r}x\). Because \(J_N^{-1}\) is the first-difference matrix, \(\|J_N^{-1}\|\le2\). Also \(a_i\ge c/(4N_r^2)\) throughout \(I_r\), so
\[
\|Bx\|\ge \frac{c}{8N_r^2}\|x\|\qquad(x\in E_r).
\]
The subspaces \(E_r\) are mutually orthogonal and their images under \(B\) have disjoint supports. On \(E_1\oplus\cdots\oplus E_R\), the same lower bound holds with \(N_R=2^R\); its dimension is \(2^{R+1}-R-2\ge2^R\) for \(R\ge2\). Choosing the least \(R\ge2\) for which \(2^R\ge n\), and applying the variational characterization of singular values, gives a universal constant \(c'>0\) with \(s_n(B)\ge c'n^{-2}\). In fact, the preceding estimates allow \(c'=c/128\). This completes the two-sided assertion.

**4. Exact Hilbert–Schmidt norm.** The \(i\)-th row of \(B_m\) has exactly \(i+1\) nonzero entries, all equal to \(a_i\). Therefore, by nonnegative summation,
\[
\|D_m\|_{\mathcal S_2}^2
= m^2\sum_{r=1}^\infty\frac{1}{r(r+m)^2}
=\sum_{r=1}^\infty\left(\frac1r-\frac1{r+m}-\frac{m}{(r+m)^2}\right)
=H_m+mH_m^{(2)}-m\zeta(2).
\]
Finally, \(\sum_ns_n(D_m)^p\) converges if and only if \(\sum_nn^{-2p}\) does, which gives the exact Schatten and weak-Schatten assertions.

## Verification
Run `python checker.py` in the same directory as this file. The checker uses only the Python standard library and compares exact rational finite matrices of \(CS^m-S^mC\) with the asserted factorable formula, tests block cancellation/inverse identities, and checks finite partial sums of the Hilbert–Schmidt series. It reports `CESARO_SHIFT_COMMUTATOR_EXACT_FINITE_OK 20678`. The finite checks are corroboration; all infinite singular-value conclusions are proved in the dyadic argument above.

## Relationship to prior work
Yuanqi Sang's 2026 paper proves that the classical Cesàro operator belongs to the \(C^*\)-algebra generated by all bounded Hardy-space Toeplitz operators, building on Barría–Halmos's earlier Hilbert–Schmidt asymptotic-Toeplitz calculation. That work establishes an algebraic position of \(C\), not the quadratic singular-number bounds for \([C,S^m]\). The general Rhaly/terraced matrix literature is relevant because the shifted commutator is exactly such a matrix; in particular, Bellavita–Dellepiane–Stylogiannis establish ordinary Schatten criteria in the range \(1<p<\infty\), and related later work considers factorable matrices. The present quantitative result identifies the optimal *sub-trace-class* weak-ideal threshold of the shift commutators, including the sharp failure at \(p=1/2\), through a standalone two-sided approximation-number proof. This is a best-knowledge distinction, not an independent assertion of publication priority.

## Limitations
The result concerns the discrete Cesàro operator on complex \(\ell^2\) and monomial powers of the forward shift, with \(m\) fixed as \(n\to\infty\). Constants in \(s_n(D_m)\asymp_mn^{-2}\) are not optimized, and no exact leading singular-value constant is established. It does not cover arbitrary Toeplitz symbols. A 2026 follow-up on Rhaly operators and factorable matrices could not be fully inspected; this creates a residual overlap/priority risk. No independent mathematical audit has been performed.

## References
1. Y. Sang, *The Cesàro Operator is in the Toeplitz Algebra*, arXiv:2608.25740, first posted 2026-08-26, https://arxiv.org/abs/2608.25740.
2. J. Barría and P. R. Halmos, *Asymptotic Toeplitz operators*, Transactions of the AMS 273 (1982), 621–630.
3. C. Bellavita, E. Dellepiane, and G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, J. London Math. Soc. 112 (2025), e70304, doi:10.1112/jlms.70304.
4. C. Bellavita, E. Dellepiane, and G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875, first posted 2026-06-14, https://arxiv.org/abs/2606.15875.
