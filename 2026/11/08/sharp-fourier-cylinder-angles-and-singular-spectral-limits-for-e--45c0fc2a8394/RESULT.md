# Sharp Fourier–cylinder angles and singular spectral limits for even-base Cantor measures

## Finding
Let \(b\ge4\) be an even integer. Consider the probability measure \(\mu_b\) on the real line given by the law of \(X_b=\sum_{j\ge1}\varepsilon_jb^{-j}\), where the signs \(\varepsilon_j\) are independent and equiprobable. In \(L^2(\mu_b)\), let \(C_m\) be the \(2^m\)-dimensional space of functions constant on each cylinder specified by the first \(m\) signs. Let \(E_m\) be the span of the \(2^m\) exponentials \(e_{\lambda}(x)=e^{2\pi i\lambda x}\) for
\[
\Lambda_{b,m}=\left\{\frac b4\sum_{j=0}^{m-1}a_jb^j:a_j\in\{0,1\}\right\},\qquad m\ge1.
\]
Write
\[
F_b(t)=\prod_{j=1}^{\infty}\cos\left(\frac{2\pi t}{b^j}\right),\quad
\tau_b=\frac{b}{4(b-1)},\quad
\beta_b=F_b(\tau_b)>0.
\]
**Complete principal-angle law.** The \(2^m\) cosines of the principal angles between \(C_m\) and \(E_m\), counted with multiplicity, are precisely
\[
\left\{F_b\left(\frac{\lambda}{b^m}\right):\lambda\in\Lambda_{b,m}\right\}.
\]
In particular the maximum is \(1\) and the **smallest cosine**, with no genericity qualification, is exactly
\[
\beta_{b,m}=F_b\bigl(\tau_b(1-b^{-m})\bigr),\qquad
\beta_{b,m}>\beta_b,\quad\beta_{b,m}\downarrow\beta_b.
\]
Thus the orthogonal projection \(P_{E_m}:C_m\longrightarrow E_m\) is invertible onto its image with sharp lower bound \(\beta_{b,m}\), sharp inverse norm \(\beta_{b,m}^{-1}\), and exact projector gap
\[
\|P_{E_m}-P_{C_m}\|=\sqrt{1-\beta_{b,m}^{2}}.
\]
The best bound uniform over all levels is \(\beta_b\), not attained at any finite level. Moreover
\[
\beta_{b,m}-\beta_b=c_b b^{-m}+O_b(b^{-2m}),
\quad c_b=-\tau_b F_b'(\tau_b)>0.
\]
**Singular-continuous limiting angle spectrum.** Let \(T_b=(b/4)\sum_{j\ge1}\xi_jb^{-j}\) for independent fair digits \(\xi_j\in\{0,1\}\). The empirical measures of the \(2^m\) principal-angle cosines converge weakly to the law of \(F_b(T_b)\). That law is non-atomic and singular with respect to Lebesgue measure. For every real-valued 1-Lipschitz function \(h\) on \([\beta_b,1]\), the difference between the empirical average of \(h\) and its limiting expectation is at most
\[
L_b\tau_b b^{-m},\qquad
L_b=\sup_{0\le t\le\tau_b}|F_b'(t)|<\infty.
\]
Finally, as the even base tends to infinity,
\[
1-\beta_b=\frac{\pi^2}{8(b-1)^2}+O(b^{-4}),\qquad
\sqrt{1-\beta_b^2}=\frac{\pi}{2(b-1)}+O(b^{-3}).
\]
For the middle-fourth measure, \(\beta_4=0.858126088709\ldots\). The associated limiting worst projector gap is \(0.513439008916\ldots\).

## Assumptions and scope
The assertions hold for every even integer \(b\ge4\) and every positive integer \(m\), with no restriction on cylinder word or choice of basis ordering. Inner products and all operator norms are those of complex \(L^2(\mu_b)\). Cylinder means are with respect to the fair Bernoulli measure. This is a comparison of *equal-dimensional spatial and spectral truncations*, not a statement about the strong or pointwise convergence rate of arbitrary Fourier partial sums. Frequencies may be half-integers when \(b\equiv2\pmod4\); no artificial integrality assumption is imposed.

## Proof
**(1) Fourier product and normalized bases.** Independence of the signs gives \(\widehat\mu_b(t)=F_b(t)\) for the convention \(\widehat\mu_b(t)=\int e^{-2\pi itx}\,d\mu_b(x)\). Absolute and locally uniform convergence follows because \(1-\cos(2\pi t/b^j)=O_K(b^{-2j})\) on every compact \(K\). For a cylinder word \(\omega=(\omega_1,\ldots,\omega_m)\in\{-1,1\}^m\), write \(s_\omega=\sum_{j=1}^m\omega_jb^{-j}\); conditional on that word, \(X_b=s_\omega+b^{-m}X_b'\) with independent copy \(X_b'\). The normalized indicators \(\phi_\omega=2^{m/2}\mathbf 1_{\{\varepsilon_1=\omega_1,\ldots,\varepsilon_m=\omega_m\}}\) form an orthonormal basis of \(C_m\).

For distinct frequencies \(\lambda,\eta\in\Lambda_{b,m}\), let \(r\in\{0,\ldots,m-1\}\) be the least digit position at which they differ. Then \(\lambda-\eta=(b/4)b^r u\), where \(u\) is odd because \(b\) is even. Hence
\[
\cos\left(\frac{2\pi(\lambda-\eta)}{b^{r+1}}\right)
=\cos\left(\frac{\pi u}{2}\right)=0.
\]
Thus the \(e_\lambda\) form an orthonormal basis of \(E_m\) (the required factor appears in the Fourier product, and all exponential norms are one).

