# Logarithmic radial weights restore the critical Schatten eigenarc endpoints of a Bergman channel

## Finding

For every \(b>0\), \(\gamma\in\mathbb R\), and \(1\le p<\infty\), consider the radial weight
\[
 w_{b,\gamma}(z)=C_{b,\gamma}(1-|z|^2)^{b-1}
 \left[\log\frac{e}{1-|z|^2}\right]^\gamma,
 \qquad \int_{\mathbb D}w_{b,\gamma}\,dA=1.
\]
Let \(\Psi_{b,\gamma}\) be the unital completely positive harmonic-Toeplitz map of Panja, and let \(\mathcal D_p\) be the diagonal Schatten ideal in the orthonormal monomial basis. Put \(\omega_n=\int_{\mathbb D}|z|^{2n}w_{b,\gamma}\,dA\), \(\rho=\omega_1\), and, for \(0<\theta<\pi\),
\[
 \lambda_\theta=1-\rho+\rho e^{i\theta},\qquad t_\theta=1-\cos\theta.
\]
There is a unique formal diagonal eigenoperator of \(\Psi_{b,\gamma}\) at \(\lambda_\theta\), up to scalar. With first diagonal entry one, its entries satisfy
\[
 \boxed{|x_n|\sim K_{b,\gamma,\theta}\,
 n^{-bt_\theta}(\log n)^{\gamma t_\theta}},\qquad 0<K_{b,\gamma,\theta}<\infty.
\]
Consequently, **the exact nonreal boundary eigenvalue criterion** on \(\mathcal D_p\) is
\[
 \boxed{\lambda_\theta\in\sigma_{\rm point}(\Psi_{b,\gamma}|_{\mathcal D_p})
 \iff pbt_\theta>1\quad\text{or}\quad[pbt_\theta=1\ \text{and}\ p\gamma t_\theta<-1].}
\]
The same holds at the conjugate boundary value. In particular, whenever \(2pb>1\), the two critical angles satisfying \(t_\theta=1/(pb)\) produce genuine Schatten eigenoperators **if and only if** \(\gamma<-b\). Thus the critical boundary eigenvalues excluded by the pure power weight \(\gamma=0\) become included after sufficient logarithmic suppression of the weight near the circle.

## Assumptions and scope

The area measure is \(dA=\pi^{-1}dx\,dy\). The normalization constant is the reciprocal of \(\int_0^1t^{b-1}[\log(e/t)]^\gamma\,dt\), finite and strictly positive. The weight is admissible in Panja's sense. The Hilbert space is the analytic weighted Bergman space with basis \(e_n=z^n/\sqrt{\omega_n}\). The space \(\mathcal D_p=\{\operatorname{diag}(x_n):(x_n)\in\ell^p\}\), \(p\ge1\), inherits the Schatten norm. The claim concerns this invariant diagonal ideal, not the full ideal of all matrices. The restriction \(0<\theta<\pi\) excludes the fixed-point value and the real left endpoint, where a terminating product can require separate treatment.

## Proof

