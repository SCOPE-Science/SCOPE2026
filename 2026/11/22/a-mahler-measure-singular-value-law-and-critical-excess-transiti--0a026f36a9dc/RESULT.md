# A Mahler-measure singular-value law and critical excess transition for two-tap Hardy dilations

## Finding
Let \(H^2(\mathbb D)\) be the standard analytic Hardy Hilbert space, and let \(0<r<1\), \(m\in\mathbb N\), and \(c\in\mathbb C\setminus\{0\}\). Define the compact weighted composition operator
\[
(W_{r,m,c}f)(z)=(1+cz^m)f(rz).
\]
Write \(s_1(W)\ge s_2(W)\ge\cdots>0\) for its approximation/singular values and put \(M_c=\max\{1,|c|\}\). Then
\[
\boxed{\lim_{n\to\infty}\frac{s_n(W_{r,m,c})}{r^{n-1}}=M_c
=\exp\left(\frac1{2\pi}\int_0^{2\pi}\log|1+ce^{i\theta}|\,d\theta\right).}
\]
The nonnegative normalized excess exhibits a sharp boundary-zero transition:
\[
\boxed{\sum_{n=1}^\infty\left(\frac{s_n(W_{r,m,c})}{M_c r^{n-1}}-1\right)
\begin{cases}<\infty,& |c|\ne1,\\=\infty,&|c|=1.\end{cases}}
\]
For every \(n\), \(s_n(W_{r,m,c})\ge M_c r^{n-1}\). For the one-tap operator (\(m=1\)), the normalized values \(s_n(W_{r,1,c})/r^{n-1}\) are nonincreasing. Off the critical circle \(|c|=1\), this gives the stronger individual rate
\[
\frac{s_n(W_{r,m,c})}{M_c r^{n-1}}=1+o(n^{-1}).
\]
For fixed \(m\), the singular values eventually occur in the natural order of their residue-class chains: for all sufficiently large \(k\) and each \(0\le b<m\),
\[
s_{mk+b+1}(W_{r,m,c})=r^b s_{k+1}(A_{r^m,|c|}),
\quad A_{q,a}=(I+aS)D_q,\quad D_q e_j=q^je_j,
\]
where \(S e_j=e_{j+1}\) on \(\ell^2(\mathbb N_0)\).

## Assumptions and scope
All singular values are indexed starting at one and counted with multiplicity. The Hardy norm is the square sum of Taylor coefficients. The claims hold for every fixed real \(0<r<1\), positive integer \(m\), and nonzero complex \(c\); no uniformity as \(r\uparrow1\), \(m\to\infty\), or \(|c|\to1\) is asserted. The right-hand integral is the logarithmic Mahler measure of \(1+cz\), including its integrable logarithmic zero when \(|c|=1\). The distinction at the critical circle concerns the summability of the normalized **excess**, not Schatten membership: all these operators lie in every positive Schatten class.

## Proof
**1. Reduction and compact Jacobi operator.** The monomial basis splits into \(m\) mutually orthogonal reducing chains indexed by \(b=0,\ldots,m-1\). Rotating phases on each chain yields the unitary equivalence
\[
W_{r,m,c}\simeq\bigoplus_{b=0}^{m-1}r^b A_{q,a},
\qquad q=r^m,\quad a=|c|.
\]
The operator \(A_{q,a}=(I+aS)D_q\) is trace class, injective, and has infinite rank. Its squared modulus \(B=A_{q,a}^*A_{q,a}\) is the compact, positive, strictly irreducible Jacobi matrix
\[
B_{ij}=q^{i+j}\big((1+a^2)\mathbf1_{i=j}+a\mathbf1_{|i-j|=1}\big).
\]
Let \(\lambda_1\ge\lambda_2\ge\cdots>0\) be its eigenvalues. Deleting the zeroth row and column yields exactly \(q^2B\) after identifying the tail with the whole space. The min--max interlacing inequality therefore gives
\[
\lambda_{j+1}\le q^2\lambda_j,\qquad
x_j:=\frac{\lambda_j}{q^{2(j-1)}}\ge x_{j+1}>0.
\tag{1}
\]
In particular the normalized singular values form a decreasing sequence. We compute its limit and excess directly.

