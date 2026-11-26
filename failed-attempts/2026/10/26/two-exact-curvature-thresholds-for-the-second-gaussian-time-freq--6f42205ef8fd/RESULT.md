# Two exact curvature thresholds for the second Gaussian time-frequency concentration eigenvalue

## Finding
Let \(R>0\). On Gaussian Bargmann–Fock space \(\mathcal F^2\), let \(T_\Omega\) denote localization to the planar domain \(\Omega\), and let \(\lambda_2(\Omega)\) be its **second largest**, multiplicity-counted eigenvalue. For every real \(h\in C^2(\mathbb T)\) of angular mean zero and sufficiently small real \(\varepsilon\), define the **exactly area-preserving** deformation
\[
\Omega_\varepsilon=\{re^{i\theta}:0\le r^2<R+\varepsilon h(\theta)\},\qquad |\Omega_\varepsilon|=\pi R.
\]
Put \(\widehat h_m=(2\pi)^{-1}\int_0^{2\pi}h(\theta)e^{-im\theta}\,d\theta\). Then
\[
\boxed{\lambda_2(\Omega_\varepsilon)=1-(1+R)e^{-R}+\varepsilon^2 e^{-R}\sum_{m=2}^\infty q_m(R)|\widehat h_m|^2+o(\varepsilon^2)}
\]
where
\[
q_m(R)=1-R+R\frac{R^{m+1}/(m+1)!}{\sum_{j=2}^{m+1}R^j/j!},\quad m\ge2,
\qquad q_2(R)=\frac{3-2R}{R+3},\quad \lim_{m\to\infty}q_m(R)=1-R.
\]
The coefficients are **strictly decreasing** in \(m\ge2\). Consequently the second-order shape signature, modulo infinitesimal translation modes \(m=1\), has exactly these regimes:

* \(0<R\le1\): every nontranslation angular mode is positive; at \(R=1\) there is no uniform positive \(L^2\) spectral gap because the coefficients tend to zero.
* \(1<R<3/2\): low modes are positive but all sufficiently high modes are negative, so the disk is a second-order saddle.
* \(R=3/2\): mode \(m=2\) is neutral, and every mode \(m\ge3\) is negative.
* \(R>3/2\): every nontranslation angular mode is negative.

Here “positive/negative/neutral” refers precisely to the quadratic coefficient in the displayed expansion, not to a proven nonlinear local maximum or minimum.

## Assumptions and scope
Use the normalization
\[
\mathcal F^2=\left\{F\text{ entire}:\ \|F\|^2=\int_{\mathbb C}|F(z)|^2e^{-|z|^2}\frac{dA(z)}\pi<\infty\right\},\quad e_j(z)=\frac{z^j}{\sqrt{j!}}\ (j\ge0).
\]
The localization operator is the compact positive Toeplitz operator associated with the indicator of \(\Omega\): \(\langle T_\Omega F,G\rangle=\int_\Omega F\overline G e^{-|z|^2}dA/\pi\). Thus \(0\le T_\Omega\le I\). All eigenvalues are counted in nonincreasing order with multiplicity. The radius parameter is \(R=\text{area}/\pi\) **in this Fock plane**, so the numerical thresholds are normalization-dependent but the physical eigenvalue statement is not. For Gaussian short-time Fourier phase-space coordinates with Fock variable \(z=\sqrt\pi(x+i\xi)\), the physical phase-space area is \(R\).

The angular perturbation is real and \(C^2\); \(\widehat h_0=0\) fixes area exactly. For sufficiently small \(\varepsilon\), \(R+\varepsilon h>0\) and the domain is star-shaped. A translation of the original disk gives an \(m=1\) tangent perturbation; the particular radial path above is not itself exactly a translation at nonzero \(\varepsilon\).

## Proof
**1. Disk spectrum and spectral isolation.** Integrating monomials over the disk yields
\[
\langle T_{\Omega_0}e_j,e_k\rangle=\delta_{jk}\left(1-e^{-R}\sum_{\ell=0}^j\frac{R^\ell}{\ell!}\right)=:\delta_{jk}\Lambda_j(R).
\]
For every \(R>0\), \(\Lambda_0>\Lambda_1>\Lambda_2>\cdots>0\), so \(\lambda_2(\Omega_0)=\Lambda_1=1-(R+1)e^{-R}\) is a simple isolated eigenvalue. The Toeplitz operators form a real-analytic compact self-adjoint family near \(\varepsilon=0\): their matrix elements are integrals over a compact radial interval with analytic moving endpoints, and the same conclusion in trace norm follows from integrating coherent-state rank-one projections over the compact perturbation annulus (their trace norms are uniformly one). Hence ordinary simple-eigenvalue perturbation applies without truncating the infinite basis.

