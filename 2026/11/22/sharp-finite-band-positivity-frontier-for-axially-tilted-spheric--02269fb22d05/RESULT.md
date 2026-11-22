# Sharp finite-band positivity frontier for axially tilted spherical heat covariance

## Finding

Let \(S^2\) carry normalized surface area, fix \(t>0\), and let \(H_t\) be its positive heat kernel at time \(t\) for the nonpositive Laplace–Beltrami operator. For real \(\varepsilon\) set
\[
K_{t,\varepsilon}(x,y)=H_t(x,y)\,[1+\varepsilon(x_3+y_3)].
\]
Let \(P_L\) be the orthogonal projection onto spherical harmonics of degrees \(0,\ldots,L\), and let \(T_{t,\varepsilon}\) be the integral operator with kernel \(K_{t,\varepsilon}\). For every integer \(L\ge1\), define the real symmetric \((L+1)\)-square Jacobi matrix \(J_{L,t}\) with diagonal zero and adjacent entries
\[
(J_{L,t})_{\ell,\ell+1}=\frac{2(\ell+1)\cosh(t(\ell+1))}{\sqrt{(2\ell+1)(2\ell+3)}}
\quad(0\le\ell<L).
\]
Write \(\Lambda_L(t)=\lambda_{\max}(J_{L,t})\). Then the finite harmonic compression \(P_LT_{t,\varepsilon}P_L\), **as a quadratic form on its full degree-\(\le L\) range**, is positive semidefinite exactly when
\[
\boxed{|\varepsilon|\le\varepsilon_L(t):=\Lambda_L(t)^{-1}.}
\]
At either sharp endpoint its nullity within that range is exactly one. The sequence \(\varepsilon_L(t)\) strictly decreases to zero. Every fixed nonzero \(\varepsilon\) makes the full kernel indefinite on finite point configurations, and its compact integral operator has infinitely many negative eigenvalues, even if \(|\varepsilon|<1/2\) makes every kernel value strictly positive.

There is an explicit **sharp spectral boundary layer**. For \(0<q<1\), let \(B_q\) be the compact self-adjoint half-line Jacobi operator on \(\ell^2(\mathbb N_0)\) with zero diagonal and offdiagonal \((B_q)_{j,j+1}=q^j\). Its largest eigenvalue \(\rho(q)>0\) is simple and satisfies \(\sqrt{1+q^2}<\rho(q)<1+q\). For each fixed \(t>0\),
\[
\boxed{\varepsilon_L(t)=\frac{2e^{-tL}}{\rho(e^{-t})}\left(1-\frac{1}{8L^2}+O_t(L^{-3})\right),\qquad L\to\infty.}
\]
Thus the cutoff is exponentially small in the bandlimit, with a nontrivial geometric-Jacobi prefactor and a universal relative second-order coefficient \(-1/8\).

## Assumptions and scope

The sphere is \(S^2=\{x\in\mathbb R^3:|x|=1\}\), and surface probability \(\sigma\) is used throughout. Complex spherical harmonics \(Y_{\ell m}\) are orthonormal in \(L^2(\sigma)\), for integers \(\ell\ge0\), \(-\ell\le m\le\ell\). The heat kernel is specified without normalization ambiguity by the uniformly convergent expansion
\[
H_t(x,y)=\sum_{\ell=0}^\infty e^{-t\ell(\ell+1)}\sum_{m=-\ell}^{\ell}Y_{\ell m}(x)\overline{Y_{\ell m}(y)}.
\]
The finite-band object is the **double compression** of the full perturbed operator. It is not the product of a truncated heat-kernel series and the latitude factor, which is a different finite-rank operator. Positive semidefiniteness of a continuous kernel means positivity of Gram forms for arbitrary finite sets with complex coefficients. All large-\(L\) estimates fix \(t>0\); no uniformity as \(t\downarrow0\) is asserted.

## Proof

