# Sharp polynomial-annihilator spectra for Volterra integration

## Finding

Let \(J:L^2(0,1)\to L^2(0,1)\) be \((Jf)(x)=\int_0^x f(t)\,dt\). For each integer \(m\ge1\), let \(P_{<m}\) be the orthogonal projection onto algebraic polynomials of degree less than \(m\) and set \(T_m=J(I-P_{<m})\). Equivalently, \(T_m\) integrates functions with their first \(m\) polynomial moments removed. Write \(s_1(T_m)\ge s_2(T_m)\ge\cdots\) for the singular values, including multiplicity.

**Theorem.** The following assertions hold for every \(m\ge1\), with all norms on \(L^2(0,1)\):

1. The squared Hilbert–Schmidt norm is exactly
   \[
   \|T_m\|_{\mathcal S_2}^{2}=\sum_{j\ge1}s_j(T_m)^2=\frac{m}{2(4m^2-1)}.
   \]
2. For every fixed positive integer \(k\), the sharp leading singular-value limit is
   \[
   \lim_{m\to\infty}m\,s_k(T_m)=\frac12.
   \]
   In particular, \(\lim_{m\to\infty}m\|T_m\|=1/2\), and the scaled spectral edge has arbitrarily many singular values near \(1/2\).
3. For every real \(p>1\), the exact global Schatten-mass law is
   \[
   \boxed{\lim_{m\to\infty}m^{p-1}\sum_{j\ge1}s_j(T_m)^p
   =\frac{\Gamma((p+1)/2)}{2^p(p-1)\sqrt\pi\,\Gamma((p+2)/2)}.}
   \]
   For every fixed \(m\), \(T_m\in\mathcal S_p\) if and only if \(p>1\); the sums for \(0<p\le1\) diverge. The formula is valid for all real \(p>1\), not just even integers.

## Assumptions and scope

Lebesgue measure is unweighted on \((0,1)\). Functions may be real or complex. The polynomial projection is orthogonal in \(L^2\), not a nodal interpolant. The limit fixes \(p\) or \(k\) before sending the number of annihilated moments \(m\) to infinity. The full operator \(T_m\) remains infinite rank for every finite \(m\).

## Proof

**1. Exact coefficient matrix.** The normalized shifted Legendre functions \(e_n(x)=\sqrt{2n+1}\,P_n(2x-1)\), \(n\ge0\), form an orthonormal basis. The classical polynomial identity
\[
(2n+1)P_n(u)=P_{n+1}'(u)-P_{n-1}'(u)
\]
shows for every \(n\ge1\) that
\[
Je_n=a_n e_{n+1}-b_n e_{n-1},\qquad
 a_n=\frac1{2\sqrt{(2n+1)(2n+3)}},\quad
 b_n=\frac1{2\sqrt{(2n+1)(2n-1)}}.
\]
Thus the matrix of \(T_m\) consists of two first off-diagonals on input columns \(n\ge m\). The Gram matrix \(G_m=T_m^*T_m\) in those columns has precisely
\[
(G_m)_{nn}=a_n^2+b_n^2=\frac1{2(2n-1)(2n+3)},\qquad
(G_m)_{n,n+2}=(G_m)_{n+2,n}=-a_n b_{n+2},
\]
and all other entries zero. In particular, the two parity sectors decouple.

**2. Exact trace.** Telescoping the absolutely convergent diagonal series gives
\[
\operatorname{tr}G_m=\frac18\sum_{n=m}^{\infty}
 \left(\frac1{2n-1}-\frac1{2n+3}\right)
 =\frac18\left(\frac1{2m-1}+\frac1{2m+1}\right)
 =\frac{m}{2(4m^2-1)}.
\]
This equality is an infinite-dimensional trace identity, not an extrapolation from a finite matrix.

