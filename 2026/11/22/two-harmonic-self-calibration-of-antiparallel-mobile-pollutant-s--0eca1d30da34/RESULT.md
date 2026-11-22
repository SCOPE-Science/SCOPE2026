# Two-harmonic self-calibration of antiparallel mobile pollutant scans

## Finding

Consider two exactly periodic, constant-speed scans in opposite directions through one *unknown but unchanged* spatial concentration field, with a common first-order response length \(\ell>0\). Allow an unknown relative position offset, two arbitrary additive instrument baselines, and two unknown **positive** instrument gains. The spatial concentration itself need not be sinusoidal, calibrated, or reconstructed in advance.

**Theorem (exact two-harmonic calibration and sharp feasibility).** Suppose the first and second complex Fourier coefficients in both scans are nonzero and the underlying concentration coefficients at these frequencies are nonzero. Define the complex reverse-to-forward scan ratios \(R_1,R_2\) as in the next section. There exists a positive finite response length \(\ell\), a positive relative gain \(\rho\), and a relative registration shift \(\delta\in\mathbb R/(2\pi\mathbb Z)\) consistent with the pair of ratios **if and only if**

\[
 |R_1|=|R_2|>0,\qquad
 -\pi<\operatorname{Arg}\!\left(\frac{R_2/|R_2|}{(R_1/|R_1|)^2}\right)<0.
\]

When these conditions hold, all three quantities \((\ell,\rho,\delta)\) are uniquely determined by the two complex ratios. In fact, writing \(z=(R_2/|R_2|)/(R_1/|R_1|)^2\), \(\theta=\operatorname{Arg}z\), and \(q=-\tan(\theta/2)>0\), \(\ell\) is the unique positive solution of

\[
 \frac{2\ell^3}{1+3\ell^2}=q,
\]

and

\[
\rho=|R_1|,\qquad
\delta\equiv2\arctan\ell-\operatorname{Arg}(R_1)\pmod{2\pi}.
\]

Two nonzero harmonics are **minimal** for identifying an unknown response length and an unknown relative position shift jointly: observing only one harmonic leaves a continuous family of positive \(\ell\) values compatible with the same observations. The inversion becomes ill-conditioned for very short or very long sensor response lengths, according to the exact phase derivative and endpoint expansions below.

The theorem is about the *two ratios*, not about arbitrary full observed traces: for full traces, additional harmonics must satisfy corresponding model equalities. Its scope is an idealized inverse measurement model rather than calibrated outdoor deployment.

## Assumptions and scope

Use the angular coordinate \(x\in\mathbb R/(2\pi\mathbb Z)\) on a closed transect of physical circumference \(L>0\), scanned at known speed \(v>0\). Let \(c(x)\) be a real, strictly positive, sufficiently smooth, periodic concentration profile, unchanged over both scans, with Fourier coefficients

\[
 C_n=\frac{1}{2\pi}\int_0^{2\pi}c(x)e^{-inx}\,dx,\qquad C_1C_2\ne0.
\]

Let \(\ell=(2\pi v/L)\tau\), where \(\tau>0\) is the same unknown physical first-order sensor time constant in both scan directions. After stationary periodic transients have decayed, forward and reverse physical response profiles satisfy

\[
 \ell\,w_+'(x)+w_+(x)=c(x),\qquad
 -\ell\,w_-'(x)+w_-(x)=c(x).
\]

Measured registered profiles have the form

\[
 y_+(x)=b_++g_+w_+(x),\qquad
 y_-(x)=b_-+g_-w_-(x-\delta),
\]

where offsets \(b_\pm\in\mathbb R\), gains \(g_\pm>0\), and relative shift \(\delta\) are unknown. Their nonzero-frequency Fourier coefficients are \(Y_{\pm,n}\); define \(R_n=Y_{-,n}/Y_{+,n}\) for \(n=1,2\). The unknown concentration field can have any further harmonics. The positive-gain assumption excludes a sign-flip ambiguity; the same-time-constant assumption and stationary periodic field are essential.

## Proof