**(2) Exact cross-Gram diagonalization.** Use the inner product conjugate-linear in its first entry. Conditional expectation on one cylinder yields
\[
K_{\lambda,\omega}=\langle e_\lambda,\phi_\omega\rangle
=2^{-m/2}e^{-2\pi i\lambda s_\omega}
F_b(\lambda/b^m).
\]
Let \(B_{\lambda,\omega}=2^{-m/2}e^{-2\pi i\lambda s_\omega}\). The inner product of distinct rows \(\lambda,\eta\) of \(B\) equals
\[
2^{-m}\sum_{\omega}e^{-2\pi i(\lambda-\eta)s_\omega}
=\prod_{j=1}^m\cos\left(\frac{2\pi(\lambda-\eta)}{b^j}\right)=0
\]
by the same least-differing-digit argument; diagonal row norms are one. Since \(B\) is square, it is unitary. Therefore \(K=\operatorname{diag}(F_b(\lambda/b^m))B\), proving the full singular-value claim. All diagonal factors are positive: \(0\le\lambda/b^m\le\tau_b(1-b^{-m})\), and for \(0\le t\le\tau_b\) every cosine argument lies in \([0,\pi/(2(b-1))]\subset[0,\pi/6]\). These singular values are precisely the principal-angle cosines; in particular the projection-restriction map has the stated sharp bound.

**(3) Extremal sharpness.** Each cosine factor is strictly decreasing on \((0,\tau_b]\), so \(F_b\) is strictly decreasing there. The largest frequency is \(\lambda_{\max}=(b/4)(b^m-1)/(b-1)\), yielding the least singular value \(\beta_{b,m}\). The smallest frequency \(0\) yields singular value one. Taylor expansion of the continuously differentiable positive function \(F_b\) at \(\tau_b\) gives the stated \(b^{-m}\) correction and the strict positive coefficient. For equal-dimensional finite subspaces, the norm of the difference of orthogonal projections equals the sine of their largest principal angle, which proves the exact projector gap.

**(4) Limit law.** Reverse the independent binary digits in the finite set \(\Lambda_{b,m}\). Uniformly sampling \(\lambda\) is equivalent to sampling
\[
T_{b,m}=\frac b4\sum_{j=1}^m\xi_j b^{-j}.
\]
Couple these truncated digits to \(T_b\) using the same infinite digit sequence. Then \(|T_b-T_{b,m}|\le\tau_b b^{-m}\) almost surely. Since \(F_b\) is \(L_b\)-Lipschitz on \([0,\tau_b]\), the displayed quantitative weak-convergence bound follows. The base-\(b\) digit set has Hausdorff dimension at most \(\log2/\log b<1\); its image under the Lipschitz map \(F_b\) is Lebesgue-null. The distribution is non-atomic since the digit law has no atoms and \(F_b\) is strictly injective, hence its limit is singular continuous.

**(5) Large-base asymptotics.** At \(t=\tau_b\), the first product factor is \(\cos(\pi/[2(b-1)])\). All remaining factors multiply to \(1+O(b^{-4})\), by \(\sum_{j\ge2}(2\pi\tau_b/b^j)^2=O(b^{-4})\). Expanding the first cosine proves the formula for \(1-\beta_b\). Taking the square root of \(1-\beta_b^2\) gives the claimed projector-gap expansion.

## Verification
The standalone `CHECK.py` uses direct finite Fourier/cylinder cross-Gram matrices, numerical singular-value decomposition, exact integer leading-digit parity tests, separate finite-tail cylinder quadrature, and digit-coupling bounds. Run `python CHECK.py` with NumPy. Its finite verification does not prove infinite statements: steps (1)–(5) provide the proof for every level and base. The numerical constants are approximations of convergent infinite products, not definitions by finite truncation.

## Relationship to prior work
Jorgensen and Pedersen established the existence of orthonormal exponential spectra for scale-four and more general self-similar measures, including the foundational finite Hadamard pairing and Fourier-product identities. Strichartz studied the resulting mock Fourier expansions. Tang and Wu (first posted July 30, 2026) proved the endpoint weak-type maximal inequality for the middle-fourth measure and worked explicitly with digit cylinders and Fourier Dirichlet kernels. The present statement concerns a different invariant: the entire cross-filtration principal-angle spectrum, its sharp uniform conditioning for all even bases, and its singular-continuous asymptotic law. The Hadamard pairing and self-similar Fourier product are used as established ingredients, not claimed as new. An equivalent reformulation in broader Hadamard-filter literature remains a possible priority risk.

## Limitations
No pointwise-convergence or maximal-function estimate is claimed. This result does not treat uneven Bernoulli digit weights, odd bases, or arbitrary noncanonical spectral sets. It gives exact Hilbert-space angles, not \(L^1\) conditioning. The principal-angle spectrum is a new comparison of two familiar filtrations; its elementary factorization might be implicit in older general filter-bank treatments not fully available for inspection. Independent audit and publication-priority determination have not been performed.

## References
1. M.-W. Tang and Z.-Y. Wu, *Almost everywhere convergence of mock Fourier series for the middle-fourth Cantor measure*, arXiv:2607.27796 (first posted 2026-07-30), https://arxiv.org/abs/2607.27796.
2. P. E. T. Jorgensen and S. Pedersen, *Dense analytic subspaces in fractal \(L^2\)-spaces*, arXiv:funct-an/9709007 (first posted 1997-09-30), https://arxiv.org/abs/funct-an/9709007.
3. R. S. Strichartz, *Mock Fourier series and transforms associated with certain Cantor measures*, Journal d'Analyse Mathématique **81** (2000), 209–238, https://doi.org/10.1007/BF02788990.
4. R. S. Strichartz, *Convergence of mock Fourier series*, Journal d'Analyse Mathématique **99** (2006), 333–353, https://doi.org/10.1007/BF02789451.
