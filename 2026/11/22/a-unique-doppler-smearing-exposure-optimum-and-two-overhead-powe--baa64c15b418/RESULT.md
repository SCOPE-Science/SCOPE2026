# A unique Doppler-smearing exposure optimum and two overhead power laws

## Finding
For an ideal photon-noise-limited, constant-Doppler-drift spectral observation with a fixed positive overhead per exposure, a strictly decreasing nonnegative line autocorrelation makes the **matched-filter squared signal-to-noise per unit wall time uniquely maximized** by one finite positive exposure duration. The optimizer strictly increases with the overhead and obeys two different, explicit asymptotic laws: an overhead-power law set by the small-lag autocorrelation cusp and an overhead-square-root law set by the autocorrelation's first two integrals. For a Gaussian line the small-overhead law is a cube root, while the large-overhead law is a square root.

## Assumptions and scope
Let \(g\in L^2(\mathbb R)\) be a real, nonnegative, nonzero spectral-line template normalized by \(\|g\|_2=1\), and let \(a>0\) be the magnitude of its constant velocity drift in the spectral coordinate per unit exposure time. Let
\[
K(u)=\int_{\mathbb R}g(v)g(v-u)\,dv\quad(u\geq0).
\]
Assume \(K\) is continuous, strictly decreasing and nonnegative on \([0,\infty)\), with \(K(0)=1\), and \(\int_0^\infty(1+u)K(au)\,du<\infty\). Fix an instrumental overhead \(h>0\). For exposure length \(T>0\), the accumulated ideal signal is \(S_T(v)=\int_0^T g(v-at)\,dt\). Assume spectrally white photon noise with variance proportional to \(T\) in each exposure; identical, independent exposures; optimally matched spectral templates; and a wall-time-limited sequence with exposure/overhead cycle \(T+h\). Up to multiplicative constants independent of \(T\), the squared signal-to-noise per wall time is
\[
Q_h(T)=\frac{F(T)}{T+h},\qquad
F(T)=\frac{\|S_T\|_2^2}{T}=\frac2T\int_0^T(T-u)K(au)\,du.
\]
This is a *stationary infinite-cycle information rate*, not a finite-transit discrete-visit optimum or a theorem about SYSREM-detrended detection statistics. Noise is modeled as photon noise proportional to exposure duration; there is no detector read-noise term.