**1. Fourier elimination of the unobserved field.** Integrating the response equations against \(e^{-inx}\) and using periodic boundary conditions gives, for each integer \(n\ne0\),

\[
 W_{+,n}=\frac{C_n}{1+in\ell},\quad
 W_{-,n}=\frac{C_n}{1-in\ell}.
\]

The additive baselines affect only the zero Fourier mode; the spatial offset multiplies the reverse coefficient by \(e^{-in\delta}\). Therefore

\[
 \boxed{R_n=\rho e^{-in\delta}\frac{1+in\ell}{1-in\ell}},\qquad
 \rho=\frac{g_-}{g_+}>0.
\]

In particular, \(|R_n|=\rho\) for every measured nonzero harmonic. The unknown field coefficient \(C_n\) has cancelled *without any assumption on its phase or magnitude*.

**2. Shift-free phase curvature.** Since \((1+iu)/(1-iu)=\exp(2i\arctan u)\) for real \(u>0\), set \(u_n=R_n/|R_n|\). Then

\[
 u_n=\exp\big(i[2\arctan(n\ell)-n\delta]\big).
\]

Consequently

\[
 z=\frac{u_2}{u_1^2}=\exp\big(i\Theta(\ell)\big),\qquad
 \Theta(\ell)=2\arctan(2\ell)-4\arctan\ell.
\]

Direct differentiation yields

\[
\Theta'(\ell)=-\frac{12\ell^2}{(1+\ell^2)(1+4\ell^2)}<0,
\]

and \(\Theta(0+)=0\), \(\Theta(+\infty)=-\pi\). Thus \(\Theta\) is a bijection from \((0,\infty)\) to \((-\pi,0)\). It never winds around the unit circle, so its principal argument specifies \(\ell\) uniquely. Taking the tangent of half this phase difference gives the rational exact inverse

\[
 -\tan\frac{\Theta(\ell)}2=\tan(2\arctan\ell-\arctan(2\ell))=\frac{2\ell^3}{1+3\ell^2}.
\]

The right-hand side is strictly increasing from zero to infinity, since its derivative is \(6\ell^2(1+\ell^2)/(1+3\ell^2)^2>0\). Thus there is one and only one positive root for any \(q>0\).

**3. Reconstruction, sufficiency and exact limitations.** The modulus of either ratio gives \(\rho\). The first ratio determines \(\delta\) uniquely modulo the circumference by the displayed formula. Conversely, suppose two nonzero complex ratios have equal moduli and their invariant argument lies in \((-\pi,0)\). Construct the unique \(\ell\), then \(\rho,\delta\). The reconstructed model exactly reproduces \(R_1\) and \(R_2\) because the modulus, first-harmonic phase, and relative second-harmonic phase all agree. These ratio data can be realized using a real strictly positive concentration \(c(x)=C_0+\varepsilon\cos x+\varepsilon\cos2x\) with \(C_0>2\varepsilon>0\), suitable positive gains, and arbitrary baselines, because the Fourier transfer coefficients cancel in both ratios. This proves sufficiency at the ratio level.

For only one available nonzero mode \(n\), fix its nonzero ratio \(R_n\). For every choice \(\ell>0\) let \(\rho=|R_n|\) and \(\delta\equiv[2\arctan(n\ell)-\operatorname{Arg}(R_n)]/n\pmod{2\pi/n}\). Thus a continuum of distinct positive response lengths yields the same ratio. Even knowing the entire shape of the unknown single-harmonic input only up to scale and phase cannot resolve that confounding.

For an additional nonzero mode \(n\ge3\), an independent falsifiable restriction is

\[
\frac{R_n}{\rho}=e^{-in\delta}\frac{1+in\ell}{1-in\ell}.
\]

No claim is made that arbitrary full-trace data satisfying only the first two ratios necessarily come from the model.

**4. Sharp conditioning at both boundaries.** Taylor expansion of the *exact* invariant yields

\[
 \Theta(\ell)=-4\ell^3+12\ell^5+O(\ell^7)\quad(\ell\downarrow0),
\]

