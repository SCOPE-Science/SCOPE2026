# Trace-class invariance and a dyadic nuclear criterion for polynomially weighted Rhaly operators

## Finding
For every real \(a<1\), let \(\mathcal H_a\) be the coefficient Hilbert space of analytic functions on the unit disk with norm
\[
 \left\|\sum_{n\geq0}c_nz^n\right\|_a^2=\sum_{n\geq0}(n+1)^a|c_n|^2.
\]
For an arbitrary complex sequence \(\eta=(\eta_n)_{n\geq0}\), define the formal Rhaly operator by
\[
 R_\eta\!\left(\sum_{n\geq0}c_nz^n\right)=
 \sum_{n\geq0}\eta_n\left(\sum_{j=0}^nc_j\right)z^n.
\]
Set \(I_0=\{0\}\) and \(I_k=\{2^{k-1},\ldots,2^k-1\}\) for \(k\geq1\). For each \(k\), let \(L_k(\eta)\) denote the finite matrix on \(\ell^2(I_k)\) with entries \(\eta_n\mathbf1_{\{j\le n\}}\), and put
\[
 \mathcal Q(\eta)=|\eta_0|+
 \sum_{k=1}^\infty\left[
 \|L_k(\eta)\|_{\mathcal S_1}
 +2^{(k-1)/2}\left(\sum_{n\in I_k}|\eta_n|^2\right)^{1/2}\right].
\]
**Theorem.** For each fixed real \(a<1\), there exist constants \(0<c_a\le C_a<\infty\), independent of \(\eta\), such that the following statements are equivalent: \(R_\eta\) extends to a trace-class operator on \(\mathcal H_a\); and \(\mathcal Q(\eta)<\infty\). In that case
\[
 c_a\mathcal Q(\eta)\le \|R_\eta\|_{\mathcal S_1(\mathcal H_a)}\le C_a\mathcal Q(\eta).
\]
Consequently, for **every** pair \(a,b<1\) and **every** complex coefficient sequence \(\eta\), trace-class membership is invariant under the change \(\mathcal H_a\leftrightarrow\mathcal H_b\), and the corresponding trace norms are equivalent with constants depending only on \(a,b\). The restriction \(a<1\) is sharp for this invariant family: an explicit sequence below gives \(R_\eta\in\mathcal S_1(\mathcal H_0)\) but \(R_\eta\notin\mathcal S_2(\mathcal H_1)\). The theorem also applies, through equivalence of monomial coefficient norms, to standard weighted Bergman spaces \(A^2_\gamma\) for \(\gamma>-1\) and weighted Dirichlet-type spaces \(\mathcal D^2_\alpha\) for \(\alpha>0\), yielding the same trace-class membership criterion in these classical families.

## Assumptions and scope
All Hilbert spaces are complex, the trace norm is the sum of singular values, and \(R_\eta\) initially acts on polynomials. No positivity, regularity, monotonicity, phase, or nonvanishing hypothesis is imposed on \(\eta\). The theorem treats exactly polynomial coefficient weights \((n+1)^a\) with \(a<1\); it does **not** claim equivalence at \(a=1\) or for arbitrary oscillating weights. Every finite block norm entering \(\mathcal Q\) is an ordinary finite-dimensional trace norm, so this is a criterion purely in terms of \(\eta\).

## Proof
**1. Unitary matrix model.** In the orthonormal basis \(e_n=z^n/(n+1)^{a/2}\), the coefficient matrix is
\[
 F^{(a)}_{nj}=\eta_n\left(\frac{n+1}{j+1}\right)^{a/2}\mathbf1_{\{j\le n\}}.
\]
Every finite compression of this matrix is well defined even when the full operator is not bounded. Let \(P_k\) denote coordinate projection onto \(I_k\), and write \(B_k^{(a)}=P_kF^{(a)}P_k\). For \(k\ge1\), the adjacent lower block \(P_kF^{(a)}P_{k-1}\) has rank at most one and trace norm
\[
 t_k^{(a)}=
 \left(\sum_{n\in I_k}|\eta_n|^2(n+1)^a\right)^{1/2}
 \left(\sum_{j\in I_{k-1}}(j+1)^{-a}\right)^{1/2}.
\]
The dyadic positions imply that, for each fixed real \(a\), uniformly for all \(k\ge1\),
\[
 t_k^{(a)}\asymp_a 2^{(k-1)/2}
 \left(\sum_{n\in I_k}|\eta_n|^2\right)^{1/2}.
\]
Here and below \(\asymp_a\) means two-sided positive bounds depending only on \(a\), never on \(\eta,k\).

