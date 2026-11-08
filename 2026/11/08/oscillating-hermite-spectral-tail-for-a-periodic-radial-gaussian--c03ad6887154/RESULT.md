# Oscillating Hermite spectral tail for a periodic radial Gaussian localization mask

## Finding
Fix real numbers \(T>0\) and \(0<s<T\). Define the infinite-area phase-space mask
\[
E_{T,s}=\left\{(x,\xi)\in\mathbb R^2:\pi(x^2+\xi^2)\in\bigcup_{j=0}^{\infty}[jT,jT+s]\right\}.
\]
For the normalized Gaussian \(\varphi(t)=2^{1/4}e^{-\pi t^2}\), let \(P_{T,s}=V_\varphi^*\mathbf1_{E_{T,s}}V_\varphi\) on \(L^2(\mathbb R)\). Let \(h_k\) denote normalized Hermite functions with \(h_0=\varphi\), and define
\[
\rho_j(T)=\left(1+\frac{4\pi^2j^2}{T^2}\right)^{-1/2},\qquad
\theta(T)=\arctan\frac{2\pi}{T},\qquad
\beta=\frac{\pi s}{T}.
\]
Then the full diagonal spectrum is \(P_{T,s}h_k=\lambda_kh_k\), where
\[
\lambda_k=\sum_{j=0}^{\infty}\int_{jT}^{jT+s}\frac{r^k e^{-r}}{k!}\,dr.
\]
The exact operator norm, uniquely attained up to scalar phase by \(h_0\), is
\[
\|P_{T,s}\|=\lambda_0=\frac{1-e^{-s}}{1-e^{-T}}.
\]
More quantitatively, for **every** integer \(k\ge1\),
\[
\lambda_0-\lambda_k\ \ge\
\frac{e^{-T}}{1-e^{-T}}
\left(T\frac{1-e^{-s}}{1-e^{-T}}-s\right)>0.
\]
The operator is noncompact with the single-point essential spectrum \(\{s/T\}\). Its Hermite eigenvalues approach that point through an exponentially damped but persistently oscillating sequence: as \(k\to\infty\),
\[
\boxed{\quad
\lambda_k-\frac{s}{T}=
\frac{2\sin\beta}{\pi}\rho_1(T)^{k+1}
\cos\big((k+1)\theta(T)-\beta\big)
+O_{T,s}\big(\rho_2(T)^{k+1}\big).
\quad}
\]
For every \(T>0\) and \(0<s<T\), infinitely many Hermite eigenvalues lie strictly **above** \(s/T\), and infinitely many lie strictly **below** it. Thus the spectral tail is never eventually one-sided, even though the Gaussian is the uniformly isolated unique top mode.

## Assumptions and scope
The short-time Fourier transform is \(V_\varphi f(x,\xi)=\int_{\mathbb R}f(t)\overline{\varphi(t-x)}e^{-2\pi i\xi t}\,dt\). Its Gaussian window has unit \(L^2\)-norm. The symbol is the bounded indicator of \(E_{T,s}\); its infinite planar measure is permitted because \(0\le P_{T,s}\le I\) is bounded. The Hermite basis is indexed by \(k=0,1,2,\ldots\), and the constants in the asymptotic may depend on fixed \(T,s\). No uniformity as either parameter approaches an endpoint is asserted. The classification concerns the spectrum, not individual sample recovery or a finite-rank truncation.

## Proof
**Diagonalization.** The Gaussian STFT has the exact radial identity
\[
|V_\varphi h_k(x,\xi)|^2=e^{-\pi(x^2+\xi^2)}\frac{\big(\pi(x^2+\xi^2)\big)^k}{k!}.
\]
Rotation covariance annihilates the off-diagonal Hermite matrix elements for radial symbols. Polar integration with \(r=\pi(x^2+\xi^2)\) gives the stated \(\lambda_k\). This remains valid for the nonintegrable indicator by bounded convergence on increasing disks, since the diagonalization persists in the strong operator limit.

**Exact isolated top and gap.** Let \(\mathbb T_T=\mathbb R/T\mathbb Z\) carry Lebesgue measure on \([0,T)\), and let \(\mu\) be the wrapped exponential probability law with density
\[
p_T(t)=\frac{e^{-t}}{1-e^{-T}},\qquad 0\le t<T.
\]
Since a Gamma\((k+1,1)\) random variable is the sum of \(k+1\) independent rate-one exponentials, \(\lambda_k=\mu^{*(k+1)}([0,s])\), with convolution on \(\mathbb T_T\). For any shift \(a\), the \(\mu\)-mass of the circular interval \([a,a+s]\) is at most \(\mu([0,s])=\lambda_0\): on \(0\le a\le T-s\), this mass decreases strictly with \(a\), while on \(T-s<a<T\), it increases strictly up to its value at \(a=T\). Therefore, writing \(F(t)=\mu([-t,s-t]\pmod T)\), we have \(0\le\lambda_0-F(t)\), with equality only at \(t=0\pmod T\).

