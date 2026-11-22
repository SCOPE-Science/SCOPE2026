# Exterior-power ordering and an elliptic singular-value law for compact generalized Cesàro operators

## Finding
For \(0\le t<1\), define the generalized Cesàro operator on \(\ell^2(\mathbb N_0)\) by
\[
 (C_t x)_i=\frac1{i+1}\sum_{j=0}^i t^{i-j}x_j\qquad(i\ge0).
\]
Let \(s_1(C_t)\ge s_2(C_t)\ge\cdots\) be its singular values, counted with multiplicity. The following *one-parameter singular-order theorem* holds.

1. **Full exterior-power order.** If \(0\le r\le t<1\), then for every integer \(k\ge1\),
\[
 \prod_{j=1}^k s_j(C_r)\ \le\ \prod_{j=1}^k s_j(C_t).
\]
For \(0\le r<t<1\), the first-rank inequality is strict, so the parameter is completely distinguished by the singular-order chain. Also for each \(k\), \(\sum_{j=1}^k s_j(C_r)\le\sum_{j=1}^k s_j(C_t)\); the Schatten \(p\)-norm is strictly increasing for each \(1<p<\infty\).

2. **Sharp singular endpoint.** For every fixed \(0\le t<1\),
\[
 \lim_{n\to\infty} n\,s_n(C_t)=\chi(t)
 :=\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{\sqrt{1-2t\cos\theta+t^2}}
 =\frac2{\pi(1+t)}K\!\left(\frac{2\sqrt t}{1+t}\right),
\]
where \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2 u)^{-1/2}\,du\). Thus \(C_t\in\mathcal S_p\) precisely for \(p>1\),
\[
 \lim_{N\to\infty}\frac1{\log N}\sum_{j=1}^N s_j(C_t)
 =\lim_{p\downarrow1}(p-1)\operatorname{Tr}|C_t|^p=\chi(t),
\]
and its nonnormal singular trace amplification is strictly increasing from \(\chi(0)=1\) with
\[
 \chi(t)\sim\frac1\pi\log\frac8{1-t}\qquad(t\uparrow1).
\]
By contrast the compact triangular operator has nonzero eigenvalues \(1,1/2,1/3,\ldots\), independent of \(t\). The singular-order statement is not an assertion that *individual* singular values increase, and the limits above hold at each fixed \(t<1\), not uniformly at the noncompact endpoint \(t=1\).

## Assumptions and scope
Throughout \(\ell^2(\mathbb N_0)\) has its canonical orthonormal basis \((e_i)_{i\ge0}\); the operator \(S e_i=e_{i+1}\) is the unilateral shift; \(D e_i=(i+1)^{-1}e_i\). Then \(C_t=D(I-tS)^{-1}\), which is compact because \(D\) is compact and \(\|(I-tS)^{-1}\|\le(1-t)^{-1}\). All products involve the **largest** \(k\) singular values. The zero parameter is included. No claim concerns the classical noncompact operator \(C_1\) or parameter-dependent interchange of \(n\to\infty\) and \(t\uparrow1\).

## Proof
### 1. Exact compound-matrix positivity
Take increasing \(k\)-tuples of nonnegative integers \(I=(i_1<\cdots<i_k)\) and \(J=(j_1<\cdots<j_k)\). Factoring the row denominators and the powers gives, for \(t>0\),
\[
 \det C_t[I,J]=\frac{t^{\sum_h(i_h-j_h)}}{\prod_h(i_h+1)}
 \det[\mathbf1_{i_h\ge j_l}]_{h,l=1}^k.
\]
Subtract column \(l+1\) from column \(l\), successively from left to right (equivalently, apply one upper-bidiagonal column transformation). The resulting columns are indicators of the **disjoint** integer intervals \([j_l,j_{l+1})\) for \(l<k\), and \([j_k,\infty)\) for \(l=k\). Because the row indices are increasing, the determinant of these ordered indicator columns is exactly \(1\) if each interval contains exactly one selected row, and \(0\) otherwise. Hence
\[
 \det C_t[I,J]=
 \begin{cases}
 \displaystyle\frac{t^{\sum_h(i_h-j_h)}}{\prod_h(i_h+1)},
 &j_h\le i_h<j_{h+1}\ (h<k),\quad j_k\le i_k,\\
 0,&\text{otherwise}.
 \end{cases}
\]
The exponent of \(t\) is then a nonnegative integer. By continuity the same assertion holds for \(t=0\), with the usual convention \(0^0=1\). In particular **every** entry of the matrix of the exterior-power operator \(\bigwedge^k C_t\), in the standard wedge basis, is nonnegative and nondecreasing in \(t\).

If bounded operators \(A,B\) on \(\ell^2\) have nonnegative matrix entries and \(A\le B\) entrywise, then \(|Ax|\le A|x|\le B|x|\) coordinatewise and \(\|A\|\le\|B\|\). Apply this observation to \(\bigwedge^k C_r\) and \(\bigwedge^k C_t\). The standard singular-value identity \(\|\bigwedge^k C_t\|=\prod_{j=1}^k s_j(C_t)\) proves the full exterior-power order. Compactness justifies the standard singular-value decomposition on each exterior power.