**2. Contractive block Fourier extraction.** For \(\theta\in[0,2\pi]\), let \(U_\theta=\sum_{k\ge0}e^{ik\theta}P_k\), a unitary on the coefficient \(\ell^2\). For any trace-class operator \(A\), the maps
\[
 \mathcal E_d(A)=\frac1{2\pi}\int_0^{2\pi}
 e^{-id\theta}U_\theta A U_\theta^*\,d\theta
 =\sum_{k\ge d}P_k A P_{k-d},\qquad d=0,1,
\]
are contractions in trace norm. Their ranges are block-diagonal and one-block-subdiagonal, respectively, so
\[
 \sum_{k\ge0}\|B_k^{(a)}\|_1\le\|F^{(a)}\|_1,
 \qquad \sum_{k\ge1}t_k^{(a)}\le\|F^{(a)}\|_1.
\]
The second equality uses the pairwise orthogonal input and output spaces of the adjacent rank-one blocks. Thus the sum of the two quantities is bounded by twice the trace norm. This proves necessity of the finite dyadic criterion, after comparing diagonal blocks as in step 4.

**3. Every more distant lower block is controlled by the adjacent blocks.** All entries in row block \(I_k\) with columns in the preceding union \(I_0\cup\cdots\cup I_{k-1}\) factor as one rank-one matrix. Its trace norm is
\[
 r_k^{(a)}=
 \left(\sum_{n\in I_k}|\eta_n|^2(n+1)^a\right)^{1/2}
 \left(\sum_{0\le j<2^{k-1}}(j+1)^{-a}\right)^{1/2}.
\]
For \(a<1\), comparison of a geometric series of dyadic blocks gives
\[
 \sup_{k\ge1}\frac{r_k^{(a)}}{t_k^{(a)}}
 =\sup_{k\ge1}
 \left(\frac{\sum_{j<2^{k-1}}(j+1)^{-a}}{\sum_{j\in I_{k-1}}(j+1)^{-a}}\right)^{1/2}<\infty,
\]
with the zero-over-zero case interpreted by the coefficient-independent ratio of the two positive denominator sums. Since
\[
 F^{(a)}=\bigoplus_{k\ge0}B_k^{(a)}
  +\sum_{k\ge1}u_k^{(a)}(v_{<k}^{(a)})^*,
\]
the triangle inequality yields, first for finite sections and then by trace-norm convergence,
\[
 \|F^{(a)}\|_1\le\sum_{k\ge0}\|B_k^{(a)}\|_1
 +C'_a\sum_{k\ge1}t_k^{(a)}.
\]
When the right side is finite, the series defines the desired trace-class extension, agreeing with the polynomial action on each finite coordinate.

**4. Weight independence.** On \(I_k\), \(k\ge1\), the quotient between the largest and smallest \((n+1)^{(a-b)/2}\) is at most \(2^{|a-b|/2}\). Hence
\[
 B_k^{(a)}=D_kB_k^{(b)}D_k^{-1},\qquad
 \|B_k^{(a)}\|_1\le2^{|a-b|/2}\|B_k^{(b)}\|_1.
\]
This is symmetric in \(a,b\). The adjacent-block expression in step 1 likewise satisfies \(t_k^{(a)}\asymp_a 2^{(k-1)/2}\|\eta|_{I_k}\|_2\). Combining these facts with steps 2 and 3 gives the two-sided bound by \(\mathcal Q(\eta)\). For the reference exponent \(b=0\), \(B_k^{(0)}=L_k(\eta)\), completing the proof of the theorem.

