# Wick-cubic information and finite-volume resonance at the stochastic Swift–Hohenberg onset

## Finding
For stationary full-field observations of the one-dimensional **linearized** stochastic Swift–Hohenberg equation, the cubic drift score with every linear drift nuisance projected away has an exact Wick-polynomial form. Its squared norm exhibits three mathematically distinct critical regimes: bounded off-resonant information at fixed periodic length, an inverse-cube pole at finite-volume resonance, and two thermodynamic critical exponents depending on whether the preferred pattern wavenumber vanishes.

In particular, putting \(\mathcal J_L=I_{L,T}/(LT)\), for every \(a,L,\Gamma,\sigma>0\) and \(k_*\ge0\),
\[
\mathcal J_L=\frac{6v_L^3}{\sigma^2},\qquad
v_L=\frac{\sigma^2}{2L}\sum_{j\in\mathbb Z}\frac{1}{a+\Gamma((2\pi j/L)^2-k_*^2)^2}.
\]
The positive quantities \(\Gamma\), \(\sigma\), \(L\) remain fixed in the small-damping comparisons below.

At fixed \(L\), if \(k_*\notin\{2\pi j/L:j\in\mathbb Z_{\ge0}\}\), \(\mathcal J_L\) has a finite positive limit as \(a\downarrow0\). If \(k_*=0\) set \(r=1\); if \(k_*=2\pi j/L\) for an integer \(j\ge1\) set \(r=2\). Precisely in these resonant cases,
\[
\mathcal J_L\sim\frac{3\sigma^4r^3}{4L^3}\,a^{-3}.
\]

When \(L\to\infty\) **before** \(a\downarrow0\), define \(\eta=k_*(\Gamma/a)^{1/4}\). Then the exact limiting variance and information are
\[
v_\infty=\frac{\sigma^2}{4\pi\Gamma^{1/4}a^{3/4}}\,\Phi(\eta),\quad
\Phi(\eta)=\frac{\pi}{\sqrt2}\frac{\sqrt{\sqrt{1+\eta^4}+\eta^2}}{\sqrt{1+\eta^4}},\quad
\mathcal J_\infty=\frac{6v_\infty^3}{\sigma^2}.
\]
Thus
\[
\mathcal J_\infty(a,0)=\frac{3\sigma^4}{64\sqrt2\Gamma^{3/4}}a^{-9/4},
\qquad
\mathcal J_\infty(a,k_*)\sim\frac{3\sigma^4}{32\Gamma^{3/2}k_*^3}a^{-3/2}\quad(k_*>0\text{ fixed}).
\]
The function \(\Phi\) gives the complete crossover at the natural scale \(k_*\asymp(a/\Gamma)^{1/4}\).

## Assumptions and scope
Let the spatial domain be \(\mathbb T_L=\mathbb R/L\mathbb Z\) with Lebesgue measure \(dx\), and let \(W\) be real cylindrical Brownian motion in \(L^2(\mathbb T_L)\), normalized so its real orthonormal Fourier coefficients have unit independent Brownian increments. Consider the stationary solution of
\[
du_t=-\left(a+\Gamma(k_*^2+\partial_x^2)^2\right)u_t\,dt+\sigma\,dW_t.
\]
Every Fourier frequency \(q_j=2\pi j/L\) has damping \(\lambda_j=a+\Gamma(q_j^2-k_*^2)^2>0\) and stationary variance \(\sigma^2/(2\lambda_j)\) in the orthonormal Fourier basis. The covariance series converges absolutely, and the random field admits the spatial regularity required for its pointwise cubic to lie in \(L^2(\mathbb T_L)\) almost surely.

The time interval is any \(0<T<\infty\). Define the baseline cubic and linear drift *score martingales*, not finite-sample prediction probabilities, by
\[
S_3=\sigma^{-1}\int_0^T\langle u_t^3,dW_t\rangle,\quad
S_B=\sigma^{-1}\int_0^T\langle Bu_t,dW_t\rangle,
\]
where \(B\) ranges over deterministic linear maps for which the indicated Itô integral has finite second moment (including the identity). One may also allow square-integrable deterministic time-dependent linear maps. This is the conditional observation score geometry with the initial state held to its baseline law; it does not include derivatives of the initial stationary law with respect to unknown parameters.

## Proof
**Covariance and score projection.** Translation invariance implies that \(v_L=\mathbb E[u_t(x)^2]\) does not depend on time or location. For every pair of points \(x,y\), centered joint Gaussianity and Wick's formula give
\[
\mathbb E[u_t(x)^3u_t(y)]=3v_L\,\mathbb E[u_t(x)u_t(y)].
\]
Therefore, with \(:u^3:=u^3-3v_Lu\), for every admissible deterministic linear map \(B\),
\[
\mathbb E\langle :u_t^3:,Bu_t\rangle=0.
\]
Itô isometry makes the corresponding cubic residual score orthogonal in \(L^2\) to *every* indicated linear score. Moreover, \(3v_LS_{\mathrm{Id}}\) is itself a linear score. Hence the orthogonal projection of \(S_3\) onto the closed linear-score span is exactly \(3v_LS_{\mathrm{Id}}\), and its orthogonal residual is \(S_{\rm eff}=\sigma^{-1}\int_0^T\langle:u_t^3:,dW_t\rangle\). The sixth, fourth and second centered Gaussian moments are respectively \(15v_L^3\), \(3v_L^2\), and \(v_L\), so
\[
\mathbb E[(:u_t(x)^3:)^2]=(15-18+9)v_L^3=6v_L^3.
\]
A second application of Itô isometry and integration over space and time yields \(I_{L,T}=\mathbb E[S_{\rm eff}^2]=6LTv_L^3/\sigma^2\). The identity holds for all stated parameters and durations, with no long-observation-time approximation.