To see that the first-rank order is strict, note that for \(0\le r<t<1\), **every** entry of the positive compact Gram matrices satisfies
\[
 (C_t^*C_t)_{j,l}>(C_r^*C_r)_{j,l},
 \quad (C_u^*C_u)_{j,l}
 =\sum_{i\ge\max(j,l)}\frac{u^{2i-j-l}}{(i+1)^2}.
\]
For any \(r\), the maximal eigenvalue of \(C_r^*C_r\) has a normalized nonnegative eigenvector: take the coordinatewise modulus of a maximizing eigenvector and use nonnegativity of all matrix entries. Its Rayleigh quotient strictly increases on replacing \(r\) by \(t\), proving \(\|C_t\|>\|C_r\|\).

There is also a separate additive majorization mechanism. For \(0\le r<t<1\), set \(q=r/t\) and let \(U_\theta e_j=e^{ij\theta}e_j\). The Poisson probability density \(P_q(\theta)=(1-q^2)/(1-2q\cos\theta+q^2)\) has Fourier coefficients \(q^{|m|}\), so entrywise and in operator norm
\[
 C_r=\frac1{2\pi}\int_0^{2\pi}
 P_q(\theta)U_\theta C_tU_\theta^*\,d\theta.
\]
Convexity and unitary invariance of each Ky Fan \(k\)-norm prove the additive inequalities. The \(\mathcal S_p\) norms are strictly convex for \(1<p<\infty\), and the conjugates are nonconstant when \(t>0\), so their norms are strictly increasing whenever finite; finiteness is proved below.

### 2. A self-contained weighted Toeplitz counting lemma
Let \((a_j)_{j\ge0}\in\ell^1\), \(f(e^{i\theta})=\sum_{j\ge0}a_j e^{ij\theta}\), and \(A=Df(S)\). For every nonzero \(f\),
\[
 \lim_{\varepsilon\downarrow0}\varepsilon\#\{n:s_n(A)>\varepsilon\}
 =\frac1{2\pi}\int_0^{2\pi}|f(e^{i\theta})|\,d\theta.
 \tag{*}
\]
Here is the needed elementary proof, including boundary control. First suppose \(f=p\) is a polynomial of degree \(m\). Fix \(\lambda>0\) and examine the threshold \(\lambda/N\) as \(N\to\infty\). Rows with index below \(aN\) form a perturbation of rank at most \(aN+1\). Rows above \(bN\) give an operator with norm at most \(\|p(S)\|/(bN)\); choose \(b\) large relative to \(\lambda\) and then send \(b\to\infty\). On \([aN,bN]\), partition rows and columns into blocks of width \(\delta N\), with \(a>0\). Because the bandwidth is \(m\), off-block entries have rank at most \(m\) times the number of blocks, independently of \(N\). Within each block, replacing the diagonal \(ND\) by the scalar \(1/x\), where \(x\) represents the block position divided by \(N\), changes the operator norm by at most \(O_{p,a}(\delta)\). Each remaining square block is a finite Toeplitz section of \(p(S)\).

For a finite-band Toeplitz section of length \(L\to\infty\), the empirical singular distribution converges to the distribution of \(|p(e^{i\theta})|\): indeed, for each fixed positive integer \(h\), normalized traces of the \(h\)-th powers of its Gram matrix differ by \(O_{p,h}(1/L)\) from the Fourier constant coefficient of \(|p|^{2h}\). Polynomial approximation on the bounded spectral interval then proves weak convergence of empirical singular measures. Consequently the normalized threshold count of the middle blocks tends, upon refining the partition, to
\[
 \int_a^b\frac1{2\pi}
 \big|\{\theta:|p(e^{i\theta})|>\lambda x\}\big|\,dx.
\]
The function of \(x\) under the integral is monotone, so its Riemann sums converge (no assumption that \(|p|\) has an atom-free distribution is necessary). Weyl's counting inequalities control each of the low-rank and operator-norm perturbations described above. Send \(\delta\downarrow0\), then \(a\downarrow0\) and \(b\uparrow\infty\), using the elementary bound \(\|D p(S)\|\le\|p(S)\|\), to obtain
\[
 \lim_{N\to\infty}\frac1N\#\{n:s_n(Dp(S))>\lambda/N\}
 =\frac1{2\pi\lambda}\int_0^{2\pi}|p(e^{i\theta})|\,d\theta.
 \tag{**}
\]
The right side follows by integrating the indicator over \(0<x<\infty\). The bounds for the upper tail can be made arbitrarily small by first fixing a margin in the threshold and choosing \(b\) accordingly. The lower tail costs at most \(a\) in normalized count. This supplies both upper and lower limits in (**).

