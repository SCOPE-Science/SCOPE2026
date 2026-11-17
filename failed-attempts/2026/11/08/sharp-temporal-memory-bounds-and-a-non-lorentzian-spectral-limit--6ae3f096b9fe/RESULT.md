# Sharp temporal memory bounds and a non-Lorentzian spectral limit for a resetting Thomas–Fermi condensate edge

## Finding

In the stationary Poisson-reset Thomas–Fermi expansion described below, let \(V_r=\operatorname{Var}(X_0)\), \(C_r(t)=\operatorname{Cov}(X_0,X_t)\), and \(\rho_r(t)=C_r(t)/V_r\). For every positive reset rate \(r\), expansion frequency \(\omega\), and lag \(t>0\),

\[
e^{-rt}<\rho_r(t)<e^{-rt/2},\qquad
1<\Theta_r:=r\int_0^\infty\rho_r(t)\,dt<2.
\]

The function \(e^{rt}\rho_r(t)\) increases strictly to the finite value

\[
B_r=\frac{\sqrt2\,\omega\,\operatorname{Cov}(\lambda(A),A)}{\operatorname{Var}(\lambda(A))}>1,
\qquad A\sim\operatorname{Exp}(r).
\]

At every fixed scaled lag \(s\ge0\), the rare- and frequent-reset limits are

\[
\lim_{r/\omega\to0}\rho_r(s/r)=e^{-s},\qquad
\lim_{r/\omega\to\infty}\rho_r(s/r)=e^{-s}\left(1+\frac{2s}{5}\right).
\]

In particular \(\Theta_r\to1\) in the rare-reset limit and \(\Theta_r\to7/5\) in the frequent-reset limit. With the two-sided stationary spectral density defined by \(S_r(\nu)=2\int_0^\infty C_r(t)\cos(\nu t)\,dt\), the scaled spectra converge at fixed real \(\xi\):

\[
\lim_{r/\omega\to0}\frac{rS_r(r\xi)}{2V_r}=\frac1{1+\xi^2},\qquad
\lim_{r/\omega\to\infty}\frac{rS_r(r\xi)}{2V_r}
=\frac{7/5+(3/5)\xi^2}{(1+\xi^2)^2}.
\]

Thus the hydrodynamic edge does not generally inherit the pure exponential correlation of a reset process with constant drift. It has a rigorously bounded extra-memory factor and a universal non-Lorentzian rapid-reset spectrum.

## Assumptions and scope

Consider the one-dimensional free expansion of a weakly repulsive Bose–Einstein condensate initially in its Thomas–Fermi profile, in the hydrodynamic approximation in which the quantum-pressure term and finite-particle edge fluctuations are omitted. Its deterministic right support boundary is \(x_0\lambda(a)\), where \(x_0>0\), the age \(a\ge0\) is the elapsed time since the last instantaneous reset to the same initial profile, and \(\lambda\) is the unique positive classical solution

\[
\lambda''(a)=\frac{\omega^2}{\lambda(a)^2},\quad\lambda(0)=1,\quad\lambda'(0)=0,\quad\omega>0.
\]

Resets form an independent stationary Poisson process of rate \(r>0\). The age \(A_t\) is the time since the most recent reset, so \(A_t\) is stationary with exponential law of parameter \(r\); the observable is \(X_t=x_0\lambda(A_t)\). All covariance statements concern this classical common-reset hydrodynamic edge, not the extreme microscopic atom coordinate. Write \(F=\lambda\) and \(A\sim\operatorname{Exp}(r)\).

## Proof

