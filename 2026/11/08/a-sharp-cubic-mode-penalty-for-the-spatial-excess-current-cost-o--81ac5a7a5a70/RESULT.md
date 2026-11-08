# A sharp cubic mode penalty for the spatial excess-current cost of open-exclusion correlations

## Finding

For the weak harmonic boundary protocol and mode-response convention of [1], consider the **spatially integrated excess-current cost** defined directly from the deterministic hydrodynamic boundary-value problem, rather than from a separately postulated closed form. For each positive integer \(n\), define the dimensionless ratio \(\widetilde Q_n(\omega)\) in the next section. Let \(M_n=\sup_{\omega>0}\widetilde Q_n(\omega)\).

There is an integer \(n_0\) such that, for every \(n\ge n_0\), the supremum is achieved at **exactly one positive frequency** \(\omega_n\). Let \(z_*\) be the unique positive root of
\[
 z^6+30z^4+17z^2-108=0,
\]
and define \(h(z)=z^{3/2}(z^2+9)/[(z^2+1)(z^2+4)]\). Then
\[
 \frac{\omega_n}{(n\pi)^2}=2z_*+O(n^{-1}),\qquad
 M_n=\frac{2\pi^3}{405}h(z_*)n^3+\frac{4\pi^2}{405\sqrt{z_*}}h(z_*)n^2+O(n).
\]
The leading coefficient is \(0.15858389653283\ldots\), the next coefficient is \(0.08977661339127\ldots\), and the optimal frequency ratio tends to \(2z_*=2.52919301377288\ldots\). These coefficients are **sharp**, as they are attained asymptotically at the actual maximizing frequencies. The result is a sequential hydrodynamic/high-mode statement: continuum weak-drive response first, then \(n\to\infty\).

An exact intermediate identity is the spatial excess-current form factor
\[
 J(s)=\int_0^1\lvert U_\omega'(x)-1\rvert^2\,dx
 =\frac{s(\sinh s+\sin s)}{2(\cosh s-\cos s)}-1,\qquad s=\sqrt{\omega/2}.
\]
It behaves as \(J(s)=s^4/180+O(s^8)\) at low frequency and \(J(s)=s/2-1+O(se^{-s})\) at high frequency. This spatial integral, not a different algebraic form factor, defines the dissipative observable proved here.

## Assumptions and scope

Fix a mean density \(\rho_0\in(0,1)\), \(\chi_0=\rho_0(1-\rho_0)\), and weak boundary-gradient parameters \(0<\epsilon\ll\lvert g_0\rvert\ll1\). The deterministic first-harmonic response on \(0<x<1\), with diffusivity normalized to one, is
\[
 U_\omega''=i\omega U_\omega,\quad U_\omega(0)=-1/2,\quad U_\omega(1)=1/2,\quad
 U_\omega(x)=\frac{\sinh(k(x-1/2))}{2\sinh(k/2)},\quad k=\sqrt{i\omega}.
\]
For every integer \(n\ge1\), set \(\lambda_n=(n\pi)^2\). The complex long-range-correlation mode response used here is exactly the explicit linearized expression of [1]:
\[
 \delta a_n(\omega)=\frac{16g_0\epsilon\lambda_n}{(2\lambda_n+i\omega)(4\lambda_n+i\omega)},\quad
 \delta a_n^{\rm ad}=\frac{2g_0\epsilon}{\lambda_n},\quad
 \ell_n=\delta a_n-\delta a_n^{\rm ad}.
\]
Define the **specified** mean quadratic excess-current observable and normalized ratio by
\[
 \Sigma_{\rm spatial}(\omega)=\frac{\epsilon^2}{2\chi_0}\int_0^1\lvert U_\omega'(x)-1\rvert^2\,dx,
 \qquad \widetilde Q_n(\omega)=\frac{\lambda_n^4\lvert\ell_n(\omega)\rvert^2}{3240g_0^2\chi_0\Sigma_{\rm spatial}(\omega)}.
\]
The factor \(3240\) is chosen so \(\widetilde Q_n(\omega)\to1\) for each fixed \(n\) as \(\omega\downarrow0\). All quantities are defined for positive \(\omega\). The result is mathematical within these hydrodynamic response formulas; it is **not** a uniform theorem for lattice modes growing with finite lattice size and does not assert an exact microscopic entropy-production identity beyond the stated quadratic observable.