For general \(f\), truncate to \(p_m(z)=\sum_{j=0}^m a_jz^j\), let \(\tau_m=\sum_{j>m}|a_j|\), and factor
\[
 A-Dp_m(S)=D S^{m+1}q_m(S),\qquad \|q_m(S)\|\le\tau_m.
\]
Since \(s_n(DS^{m+1})=1/(n+m+1)\), the error satisfies \(s_n(A-Dp_m(S))\le\tau_m/n\) and thus \(\#\{n:s_n(A-Dp_m(S))>u\}\le1+\tau_m/u\). Weyl's two-sided counting inequalities with threshold portions \((1-\eta)u,\eta u\) and \((1+\eta)u,\eta u\) transfer (**) to \(A\); choose \(\eta=\sqrt{\tau_m}\), then \(m\to\infty\), and use uniform convergence of \(p_m\to f\) to obtain (*). Since the right side is positive, monotonic inversion of the counting function yields the stronger ordered limit
\[
 \lim_{n\to\infty}n\,s_n(A)=\frac1{2\pi}\int|f|.
\]

### 3. Explicit coefficient and spectral consequences
For \(C_t\), take \(a_j=t^j\) and \(f(z)=(1-tz)^{-1}\) in the counting lemma. The integral in the statement follows. Substituting \(\theta=2u\) and then translating \(u\) by \(\pi/2\) yields the complete elliptic integral formula with modulus \(2\sqrt t/(1+t)\). The elementary binomial expansion gives the absolutely convergent series
\[
 \chi(t)=\sum_{m=0}^\infty\frac{\binom{2m}{m}^2}{16^m}t^{2m},
\]
which proves strict increase for \(t>0\). The complementary elliptic modulus is \((1-t)/(1+t)\); the standard logarithmic endpoint expansion \(K(k)\sim\log(4/\sqrt{1-k^2})\) gives \(\chi(t)\sim\pi^{-1}\log(8/(1-t))\). The Schatten threshold and both logarithmic trace limits follow directly from \(s_n\sim\chi(t)/n\) by comparison with harmonic sums and by the Abelian limit \((p-1)\sum_{n\ge1}n^{-p}\to1\) as \(p\downarrow1\). For fixed \(t\), compact triangularity yields the diagonal nonzero eigenvalue list \((1/n)_{n\ge1}\).

## Verification
The enclosed `check.py` uses exact rational determinants of step minors and finite-section SVD diagnostics. Its 2,182 tests passed when executed with Python 3, NumPy and SciPy, including independent direct angular integration of the elliptic constant. The first verification is exact for finite combinations and the SVD checks are finite/numerical. They are **not** proofs of the count, the infinite-dimensional exterior-power assertions, or the limit; those follow from the steps above. No external independent proof validation was performed.

## Relationship to prior work
Albanese–Bonet–Ricker (first public preprint 2023) established spectral and compactness properties of generalized Cesàro operators on sequence spaces, and their 2024 preprint examines Hardy spaces. Earlier work of Rhaly (1984) already establishes the compact Hilbert–Schmidt nature of \(C_t\) for \(t<1\) and its fixed ordinary spectrum; all these facts are credited. The distinction here is the **rank-by-rank exterior-norm order between parameters**, together with an explicit sharp ordered singular asymptotic and critical trace coefficient. General Toeplitz distribution and classical pseudodifferential Weyl techniques provide related machinery; the derived special symbol integral alone is not presented as a new general Weyl principle. Literature on Rhaly/terraced matrices with constant rows, or the classical \(t=1\) matrix, does not directly give the stated ordering for geometric difference weights. The reviewed published published-finding corpus results on finite classical Cesàro sections and on power-decaying Rhaly rows likewise cover different families/parameters.

## Limitations
The strict order is proved at rank one and for finite Schatten norms, while all-rank exterior products and Ky Fan sums are stated non-strictly. No uniform \(t\uparrow1\) singular-value asymptotic is proved, and no individual-rank singular-value monotonicity is claimed. General pseudodifferential spectral-asymptotic literature may imply the singular coefficient as an application; originality rests chiefly on the explicit **total-positive exterior-product order** across the entire geometric Cesàro family. Searches do not prove the absence of an earlier formulation, and independent mathematical review remains outstanding.

## References
- A. A. Albanese, J. Bonet, W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, arXiv:2305.04805 (first submitted 8 May 2023), https://arxiv.org/abs/2305.04805 ; journal DOI: https://doi.org/10.1007/s13398-023-01470-2.
- A. A. Albanese, J. Bonet, W. J. Ricker, *Generalized Cesàro operators in the disc algebra and in Hardy spaces*, arXiv:2410.08056 (first submitted 10 October 2024), https://arxiv.org/abs/2410.08056 ; journal DOI: https://doi.org/10.1007/s43036-024-00396-9.
- H. C. Rhaly Jr., *Generalized Cesàro Matrices*, Canadian Mathematical Bulletin 27 (1984), 417–422, https://doi.org/10.4153/CMB-1984-064-5.
- C. Bellavita, E. Dellepiane, G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930 (2025), https://arxiv.org/abs/2503.21930. Their matrices are the terraced/row-weighted family, not the geometrically weighted-difference family above.
