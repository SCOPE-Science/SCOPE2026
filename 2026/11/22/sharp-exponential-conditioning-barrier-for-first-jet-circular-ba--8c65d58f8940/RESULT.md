# Sharp exponential conditioning barrier for first-jet circular Bargmann–Fock sampling

## Finding

A regular circle of \(M\) sites, each giving both a complex value and a first complex derivative, interpolates all degree-at-most-\(2M-1\) Bargmann–Fock polynomials for every positive radius. Yet even after optimizing the common radius, this critical \(2M\)-measurement design has an exponentially increasing **squared** spectral condition number. With the covariantly normalized first jet specified below,
\[
\boxed{\lim_{M\to\infty}\frac1M\log\inf_{x>0}\kappa_2(T_{M,x})^2=\frac2e.}
\]
The optimal radius satisfies the sharp asymptotic law \(x/M\to 2/e\), in contrast to the **exact determinant-maximizing** squared radius \(x=M-1\). More precisely, at every fixed \(\rho>0\),
\[
\lim_{M\to\infty}\frac1M\log\kappa_2(T_{M,\rho M})^2=
F(\rho)=\begin{cases}
\max\{\rho,\rho-2+2\log(2/\rho)\},&0<\rho\le2,\\
2+2\log(\rho/2),&\rho\ge2.
\end{cases}
\]
The function \(F\) has a unique global minimizer \(\rho_*=2/e\), and every sequence of radii attaining the global exponential rate must satisfy \(x_M/M\to2/e\). This is a statement about the asymptotic squared singular-value ratio, not an assertion of a finite-degree closed form for its optimal radius.

## Assumptions and scope

