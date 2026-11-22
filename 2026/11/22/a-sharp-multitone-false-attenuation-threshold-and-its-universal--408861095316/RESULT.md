# A sharp multitone false-attenuation threshold and its universal onset law for river grab samples

## Finding

For a plug-flow river with strictly positive first-order contaminant attenuation, a mismatched upstream–downstream sampling clock can nevertheless produce an **apparent increase** in concentration. A finite quasiperiodic source admits an exact, phase-independent threshold for whether such reversals ever occur. Moreover, if the source has \(m\) rationally independent positive frequencies, the fraction of time showing this misleading increase has a sharp \(m/2\)-power onset above the threshold.

Precisely, fix an integer \(m\ge1\), positive amplitudes \(b_1,\ldots,b_m\), and rationally independent frequencies \(\omega_1,\ldots,\omega_m>0\). Let the upstream signal be
\[
U(t)=C_0\left(1+\rho\sum_{j=1}^{m}b_j\cos(\omega_jt+\phi_j)\right),
\]
where \(C_0>0\), \(0<\rho<1/B\), \(B=\sum_jb_j\), and phases \(\phi_j\in\mathbb R\) are arbitrary. For travel time \(\tau>0\), attenuation rate \(\kappa>0\), and clock offset \(h\in\mathbb R\), the true downstream concentration is \(V(s)=e^{-\kappa\tau}U(s-\tau)\). Compare the **different** water parcels sampled as \(U(t)\) and \(V(t+\tau+h)\).

Put \(E=e^{\kappa\tau}>1\),
\[
c_j=b_j\sqrt{E^2+1-2E\cos(\omega_jh)},\qquad
S=\sum_{j=1}^{m}c_j,\qquad
\rho_c=\frac{E-1}{S}.
\]
Then \(V(t+\tau+h)>U(t)\) occurs at some time \(t\) **if and only if** \(\rho>\rho_c\). At or below \(\rho_c\) it never occurs. For \(\rho>\rho_c\), it occurs for a strictly positive asymptotic fraction \(P(\rho)\) of observation times, independent of the initial phases. The fraction is exactly
\[
P(\rho)=\frac1{(2\pi)^m}\operatorname{vol}\left\{\theta\in[0,2\pi)^m:\rho\sum_{j=1}^{m}c_j\cos\theta_j>E-1\right\}.
\]
For \(\rho\downarrow\rho_c\) from above in the physically admissible interval,
\[
P(\rho)=K_m(\rho-\rho_c)^{m/2}+o\big((\rho-\rho_c)^{m/2}\big),
\quad
K_m=\frac{\pi^{m/2}}{(2\pi)^m\Gamma(1+m/2)}
\frac{(2S/\rho_c)^{m/2}}{\sqrt{\prod_{j=1}^{m}c_j}}.
\]
There is a nonempty admissible reversal regime \(\rho_c<\rho<1/B\) **if and only if** at least one \(\omega_jh\) is not an integer multiple of \(2\pi\). In particular, matched water-parcel sampling \(h=0\) cannot create an apparent concentration gain, and for two rationally independent frequencies it is the *only* real clock offset that prevents false gains for **every** physically admissible modulation amplitude. This last uniqueness statement holds for any \(m\ge2\) with rationally independent positive frequencies.

## Assumptions and scope

This is a deterministic, stationary-source, one-dimensional plug-flow model with constant water flux, travel time and first-order reaction. There are no tributaries, dilution changes, dispersion, measurement noise, or true downstream sources. Phases are fixed but arbitrary. The strict bound \(\rho B<1\) ensures \(U(t)>0\) for all times. Frequencies are rationally independent over the integers: \(\sum_jn_j\omega_j=0\) for integers \(n_j\) implies all \(n_j=0\). Observation time ranges over the entire nonnegative half-line when time fractions are defined. A reported apparent increase means the strictly positive inequality \(V(t+\tau+h)>U(t)\), not true negative attenuation.

At the threshold \(\rho_c\), the strictly positive event never occurs, even if the quasiperiodic phase orbit only approaches rather than reaches its maximizing phase. The onset statement concerns fixed positive amplitudes and fixed frequencies as \(\rho\) varies; it is not uniform when some amplitudes tend to zero or frequencies become resonant.

## Proof

**1. Reduction to independent phasors.** Since \(V(t+\tau+h)=E^{-1}U(t+h)\), an apparent increase is equivalent to \(U(t+h)>EU(t)\). Substituting the signal gives
\[
\rho\sum_jb_j\big[\cos(\omega_jt+\phi_j+\omega_jh)-E\cos(\omega_jt+\phi_j)\big]>E-1.
\]
Each bracket is a sinusoid of phase \(\omega_jt+\phi_j\) with amplitude \(c_j/b_j\). Thus, after constant phase rotations, the inequality is \(\rho\sum_jc_j\cos\theta_j(t)>E-1\). The maximum on the phase torus is \(\rho S\), attained uniquely modulo \(2\pi\) at \(\theta_1=\cdots=\theta_m=0\). If \(\rho\le\rho_c\), no phase can satisfy the strict inequality. If \(\rho>\rho_c\), an open neighborhood of the maximizing phase satisfies it.

**2. The time-frequency dichotomy.** For each nonzero integer vector \(n\), rational independence gives \(n\cdot\omega\ne0\), and hence
\[
\lim_{T\to\infty}\frac1T\int_0^T e^{i n\cdot(\omega t+\phi)}\,dt=0.
\]
By trigonometric approximation, the phase trajectory is equidistributed on the \(m\)-torus. The boundary \(\sum_jc_j\cos\theta_j=(E-1)/\rho\) has zero torus volume: fixing all but the last angle leaves at most two solutions in that angle because \(c_m>0\). Continuous approximation of the indicator then gives the asserted asymptotic time fraction. Above threshold the admissible set is a nonempty open subset, so the fraction is positive and the event occurs at arbitrarily late times.

