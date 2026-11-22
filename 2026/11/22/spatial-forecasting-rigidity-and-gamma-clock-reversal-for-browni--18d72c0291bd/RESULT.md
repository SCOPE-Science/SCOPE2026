# Spatial forecasting rigidity and Gamma-clock reversal for Brownian resetting

## Finding
Consider one-dimensional Brownian motion with diffusion generator \(D\partial_{xx}\), \(D>0\), independently and instantaneously restarted at the origin at the epochs of an equilibrium renewal process. Let \(X\) be the stationary particle position and \(F\) the time remaining until its next reset. The following constitutes one spatial-forecast classification theorem.

**Rigidity for arbitrary renewal clocks.** For any strictly positive, absolutely continuously distributed inter-reset time \(T\) with finite mean, \(F\) is independent of the stationary position \(X\) **if and only if** \(T\) is exponentially distributed. In particular, there is no non-Poisson renewal protocol whose entire future-reset survival curve is independent of the currently observed position.

**Complete Gamma-clock ordering.** If \(T\sim\operatorname{Gamma}(k,\lambda)\), with shape \(k>0\) and rate \(\lambda>0\), then for every fixed \(u>0\) the spatial forecast \(\Pr(F>u\mid X=x)\) is strictly decreasing in \(|x|\) when \(k>1\), strictly increasing when \(0<k<1\), and independent of \(x\) exactly when \(k=1\). Thus all positive increasing future-reset-time costs, including the conditional mean, inherit this strict ordering whenever their expectations are finite.

**Sharp rare-position forecast.** For every fixed \(k,\lambda,D,u>0\),
\[
 \Pr(F>u\mid X=x)=e^{-\lambda u}\left[1+
 \frac{2(k-1)u\sqrt{D\lambda}}{|x|}+O_{k,\lambda,D,u}(|x|^{-2})\right]
 \qquad (|x|\to\infty).
\]
Moreover,
\[
 \mathbb E(F\mid X=x)=\frac1\lambda+
 \frac{2(k-1)\sqrt{D\lambda}}{\lambda^2|x|}
 +O_{k,\lambda,D}(|x|^{-2}).
\]
The leading exponential limit is consistent with known extreme-position residual-clock behavior in related Gamma-return models; the explicit first correction, strict spatial ordering, and general independence characterization are the assessed conclusions.

For the first non-Poisson Erlang case \(k=2\), the entire conditional survival curve is elementary:
\[
 \Pr(F>u\mid X=x)=e^{-\lambda u}
 \left(1+\frac{2\lambda u}{3+|x|\sqrt{\lambda/D}}\right).
\]
For \(k=3\), writing \(a=|x|\sqrt{\lambda/D}\), it is
\[
 e^{-\lambda u}\left[1+
 \frac{4\lambda u(a+3)+4(\lambda u)^2}{a^2+7a+15}\right].
\]
These closed forms are concrete calibrations of the theorem, not separate claims.

## Assumptions and scope
Let independent renewal intervals \(T_j\) have a common law with \(0<T_j<\infty\) almost surely, an absolutely continuous density, and mean \(0<\mu<\infty\). Form the stationary two-sided renewal process, with the interval containing observation time zero chosen by length bias, and with zero uniformly positioned in that interval. Each reset instantaneously places the particle at zero and independently renews its Brownian increments, with \(\operatorname{Var}(B_t)=2Dt\). The observed \(X\) is the position at time zero; \(B\) denotes backward recurrence age and \(F\) the forward recurrence time. The law of \(X\) has a positive, even density and the conditional laws are understood in their continuous versions, including at \(x=0\).

The Gamma convention is density \(f_T(t)=\lambda^kt^{k-1}e^{-\lambda t}/\Gamma(k)\) for \(t>0\); its shape need not be an integer. The rate \(\lambda\) is the large-age hazard, not the mean reset frequency \(\lambda/k\). All parameters in the Gamma assertion are fixed before the limit \(|x|\to\infty\); neither the remainder nor the asymptotic is claimed uniform as \(k\), \(u\), or \(\lambda\) varies.

## Proof
**1. Exact equilibrium conditional law.** Write \(S(b)=\Pr(T>b)\) and \(g_b(x)=(4\pi Db)^{-1/2}\exp(-x^2/(4Db))\). Renewal inspection gives the joint law of age and residual as \(f_{B,F}(b,f)=f_T(b+f)/\mu\), for positive \(b,f\). Consequently
\[
 \Pr(F>u\mid X=x)
 =\frac{\int_0^\infty S(b+u)g_b(x)\,db}
 {\int_0^\infty S(b)g_b(x)\,db},\quad u\ge0. \tag{1}
\]
Both integrals are finite because \(\int_0^\infty S(b)\,db=\mu\), with integrable \(b^{-1/2}\) singularity at zero; the denominator is strictly positive for every finite \(x\). This formula is a known renewal-conditioned-position representation, not by itself the new theorem.