**1. Exact diagonal reduction.** For a normalized admissible radial weight, set \(\delta_n=\omega_n/\omega_{n+1}\). Panja's formula is
\[
 \Psi(X)=\omega_1\left[S'^*XS'+\sum_{k\ge1}(\delta_{k-1}-\delta_k)Q_kXQ_k\right].
\]
Since \(S'e_n=\sqrt{\delta_n}e_{n+1}\) and \(Q_ke_n=\mathbf1_{n\ge k}e_n\), direct substitution and telescoping give
\[
 (\Psi\operatorname{diag}x)_{nn}=\rho\delta_n x_{n+1}+(1-\rho\delta_n)x_n.
 \tag{1}
\]
The coefficients are uniformly bounded, hence the diagonal \(\ell^p\) class is invariant for all \(1\le p<\infty\). Write \(r_n=\omega_{n+1}/\omega_n\in(0,1)\). At \(\lambda_\theta=1-\rho+\rho e^{i\theta}\), the equation \(\Psi X=\lambda_\theta X\) becomes
\[
 x_{n+1}=[(1-r_n)+e^{i\theta}r_n]x_n,
 \quad x_0=1.
 \tag{2}
\]
Its nonreal multiplier never vanishes, so every nonzero solution is a scalar multiple of this one.

**2. Precise moment scale.** With \(t=1-|z|^2\),
\[
 \omega_n=C_{b,\gamma}\int_0^1(1-t)^n t^{b-1}[\log(e/t)]^\gamma\,dt.
\]
Set \(u=nt\), split at \(u=\sqrt n\), and apply dominated convergence on the first part; the second is exponentially negligible. This gives
\[
 \omega_n\sim C_{b,\gamma}\Gamma(b)n^{-b}(\log n)^\gamma.
 \tag{3}
\]
Applying the same argument with \(t^b\) gives
\[
 \omega_n-\omega_{n+1}\sim C_{b,\gamma}\Gamma(b+1)n^{-b-1}(\log n)^\gamma.
\]
Therefore \(\varepsilon_n:=1-r_n=(\omega_n-\omega_{n+1})/\omega_n\sim b/n\), so \(\sum_n\varepsilon_n^2<\infty\).

**3. Boundary multiplier comparison.** Let \(a=e^{i\theta}\) and \(t_\theta=1-\operatorname{Re}a>0\). As \(\varepsilon\to0\), uniformly for each fixed angle,
\[
 \log|a+(1-a)\varepsilon|=-t_\theta\varepsilon+O(\varepsilon^2),
 \qquad\log(1-\varepsilon)=-\varepsilon+O(\varepsilon^2).
\]
The summability just proved implies that the infinite product
\[
 K'_{b,\gamma,\theta}=\prod_{n=0}^\infty
 \frac{|(1-r_n)+a r_n|}{r_n^{t_\theta}}
\]
converges to a finite strictly positive number. Since \(\omega_0=1\) and \(\prod_{j=0}^{n-1}r_j=\omega_n\), equation (2) yields
\[
 |x_n|\sim K'_{b,\gamma,\theta}\,\omega_n^{t_\theta}.
 \tag{4}
\]
Combining (3)–(4) gives the asserted constant \(K=K'[C_{b,\gamma}\Gamma(b)]^{t_\theta}\) and exact asymptotic.

**4. Sharp ideal criterion.** The diagonal operator belongs to \(\mathcal S_p\) exactly when \(\sum_n|x_n|^p<\infty\). Equations (3)–(4) reduce this to the convergence of
\[
 \sum_{n\ge2}n^{-pbt_\theta}(\log n)^{p\gamma t_\theta}.
\]
The integral test proves the stated dichotomy, including the equality case. When \(pbt_\theta=1\), the logarithmic condition becomes precisely \(\gamma/b<-1\). For \(2pb>1\), there is a unique angle in \((0,\pi)\) with \(t_\theta=1/(pb)\), and the conjugate eigenvalue has the same modulus profile. This proves the theorem.

## Verification

Equations (1) and (2) follow by direct monomial-basis calculation, without numerical approximation. The moment difference is the same integral with one extra power of \(t\), supplying the critical \(b/n\) ratio required for the infinite-product argument. The proof compares the *actual* eigenoperator coefficients, not only approximate spectral points. For the illustrative case \(b=1\), \(\gamma=-2\), \(p=2\), and \(\theta=\pi/3\), the theorem gives \(|x_n|^2\asymp[n(\log n)^2]^{-1}\); direct numerical quadrature at finite indices corroborates the positive limit in (4), but the infinite-dimensional claim follows from the integral and product proof.

## Relationship to prior work

Panja's 2026 preprint constructs the completely positive map and characterizes its fixed points; it does not classify logarithmically corrected Schatten boundary eigenoperators. The existing Hilbert–Schmidt boundary eigenarc classification for the ordinary Bergman weight and the beta-weighted diagonal Schatten classification already prove the **strict power-weight boundary inequality** and exclude its equality case. These results are credited, not relabelled as new. The present theorem isolates a distinct, sharp endpoint phenomenon unavailable in those power-weight families: for \(\gamma<-b\), critical nonreal boundary eigenoperators enter the Schatten class. Blaschke's earlier work establishes asymptotics for logarithmic Bergman weights, not the channel's eigenoperator boundary criterion. The proof technique uses classical Laplace asymptotics and products; no general novelty is claimed for those methods.

## Limitations

Only nonreal boundary eigenvalues on the diagonal Schatten subspace are classified; the real boundary endpoints, the complete channel spectrum, the full off-diagonal Schatten ideal, and general admissible radial weights outside this specific logarithmic family are not treated. The originality assessment is based on the named comparisons; implicit coverage by a broader weighted-shift theorem or unindexed analysis cannot be excluded. No independent mathematical audit has been performed.

## References

1. S. Panja, *Toeplitz operators with bounded harmonic symbols on weighted Bergman spaces are the fixed points of a normal unital completely positive map*, arXiv:2611.09731v1, first posted 2026-11-06, especially eqs. (1.9), (4.10) and Theorem 4.5. https://arxiv.org/abs/2611.09731
2. P. Blaschke, *Asymptotic behavior of Bergman kernels with logarithmic weight*, J. Math. Anal. Appl. 385 (2012), 293–302, doi:10.1016/j.jmaa.2011.06.044, especially §2.
3. *A boundary eigenarc for the Hilbert–Schmidt spectrum of a Bergman completely positive map*, published-finding corpus (2026-11-17), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-boundary-eigenarc-for-the-hilbert-schmidt-spectrum-of-a-bergma--0ea8587b2d0c.
4. *Sharp Schatten boundary eigenarcs for beta-weighted Bergman harmonic-Toeplitz dynamics*, prior research statement on beta-weighted diagonal Schatten spectra (2026), cited for its beta-weighted scope only.