**1. Growth and strict curvature.** Multiplying the scale equation by \(\lambda'\) gives the first integral

\[
\bigl(\lambda'(a)\bigr)^2=2\omega^2\left(1-\frac1{\lambda(a)}\right).
\]

Consequently \(F\) is strictly increasing for positive ages, \(F''>0\), \(0<F'(a)<\sqrt2\omega\) for \(a>0\), and \(F'(a)\uparrow\sqrt2\omega\). In particular \(F(a)-1\le\sqrt2\omega a\), and convexity also gives \(F(a)-1\le\omega^2a^2/2\). The local Taylor expansion is \(F(a)=1+\omega^2a^2/2+O(\omega^4a^4)\) for small ages. These inequalities ensure all subsequent exponential-age moments and dominated limits exist.

**2. Last-reset identity.** Between time zero and positive time \(t\), either there is no reset (probability \(e^{-rt}\)), when the joint ages are \((A,A+t)\), or there is at least one reset, in which case the final age is independent of \(A\). Subtracting the products of stationary means yields exactly

\[
C_r(t)=x_0^2e^{-rt}\operatorname{Cov}(F(A),F(A+t)),\qquad
V_r=x_0^2\operatorname{Var}(F(A))>0.
\]

The factor \(x_0\) cancels from the normalized covariance.

**3. Strict lower envelope and corrected monotonicity.** For independent identically distributed \(A,A'\), any square-integrable increasing functions \(g,h\) satisfy

\[
2\operatorname{Cov}(g(A),h(A))
=\mathbb E[(g(A)-g(A'))(h(A)-h(A'))]\ge0.
\]

The inequality is strict if both functions increase strictly. As \(F''>0\), the increment \(F(a+t)-F(a)\) is strictly increasing in \(a\) for every \(t>0\). Therefore

\[
\operatorname{Cov}(F(A),F(A+t))>
\operatorname{Var}(F(A)),
\]

proving \(\rho_r(t)>e^{-rt}\). For \(t_2>t_1\ge0\), \(F(a+t_2)-F(a+t_1)\) is also strictly increasing in \(a\), so the same identity makes \(e^{rt}\rho_r(t)\) strictly increasing. Since \(F(A+t)-F(t)=\int_0^A F'(t+u)\,du\) converges pointwise to \(\sqrt2\omega A\) and is dominated by \(\sqrt2\omega A\), the limit of the corrected covariance ratio equals \(B_r\) as stated, finite and strictly above one.

**4. Strict upper envelope.** The exponential distribution is memoryless. For the event \(E_t=\{A\ge t\}\), which has probability \(e^{-rt}\), the conditional law of \(A\) is \(t+A'\), where \(A'\sim\operatorname{Exp}(r)\). The law of total variance, including its nonzero contributions from the complementary event and conditional-mean separation, implies, strictly for positive \(t\),

\[
\operatorname{Var}(F(A))>
 e^{-rt}\operatorname{Var}(F(t+A')).
\]

Cauchy–Schwarz and the last-reset identity then give

\[
\rho_r(t)
=e^{-rt}\frac{\operatorname{Cov}(F(A),F(t+A))}{\operatorname{Var}(F(A))}
<e^{-rt/2}.
\]

Integrating the two strict exponential inequalities for positive lags gives \(1<\Theta_r<2\).

**5. The two universal scaling limits.** Let \(Z\) be exponential of mean one and put \(t=s/r\). By scaling \(A=Z/r\), the normalized covariance is \(e^{-s}\) times the correlation numerator \(\operatorname{Cov}(F(Z/r),F((Z+s)/r))\) divided by \(\operatorname{Var}(F(Z/r))\). For \(r/\omega\to0\), \(F(z/r)/(\sqrt2\omega/r)\to z\) in \(L^2\) for exponential \(Z\), by the global linear growth bound. Thus the ratio tends to \(\operatorname{Cov}(Z,Z+s)/\operatorname{Var}(Z)=1\).

For \(r/\omega\to\infty\), the centered and rescaled variable \((2r^2/\omega^2)(F(Z/r)-1)\) converges in \(L^2\) to \(Z^2\) by the quadratic Taylor law and quadratic upper bound. Accordingly the covariance ratio tends to

\[
\frac{\operatorname{Cov}(Z^2,(Z+s)^2)}{\operatorname{Var}(Z^2)}
=\frac{20+8s}{20}=1+\frac{2s}{5},
\]

because \(\mathbb E[Z^k]=k!\), \(\operatorname{Var}(Z^2)=20\) and \(\operatorname{Cov}(Z^2,Z)=4\). The envelope \(0<\rho_r(s/r)<e^{-s/2}\), uniform in \(r\), justifies dominated convergence for both the normalized time integral and Fourier-cosine transform. The integrals \(\int_0^\infty e^{-s}\,ds=1\), \(\int_0^\infty se^{-s}\,ds=1\), and the elementary cosine transforms produce the stated \(1\), \(7/5\), Lorentzian and non-Lorentzian limits. This completes the proof.

## Verification

The standalone `verify_edge.py` uses NumPy and SciPy to compare the exact implicit solution for \(\lambda\) with independent ODE integration, check the exact exponential-moment coefficients, and evaluate the covariance and integrated response by Gauss–Laguerre and Gauss–Legendre quadrature across multiple reset rates. Its fixed deterministic checks cover the strict envelopes, increasing corrected covariance, finite corrected tail amplitude, rare- and frequent-reset profiles, and integrated limiting factors. Run with `python verify_edge.py` in an environment containing NumPy and SciPy. Finite numerical tests corroborate but do not establish the global inequalities or asymptotic theorems; those follow from the proof above.

## Relationship to prior work

Mesquita, Kulkarni, Majumdar and Sabhapandit (2026), arXiv:2609.37110v1, derive the identical Thomas–Fermi expansion law, stationary age-mixture density, and one-time edge distribution, and analyze particle-number fluctuations. Those ingredients are assumed here. The new object is a stationary **two-time edge correlation**, together with strict all-rate envelopes, a sharp rapid-reset non-Lorentzian spectrum and its integrated \(7/5\) factor.

Stojkoski, Sandev, Kocarev and Pal (2021), arXiv:2107.11686v1, compute reset diffusion and constant-drift autocorrelations; their stationary drift result is a pure \(e^{-rt}\). The present rare-reset limiting law agrees with that drift benchmark, whereas the nonlinear Thomas–Fermi scale evolution produces a strictly larger correlation at every finite reset rate and positive lag, and a different quadratic-age limit at high reset rates. The last-renewal decomposition itself is not claimed to be new; see Evans, Majumdar and Schehr (2020), arXiv:1910.07993v2.

## Limitations

This theorem concerns the deterministic classical hydrodynamic *support edge*, not a fluctuating maximum over finitely many condensate particles. The Thomas–Fermi approximation neglects quantum-pressure boundary layers, and the protocol assumes instantaneous complete resets to the same initial profile, constant Poisson reset rate, no thermal fluctuations and no residual state memory. The spectral statements do not automatically extend to measured finite-particle edge or unequal reset preparations. The oldest general renewal/correlation machinery is known; publication priority of the precise edge-specific inequalities and scaling factors is subject to further specialized-literature comparison and independent audit.

## References

1. N. Mesquita, M. Kulkarni, S. N. Majumdar, S. Sabhapandit, *Weakly interacting Bose-Einstein condensate with stochastic resetting*, arXiv:2609.37110v1 (first public 2026-09-29), https://arxiv.org/abs/2609.37110 . See scaling equation (37), implicit solution (41), and steady-state renewal equations (44)–(49).
2. V. Stojkoski, T. Sandev, L. Kocarev, A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686v1 (2021), https://arxiv.org/abs/2107.11686 . See Section 3.2, especially stationary autocorrelation equation (26).
3. M. R. Evans, S. N. Majumdar, G. Schehr, *Stochastic Resetting and Applications*, arXiv:1910.07993v2, https://arxiv.org/abs/1910.07993 . See Section 2.2, last-renewal equation (2.10).