**5. Endpoint is genuinely exceptional.** For integers \(h\ge1\), set \(n_h=2^{h^2}\) and choose the sparse sequence
\[
 \eta_{n_h}=(n_h+1)^{-1/2}h^{-5/4},\qquad
 \eta_n=0\quad\text{otherwise}.
\]
On \(\mathcal H_0\), the individual nonzero matrix rows are rank-one operators of trace norm \(h^{-5/4}\), and therefore \(\|R_\eta\|_{\mathcal S_1(\mathcal H_0)}\le\sum_{h\ge1}h^{-5/4}<\infty\). At \(a=1\), the Hilbert--Schmidt norm squared is instead
\[
 \|R_\eta\|_{\mathcal S_2(\mathcal H_1)}^2
 =\sum_{h\ge1}h^{-5/2}\sum_{j=0}^{n_h}\frac1{j+1}
 \ge (\log2)\sum_{h\ge1}h^{-1/2}=\infty.
\]
This establishes sharpness of the upper weight boundary for the family-invariance statement; it is not a claim of complete classification at the critical exponent.

## Verification
The accompanying dependency-free `verify.py` checks dyadic partitions, the exact finite matrix decomposition, the rank-one adjacent-block identities and finite dyadic weight comparisons for several complex coefficient patterns and several exponents. It also checks the exact finite partial sums in the endpoint example. These tests support the algebra but cannot prove the infinite trace-class equivalence. The infinite proof is the Fourier pinching, geometric lower-block bound, and trace-norm series argument above.

## Relationship to prior work
Bellavita, Dellepiane and Stylogiannis (2026) obtain boundedness and compactness criteria on weighted Hardy spaces and a polynomial-weight-invariant Schatten criterion **for \(1<p<\infty\)**. Their Theorems 1.2--1.4 explicitly restrict the Schatten exponent to that open interval; the present theorem concerns the previously excluded trace-class endpoint and arbitrary complex sequences. Their 2025 paper likewise treats \(1<p<\infty\) for unweighted Rhaly matrices. A separately published October 2026 mathematical result characterizes the trace-class endpoint for **monotone-modulus unweighted** Rhaly matrices; that implies monotone special cases but does not imply this arbitrary-sequence, multiweight equivalence. Lin--Doan--Khoi (2018) prove Schatten properties for *small* weighted Hardy spaces with a different (not polynomial) weight regime. Galanopoulos--Girela (2026) address boundedness and compactness, not this trace-class equivalence. Endpoint comparisons remain subject to independent literature review, particularly general trace-ideal results on discrete factorable matrices.

## Limitations
The constants are not optimized. The criterion requires finite trace norms of dyadic blocks and does not simplify to a scalar sum for arbitrary nonmonotone coefficients. No uniform bound as \(a\uparrow1\) is claimed, and the explicit sparse example shows no such full invariance can include \(a=1\). The argument is not an independence or exhaustive priority certification; it does not classify arbitrary non-polynomial weights.

## References
1. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875v1, first posted 2026-06-14, https://arxiv.org/abs/2606.15875 (full arXiv HTML: https://arxiv.org/html/2606.15875).
2. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, Journal of the London Mathematical Society 112 (2025), e70304, https://doi.org/10.1112/jlms.70304; arXiv:2503.21930.
3. P. Galanopoulos and D. Girela, *Rhaly Operators Acting on Hardy, Bergman, and Dirichlet Spaces*, Journal of Geometric Analysis 36 (2026), article 115, https://doi.org/10.1007/s12220-026-02361-9.
4. T. P. Lin, M. L. Doan and L. H. Khoi, *Rhaly Operators on Small Weighted Hardy Spaces*, Acta Mathematica Vietnamica 43 (2018), 749--759, https://doi.org/10.1007/s40306-018-0277-9 (institutional manuscript: https://dr.ntu.edu.sg/server/api/core/bitstreams/5b60f864-e5cd-40fa-a060-ec87a945a903/content).
5. *The sharp trace-class endpoint for monotone-modulus Rhaly matrices*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-sharp-trace-class-endpoint-for-monotone-modulus-rhaly-matric--182bfa9e0a1a.