**1. Exact harmonic block reduction.** Write \(D=T_{H_t}\) and let \(M\) multiply by \(x_3\). The defining operator identity is
\[
T_{t,\varepsilon}=D+\varepsilon(MD+DM).
\]
Here \(D Y_{\ell m}=d_\ell Y_{\ell m}\) with \(d_\ell=e^{-t\ell(\ell+1)}>0\). Latitude multiplication has only adjacent-degree entries within fixed azimuthal order,
\[
\langle Y_{\ell+1,m},MY_{\ell m}\rangle
=a_{\ell m}:=\sqrt{\frac{(\ell+1)^2-m^2}{(2\ell+1)(2\ell+3)}}.
\]
On \(P_LL^2\) the positive diagonal \(D_L=P_LDP_L\) is invertible. The congruent form
\[
D_L^{-1/2}(P_LT_{t,\varepsilon}P_L)D_L^{-1/2}=I+\varepsilon\mathcal J_{L,t}
\]
has a direct sum of Jacobi blocks indexed by \(m\), with offdiagonals
\[
a_{\ell m}\left(\sqrt{d_\ell/d_{\ell+1}}+\sqrt{d_{\ell+1}/d_\ell}\right)
=2a_{\ell m}\cosh(t(\ell+1)),\quad |m|\le\ell<L.
\]
The \(m=0\) block is \(J_{L,t}\). For every nonzero \(|m|\), its entries are strictly smaller than the corresponding principal subpath entries of the zonal block. A zero-diagonal Jacobi block with positive adjacent weights has spectral symmetry about zero; its spectral radius is its simple positive Perron eigenvalue. Entrywise comparison of Perron quotients, followed by strictness for proper subpaths, shows that \(\mathcal J_{L,t}\) has exactly one positive eigenvalue of maximum modulus, \(\Lambda_L(t)\), and exactly one negative eigenvalue \(-\Lambda_L(t)\). Consequently \(I+\varepsilon\mathcal J_{L,t}\succeq0\) exactly at the claimed interval, and either endpoint has nullity one. Because \(J_{L,t}\) is a proper principal submatrix of the irreducible \(J_{L+1,t}\), its largest eigenvalue increases strictly with \(L\), so \(\varepsilon_L(t)\) decreases strictly.

**2. Failure and infinite negative index beyond every finite cutoff.** The zonal adjacent edge between degrees \(\ell\) and \(\ell+1\) has normalized weight
\[
w_\ell=2a_{\ell0}\cosh(t(\ell+1))\to\infty.
\]
Its two-by-two preconditioned principal matrix is \(\left(\begin{smallmatrix}1&\varepsilon w_\ell\\\varepsilon w_\ell&1\end{smallmatrix}\right)\), which has a negative direction as soon as \(|\varepsilon|w_\ell>1\). Choose infinitely many such edges with left endpoints \(\ell=3j\). Their two-dimensional harmonic supports are separated by at least one unselected degree; the quadratic form has no coupling between different pairs, since latitude changes degree only by one. One negative vector per pair therefore spans arbitrarily large negative definite subspaces. The original operator is compact and self-adjoint, indeed trace class because \(D\) is trace class and \(M\) is bounded. The min–max principle now gives infinitely many negative eigenvalues. Continuity of \(K_{t,\varepsilon}\) and quadrature approximation of a smooth negative test-density form produce a finite point-configuration Gram witness. Since \(H_t(x,y)>0\) and \(1+\varepsilon(x_3+y_3)>0\) for \(|\varepsilon|<1/2\), such examples may even have everywhere-positive kernel values.

**3. Compact boundary operator.** Set \(q=e^{-t}\) and consider \(B_q\) as above. Since its offdiagonals tend geometrically to zero, it is compact. Its top eigenvalue is positive and simple: compactness gives an eigenvector at the positive spectral maximum; replacing its entries by absolute values cannot lower its Rayleigh quotient, so a nonnegative maximizing vector exists. The three-term eigenvector recurrence and strictly positive adjacent weights force every entry positive, while the left-end recurrence determines the entire eigenvector from its first entry, proving simplicity. Its first three-by-three principal section has largest eigenvalue \(\sqrt{1+q^2}\), strictly below the infinite top eigenvalue because the next offdiagonal is nonzero. The largest row sum is \(1+q\), giving \(\rho(q)\le1+q\); strict inequality follows from the positive top eigenvector and the smaller zeroth row sum (equality would force a constant maximum along the connected graph).