For every integer \(M\ge2\) let \(\mathcal P_{2M-1}\) be the analytic Fock polynomial Hilbert space
\[
f(z)=\sum_{n=0}^{2M-1}c_n\frac{z^n}{\sqrt{n!}},\qquad
\|f\|^2=\sum_{n=0}^{2M-1}|c_n|^2.
\]
Fix the squared radius \(x>0\), the regular vertices \(z_j=\sqrt{x}\,e^{2\pi i j/M}\) for \(0\le j<M\), and the sample map \(T_{M,x}:\mathcal P_{2M-1}\to\mathbb C^{2M}\) whose two rows at vertex \(j\) are
\[
(T_{M,x}f)_{j,0}=M^{-1/2}e^{-x/2}f(z_j),\qquad
(T_{M,x}f)_{j,1}=M^{-1/2}e^{-x/2}\frac{z_jf'(z_j)-xf(z_j)}{\sqrt{x}}.
\]
The second observable is a normalized covariant radial derivative; knowledge of these two channels is equivalent to knowledge of value and first complex derivative since \(x>0\). The normalization, factorial coefficient Hilbert norm, equal weights, one common radius, and a primitive regular polygon are part of the theorem. We use \(\kappa_2(T)=\sigma_{\max}(T)/\sigma_{\min}(T)\), taking \(+\infty\) if singular.

## Proof

**1. Exact cyclic singular spectrum and interpolation.** Put \(p_n(x)=e^{-x}x^n/n!\), and perform a unitary discrete Fourier transform separately in each of the two observation channels. The source harmonics \(n=k\) and \(n=k+M\) have the same Fourier residue \(k\pmod M\). The transformed matrix is the orthogonal direct sum, over \(0\le k<M\), of
\[
B_{k,M}(x)=\begin{pmatrix}
\sqrt{p_k(x)}&\sqrt{p_{k+M}(x)}\\
\dfrac{k-x}{\sqrt x}\sqrt{p_k(x)}&\dfrac{k+M-x}{\sqrt x}\sqrt{p_{k+M}(x)}
\end{pmatrix}.
\]
In particular
\[
\det B_{k,M}(x)=\frac M{\sqrt x}\sqrt{p_k(x)p_{k+M}(x)}>0.
\]
Thus all \(2M\) source coefficients are uniquely recoverable from the \(2M\) measurements, for every radius \(x>0\). The two squared singular values within a residue block are the roots of
\[
\lambda^2-t_{k,M}(x)\lambda+d_{k,M}(x)=0,
\]
where
\[
t_{k,M}=p_k\left(1+\frac{(k-x)^2}{x}\right)
+p_{k+M}\left(1+\frac{(k+M-x)^2}{x}\right),\quad
 d_{k,M}=\frac{M^2}{x}p_kp_{k+M}.
\]
These formulas also give a finite-dimensional, numerically stable singular-value calculation via the block trace and determinant.

**2. Exact determinant optimum.** Multiplying the block determinants and noting \(\sum_{n=0}^{2M-1}n=M(2M-1)\) gives the exact Gram determinant
\[
\det(T_{M,x}^{*}T_{M,x})
=\frac{M^{2M}}{\prod_{n=0}^{2M-1}n!}\,
 e^{-2Mx}x^{2M(M-1)}.
\]
Its log derivative is \(-2M+2M(M-1)/x\); strict concavity in \(\log x\) and vanishing at both radius endpoints prove that \(x=M-1\) is the unique determinant-maximizing squared radius.

**3. Uniform logarithmic spectral estimates.** Fix any compact interval \(\rho\in[a,b]\subset(0,\infty)\) and put \(x=\rho M\). Uniform Stirling estimates, including the endpoint \(n=0\), give
\[
\log p_n(\rho M)=-M I_\rho(n/M)+O_{a,b}(\log M),\qquad
I_\rho(s)=\rho-s+s\log(s/\rho),
\]
for all \(0\le n<2M\), with \(0\log0=0\). The diagonal factors
\(L_n=1+(n-x)^2/x\) obey \(1\le L_n\le C_{a,b}M\). For any two Poisson weights \(u=p_k\), \(v=p_{k+M}\), write \(u_+=\max(u,v)\), \(u_-=\min(u,v)\). The larger eigenvalue of the block Gram is between \(u_+\) and \(C_{a,b}M u_+\), from the trace and the two diagonal Rayleigh quotients. The smaller eigenvalue is the block determinant divided by the larger eigenvalue, and \(M^2/x\asymp_{a,b}M\), so it is between \(c_{a,b}u_-\) and \(C'_{a,b}M u_-\). Thus polynomial-in-\(M\) factors are the entire difference between the extreme block singular energies and the extreme Poisson weights. Since \(n/M\) runs through a mesh of \([0,2)\), continuity of \(I_\rho\) yields uniformly for \(\rho\in[a,b]\)
\[
\frac1M\log\kappa_2(T_{M,\rho M})^2
=\max_{0\le s\le2}I_\rho(s)
 -\min_{0\le s\le2}I_\rho(s)
 +O_{a,b}\!\left(\frac{\log M}{M}\right).
\]
(The endpoint discrepancy at \(2\) is absorbed by the error.)

**4. Sharp scalar minimization.** The rate function \(I_\rho\) is convex, has derivative \(\log(s/\rho)\) at positive \(s\), and has minimum zero at \(s=\rho\) if \(\rho\le2\), or \(I_\rho(2)\) if \(\rho\ge2\). Its maximum on \([0,2]\) is the larger endpoint value \(I_\rho(0)=\rho\) or \(I_\rho(2)=\rho-2+2\log(2/\rho)\). These facts produce the displayed piecewise formula. On \((0,2]\), the second branch inside the maximum is strictly decreasing, while the first is strictly increasing; they cross uniquely at \(\log(2/\rho)=1\), or \(\rho=2/e\). For \(\rho\ge2\), the displayed formula is strictly increasing. Hence \(F\) uniquely minimizes at \(2/e\), with minimum \(2/e\).

**5. Excluding all escaping radii.** To justify minimizing over arbitrary \(x>0\) rather than only \(x=\rho M\) with bounded \(\rho\), use column squared norms \(d_n(x)=p_n(x)[1+(n-x)^2/x]\). For any matrix, the squared condition ratio is at least \(\max_n d_n/\min_n d_n\). Write \(N=2M-1\). The endpoint-column ratio satisfies
\[
\frac{d_N(x)}{d_0(x)}=
\frac{x^N}{N!}\,
\frac{1+(N-x)^2/x}{1+x},
\]
and all displayed factors are positive. If \(x/M\to0\), Stirling and the explicit rational factor show \(M^{-1}\log(d_N/d_0)\to-\infty\). If \(x/M\to\infty\), the same expression tends to \(+\infty\). This remains true when \(x\) approaches either endpoint faster than polynomially: the rational factor has at most one net factor of \(x\) or its inverse, whereas the factorial-weight ratio contains the \((2M-1)\)-st power. Therefore every sequence with bounded condition exponent stays in a fixed compact positive interval of \(x/M\). The uniform rate from step 3 applies there. Comparing with the admissible choice \(x=(2/e)M\) proves the global infimum and the necessary asymptotic radius for every sequence satisfying
\(M^{-1}\log\kappa_2(T_{M,x_M})^2\to2/e\).

## Verification

The attached `check_fock_jet.py` reconstructs the literal complex sampling matrices independently of Fourier block diagonalization for multiple small dimensions, compares direct singular values with the block formula, and checks the complete exact determinant identity against independent matrix determinants. It also performs finite-size radius optimizations through \(M=512\) and evaluates fixed-radius rates against the analytic limit. Running `python3 check_fock_jet.py` with NumPy and SciPy prints `ALL TESTS PASSED` and `DETERMINANT CHECKS PASSED`. Finite tests support, but do not replace, the all-degree argument in steps 1–5.

## Relationship to prior work

Escudero, Haimi and Romero (2020) developed multiple sampling and interpolation of entire functions using derivative data and density criteria. Their full-text theorem concerns infinite sampling sets and density, not sharp spectral conditioning on one finite orbit. Calixto, Guerrero and Sánchez-Monreal (2011) derived a Poisson-weighted eigenvalue spectrum for value-only coherent-state samples on a circle, and established exact truncated-state interpolation; our derivative-augmented two-channel block spectrum is a different finite matrix. Cruz, Massaneda and Ortega-Cerdà (2024) treated multiple sampling of polynomial Hilbert spaces using multiplicities and geometrical separation conditions, not this sharp circular first-jet rate. Berriochoa, Cachafeiro and Díaz (2014) give FFT-based Hermite interpolation on the unit circle for Laurent polynomials and up to two derivatives; their unit-circle formulas do not optimize Gaussian factorial coefficients or the exponential Fock-frame condition rate. Related exact circle-condition results for *point evaluation only* and results on *single-monomial first-jet projection* do not imply the simultaneous all-degree \(2M\)-coefficient minimax rate: the former lack derivative channels, and the latter optimize a rank-one projection rather than the smallest and largest singular values of the entire critical map. The determinant-radius versus condition-radius separation is likewise not a corollary of the point-only spectrum.

## Limitations

The claim uses a single regular circle, equal angular weights, the explicitly fixed covariant first-derivative scaling, and critical two-channel sampling of \(2M\) normalized coefficients. It does not optimize arbitrary angles, derivative-channel weights, multiple radii, or arbitrary node sets. It establishes the sharp **exponential rate** and limiting radius, not exact finite-dimensional condition-optimal radii or their polynomial prefactors. The derivative channel uses a radius-dependent normalization, so other noise metrics can have a different optimal radius. Earlier specialized coherent-state or confluent Fourier literature could contain an equivalent result; priority is not certified independently.

## References

1. L. A. Escudero, A. Haimi, J. L. Romero, *Multiple Sampling and Interpolation in Weighted Fock Spaces of Entire Functions*, arXiv:2004.12922v1, first posted 2020-04-27, https://arxiv.org/abs/2004.12922.
2. M. Calixto, J. Guerrero, J. C. Sánchez-Monreal, *Almost Complete Coherent State Subsystems and Partial Reconstruction of Wave Functions in the Fock-Bargmann Phase-Number Representation*, arXiv:1109.2171v1, 2011-09-09, https://arxiv.org/abs/1109.2171.
3. C. A. Cruz, X. Massaneda, J. Ortega-Cerdà, *Multiple sampling and interpolation in a space of polynomials*, arXiv:2405.19945v1, 2024-05-30, https://arxiv.org/abs/2405.19945.
4. E. Berriochoa, A. Cachafeiro, J. Díaz, *Hermite Interpolation on the Unit Circle Considering up to the Second Derivative*, 2014-03-10, https://doi.org/10.1155/2014/808519.