**3. The sharp onset.** Write \(\rho=\rho_c+\varepsilon\) with \(\varepsilon>0\). The inequality is equivalent to
\[
\rho\sum_jc_j(1-\cos\theta_j)<\varepsilon S.
\]
For sufficiently small \(\varepsilon\), all admissible phases lie near the unique maximizer. On the centered torus, \(1-\cos\theta_j=\theta_j^2/2+O(\theta_j^4)\). The change of variables \(\theta_j=\sqrt\varepsilon\,y_j\), followed by dominated convergence in this shrinking neighborhood, yields the limiting ellipsoid
\[
\sum_jc_jy_j^2<\frac{2S}{\rho_c}.
\]
Its Euclidean volume is \(\pi^{m/2}(2S/\rho_c)^{m/2}/[\Gamma(1+m/2)\sqrt{\prod_jc_j}]\). Dividing by the torus volume \((2\pi)^m\) proves the stated constant and exponent. In particular the one-tone onset is square-root and the two-tone onset is linear.

**4. Clock matching.** From \(c_j^2=b_j^2[(E-1)^2+2E(1-\cos(\omega_jh))]\), each \(c_j\ge b_j(E-1)\), with equality exactly when \(\omega_jh\in2\pi\mathbb Z\). Thus \(\rho_c\le1/B\), with strict inequality exactly if at least one mode is phase-mismatched. If two positive frequencies are rationally independent, their simultaneous congruences \(\omega_jh\in2\pi\mathbb Z\) force \(h=0\); otherwise their ratio would be rational. This completes the proof.

## Verification

The accompanying `checker.py` uses only the Python standard library. Running `python3 checker.py` produces **PASS 1531 diagnostics**. It verifies 750 randomly selected phasor identities and 750 amplitude lower bounds, the sample critical value and onset constant, positivity and numerical two-tone phase fractions, the convergent one-tone and two-tone onset rates, exact clock alignment, and a long deterministic two-frequency time-sampling comparison. These finite diagnostics support implementation and numerical examples; the universal theorem is established by the preceding argument, not by finite sampling.

For the concrete example \(E=1.1\), \(h=1\), \((\omega_1,\omega_2)=(1,\sqrt2)\), and \((b_1,b_2)=(0.3,0.3)\), the admissible threshold is \(\rho_c=0.140234828216551\ldots\), and the near-threshold occupation fraction is \(2.29569085948377\ldots(\rho-\rho_c)+o(\rho-\rho_c)\). At \(\rho=0.5\), exact conditional-angle integration gives \(P(0.5)\approx0.2989389766\); a deterministic time sample gives approximately \(0.2987\).

## Relationship to prior work

Facchi, Gandolfi and Whelan (first publicly indexed online in 2006) studied grab-versus-composite river monitoring under strongly variable wastewater loads and documented the limitation of snapshot measurements. Antweiler, Writer and Murphy (online 2013) studied verified Lagrangian tracing and the need to match parcels. Schwientek and colleagues (2015) developed a high-precision mass-balance sampling protocol for variable rivers. Their 2015 open-access article, including its mathematical methodological section and mass-balance formulation, was inspected. These contributions motivate the problem and directly warn that asynchronous pollutant samples can yield spurious interpretations, but the inspected material does not give the all-mode phase-independent trigger, the quasiperiodic occupation fraction, or the \(m/2\) onset law under the precise model above.

The result specializes elementary phasor geometry and equidistribution, but is not asserted to be a new general theorem of harmonic analysis: its candidate contribution is the joint sharp diagnosis and frequency-count sensitivity for an idealized river monitoring problem. Earlier literature may contain equivalent formulas; historical priority remains provisional, especially because two closely relevant primary full texts could not be retrieved.

## Limitations

The result does not cover temporal trends, stochastic flows, hydrodynamic dispersion, phase drift, detection limits, irregular sampling windows, time-varying reaction rates, or nonlinear chemistry. Irrational-frequency equidistribution is an infinite-time idealization; arbitrarily slow convergence may occur for near-resonant frequencies, and the theorem supplies no finite-horizon guarantee. A downstream increase under different-parcel sampling does not prove downstream production, while an observed decrease does not prove absence of production when the model assumptions fail. The threshold uses known source modulation amplitudes and travel time. No field-performance or calibration claim is made.

## References

1. Facchi, A., Gandolfi, C. and Whelan, M. J. (2007). *A comparison of river water quality sampling methodologies under highly variable load conditions*. Chemosphere 66, 746–756. Earliest online article date 2006-09-27, PubMed PMID 17007904. https://doi.org/10.1016/j.chemosphere.2006.07.050
2. Antweiler, R. C., Writer, J. H. and Murphy, S. F. (2014). *Evaluation of wastewater contaminant transport in surface waters using verified Lagrangian sampling*. Science of the Total Environment 470–471, 551–558. First online 2013-10-26. https://doi.org/10.1016/j.scitotenv.2013.09.079
3. Schwientek, M., Guillet, G., Rügner, H., Kuch, B. and Grathwohl, P. (2015). *A high-precision sampling scheme to assess persistence and transport characteristics of micropollutants in rivers*. Science of the Total Environment. Open-access complete text https://www.academia.edu/26321316/A_high_precision_sampling_scheme_to_assess_persistence_and_transport_characteristics_of_micropollutants_in_rivers ; DOI https://doi.org/10.1016/j.scitotenv.2015.07.135