The density of \(\mu\) is bounded below almost everywhere by \(m_T=e^{-T}/(1-e^{-T})\), so every convolution power \(\mu^{*k}\) for \(k\ge1\) also has density at least \(m_T\). Circular Fubini gives \(\int_0^T F(t)\,dt=s\). Hence
\[
\lambda_0-\lambda_k=\int_0^T(\lambda_0-F(t))\,d\mu^{*k}(t)
\ge m_T(T\lambda_0-s).
\]
Because the strictly decreasing wrapped-exponential density assigns strictly more mass to the initial interval than uniform measure does, \(T\lambda_0>s\). The bound is positive, proving isolation and uniqueness of the top eigenvalue.

**Fourier expansion and tail.** With the Fourier convention \(\widehat\nu(n)=\int_0^T e^{-2\pi int/T}\,d\nu(t)\), the wrapped exponential has
\[
\widehat\mu(n)=\left(1+\frac{2\pi in}{T}\right)^{-1}.
\]
Fourier inversion of \(\mu^{*(k+1)}\), integrated over the interval, yields for every \(k\ge1\) the absolutely convergent identity
\[
\lambda_k=\frac{s}{T}+2\operatorname{Re}\sum_{n=1}^{\infty}
\frac{e^{\pi ins/T}\sin(\pi ns/T)}{\pi n}
\left(1+\frac{2\pi in}{T}\right)^{-(k+1)}.
\]
The \(n=1\) summand is the displayed leading oscillation. For \(n\ge2\), the absolute value of the other summands is bounded by \((\pi n)^{-1}\rho_n(T)^{k+1}\). Since \(\rho_n<\rho_2\) for \(n>2\) and \(\sum_{n\ge2}(\rho_n/\rho_2)^2/n<\infty\), their sum is \(O_T(\rho_2^{k+1})\). The same expansion shows \(\lambda_k\to s/T\), so the diagonal operator has essential spectrum exactly \(\{s/T\}\) and is not compact.

**Infinitely many signs.** Since \(0<\theta(T)<\pi/2\), the angles \((k+1)\theta(T)-\beta\) visit infinitely many positions where their cosine is bounded below by a positive constant and infinitely many where it is bounded above by a negative constant. If \(\theta(T)/(2\pi)\) is irrational, use density of irrational rotations; if rational, its reduced denominator is at least five and one full orbit of equally spaced roots of unity has cosines of both signs. Since \(\rho_2/\rho_1<1\) and \(\sin\beta>0\), the asymptotic error cannot reverse those two subsequential signs once \(k\) is large. This proves the claimed infinite two-sided approach.

## Verification
The standalone Python file `checks/periodic_comb_check.py` uses exact cell-integral gamma survival formulas and an independently evaluated Fourier series. Running `python checks/periodic_comb_check.py` with Python 3 (standard library only) checks 16 period-width pairs, compares 11 non-Gaussian Hermite modes per pair, tests the uniform spectral-gap inequality, and verifies finite Fourier tail bounds for three orders per pair. It reports `PERIODIC_GAUSSIAN_COMB_CHECKS_PASS 624`. These finite tests are corroboration; the arbitrary-parameter and infinitely-many-sign statements are proved above.

## Relationship to prior work
Daubechies' 1988 Hermite diagonalization provides the radial eigenvalue identity. Knutsen's 2019 preprint, published in 2020, treats the exact same infinite radial unit-period mask in Section 3.2, proves a two-sided norm estimate for every aperture width and an equality formula for sufficiently small widths only. The 2021 continuation establishes Gaussian top modes for related *finite* generalized Cantor masks, but does not analyze the infinite periodic mask's essential spectrum or its oscillating Hermite tail. The wrapped-exponential Fourier transform and general circular-convolution facts are standard inputs, not newly asserted identities. The specific all-period positive-gap bound and essential-spectrum oscillation statement are the proposed contribution. A later norm inequality for integrable \(L^p\cap L^q\) localization symbols does not apply directly to this infinite-measure indicator.

## Limitations
The norm formula alone is a short consequence of classical convolution concentration and should not be mistaken for a fundamentally new general concentration inequality. The substantive statement here is the explicit quantitative spectral isolation together with the exponential oscillatory accumulation and universal two-sidedness for an infinite-area radial Gabor mask. The theorem does not claim a sharp best constant in the displayed uniform gap bound, an exact classification of all finite-index spectral crossings, or analogous behavior for non-Gaussian windows, non-prefix periodic masks, or nonradial symbols. Historical priority of the combined spectral statement remains provisional.

## References
1. I. Daubechies, *Time-Frequency Localization Operators: A Geometric Phase Space Approach*, IEEE Trans. Inf. Theory 34 (1988), 605–612, doi:10.1109/18.9761.
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets*, arXiv:1907.00848, first posted 2019-07-01; Journal of Fourier Analysis and Applications 26 (2020), article 47, Section 3.2, doi:10.1007/s00041-020-09751-9.
3. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets II*, arXiv:2104.10976, first posted 2021-04-22, especially Section 3 and Corollary 3.1.
4. F. Riccardi, *A new optimal estimate for the norm of time-frequency localization operators*, arXiv:2311.06525, first posted 2023-11-11.