**3. A finite-window spectral-density lemma.** Fix \(R>1\) and let \(N_m=\lfloor Rm\rfloor\). Write \(T_{m,R}=J\Pi_{[m,N_m]}\), where \(\Pi\) is the orthogonal projector onto \(e_m,\ldots,e_{N_m}\), and \(G_{m,R}=T_{m,R}^*T_{m,R}\) on that finite-dimensional domain. For every continuous \(F\) on a common compact interval containing the spectra, with \(F(0)=0\),
\[
\lim_{m\to\infty}\frac1m\operatorname{tr}F(m^2G_{m,R})
=\frac1{2\pi}\int_1^R\int_0^{2\pi}
F\!\left(\frac{\sin^2\theta}{4x^2}\right)\,d\theta\,dx.\tag{1}
\]
To prove (1), first take \(F(z)=z^j\) for a positive integer \(j\). Each diagonal entry in the trace expansion is a sum of finitely many closed walks with steps \(0,\pm2\). At an index \(n\) whose distance to both endpoints exceeds \(2j\), the coefficients, after multiplying by \(m^2\), converge uniformly when \(n/m\) lies in a compact subinterval of \((1,R)\) to a constant-coefficient tridiagonal symbol with diagonal \(1/(8x^2)\) and adjacent parity-band entries \(-1/(16x^2)\). Its Fourier symbol is \((1-\cos2\theta)/(8x^2)=\sin^2\theta/(4x^2)\). At most \(4j+O(1)\) boundary indices have altered walks, all with uniformly bounded contributions, so their normalized total is \(o(1)\). The remaining sum is a Riemann sum. This proves (1) for polynomials with zero constant term. Since \(\|mT_{m,R}\|\) is uniformly bounded (see step 5), Weierstrass approximation, with the constant term removed, extends it to each such continuous \(F\).

**4. Global Schatten limits, including the infinite tail.** For \(p>1\), choose \(F(z)=z^{p/2}\) in (1). Its right side is
\[
\frac1{2^p}\left(\frac1{2\pi}\int_0^{2\pi}|\sin\theta|^p\,d\theta\right)
\int_1^R x^{-p}\,dx.
\]
The remaining columns form a pair of weighted unilateral shifts with coefficients bounded by \(C/n\); hence, by the triangle inequality for the Schatten \(p\)-norm,
\[
\|T_m-T_{m,R}\|_{\mathcal S_p}
\le 2\left(\sum_{n>N_m}(C/n)^p\right)^{1/p}
\le C_p(Rm)^{1/p-1}.
\]
Also \(\sup_m m^{1-1/p}\|T_m\|_{\mathcal S_p}<\infty\) by the same decomposition. The norm inequality therefore lets \(R\to\infty\) after \(m\to\infty\), without interchanging an uncontrolled infinite trace and a limit. Evaluate \(\int_1^\infty x^{-p}dx=1/(p-1)\) and
\[
\frac1{2\pi}\int_0^{2\pi}|\sin\theta|^p d\theta
=\frac{\Gamma((p+1)/2)}{\sqrt\pi\,\Gamma((p+2)/2)}
\]
to obtain assertion 3. For \(0<p\le1\), \(J-T_m=JP_{<m}\) has rank at most \(m\), while the classical singular values of \(J\) are \(1/((j-1/2)\pi)\). Finite-rank singular-value interlacing gives \(s_j(T_m)\sim1/(\pi j)\), proving the sharp fixed-\(m\) threshold.

**5. Sharp top-edge limit.** Decompose the coefficient matrix of \(T_m\) into its forward and backward weighted shifts. Their norms are at most \(a_m\) and \(b_m\), respectively; hence
\[
\limsup_{m\to\infty}m\|T_m\|\le
\lim_{m\to\infty}m(a_m+b_m)=\frac12.
\]
For every \(\varepsilon>0\), choose \(R>1\) sufficiently close to \(1\) that the measurable subset of \([1,R]\times[0,2\pi]\) with \(|\sin\theta|/(2x)>1/2-\varepsilon\) has positive measure. Applying (1) to continuous upper and lower approximations of the indicator of the corresponding squared-singular-value interval shows that the number of singular values of \(mT_{m,R}\) exceeding \(1/2-\varepsilon\) grows at least proportionally to \(m\). The min–max characterization and \(T_{m,R}=T_m\Pi_{[m,N_m]}\) imply the same fixed-index lower bound for \(m s_k(T_m)\) for all sufficiently large \(m\). The upper bound just proved completes assertion 2.