**2. Exact principal minors.** Let \(T=(I+aS)^*(I+aS)\), so \(B=D_qTD_q\). The \(\ell\)-by-\(\ell\) consecutive principal determinant of the tridiagonal Toeplitz matrix \(T\) is
\[
d_\ell(a)=\sum_{h=0}^{\ell}a^{2h}.
\tag{2}
\]
Indeed \(d_0=1\), \(d_1=1+a^2\), and \(d_\ell=(1+a^2)d_{\ell-1}-a^2d_{\ell-2}\). More generally, if an index set \(I=\{i_1<\cdots<i_n\}\) has \(v\) maximal consecutive runs of lengths \(\ell_1,\ldots,\ell_v\), then
\[
\det B[I,I]=q^{2\sum_{j=1}^n i_j}\prod_{h=1}^v d_{\ell_h}(a).
\tag{3}
\]
Put \(\delta_j=i_j-(j-1)\). These are nonnegative nondecreasing integers, and \(L=\sum_j\delta_j\) measures the displacement from \(\{0,\ldots,n-1\}\). Every new run requires a strict jump among the \(\delta_j\); to create \(v-1\) such jumps with minimal displacement, place them at the final positions. Consequently
\[
L\ge\frac{v(v-1)}2,\qquad v\le1+\sqrt{2L}.
\tag{4}
\]
For fixed \(L\), the number of such index sets is at most the partition number \(p(L)\), since the positive \(\delta_j\) form a partition of \(L\). The generating function \(\sum_{L\ge0}p(L)t^L=\prod_{j\ge1}(1-t^j)^{-1}\) is finite whenever \(0\le t<1\).

**3. Noncritical determinant bounds and exact coefficient.** Suppose \(0<a<1\) and set \(C=(1-a^2)^{-1}\). Formula (2) gives \(1\le d_\ell(a)\le C\). As \(B\) is positive trace class, its \(n\)-th elementary spectral symmetric function is the sum of its order-\(n\) principal minors. Equations (3)--(4) give
\[
\begin{split}
\prod_{j=1}^n\lambda_j
&\le e_n(B)=\sum_{|I|=n}\det B[I,I]\\
&\le q^{n(n-1)} C\sum_{L\ge0}p(L)q^{2L}C^{\sqrt{2L}}
=:K_{q,a}q^{n(n-1)}.
\end{split}
\tag{5}
\]
The constant is finite, since \(C^{\sqrt{2L}}\le C_\epsilon e^{\epsilon L}\) for any \(\epsilon>0\), and one may choose \(q^2e^\epsilon<1\). The leading \(n\)-coordinate compression supplies the opposite bound by the variational characterization of the top exterior eigenvalue:
\[
\prod_{j=1}^n\lambda_j\ge\det B[\{0,\ldots,n-1\},\{0,\ldots,n-1\}]
=q^{n(n-1)}d_n(a)\ge q^{n(n-1)}.
\tag{6}
\]
Thus \(1\le\prod_{j=1}^n x_j\le K_{q,a}\), using the normalized eigenvalues in (1). The nonincreasing sequence \((x_j)\) therefore converges to \(1\): its Cesàro average of logarithms converges to zero by (5)--(6), and for a monotone sequence the Cesàro and ordinary limits agree. Moreover \(x_j\ge1\) and \(\sum_j\log x_j<\infty\). Since \(\sqrt{x_j}-1\le\tfrac12(x_j-1)\) is not directly controlled by \(\log x_j\) globally, use the bounded range \(1\le x_j\le x_1\), on which \(\sqrt{x}-1\le C_{q,a}\log x\). It follows that
\[
\sum_{j=1}^\infty(\sqrt{x_j}-1)<\infty,
\quad \sqrt{x_j}-1=o(j^{-1}),
\tag{7}
\]
where the final assertion uses positivity, monotonicity, and summability. This proves the one-chain claims for \(0<a<1\).

For \(a>1\), set \(b=a^{-1}\in(0,1)\). The Blaschke factor \(\beta_b(z)=(z+b)/(1+bz)\) is inner, so multiplication by \(\beta_b\) is an isometry on \(H^2\). Since \(1+az=a\beta_b(z)(1+bz)\),
\[
s_j(A_{q,a})=a\,s_j(A_{q,b})\quad(j\ge1).
\tag{8}
\]
All the preceding conclusions transfer exactly, with limiting coefficient \(a\). Complex phases are removed by a diagonal unitary.

**4. Boundary-zero case.** Let \(a=1\). Then \(d_\ell(1)=\ell+1\), and (6) becomes
\[
\prod_{j=1}^n x_j\ge n+1.
\tag{9}
\]
On the other hand (3)--(4) yield
\[
e_n(B)\le q^{n(n-1)}\sum_{L\ge0}p(L)q^{2L}(n+1)^{1+\sqrt{2L}}.
\tag{10}
\]
Take any \(0<\epsilon<-\log(q^2)\). The elementary estimate \(\sqrt{2L}\log(n+1)\le\epsilon L+(\log(n+1))^2/(2\epsilon)\) and the partition generating function bound (10) by
\[
e_n(B)\le K_{q,\epsilon}q^{n(n-1)}(n+1)
\exp\big((\log(n+1))^2/(2\epsilon)\big).
\tag{11}
\]
Consequently \(\frac1n\log\prod_{j=1}^n x_j\to0\). Monotonicity (1) again implies \(x_j\downarrow1\). But (9) forces \(\sum_j\log x_j=\infty\). Since \(\log\sqrt{x_j}\le\sqrt{x_j}-1\) and \(x_j\ge1\), the normalized singular-value excess is not summable. This establishes the strict transition for \(m=1\).