## Proof
Write \(k(u)=K(au)\). The interchange of the \(L^2\) integrals is valid for every finite \(T\); symmetry of the shift autocorrelation gives \(\|S_T\|_2^2=2\int_0^T(T-u)k(u)\,du\). Differentiate, obtaining
\[
F'(T)=\frac2{T^2}\int_0^T u k(u)\,du>0,\qquad
F''(T)=\frac4{T^3}\left(\frac{T^2}{2}k(T)-\int_0^Tuk(u)\,du\right)<0.
\]
The second inequality is strict because \(k(u)>k(T)\) for \(0\le u<T\). Also \(F(0+)=0\), \(F'(0+)=1\), \(F(T)\to2M_0>0\), and \(F'(T)\to0\), where \(M_j=\int_0^\infty u^j k(u)\,du\) for \(j=0,1\). Consequently
\[
N_h(T)=(T+h)F'(T)-F(T)
\]
is strictly decreasing, since \(N_h'(T)=(T+h)F''(T)<0\). Its limits are \(N_h(0+)=h>0\) and \(N_h(\infty)=-2M_0<0\). Since \(Q_h'(T)=N_h(T)/(T+h)^2\), it has precisely one zero and therefore exactly one global maximizer \(T_h\in(0,\infty)\). The defining identity
\[
h=\frac{F(T_h)}{F'(T_h)}-T_h
\]
expresses \(h\) as a strictly increasing function of \(T_h\), with derivative \(-F(T_h)F''(T_h)/(F'(T_h))^2>0\); hence \(T_h\) grows strictly with overhead.

For the short-overhead law suppose additionally \(k(u)=1-\kappa u^\nu+o(u^\nu)\) as \(u\downarrow0\), for \(\kappa,\nu>0\). Integrating gives
\[
F(T)=T-\frac{2\kappa}{(\nu+1)(\nu+2)}T^{\nu+1}+o(T^{\nu+1}),\quad
F'(T)=1-\frac{2\kappa}{\nu+2}T^\nu+o(T^\nu).
\]
As \(h\downarrow0\) the unique optimizer tends to zero; substitution into \(N_h(T_h)=0\), using \(hT_h^\nu=o(h)\), gives
\[
T_h\sim\left[\frac{(\nu+1)(\nu+2)}{2\kappa\nu}\,h\right]^{1/(\nu+1)}.
\]
For large overhead, integrability of \(u k(u)\) yields \(F(T)=2M_0-2M_1/T+o(T^{-1})\) and \(F'(T)=2M_1/T^2+o(T^{-2})\). Thus \(T_h\to\infty\), and the stationarity identity gives
\[
T_h\sim\sqrt{\frac{M_1}{M_0}h}\qquad(h\to\infty).
\]

In particular, for a normalized Gaussian line \(g(v)\propto \exp[-v^2/(2\sigma^2)]\), put \(c=a/(2\sigma)>0\). Then \(k(u)=e^{-c^2u^2}\) and
\[
F(T)=\frac{\sqrt\pi}{c}\operatorname{erf}(cT)-\frac{1-e^{-c^2T^2}}{c^2T},\qquad
F'(T)=\frac{1-e^{-c^2T^2}}{c^2T^2}.
\]
The positive root of \((T+h)F'(T)=F(T)\) is unique. Here \(\nu=2\), \(\kappa=c^2\), \(M_0=\sqrt\pi/(2c)\), and \(M_1=1/(2c^2)\), so
\[
T_h\sim(3h/c^2)^{1/3}\ (h\downarrow0),\qquad
T_h\sim\sqrt{h/(c\sqrt\pi)}\ (h\to\infty).
\]
These formulas have the correct time dimensions and use the actual physical velocity-gradient scale \(c=a/(2\sigma)\).

## Verification
Run `python3 verify.py` using the standard Python 3 library. The script reconstructs Gaussian autocorrelation integrals by independent Simpson quadrature, checks analytic first derivatives, brackets the unique optimizer, compares its information rate against nearby and distant choices, tests overhead monotonicity and both asymptotic laws, and checks a second exponential-decay autocorrelation. It completed 225 auxiliary assertions. For \(c=h=1\), its numerical root is \(T_h\approx1.378327080411\). This numerical evidence checks implementations but the infinite-domain uniqueness and asymptotic results follow from the proof, not finite sampling.

## Relationship to prior work
Boldt-Christmas et al. (arXiv:2312.08320v1, first public on 2023-12-13) directly motivate the trade-off between observation overhead and velocity smearing, and obtain exposure optima by simulated exoplanet spectra and detrending. Their full discussion, including idealized simulations, does not state the strictly decreasing-autocorrelation theorem, its exact Gaussian stationarity equation or the two asymptotic overhead powers. Hernandez Camero et al. (arXiv:2302.02897v1) analyze cadence-dependent *transit light-curve parameter precision*, with a different signal and objective. Loomis et al. (arXiv:1803.04987) describe matched filtering for weak interferometric spectral lines but do not optimize a constant-drift exposure cycle with overhead. The underlying concavity and scalar optimization steps are classical; novelty is claimed for their combined astronomical model and exact dual-regime classification, not for elementary calculus identities. A search of related mathematical research records found different Gaussian spectral sampling and finite-horizon estimation problems, not a theorem implying the statement here.

## Limitations
The theorem assumes nonnegative, strictly declining autocorrelation; structured multi-line templates can have autocorrelation sidelobes, and a different optimum geometry may result. It assumes exact matched filtering and white, exposure-proportional noise; read noise, background correlations, saturated pixels, tellurics, varying planetary radial acceleration, detrending and finite transit duration can change the optimum. The rate is a large-repetition idealization, not empirical advice for a given telescope. The general concavity mechanism is mathematically elementary, and not all published image-smearing or signal-processing literature has been exhaustively inspected; broader historical priority remains provisional. No external independent audit has been performed.

## References
1. L. Boldt-Christmas, F. Lesjak, A. Wehrhahn, et al., *Optimising spectroscopic observations of transiting exoplanets*, arXiv:2312.08320v1 (public 2023-12-13), https://arxiv.org/html/2312.08320v1 .
2. J. Hernandez Camero, C. S. K. Ho, V. Van Eylen, *Understanding and predicting cadence effects in the characterization of exoplanet transits*, arXiv:2302.02897v1 (public 2023-02-06), https://arxiv.org/html/2302.02897v1 .
3. R. A. Loomis, K. I. Öberg, S. M. Andrews, et al., *Detecting Weak Spectral Lines in Interferometric Data through Matched Filtering*, arXiv:1803.04987 (public 2018-03-13), https://arxiv.org/abs/1803.04987 .