**2. Poisson-only independence.** Suppose \(F\) and \(X\) are independent. For each \(u\ge0\), let \(c(u)=\Pr(F>u)\). Equation (1) gives, for almost every \(x\),
\[
 \int_0^\infty [S(b+u)-c(u)S(b)]g_b(x)\,db=0.
\]
The integrand defines a finite signed measure in \(x\). Its Fourier transform is
\[
 \int_0^\infty [S(b+u)-c(u)S(b)]e^{-D\xi^2b}\,db=0
 \quad(\xi\in\mathbb R).
\]
The bracketed function is integrable in \(b\), so uniqueness of the Laplace transform (over all \(D\xi^2\ge0\)) implies \(S(b+u)=c(u)S(b)\) for almost every \(b\). Survival continuity and \(S(0)=1\) yield \(c(u)=S(u)\) and \(S(b+u)=S(b)S(u)\) for all \(b,u\ge0\). A continuous nonincreasing survival function with \(S(0)=1\), finite positive mean, and this multiplicative identity is \(S(b)=e^{-rb}\) for some \(r>0\). Conversely an exponential survival gives \(S(b+u)/S(b)=e^{-ru}\), and (1) makes \(F\) independent of \(X\).

**3. Strict Gamma spatial ordering.** Conditional on \(X=x\), the age has density proportional to \(S(b)g_b(x)\). If \(0\le x_1<x_2\), the density ratio between the latter and former is proportional to
\[
 \exp\!\left(-\frac{x_2^2-x_1^2}{4Db}\right),
\]
which is strictly increasing in \(b>0\). Hence the posterior age increases strictly in monotone-likelihood-ratio order, and therefore in first-order stochastic order, with observed \(|x|\).

For the Gamma law, its hazard \(h(b)=f_T(b)/S(b)\) obeys
\[
 \frac1{h(b)}=\int_0^\infty e^{-\lambda z}(1+z/b)^{k-1}\,dz.
\]
Thus the hazard is strictly increasing for \(k>1\), strictly decreasing for \(0<k<1\), and constant for \(k=1\). For every \(u>0\), the age-conditioned future survival \(Q_u(b)=S(b+u)/S(b)=\exp[-\int_b^{b+u}h(t)\,dt]\) is strictly decreasing, respectively increasing, in \(b\) for \(k>1\), respectively \(k<1\). Averaging \(Q_u(B)\) under the strict posterior-age order proves the announced ordering of (1). Integrating its survival probabilities over \(u\) gives the corresponding strict conditional-mean order; Gamma tails guarantee integrability.

**4. Far-field expansion.** Let \(a=|x|\sqrt{\lambda/D}\). The standard incomplete-Gamma asymptotic gives, for each fixed positive \(u\) as \(b\to\infty\),
\[
 \frac{S(b+u)}{S(b)}=e^{-\lambda u}
 \left[1+\frac{(k-1)u}{b}+O_{k,\lambda,u}(b^{-2})\right]. \tag{2}
\]
For large \(|x|\), the posterior-age weight in (1) is exponentially concentrated near \(b_x=|x|/(2\sqrt{D\lambda})\), the unique minimizer of \(\lambda b+x^2/(4Db)\). More explicitly, the leading posterior measure is proportional to \(b^{k-3/2}\exp[-\lambda b-x^2/(4Db)]\), a generalized inverse-Gaussian kernel. Its inverse moments are represented by ratios of modified Bessel functions \(K_\nu(a)\), with \(\nu=k-1/2\), and obey
\[
 \mathbb E[B^{-1}\mid X=x]=\frac{2\sqrt{D\lambda}}{|x|}+O(|x|^{-2}),\qquad
 \mathbb E[B^{-2}\mid X=x]=O(|x|^{-2}). \tag{3}
\]
The neglected small-age region is exponentially smaller than the saddle contribution. The remainder in the incomplete-Gamma expansion is controlled on any fixed large-age half-line; the Gaussian factor suppresses its complement. Combining (2) and (3) yields the conditional survival expansion.

For the mean, the Gamma mean residual life satisfies
\[
 m(b)=\int_0^\infty\frac{S(b+u)}{S(b)}\,du
 =\lambda^{-1}+(k-1)(\lambda^2b)^{-1}+O(b^{-2}),
\]
by the same incomplete-Gamma expansion applied to \(\int_b^\infty S(t)\,dt\). Substituting (3) proves the conditional-mean expansion, without unjustified integration of a fixed-\(u\) remainder.