**4. Exact edge normalization and the \(L^{-2}\) correction.** Reverse the zonal matrix order \(\ell\mapsto L-\ell\), divide by its final offdiagonal \(w_{L-1}\), and embed it by zeros into \(\ell^2(\mathbb N_0)\). The reversed edge between indices \(j\) and \(j+1\), for \(0\le j<L\), equals
\[
r_{L,j}=\frac{a_{L-1-j,0}}{a_{L-1,0}}\frac{\cosh(t(L-j))}{\cosh(tL)}.
\]
For \(j\le L/2\), the elementary exact identity
\[
a_{k,0}=\frac12\left(1-\frac{1}{4(k+1)^2}\right)^{-1/2}
\]
implies \(a_{L-1-j,0}/a_{L-1,0}=1+O((j+1)L^{-3})\), while
\[
\frac{\cosh(t(L-j))}{\cosh(tL)}=q^j(1+O_t(e^{-tL})).
\]
For \(j>L/2\), the same cosh ratio is at most \(2q^j\), and the bounded ratio of the \(a\)-coefficients contributes only a fixed factor. The omitted infinite edges of \(B_q\) are at most \(q^L\). Consequently
\[
\sup_{j\ge0}|r_{L,j}-q^j|=O_t(L^{-3}),
\qquad \left\|\frac{R_LJ_{L,t}R_L^*}{w_{L-1}}-B_q\right\|=O_t(L^{-3}),
\]
where \(R_L\) is degree reversal followed by the zero embedding. Since both matrices are self-adjoint, their largest eigenvalues differ by at most their operator-norm distance. Thus
\[
\Lambda_L(t)=w_{L-1}\,[\rho(q)+O_t(L^{-3})].
\]
Finally
\[
\frac1{w_{L-1}}=\frac{\sqrt{1-1/(4L^2)}}{\cosh(tL)}
=2e^{-tL}\left(1-\frac1{8L^2}+O_t(L^{-4}+e^{-2tL})\right).
\]
Taking the reciprocal of \(\Lambda_L(t)\) proves the stated expansion with \(O_t(L^{-3})\) relative error. This last estimate is the critical nontrivial limit; a fixed-size numerical truncation alone would not justify it.

## Verification

As low-degree normalization checks, \(\varepsilon_1(t)=\sqrt3/(2\cosh t)\) and \(\varepsilon_2(t)=[(4/3)\cosh^2t+(16/15)\cosh^2(2t)]^{-1/2}\). `CHECKER.py` provides a standalone numerical check of the exact zonal-block reduction, strict cutoff monotonicity, sample comparisons against all nonzonal blocks, the compact Jacobi eigenvalue approximation, and the universal second-order coefficient at increasing bandlimits. Execute `python3 CHECKER.py` with Python 3 and NumPy/SciPy installed. These tests corroborate finite identities but do not prove arbitrary-band claims; the preceding analytic argument supplies the proof.

## Relationship to prior work

Buhmann and Jäger (2021 preprint; 2022 article) develop positive-definite spherical harmonic coefficient-matrix and axial block criteria. Their criterion is consistent with the tridiagonal reduction here, but it does not give the sharp heat-band cutoff, its geometric Jacobi boundary constant, or the \(-1/8\) correction. A previously published result on **spherical Poisson** axial tilts has a nonzero full-kernel admissibility interval and finite-band Legendre-zero thresholds. Its normalized adjacent-degree weights are constant, unlike the exponentially increasing spherical heat weights here, so its positive threshold and Legendre-root law cannot imply this theorem. The broader 2024 axially symmetric space-time covariance framework provides structural context, not an identified version of this particular finite-band heat result; its complete text was not inspected and is recorded as a priority risk.

The qualitative loss of full positive definiteness under exponentially decaying heat multipliers can also be seen from classical neighboring-eigenvalue-ratio tests and should **not** be treated as the novel component in isolation. The specific sharp all-band positivity formula and its limiting compact Jacobi spectral law, including the explicit next-order coefficient, constitute the new quantitative claim.

## Limitations

Only standard heat multipliers \(e^{-t\ell(\ell+1)}\) on \(S^2\), real first-order latitude amplitude modulation, and double degree-cutoff compression are addressed. The boundary expansion holds for each fixed \(t>0\), not uniformly in joint small-time/high-band regimes. The constant \(\rho(e^{-t})\) is specified intrinsically by a compact Jacobi operator rather than in elementary closed form. Complete historical priority is provisional, especially against specialized Jacobi asymptotics and the uninspected full text of a related 2024 axial covariance article. This is a mathematical same-document verification, not independent scientific validation.

## References

1. M. Buhmann and J. Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, arXiv:2105.02586 (first submitted 2021-05-06), https://arxiv.org/abs/2105.02586; *Journal of Fourier Analysis and Applications* **28** (2022), article 40, https://doi.org/10.1007/s00041-022-09913-x.
2. M. Buhmann and J. Jäger, *Strictly positive definite kernels on the 2-sphere: from radial symmetry to eigenvalue block structure*, *IMA Journal of Numerical Analysis* **42** (2022), 1500–1525, first online 2021-05-03, https://doi.org/10.1093/imanum/drab012.
3. X. Emery, J. Jäger, E. Porcu, *Positive semidefinite kernels that are axially symmetric on the sphere and stationary in time: spectral and semi-spectral theory, and constructive approaches*, *Stochastic Environmental Research and Risk Assessment* **38** (2024), 2315–2329, https://doi.org/10.1007/s00477-024-02681-8.
4. *Sharp axial tilts of spherical Poisson covariances: a dimension-free positivity threshold and universal critical kernels*, research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-axial-tilts-of-spherical-poisson-covariances-a-dimension-f--2c30314f81a3.
