# A sharp fixed-template penalty for Doppler-smeared Gaussian spectroscopy

## Finding
Consider a weak Gaussian spectral line translated at a nonzero constant Doppler rate, with independent photon-noise-limited exposures and a fixed positive readout overhead. An observer who cross-correlates each time-integrated line with the **unbroadened line at that exposure's midpoint** has a unique information-rate-maximizing duration; it increases strictly with overhead but **saturates at a finite duration**. In contrast, an observer using the optimally Doppler-broadened template has a unique duration growing as the square root of overhead. The two strategies have the same cube-root optimal exposure law at small overhead. At large overhead the best fixed template retains exactly
\[
R_*=\frac{\sqrt\pi\,\operatorname{erf}(x_*)^2}{2x_*}=0.629396379324979\ldots
\]
of the optimized broadened-template squared signal-to-noise per wall time, where \(x_*=0.989939082841904\ldots\) is the unique positive solution of \(4x e^{-x^2}=\sqrt\pi\,\operatorname{erf}(x)\). This is an exact idealized **template-choice** distinction, not a statement about a particular data-reduction pipeline.

## Assumptions and scope
Fix \(\sigma>0\), Doppler drift speed \(a\in\mathbb R\setminus\{0\}\), and a fixed overhead \(h>0\) per exposure. Write \(\beta=|a|/(4\sigma)\). In the Doppler velocity coordinate \(v\in\mathbb R\), let the real normalized intrinsic line be
\[
g(v)=(\sqrt\pi\,\sigma)^{-1/2}\exp[-v^2/(2\sigma^2)],\qquad \|g\|_2=1.
\]
The integrated, known-centered line acquired in an exposure of duration \(t>0\) is
\[
S_t(v)=\int_{-t/2}^{t/2}g(v-as)\,ds.
\]
Assume a constant weak-line amplitude, spectrally white independent noise with variance per spectral coordinate proportional to \(t\), and disjoint statistically independent exposures. Each exposure incurs clock time \(t+h\); no other costs, source variability, transit boundary, finite detector aperture or changing drift rate are included. Exposures are centered accurately in their own reference frame. A *fixed-template* correlation uses \(g\) rather than the time-smeared \(S_t\); the full matched filter uses \(S_t\) itself. We optimize independent-exposure squared signal-to-noise per **total wall-clock time** over positive exposure lengths. Multiple heterogeneous durations cannot exceed the optimum homogeneous information rate, because each exposure's information is additive and its wall-clock cost is additive.