## Proof

**1. The spatial-current form factor.** Write \(s=\sqrt{\omega/2}\), so \(k=(1+i)s\). Since \(\int_0^1U_\omega'(x)\,dx=1\),
\[
 J(s)=\int_0^1\lvert U_\omega'(x)\rvert^2dx-1.
\]
The identities \(\lvert\sinh((1+i)s/2)\rvert^2=(\cosh s-\cos s)/2\) and
\(\int_{-1/2}^{1/2}\lvert\cosh((1+i)sy)\rvert^2dy=(\sinh s+\sin s)/(2s)\) give the asserted closed form. It is strictly positive, because equality would force \(U_\omega'\equiv1\) and hence \(U_\omega''=0\), contrary to the displayed boundary-value problem for \(\omega>0\). Taylor expansion gives \(J(s)=s^4/180+O(s^8)\). The hyperbolic terms give \(J(s)=s/2-1+O(se^{-s})\), as \(s\to\infty\).

**2. Exact ratio.** Direct subtraction of the two response amplitudes, followed by absolute squaring, yields
\[
 \lvert\ell_n(\omega)\rvert^2=\frac{4g_0^2\epsilon^2\omega^2(\omega^2+36\lambda_n^2)}{\lambda_n^2(\omega^2+4\lambda_n^2)(\omega^2+16\lambda_n^2)}.
\]
Using \(\omega=2s^2\) and the explicitly defined cost gives, with no approximation,
\[
 \widetilde Q_n(2s^2)=\frac{\lambda_n^2s^4(s^4+9\lambda_n^2)}{405(s^4+\lambda_n^2)(s^4+4\lambda_n^2)J(s)}.
\]
The behavior of \(J\) shows \(\widetilde Q_n\to1\) as \(s\downarrow0\), and \(\widetilde Q_n\to0\) as \(s\to\infty\) for each fixed \(n\).

**3. Compactness of maximizing scales.** Write \(\lambda=\lambda_n\), \(z=s^2/\lambda\), and \(h(z)=z^{3/2}(z^2+9)/[(z^2+1)(z^2+4)]\). The exact factorization is
\[
 \frac{\widetilde Q_n(2s^2)}{\lambda^{3/2}}=\frac1{405}h(z)\frac{s}{J(s)}.
\]
The function \(s/J(s)\) is bounded on \([1,\infty)\). Because \(h(z)\to0\) at both \(z\downarrow0\) and \(z\to\infty\), ratios with \(s\ge1\) and \(z\) outside a compact subset of \((0,\infty)\) cannot nearly maximize the positive limiting profile. For \(0<s\le1\), \(J(s)\ge c s^4\) for some \(c>0\), and \(h(s^2/\lambda)\le C(s^2/\lambda)^{3/2}\), giving a bound of order \(\lambda^{-3/2}\) for the normalized ratio. Thus all global maximizing scales are eventually confined to a fixed compact interval \(z\in[\delta,R]\subset(0,\infty)\). By positivity, continuity and the fixed-mode behavior at infinity, a positive finite maximum exists for all sufficiently large modes.

**4. Unique universal optimum.** Differentiation gives
\[
 \frac{h'(z)}{h(z)}=-\frac{z^6+30z^4+17z^2-108}{2z(z^2+1)(z^2+4)(z^2+9)}.
\]
The polynomial in the numerator strictly increases from \(-108\) to infinity on \(z>0\). Hence \(z_*\) is its unique positive root, \(h\) has a unique strict global maximum there, and \(h''(z_*)<0\). On every compact positive \(z\)-interval, \(s/J(s)\to2\) in \(C^2\) as \(\lambda\to\infty\), uniformly after substituting \(s=\sqrt{\lambda z}\). The limiting normalized profile is \((2/405)h(z)\). Compact localization therefore implies every maximizing \(z_n\to z_*\). On a small neighborhood of \(z_*\), strict concavity persists in the \(C^2\)-perturbed profile, while outside it a strict peak-height gap excludes maxima. Consequently the global maximizer is unique for all sufficiently large \(n\).

**5. Sharp two-term asymptotic.** Uniformly on compact positive \(z\)-intervals,
\[
 \frac{s}{J(s)}=2\left(1+\frac2s+O(s^{-2})\right),\qquad
 \frac{\widetilde Q_n}{\lambda^{3/2}}=\frac{2}{405}h(z)\left(1+\frac{2}{\sqrt{\lambda z}}+O(\lambda^{-1})\right).
\]
Differentiating this expansion near the nondegenerate critical point gives \(z_n=z_*+O(\lambda^{-1/2})\). Because \(h'(z_*)=0\), the shift changes the maximum only at relative order \(O(\lambda^{-1})\). It follows that
\[
 M_n=\frac{2}{405}h(z_*)\lambda_n^{3/2}+\frac4{405}\frac{h(z_*)}{\sqrt{z_*}}\lambda_n+O(\lambda_n^{1/2}).
\]
Substitute \(\lambda_n=\pi^2n^2\). Finally, \(\omega_n=2\lambda_n z_n\), proving the frequency statement and both sharp coefficients.

## Verification

Run \(\texttt{python3 verify.py}\) from the directory containing that file. This uses only the Python standard library and checks the exact integral by independent Simpson quadrature of \(\lvert U_\omega'-1\rvert^2\), the complex-response formula versus the algebraic ratio, the polynomial's isolated sign change, and high-mode maximizing values. The supplied checker reported **127 passing arithmetic checks**, including 11 independent integral comparisons and 99 complex-response comparisons. Checks over finitely many frequencies or modes are not proofs of the infinite-mode theorem; the proof above handles it analytically.

## Relationship to prior work

Vijayan, Thilakaraj, Gokila and Yogeshvari [1] derived the open-SSEP mode response and introduced a normalized correlation-lag/excess-dissipation comparison. Their analysis identifies a protected longest wavelength and reports higher-mode overshoots, including an approximate mode-two peak. The present result uses the **spatial quadratic excess-current integral itself** (explicitly defined above), evaluates it independently and proves the previously unquantified sharp cubic growth, the unique asymptotically optimal forcing scale, and the second coefficient. In particular, this theorem should not be read as claiming an exact model-independent entropy-production bound. The hydrodynamic stationary covariance framework is older [2,3]; general excess/housekeeping thermodynamics [4] does not determine this high-mode optimum. The formal spectral ratio based on a different expression for the cost is not interchangeable with the spatially integrated cost in this theorem.

## Limitations

The result is conditioned on the specified linear-response mode amplitudes of [1] and the explicitly defined spatial quadratic current. The two-scale limit is continuum hydrodynamics followed by large mode number; microscopic discrete modes with wavelength comparable to lattice spacing are excluded. It is not uniform over strong modulation, nonharmonic forcing, density-dependent diffusion or finite-system ultraviolet cutoffs. There is no explicit value for the finite threshold \(n_0\), and uniqueness is not asserted for every small mode. Numeric checks are not an independent audit and publication priority may be affected by unindexed analyses of the same continuum response.

## References

1. V. Vijayan, R. Thilakaraj, Gokila V, Y. V. A., *Long-Range Nonequilibrium Correlations as a Thermodynamic Speedometer*, arXiv:2610.07964v1 (first public October 6, 2026), https://arxiv.org/html/2610.07964v1 . Relevant Sections II–III and Appendices D–G.
2. B. Derrida, J. L. Lebowitz, E. R. Speer, *Large Deviation of the Density Profile in the Steady State of the Open Symmetric Simple Exclusion Process*, arXiv:cond-mat/0109346 (2001), https://arxiv.org/abs/cond-mat/0109346 .
3. T. Bodineau, B. Dagallier, *Large deviations for out of equilibrium correlations in the symmetric simple exclusion process*, arXiv:2212.11561 (2022), https://arxiv.org/abs/2212.11561 .
4. A. Kolchinsky, A. Dechant, K. Yoshimura, S. Ito, *Generalized free energy and excess entropy production for active systems*, arXiv:2412.08432 (2024), https://arxiv.org/abs/2412.08432 .