**5. All finite tap separations.** Write \(h_k=s_{k+1}(A_{q,a})/q^k\), which is nonincreasing, bounded below by \(M=\max\{1,a\}\), and converges to \(M\). The orthogonal decomposition in Step 1 gives one singular value \(r^{mk+b}h_k\) for every integer \(k\ge0\) and \(0\le b<m\). For all sufficiently large \(k\), \(M\le h_k<M/r\). Hence, in the tail, the values indexed by \(mk+b\) are strictly ordered by that integer: each factor is at least \(M\) and at most \(M/r\), whereas adjacent base factors differ by \(r\). The finitely many earlier values eventually lie above this ordered tail. Thus the exact large-index identity in the Finding holds, and the normalized excess in the whole sequence consists eventually of \(m\) repetitions of the one-chain excess. The limit, summability dichotomy, and \(o(n^{-1})\) offcritical rate follow. Coordinatewise comparison before decreasing rearrangement also yields \(s_n(W)\ge Mr^{n-1}\) for every \(n\). Finally Jensen's formula evaluates the logarithmic integral as \(\log\max\{1,a\}\), including \(a=1\) by continuity. This proves every claimed statement.

## Verification
The accompanying standard-library-only script `verify.py` performs 852 exact rational assertions: tridiagonal leading-minor identities for multiple rational parameters, arbitrary selected principal-minor factorizations, the partition-run displacement inequality, and the exact self-similarity of the Jacobi tails. It prints `FINITE_RATIONAL_CHECKS_OK 852 assertions; infinite spectral conclusions require the written proof`. Supplementary numerical finite-section singular values were checked for dilation values \(0.5\) and \(0.8\), tap spacings \(1\) through \(4\), and amplitudes below, at, and above the critical circle; all approached the stated normalized coefficients. These computations are finite consistency checks; Steps 1--5 supply the infinite proofs.

## Relationship to prior work
Putinar and Tener (first arXiv version December 12, 2016) give general weighted-composition singular-value bounds and their relation to exterior powers; their derivative-induced weights are different, and their general results do not identify this exact two-tap geometric coefficient or the excess transition. Bernard (first arXiv version January 26, 2022) develops the generation and structure of weighted-composition semigroups, without computing this singular tail. A published result, *Two-scale singular-value laws for two-tap Hardy weighted compositions* (November 8, 2026), handles the very same \((1+cz^m)f(rz)\) family, computes all even Schatten moments, and derives a two-scale singular-value counting limit as \(r\uparrow1\) and \(m\) varies. Its stated finite-\(q\) Jacobi singular values are implicit; the fixed-\(r\), far-tail coefficient and the critical summability/ordering law proved here require the additional principal-minor/interlacing argument and are not asserted there. Its exact moment data mathematically encode the full compact spectrum, so the claim is a new explicit asymptotic extraction rather than a claim to introduce a new operator family. Kozhan's 2012 two-diagonal Jacobi asymptotics concern a zero main diagonal, not this positive diagonal Jacobi modulus. The relevant published descriptions and full texts cited below were compared by precise objects and conclusions, not by titles alone.

## Limitations
The result is restricted to binomial polynomial weights and strictly contractive radial composition symbols at fixed parameter values. It does not give an exact formula for each singular value, a critical \(1/n\) coefficient, or a convergence rate uniform in the dilation, amplitude or tap spacing. At \(|c|=1\), divergence of normalized excess is proved, but no exact divergent rate is asserted. Historical novelty was assessed against accessible literature and existing published records; potential specialized compact \(q\)-Jacobi asymptotic literature not exposed by the searches remains a priority risk. No independent mathematical audit has been performed.

## References
- M. Putinar and J. E. Tener, *Singular values of weighted composition operators and second quantization*, arXiv:1612.03970v1 (December 12, 2016), https://arxiv.org/abs/1612.03970. See the introduction, Theorem A, Theorem 2.1 and exterior-power discussion.
- E. Bernard, *Weighted composition semigroups on Banach spaces of holomorphic functions*, arXiv:2201.11042v1 (January 26, 2022), https://arxiv.org/abs/2201.11042. See the weighted-composition definition and main generator assertions.
- *Two-scale singular-value laws for two-tap Hardy weighted compositions*, published November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-scale-singular-value-laws-for-two-tap-hardy-weighted-composi--19b79a8d5f82. See the complete Finding and Proof, especially its finite-\(q\) Jacobi reduction and stated limitations.
- R. Kozhan, *Asymptotics of the eigenvalues of two-diagonal Jacobi matrices*, arXiv:1210.1292 (October 4, 2012), https://arxiv.org/abs/1210.1292. Different zero-diagonal setting.
- I. Chalendar and J. R. Partington, *Boundedness and compactness of weighted composition operators and monomial operators*, 2023, https://doi.org/10.1007/s00013-023-01909-3. General boundedness/compactness context.