Define
\[
J_f(t;h)=\frac{|\langle S_t,g\rangle|^2}{t(t+h)},\qquad
J_m(t;h)=\frac{\|S_t\|_2^2}{t(t+h)}.
\]
The result holds for every stated \(\sigma,a,h\). With \(\operatorname{erf}(x)=(2/\sqrt\pi)\int_0^x e^{-u^2}\,du\), the unique fixed-template optimizer is \(t_f=x_h/\beta\), where \(x_h\in(0,x_*)\) solves
\[
\frac{4x_h e^{-x_h^2}}{\sqrt\pi\,\operatorname{erf}(x_h)}
=1+\frac{x_h}{x_h+\beta h}.
\]
The unique full-template optimizer is \(t_m\), the positive zero of \((t+h)F'(t)-F(t)\), where
\[
F(t)=\frac2t\int_0^t(t-u)e^{-4\beta^2u^2}\,du,
\quad F'(t)=\frac2{t^2}\int_0^t u e^{-4\beta^2u^2}\,du.
\]
Both optima are strictly increasing functions of \(h\), and their sharp limits are
\[
\begin{aligned}
t_f&\sim\left(\frac{3h}{4\beta^2}\right)^{1/3},&
t_m&\sim\left(\frac{3h}{4\beta^2}\right)^{1/3},&&h\downarrow0,\\
t_f&\longrightarrow x_*/\beta,&
t_m&\sim\sqrt{\frac{h}{2\beta\sqrt\pi}},&&h\longrightarrow\infty.
\end{aligned}
\]
For every positive overhead, \(\max_tJ_f(t;h)<\max_tJ_m(t;h)\); the ratio of these maxima tends to one for small overhead and to \(R_*\) for large overhead.

## Proof
**Step 1: direct correlation and noise normalization.** Completing a square gives
\[
\langle g(\cdot-u),g\rangle=e^{-u^2/(4\sigma^2)}.
\]
Therefore, integrating at constant speed within an exposure,
\[
\langle S_t,g\rangle=\int_{-t/2}^{t/2}e^{-4\beta^2s^2}\,ds
=\frac{\sqrt\pi}{2\beta}\operatorname{erf}(\beta t).
\]
Independent spectrally white noise has projected variance proportional to \(t\|g\|_2^2=t\) for the fixed filter. The matched filter has squared signal-to-noise \(\|S_t\|_2^2/t\). The overlap of two shifted Gaussian lines yields
\[
\|S_t\|_2^2=2\int_0^t(t-u)e^{-4\beta^2u^2}\,du.
\]
Consequently
\[
J_f(t;h)=\frac{\pi\operatorname{erf}(\beta t)^2}{4\beta^2t(t+h)},
\qquad J_m(t;h)=\frac{F(t)}{t+h}.
\]
For any exposure durations \(t_1,\ldots,t_N>0\), the sum of their independent squared signal-to-noise contributions is at most \((\sum_i(t_i+h))\sup_tJ_\bullet(t;h)\). Periodic repetition of an optimizer attains that rate (up to an incomplete final cycle). This justifies optimizing the scalar rates even against heterogeneous calendars.

**Step 2: fixed-template uniqueness and monotonicity.** Put \(x=\beta t\), \(d=\beta h\), and
\[
E(x)=\frac{2xe^{-x^2}}{\sqrt\pi\operatorname{erf}(x)}
=\left(\int_0^1 e^{x^2(1-v^2)}\,dv\right)^{-1}.
\]
The integral representation proves that \(E\) decreases strictly from one to zero. Differentiating \(\log J_f\) gives the stationary equation \(2E(x)=1+x/(x+d)\). Its left-hand side strictly decreases from two to zero and its right-hand side strictly increases from one to two, so there is exactly one positive stationary point; since \(J_f\to0\) at both boundaries, it is the unique global maximum. Increasing \(d\) decreases the right-hand side at fixed \(x\), hence increases the unique root. Because \(2E(x)>1\) at the root, \(x<x_*\), where \(E(x_*)=1/2\); the unique root converges to \(x_*\) as \(d\to\infty\).

**Step 3: full-template uniqueness and divergence.** Write \(K(u)=e^{-4\beta^2u^2}\). Direct differentiation yields
\[
F'(t)=\frac2{t^2}\int_0^tuK(u)\,du>0,
\quad F''(t)=\frac4{t^3}\left(\frac{t^2}2K(t)-\int_0^t uK(u)\,du\right)<0.
\]
The final inequality is strict because \(K\) decreases strictly. Moreover \(F(0+)=0\), \(F'(0+)=1\), \(F(t)\to2M_0\), and \(F'(t)\to0\), where \(M_j=\int_0^\infty u^jK(u)\,du\). Thus \(H_h(t)=(t+h)F'(t)-F(t)\) strictly decreases from \(h\) to \(-2M_0\), so its unique zero maximizes \(J_m\). Increasing \(h\) increases \(H_h\) pointwise, hence strictly increases the zero. Its zero diverges as \(h\to\infty\), since \(F'(t)>0\) at each finite \(t\).

**Step 4: sharp overhead laws.** At small \(t\), both information-per-exposure quantities obey
\[
\frac{|\langle S_t,g\rangle|^2}{t}=t-\frac23\beta^2t^3+O(t^5),\qquad
F(t)=t-\frac23\beta^2t^3+O(t^5).
\]
Since each optimizing duration tends to zero when \(h\downarrow0\), the stationary equations give \(h\sim(4/3)\beta^2t^3\), yielding the common cube-root law. For large \(t\), \(F(t)=2M_0-2M_1/t+o(1/t)\) and \(F'(t)=2M_1/t^2+o(t^{-2})\). At the diverging optimum \(t_m\), the equation \((t_m+h)F'(t_m)=F(t_m)\) implies \(t_m/h\to0\) and \(t_m^2\sim hM_1/M_0\). Gaussian integration gives \(M_0=\sqrt\pi/(4\beta)\) and \(M_1=1/(8\beta^2)\), proving the square-root law.

**Step 5: strict advantage and sharp information loss.** Cauchy–Schwarz yields \(|\langle S_t,g\rangle|^2<\|S_t\|_2^2\) for \(t>0\): equality would require the Gaussian average of nontrivially shifted Gaussian functions to be proportional to the original Gaussian, which is false (for instance their Fourier transforms have a nonconstant sinc multiplier). Thus \(J_f(t;h)<J_m(t;h)\) pointwise; evaluating at the fixed optimizer gives a strict inequality between optimal rates. As \(h\to\infty\), multiplying both maxima by \(h\) gives
\[
\begin{aligned}
h\max_tJ_f(t;h)&\to\frac{\pi\operatorname{erf}(x_*)^2}{4\beta x_*},\\
h\max_tJ_m(t;h)&\to\frac{\sqrt\pi}{2\beta}.
\end{aligned}
\]
Their quotient is exactly \(R_*\). At small \(h\), both maximizing rates approach one in the chosen unit normalization, so their quotient approaches one. This completes the claim.

## Verification
The standalone Python 3 script `verify.py` uses only the standard library. It evaluates the two stationary equations with bisection, integrates the Gaussian autocorrelation independently by composite Simpson quadrature, checks the optimizer against off-peak exposures, tests sharp asymptotic regimes and verifies the numerical constants. It passed **3,561 supplementary numerical assertions**. These tests verify arithmetic and implementation but do not replace the proof above.

An illustrative, **not instrument-calibrated**, setting \(\sigma=1500\) meters per second, \(|a|=3\) meters per second squared, and \(h=14\) seconds gives \(\beta=0.0005\) inverse seconds, \(t_f\approx343.9138\) seconds and \(t_m\approx346.2406\) seconds. The high-overhead limit is a mathematical limit of the stationary model; real transits cannot accommodate arbitrarily long repeated exposures.

## Relationship to prior work
Boldt-Christmas and collaborators (2023/2024) simulated the cadence tradeoff for high-resolution transiting-exoplanet spectroscopy, including Doppler smearing and overhead, and identified case-dependent empirical optima. Their realistic pipeline simulations do not contain this fixed-versus-broadened Gaussian exact comparison, universal limiting template penalty or proof of unique optimum in the simplified model. Beatty and Gaudi (2015) derived Gaussian and other line-shape precision laws for radial-velocity measurements, not this exposure/overhead template-choice asymptotic. A previously available exact idealized result for **fully matched** Doppler-smeared profiles already provides the full-template uniqueness and overhead-square-root law; those components are included here as *known comparison benchmarks*, not claimed as independent new contributions. The new mathematical contribution is the fixed-template uniqueness, finite saturation and exact nonzero asymptotic information deficit relative to that benchmark. Neither empirical detection-significance optima nor the fully matched theorem alone imply the fixed-template scalar law or its \(R_*\) constant.

## Limitations
The noise law omits per-read detector variance, heteroscedastic pixels and correlation; adding them changes the objective. Doppler acceleration, a line spread function varying in time, varying photon flux, blended lines, stellar and telluric removal and a finite orbital/transit observing window are not analyzed. The fully matched and fixed filters have different assumptions about the analysis template, but neither includes uncertainty in the Doppler ephemeris or normalization fitted from the data. The large-overhead performance ratio does **not** quantify the performance of a real telescope at infinite overhead or any specific pipeline. No field or observing-campaign validation is asserted, and historical novelty remains subject to independent literature assessment.

## References
1. L. Boldt-Christmas et al., *Optimising spectroscopic observations of transiting exoplanets*, arXiv:2312.08320v1, first public 2023-12-13; *Astronomy & Astrophysics* 683, A244 (2024), https://doi.org/10.1051/0004-6361/202347398. Author-hosted open full text: https://www.astro.uu.se/~oleg/papers/lbc1.pdf.
2. T. G. Beatty and B. S. Gaudi, *Astrophysical Sources of Statistical Uncertainty in Precision Radial Velocities and Their Approximations*, arXiv:1507.00780 (2015), https://arxiv.org/abs/1507.00780.
3. J. Hernandez Camero, C. S. K. Ho, and V. Van Eylen, *Understanding and predicting cadence effects in the characterization of exoplanet transits*, arXiv:2302.02897 (2023), https://arxiv.org/abs/2302.02897. Different photometric cadence objective.