**Fixed-volume criticality.** For fixed \(L\), Fourier-mode denominators are positive at \(a=0\) unless \(q_j^2=k_*^2\). In the nonresonant case, the resulting sum is finite because the high-frequency tail is \(O(j^{-4})\), so \(v_L\) has a finite limit. If resonant, there is exactly one zero frequency for \(k_*=0\), and exactly two frequencies \(j\) and \(-j\) for positive resonant \(k_*\). Splitting these \(r\) terms from the summable remainder gives \(v_L=\sigma^2r/(2La)+O(1)\) and the asserted inverse-cube law.

**Thermodynamic crossover.** For fixed positive damping, Riemann summation gives
\[
\lim_{L\to\infty}v_L=\frac{\sigma^2}{4\pi}\int_{\mathbb R}\frac{dq}{a+\Gamma(q^2-k_*^2)^2}.
\]
Rescaling \(q=(a/\Gamma)^{1/4}z\) gives the displayed variance with \(\Phi(\eta)=\int_{\mathbb R}\left[1+(z^2-\eta^2)^2\right]^{-1}dz\). For completeness, the standard quartic integral follows without a table. If \(c>-1\), the substitutions \(x\mapsto1/x\) and \(y=x-1/x\) show
\[
2\int_0^\infty\frac{dx}{x^4+2cx^2+1}
=\int_{-\infty}^\infty\frac{dy}{y^2+2(c+1)}
=\frac{\pi}{\sqrt{2(c+1)}}.
\]
Apply this with \(s=\sqrt{1+\eta^4}\), quartic scaling \(z=s^{1/2}x\), and \(c=-\eta^2/s\) to obtain the exact \(\Phi\). At \(\eta=0\) it equals \(\pi/\sqrt2\); at \(\eta\to\infty\) it is \(\pi/\eta+O(\eta^{-5})\). Substitution into \(6v_\infty^3/\sigma^2\) proves both exponents and constants.

## Verification
The standalone standard-library script `verify_wick.py` checks exact rational Gaussian identities, high-mode Riemann-sum convergence for four parameter samples and two large lengths, finite-volume resonance growth at two Fourier multiplicities and three damping values, and independent numerical quadrature of \(\Phi\) at six values. Execute `python3 verify_wick.py`; the expected result is `VERIFY_OK checks=182 finite_lengths=2 resonance_cases=2 continuum_eta=6`. These finite checks supplement, not replace, the preceding analytic proof.

## Relationship to prior work
Sanders, Kuehn, Hilder and Bastiaansen (2026) study pre-transition discrimination of cubic bifurcation types using regression and stochastic Swift–Hohenberg trajectories, and supply the motivating nonlinear inference question. Gowda and Kuehn (2014) establish variance-based early-warning principles for stochastic pattern formation. Bernuzzi, Düx and Kuehn (2024/2025) study covariance-divergence rates at continuous spectral thresholds. The Gaussian covariance premise and Wick orthogonalization are standard; the specific exact cubic-score information, its finite-volume resonance dichotomy, and its \(k_*=0\) versus \(k_*>0\) crossover are the assessed joint result. Nothing here claims a general discovery of Gaussian Hermite polynomials, variance divergence, or ordinary Fisher-score projections.

## Limitations
The result concerns the stationary **linear Gaussian baseline**, full continuous-time full-spatial-field observation, additive spatial white noise, constant coefficients and the specified drift-score projection. It does not prove that a nonlinear stochastic Swift–Hohenberg equation with an arbitrary cubic perturbation has a global stationary solution, nor does it give a finite-sample classification success probability, observation-operator correction, or the Fisher information from parameter-dependence of the stationary initial distribution. The computed quantity is the conditional Gaussian local drift-score information, not an unconditional information bound for arbitrary nonlinear bifurcation experiments. In particular, additional quadratic or nonlinear nuisance terms are not projected out. The thermodynamic and fixed-volume conclusions use different orders of limits.

## References
1. P. A. Sanders, C. Kuehn, B. Hilder and R. Bastiaansen, *Early warning of critical transitions: Distinguishing supercritical and subcritical bifurcations from noisy observations*, arXiv:2610.38866 (first publicly posted 2026-10-28).
2. M. Gowda and C. Kuehn, *Early-Warning Signs for Pattern-Formation in Stochastic Partial Differential Equations*, arXiv:1403.5920 (2014).
3. P. Bernuzzi, M. Düx and C. Kuehn, *Early warning signs for SPDEs with continuous spectrum*, European Journal of Applied Mathematics, DOI:10.1017/S0956792524000330.
