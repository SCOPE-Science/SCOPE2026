# Elliptic Weyl coefficient and quantitative singular decay of geometrically weighted Cesàro averaging

## Finding
Let \(0<q<1\), and let \(C_q\) denote ordinary Cesàro averaging on the weighted Hilbert space
\[
 H_q=\left\{x=(x_j)_{j\ge1}:\ \sum_{j\ge1}q^j|x_j|^2<\infty\right\},\qquad
 (C_qx)_j=\frac1j\sum_{k=1}^jx_k.
\]
Its decreasing singular values \(s_n(q)\), counted with multiplicity, obey the **quantitative elliptic Weyl law**
\[
 s_n(q)=\frac{\kappa(\sqrt q)}n+O_q\!\left(\frac{\log(2+n)}{n^{3/2}}\right),
 \qquad n\longrightarrow\infty,
\]
where, for \(0<r<1\),
\[
 \kappa(r)=\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{|1-re^{i\theta}|}
 =\frac2{\pi(1+r)}\,\mathbf K\!\left(\frac{2\sqrt r}{1+r}\right),
 \quad \mathbf K(k)=\int_0^{\pi/2}\frac{d\phi}{\sqrt{1-k^2\sin^2\phi}}.
\]
Equivalently, if \(N_q(t)=\#\{n:s_n(q)>t\}\), then
\[
 N_q(t)=\frac{\kappa(\sqrt q)}t+O_q\!\left(t^{-1/2}\log(2/t)\right)
 \quad(t\downarrow0).
\]
In particular, \(C_q\) belongs to Schatten class \(\mathcal S_p\) **exactly when** \(p>1\), and
\[
 \lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^N s_n(q)=\kappa(\sqrt q).
\]
The coefficient is strictly increasing from \(1\) to \(+\infty\) as \(r\) increases from \(0\) to \(1\); more sharply,
\[
 \kappa(r)=\frac1\pi\log\!\left(\frac8{1-r}\right)+o(1)
 \quad(r\uparrow1).
\]
These statements concern singular values, not the already-known eigenvalues \(1,1/2,\ldots\), which do not depend on the geometric weight.

## Assumptions and scope
All Hilbert spaces are complex, although the matrix is real. The index set is \(\{1,2,\ldots\}\), the weight is **exactly** \(q^j\), and \(q\) is fixed in \((0,1)\) in both asymptotic estimates. The constants hidden in \(O_q\) may grow as \(q\uparrow1\); no uniform crossover theorem is claimed. Singular values are those of the infinite compact operator \(C_q\), not merely those of its principal truncation. The Schatten parameter \(p>0\) is arbitrary.

## Proof
**1. Unitarly equivalent triangular model.** Put \(r=\sqrt q\), let \(S\) be the unilateral forward shift on \(\ell^2(\mathbb N)\), and let \(D=\operatorname{diag}(1,1/2,1/3,\ldots)\). Multiplication by \(q^{j/2}\) defines an isometry \(U:H_q\to\ell^2\). Direct calculation gives
\[
 A_r=UC_qU^{-1}=D(I-rS)^{-1}
 =D\sum_{h=0}^{\infty}r^hS^h,
 \qquad (A_r)_{jk}=\frac{r^{j-k}}j\ \text{for}\ 1\le k\le j.
\]
Because \(D\) is compact and \(\|(I-rS)^{-1}\|\le(1-r)^{-1}\), \(A_r\) is compact. Its singular values equal those of \(C_q\).

**2. Uniform counting estimate for finite symbols.** For a positive integer \(M\), define \(P_M(z)=\sum_{h=0}^M r^h z^h\), \(A_{r,M}=DP_M(S)\), and
\[
 f_M(u)=\frac1{2\pi}\,\big|\{\theta\in[0,2\pi):|P_M(e^{i\theta})|>u\}\big|,
 \qquad \kappa_M=\int_0^\infty f_M(u)\,du.
\]
Here \(f_M\) is nonincreasing, lies between \(0\) and \(1\), and, by layer cake, \(\kappa_M=(2\pi)^{-1}\int|P_M(e^{i\theta})|\,d\theta\).

For each sufficiently small \(t>0\), put \(h=\lceil t^{-1/2}\rceil\), \(J=\lceil 2/((1-r)t)\rceil\), and partition \(\{1,\ldots,J\}\) into consecutive blocks of length at most \(h\). The restriction of \(A_{r,M}\) to rows and columns greater than \(J\) has operator norm at most \(t/2\). The cross-cut rectangular block at \(J\) has rank at most \(M\). Removing that cross-cut and the cross-cuts between consecutive blocks costs rank at most \(M(1+\lceil J/h\rceil)\), so changes the singular-value counting function at threshold \(t\) by at most that rank.

On a block \(I=\{a,\ldots,b\}\), its diagonal part is \(D_I T_{M,|I|}\), where \(T_{M,\ell}=P_M(S_\ell)\) is the lower triangular finite Toeplitz section. Since \(b^{-1}I\le D_I\le a^{-1}I\), the singular-value min–max principle sandwiches its count above \(t\) between the counts of \(T_{M,|I|}\) above \(tb\) and above \(ta\). The Toeplitz section differs by rank at most \(M\) from the circulant \(P_M(V_\ell)\). The circulant's singular values are exactly \(|P_M(e^{2\pi ik/\ell})|\). For any threshold \(u\), the trigonometric polynomial \(|P_M(e^{i\theta})|^2-u^2\) has at most \(2M\) zeros unless identically zero, so the discrete grid count differs from \(\ell f_M(u)\) by \(O(M+1)\), uniformly in \(u\) and \(\ell\) (the rank comparison covers \(\ell\le M\)). Therefore the block count lies between
\[
 |I|f_M(tb)-O(M+1)\quad\text{and}\quad |I|f_M(ta)+O(M+1).
\]
Summing over consecutive blocks, monotonicity of \(f_M\) sandwiches the resulting lower and upper Riemann sums around \(t^{-1}\int_0^{tJ}f_M(u)\,du\), with error \(O(h+1)\). Since \(\|P_M\|_{\infty}\le(1-r)^{-1}<tJ\), this integral equals \(\kappa_M/t\). We conclude the uniform-in-\(M\) estimate
\[
 \left|N(t;A_{r,M})-\frac{\kappa_M}{t}\right|
 \le C_r\left(t^{-1/2}+ (M+1)t^{-1/2}\right)
 =O_r\!\left((M+1)t^{-1/2}\right).
\]
The estimate holds for all positive integers \(M\), with an adjusted constant for the finitely many larger \(t\). The argument uses finite rank comparison and explicit grid counts, not an unquantified Toeplitz limit theorem.

**3. Restore the infinite geometric tail.** Choose \(M=M(t)=O_r(\log(2/t))\) large enough that
\[
 \delta_M:=\|A_r-A_{r,M}\|\le\frac{r^{M+1}}{1-r}\le t^2/4.
\]
The min–max perturbation inequality gives
\[
 N(t+\delta_M;A_{r,M})\le N(t;A_r)
 \le N(t-\delta_M;A_{r,M}).
\]
Also \(|\kappa_M-\kappa(r)|\le\delta_M\) because the symbols differ pointwise by at most \(\delta_M\). Apply the preceding finite-symbol estimate at \(t\pm\delta_M\sim t\) and use
\(\kappa_M/(t\pm\delta_M)=\kappa(r)/t+O_r(1)\). This establishes
\[
 N(t;A_r)=\kappa(r)t^{-1}+O_r(t^{-1/2}\log(2/t)).
\]
As \(\kappa(r)>0\), monotone inversion of this counting law, bounding the threshold at \(\kappa(r)/n\) by \(O_r(n^{-3/2}\log(2+n))\) from both sides, yields the asserted singular-value estimate. No finite cutoff is used to infer an unproved infinite statement.

**4. Exact coefficient and consequences.** The symbol \(P_\infty(e^{i\theta})=(1-re^{i\theta})^{-1}\) gives the displayed integral. The substitution \(\theta=2\phi\) and periodic symmetry yield the complete elliptic-integral formula. Multiplying the two absolutely convergent binomial series for \((1-re^{i\theta})^{-1/2}\) and its conjugate gives
\[
 \kappa(r)=\sum_{m=0}^{\infty}
 \left(\frac{\binom{2m}{m}}{4^m}\right)^2r^{2m},
\]
so \(\kappa(0)=1\) and strict increase holds for \(r>0\). The standard endpoint asymptotic \(\mathbf K(k)=\log(4/\sqrt{1-k^2})+o(1)\), together with \(1-k^2=(1-r)^2/(1+r)^2\), proves the logarithmic divergence. Finally \(s_n(q)\sim\kappa(\sqrt q)/n\) gives the Schatten cutoff and, by harmonic summation, the logarithmic average of singular values.

## Verification
An independent computation within the package, `checker.py`, constructs finite principal sections of \(A_r\) and checks them against their inverse-bidiagonal Gram matrices. It checks finite singular values at multiple lengths and geometric parameters, compares a numerical singular Weyl coefficient with the elliptic integral, verifies the weighted-matrix identity, and tests the Hilbert–Schmidt trace identity
\[
 \|A_r\|_{\mathcal S_2}^2=
 \frac{\zeta(2)-\operatorname{Li}_2(r^2)}{1-r^2}.
\]
These finite computations corroborate but do not prove the asymptotic remainder, which is established in the preceding block-counting argument. Run `python checker.py` with the listed scientific-Python dependencies.

## Relationship to prior work
Albanese, Bonet and Ricker (2015, Sections 3–4) prove compactness and describe the spectrum of ordinary Cesàro averaging on weighted sequence spaces, including exponentially decaying weights. We accept their compactness and spectral conclusions as prior art; the claim here is the **quantitative individual singular-value law**, its explicit elliptic coefficient, and critical Schatten endpoint. Zizler, Zuidwijk, Taylor and Arimoto (2002, Section 3) prove quantitative singular-value counts for finite Toeplitz matrices. That is the finite-block ingredient here, not a result about singular numbers of an infinite diagonally weighted Cesàro operator. Related general Toeplitz and pseudodifferential spectral principles may imply the unquantified leading law, so novelty is claimed for this operator-specific quantified result and exact constant rather than for a general Weyl principle.

## Limitations
The estimate is for each **fixed** \(q\in(0,1)\); constants are not uniform near the noncompact limit \(q=1\). The proof establishes an \(O_q(n^{-3/2}\log n)\) remainder, not an optimal second term. Exact finite singular values are not given in closed form. An undiscovered direct historical formula or a stronger quantitative weighted-Toeplitz theorem could reduce the novelty. Independent validation has not been performed.

## References
1. A. A. Albanese, J. Bonet, W. J. Ricker, *Spectrum and compactness of the Cesàro operator on weighted \(\ell_p\) spaces*, Journal of the Australian Mathematical Society 99 (2015), 287–314. DOI: https://doi.org/10.1017/S1446788715000221. Lawfully available author manuscript: https://jbonet.webs.upv.es/wp-content/uploads/2015/02/AlbaneseBonetRicker.pdf.
2. P. Zizler, R. A. Zuidwijk, K. F. Taylor, S. Arimoto, *A Finer Aspect of Eigenvalue Distribution of Selfadjoint Band Toeplitz Matrices*, SIAM J. Matrix Anal. Appl. 24 (2002), 59–67. DOI: https://doi.org/10.1137/S089547989834915X. Author-accessible full text: https://www.academia.edu/17245290/A_Finer_Aspect_of_Eigenvalue_Distribution_of_Selfadjoint_Band_Toeplitz_Matrices.