## Verification

The supplied standalone `check.py` runs using the Python standard library. It checks the exact rational Legendre-column norms and telescoping identities over 45 starting degrees and 34 endpoint choices, compares finite-window second and fourth singular moments to their rigorously derived Riemann limits, and constructs explicit alternating-coefficient lower witnesses together with shift upper bounds. Its recorded output is in `checks.txt`. These checks do not replace the global trace, density, tail or min–max arguments above.

For independent reproduction, calculate the two shifts from \(a_n,b_n\), form finite Gram sections with diagonal \(a_n^2+b_n^2\) and second off-diagonal \(-a_nb_{n+2}\), and compare with (1). The checker uses no external libraries.

## Relationship to prior work

Classical Volterra singular values and the Legendre antiderivative recurrence are established background. Tohidi, Samadi and Shateyi (first published 12 August 2014) develop Legendre spectral collocation and convergence estimates for nonlinear Volterra equations. Stenger (2018) studies integration-operator identities and finite Legendre interpolation matrices. Gutleb and Olver (2019) exploit sparse orthogonal-polynomial representations of Volterra integral equations, including Toeplitz connections. Generalized locally Toeplitz theory (Serra-Capizzano, 2003) supplies a broader formal framework for local singular distributions of finite matrices. The present statement instead specifies the high-degree orthogonal *input annihilator*, exact infinite Hilbert–Schmidt energy, all-real-exponent infinite Schatten-mass limit, and every fixed top singular value including a separate spectral-edge argument. The local-density step is related to established Toeplitz principles and is not claimed as a new general theorem.

## Limitations

No closed formula is claimed for each finite-degree singular value, no rate of convergence is asserted for the scaled Schatten-mass limits, and no uniformity as \(p\downarrow1\) or \(k\to\infty\) is asserted. General orthogonal-polynomial weights and non-Lebesgue measures are not covered. Broader locally Toeplitz theory may permit a shorter alternative deduction of the bulk limit; historic-priority comparisons remain incomplete. The mathematical arguments and numerical checks have not received independent expert validation.

## References

1. E. Tohidi, O. R. Navid Samadi, and S. Shateyi, *Convergence Analysis of Legendre Pseudospectral Scheme for Solving Nonlinear Systems of Volterra Integral Equations*, Abstract and Applied Analysis (2014), article 307907. DOI: https://doi.org/10.1155/2014/307907 (first published 2014-08-12).
2. F. Stenger, *Indefinite Integration Operator Identities and their Polynomial Approximations*, arXiv:1809.05607 (first version 2018-09-14), https://arxiv.org/abs/1809.05607.
3. T. S. Gutleb and S. Olver, *A sparse spectral method for Volterra integral equations using orthogonal polynomials on the triangle*, arXiv:1906.03907 (first version 2019-06-10), https://arxiv.org/abs/1906.03907.
4. S. Serra-Capizzano, *Generalized locally Toeplitz sequences: spectral analysis and applications to discretized partial differential equations*, Linear Algebra Appl. 366 (2003), 371–402, https://doi.org/10.1016/S0024-3795(02)00504-9.
5. NIST Digital Library of Mathematical Functions, §18.17, integrals of classical orthogonal polynomials, https://dlmf.nist.gov/18.17.
6. V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numerical Functional Analysis and Optimization 17 (1996), 453–461, https://doi.org/10.1080/01630569608816704.