\[
 \Theta(\ell)=-\pi+\frac3\ell+O(\ell^{-3})\quad(\ell\to\infty).
\]

Thus \(|\Theta'(\ell)|^{-1}\sim1/(12\ell^2)\) as \(\ell\downarrow0\) and \(|\Theta'(\ell)|^{-1}\sim\ell^2/3\) as \(\ell\to\infty\). Exact identification at both finite positive response lengths does not imply stable identification from noisy phases near either endpoint.

## Verification

For the exact witness \(\ell=1/2\), the inversion invariant equals

\[
 z=\frac{24-7i}{25},\qquad q=\frac17.
\]

The recovery equation \(14\ell^3-3\ell^2-1=0\) factors exactly as \((2\ell-1)(7\ell^2+2\ell+1)=0\). The quadratic factor is strictly positive on \(\ell>0\), so the physical solution is \(\ell=1/2\).

The accompanying standalone \(\texttt{check.py}\) uses deterministic random seeds to synthesize 2,000 strictly positive multiharmonic periodic fields, both scan filters, unknown offsets, gains and spatial shifts. It reconstructs \(\ell,\delta,\rho\) from the first two complex ratios, checks four higher harmonics per scenario, and tests the exact witness, derivative, and asymptotic expansions. It uses NumPy and SciPy. These are numerical cross-checks; the infinite-parameter theorem follows from the proof above rather than enumeration.

## Relationship to prior work

First-order sensor lag, spatial relocation during a moving traverse, and laboratory response-time correction are established in Hübner et al. (2014), particularly its response-time equation and correction procedure. That work measures response constants in separate laboratory steps and corrects directional spatial errors; the present exact idealization instead identifies an unknown response time and an unknown relative spatial shift **jointly from two opposite field traverses without measuring the input field**, despite independent gains and baselines.

Buehler et al. (2021) measured e-folding times and used calibration/reference instrumentation in mobile air-quality monitoring. Hofman et al. (2024; first public preprint 21 June 2024) studied portable mobile-air-quality sensors, spatial heterogeneity, GPS accuracy and the need for calibration. Neither empirical result, as inspected, states the two-harmonic inverse and feasibility theorem. General first-order transfer functions and the Fourier shift law are classical mathematics: originality is assessed for the combined unknown-input, registration-invariant, minimally two-harmonic reconstruction, exact admissibility region and endpoint conditioning, not for those building blocks.

## Limitations

This is a noiseless, stationary, uniform-speed, periodic-track model. It assumes the same positive first-order response length in both directions, an unchanged spatial field, a valid periodic steady state, strictly positive gains, and both harmonics detectable. If the response times differ, if the field drifts, if platform speeds differ without correction, or if there is unmodeled instrument delay, the two-harmonic conditions need not hold. A finite open transect with unknown transient state is not equivalent to the periodic steady-state problem. Sensitivity to phase noise diverges at both response-length boundaries. Physical time \(\tau\) cannot be recovered from \(\ell\) without known spatial scale and speed. Absolute pollutant concentration, absolute gain and each baseline are not identified by the two ratios. No field validation, data-fitting superiority, or priority over all possible historical system-identification literature is claimed.

## References

- Hofman, J., Lazarov, B., Stroobants, C., Elst, E., Smets, I. and Van Poppel, M. *Portable Sensors for Dynamic Exposure Assessments in Urban Environments: State of the Science*. Preprint publicly posted 21 June 2024, https://doi.org/10.20944/preprints202406.1513.v1; peer-reviewed Sensors 24 (2024) 5653, https://doi.org/10.3390/s24175653.
- Hübner, J., Olesch, J., Falke, H., Meixner, F. X. and Foken, T. *A horizontal mobile measuring system for atmospheric quantities*. Atmospheric Measurement Techniques 7 (2014), 2967–2980, https://doi.org/10.5194/amt-7-2967-2014.
- Buehler et al. *Stationary and portable multipollutant monitors for high-spatiotemporal-resolution air quality studies including online calibration*. Atmospheric Measurement Techniques 14 (2021), 995–1013, https://doi.org/10.5194/amt-14-995-2021.