**5. Exact Erlang cross-checks.** For \(k=2\), \(S(b)=e^{-\lambda b}(1+\lambda b)\). Set \(I_j=\int_0^\infty b^j e^{-\lambda b}g_b(x)db\). The Brownian resolvent gives \(I_0=e^{-a}/(2\sqrt{D\lambda})\), and differentiation yields \(\lambda I_1/I_0=(a+1)/2\). Expanding \(S(b+u)\) in (1) gives the stated \(k=2\) expression. For \(k=3\), the additional identity \(\lambda^2I_2/I_0=(a^2+3a+3)/4\) similarly gives the displayed \(k=3\) expression. Both have the same sharp coefficient as (2)-(3).

## Verification
Run `python verify_forecast.py` with NumPy/SciPy installed. It independently integrates the stationary-age kernel for noninteger Gamma shapes below and above one, checks the strict order at several displacements and future horizons, checks the exactly exponential case, compares Erlang-2 and Erlang-3 formulas to the integrals, and tests the predicted leading far-field coefficient and conditional-mean derivative. The supplied checker passes 264 deterministic assertions. These finite numerical checks corroborate but do not substitute for the transform-uniqueness, likelihood-ratio, and Laplace-method proofs.

## Relationship to prior work
Masó-Puigdellosas, Campos and Méndez (arXiv:2205.01613, especially Section IV) derive the general conditioned forward-time density and show explicitly that exponential reset times give a position-independent residual time. Their general formula is the starting identity (1); its Poisson-only converse, strict Gamma spatial forecast order, and first nonzero far-field correction are not separately stated there. The derivation here does not claim that conditional forward densities themselves are newly introduced.

Radice (arXiv:2201.01829) establishes the Gamma survival and increasing/decreasing hazard regimes in its different model with finite-speed returns. The hazard ordering alone does not prove the Brownian-position forecast ordering. Earlier conditional extreme-position analysis of Gamma reset-and-return diffusion establishes a leading limiting exponential residual time during its diffusive phase, which this result acknowledges; the present instantaneous-reset law has a distinct explicit spatial correction and a full-domain order/rigidity theorem.

Losidis, Politis and Psarrakos (2024, DOI 10.15559/24-VMSTA266) characterize conditional forward/backward recurrence-time properties and note the classical Poisson-only independence of *age and residual time*, not the Poisson-only independence of *Brownian position and residual time*. The latter requires injectivity through the diffusion kernel. A related published Brownian-gas result reconstructs reset waiting times from a **two-time positional covariance**; it does not supply the one-time position/residual-time independence criterion. General likelihood-ratio and Laplace uniqueness facts are standard mathematical tools and are not claimed as newly invented.

## Limitations
These are equilibrium stationary-renewal assertions; a process observed shortly after a deterministic initial reset need not obey the same conditional laws. The rigidity theorem uses a nondegenerate Brownian observation kernel, independent complete positional resetting, and finite-mean strictly positive absolutely continuous clock intervals. It does not extend automatically to arbitrary reset-dependent dynamics or nonrenewal clocks. The strict Gamma spatial order is an ordering of predictive *distributions*, not a claim that individual residual times decrease along every realized trajectory. The far-field expansion holds for fixed parameters and fixed positive horizon, with nonuniform constants. The original conditioned-density formula and renewal hazard properties are acknowledged as prior mathematics; priority relative to more general uninspected statistical-identifiability or stochastic-order theorems remains uncertain. No independent external scientific audit is claimed.

## References
1. A. Masó-Puigdellosas, D. Campos and V. Méndez, *Conditioned backward and forward times of diffusion with stochastic resetting: a renewal theory approach*, arXiv:2205.01613v1, first public 2022-05-03; https://arxiv.org/pdf/2205.01613; Phys. Rev. E 106, 034126 (2022).
2. M. Radice, *Diffusion processes with Gamma-distributed resetting and non-instantaneous returns*, arXiv:2201.01829v1, first public 2022-01-05; https://arxiv.org/pdf/2201.01829.
3. S. Losidis, K. Politis and G. Psarrakos, *Bivariate dependence, stochastic orders and conditional tails of the recurrence times in a renewal process*, published online 2024-11-12; https://doi.org/10.15559/24-VMSTA266.
4. *Universal hidden-phase and Gaussian age laws for extreme Gamma-reset diffusion with finite-speed returns*, publicly accessible scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-universal-hidden-phase-and-gaussian-age-laws-for-extreme-gamma-r--5c356dfeaeaf.
5. *Temporal spectroscopy and renewal-law identifiability in a synchronously reset Brownian gas*, publicly accessible scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/27/SCOPE-temporal-spectroscopy-and-renewal-law-identifiability-in-a-synch--dfa7ae68742e.