**2. Matrix elements and derivatives.** Polar integration with \(u=r^2\) gives, for \(j,k\ge0\),
\[
A_{jk}(\varepsilon)=\frac1{2\pi\sqrt{j!k!}}\int_0^{2\pi}e^{i(j-k)\theta}\int_0^{R+\varepsilon h(\theta)}u^{(j+k)/2}e^{-u}\,du\,d\theta.
\]
The mean-zero assumption implies \(A'_{11}(0)=0\). Explicit differentiation gives
\[
A''_{11}(0)=e^{-R}(1-R)\frac1{2\pi}\int_0^{2\pi}h(\theta)^2\,d\theta,
\qquad A'_{j1}(0)=\frac{e^{-R}R^{(j+1)/2}}{\sqrt{j!}}\widehat h_{1-j}.
\]
The second-order Rayleigh–Schrödinger formula is therefore
\[
\frac{1}{2}\lambda_2''(0)=\frac{A''_{11}(0)}2+
\sum_{j\ne1}\frac{|A'_{j1}(0)|^2}{\Lambda_1(R)-\Lambda_j(R)}.
\]
All denominators are nonzero, and the series is absolutely convergent because \(h\in C^2\), the powers have factorial decay, and the spectral gap from \(\Lambda_1\) is positive away from index one.

**3. Separate the translation mode.** Real-valuedness and \(\widehat h_0=0\) give \((2\pi)^{-1}\int h^2=2\sum_{m\ge1}|\widehat h_m|^2\). For the \(m=1\) Fourier coefficient, the diagonal term is \(e^{-R}(1-R)|\widehat h_1|^2\), while the \(j=0\) and \(j=2\) spectral-coupling terms are respectively \(-e^{-R}|\widehat h_1|^2\) and \(+e^{-R}R|\widehat h_1|^2\). Their sum is **exactly zero**, as required by translation invariance.

For each \(m\ge2\), the only coupled index is \(j=m+1\). Since
\[
\Lambda_1(R)-\Lambda_{m+1}(R)=e^{-R}\sum_{j=2}^{m+1}\frac{R^j}{j!},
\]
its coupling contribution equals
\[
e^{-R}R\frac{R^{m+1}/(m+1)!}{\sum_{j=2}^{m+1}R^j/j!}|\widehat h_m|^2.
\]
Adding the diagonal term yields the claimed coefficient \(q_m(R)\).

**4. Strict ordering and thresholds.** Set \(k=m+1\), \(t_j=R^j/j!>0\), and \(S_k=\sum_{j=2}^k t_j\). Since \(t_{k+1}=Rt_k/(k+1)\), the strict inequality \(t_{k+1}/S_{k+1}<t_k/S_k\) is equivalent to
\[
\frac{R}{k+1}\sum_{j=2}^{k-1}t_j<\sum_{j=2}^k t_j.
\]
But the left side equals \(\sum_{j=3}^k[j/(k+1)]t_j\), which is **strictly smaller** than \(\sum_{j=3}^k t_j\), hence smaller than the right side for every \(R>0\) and every \(k\ge3\). Therefore \(q_{m+1}(R)<q_m(R)\) for every \(m\ge2\). Since \(S_k\to e^R-1-R>0\) and \(t_k\to0\), we have \(q_m(R)\to 1-R\). Direct simplification gives \(q_2(R)=(3-2R)/(3+R)\). Strict ordering between the maximum \(q_2\) and the limiting infimum \(1-R\) proves all four sign regimes, including the two exact transition parameters.

## Verification
The exact coupling formula and cancellation of the first harmonic can be checked symbolically. A separate finite-section quadrature program (`verify_numerical.py`) compares the centered second difference of the second eigenvalue with the formula at multiple radii and angular harmonics. These computations check the constants but are not used as an infinite-dimensional proof.

## Relationship to prior work
The 2023 preprint by Gómez, Guerra, Ramos and Tilli provides quantitative stability of the **top Gaussian short-time Fourier concentration eigenvalue** and computes a Hessian for a function-optimized concentration functional, not the spectrum of fixed-domain second eigenvalues. Nicola and Tilli (2021/2022) show disk optimality for the top eigenvalue. Nicola, Riccardi and Tilli (2025/2026) optimize partial sums among **radial** domains and show that a particular annulus optimizes the second eigenvalue in the radial class, but do not state the second-eigenvalue angular shape Hessian at a disk. Later work by Ramos addresses inverse localization and local maximizers of the top eigenvalue. The present claim concerns a different eigenvalue, a different domain variation, and an exact threshold spectrum. The source comparisons do not constitute a proof of historical uniqueness.

## Limitations
The expansion concerns each fixed \(C^2\) radial deformation as \(\varepsilon\to0\). It does not provide a uniform nonlinear stability modulus over all perturbations, nor characterize globally optimal domains for the second eigenvalue. At neutral modes higher-order terms are not determined. The numerical check is finite dimensional; the infinite-dimensional conclusion follows from the perturbation proof. There remains residual historical-priority risk from sources not exhaustively indexed.

## References
1. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2307.09304v1 (first public 2023-07-18), https://arxiv.org/abs/2307.09304 ; Invent. Math. 236 (2024), 779–836. Relevant Section 5, especially Proposition 5.3 and formula (5.20).
2. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2106.03423v1 (2021-06-07), https://arxiv.org/abs/2106.03423 .
3. F. Nicola, F. Riccardi and P. Tilli, *The Faber–Krahn inequality for partial sums of eigenvalues of Toeplitz operators*, arXiv:2503.07069v1 (2025-03-10), https://arxiv.org/abs/2503.07069 .
4. J. P. G. Ramos, *Eigenfunctions, free boundaries, and time-frequency localization*, arXiv:2607.21590v1 (2026-07-23), https://arxiv.org/abs/2607.21590 .
