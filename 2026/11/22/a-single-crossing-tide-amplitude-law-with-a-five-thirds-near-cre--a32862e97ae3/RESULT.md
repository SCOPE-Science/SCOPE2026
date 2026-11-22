# A single-crossing tide-amplitude law with a five-thirds near-crest boundary layer

## Finding

Let a positive, exponentially distributed storm-surge increment be independent of the uniformly random phase of a sinusoidal astronomical tide. Comparing any two distinct tidal amplitudes, the probability that their combined level exceeds a **nonnegative** fixed threshold changes ordering exactly once: larger tides reduce low-threshold exceedance and increase high-threshold exceedance. For small tide-to-surge scale, the threshold at which this reversal occurs lies a precisely quantified fractional-power distance below the larger tidal crest.

Precisely, for independent \(S\) and \(\Phi\), with \(\Pr(S>s)=e^{-s/\sigma}\) for \(s\ge0\), \(\sigma>0\), and \(\Phi\) uniform on \([0,2\pi)\), define
\[
H_A(h)=\Pr\bigl(S+A\cos\Phi>h\bigr),\qquad A\ge0,\ h\ge0.
\]
For every \(0\le A_1<A_2\) there is exactly one \(h_*\in(0,A_2)\) such that
\[
H_{A_2}(h)<H_{A_1}(h)\ (0\le h<h_*),\quad
H_{A_2}(h_*)=H_{A_1}(h_*),\quad
H_{A_2}(h)>H_{A_1}(h)\ (h>h_*).
\]
Writing \(A_2=\sigma a\), \(A_1=\rho\sigma a\), with fixed \(0\le\rho<1\), the unique threshold has the sharp weak-tide law
\[
\frac{h_*}{\sigma}
=a-C_\rho a^{5/3}+o(a^{5/3})\quad(a\downarrow0),\qquad
C_\rho=\left(\frac{3\pi(1-\rho^2)}{8\sqrt2}\right)^{2/3}.
\]

## Assumptions and scope

The increment \(S\) is nonnegative and exponential with strictly positive mean \(\sigma\). Phase is uniform and independent of \(S\); the tide is a single sinusoid centered at zero, with no trend. Exceedance is an event at a **random instantaneous phase**, not the maximum level over an entire tide cycle and not an annual flood-exceedance probability. The compared models have the same surge distribution and datum and differ only in tidal amplitude. The sign theorem covers every \(A_2>A_1\ge0\) and all \(h\ge0\). The boundary-layer constant requires \(\rho=A_1/A_2\) fixed strictly below one as \(a\to0\); it is not claimed uniformly as \(\rho\uparrow1\).

Let \(W=|\cos\Phi|\). It has density \(2/(\pi\sqrt{1-w^2})\) for \(0<w<1\), and the two signs of \(\cos\Phi\) have equal conditional probability. Let \(R_A(h)=e^{h/\sigma}H_A(h)\). The auxiliary modified Bessel function is defined without convention ambiguity by
\[
I_0(u)=\frac1{2\pi}\int_0^{2\pi}e^{u\cos\theta}\,d\theta
=\sum_{j=0}^\infty\frac{(u^2/4)^j}{(j!)^2}.
\]

## Proof

**1. Exact conditional exceedance.** On a positive/negative tide pair of magnitude \(Aw\), if \(0\le h<Aw\), the positive tide alone exceeds \(h\), while the negative tide requires an exponential increment larger than \(h+Aw\). Thus
\[
R_A(h\mid W=w)=\frac{e^{h/\sigma}+e^{-Aw/\sigma}}2\quad(0\le h<Aw).
\]
For \(h\ge Aw\), both signs require a positive surge increment and
\[
R_A(h\mid W=w)=\cosh(Aw/\sigma).
\]
The two expressions agree at \(h=Aw\). Both are continuous, and the first has derivative \(e^{h/\sigma}/(2\sigma)\) with respect to \(h\); the second has derivative zero. These statements also include \(A=0\) by continuity.

**2. Strict one-crossing.** Put \(\Delta(h)=R_{A_2}(h)-R_{A_1}(h)\). The conditional formula and dominated differentiation show, for \(0<h<A_2\),
\[
\Delta'(h)=\frac{e^{h/\sigma}}{2\sigma}
\Pr(A_1W<h<A_2W)>0.
\]
The strict inequality follows because \(W\) has strictly positive density throughout \((0,1)\), and the interval \((h/A_2,\min\{1,h/A_1\})\) has nonzero length (use upper endpoint one if \(A_1=0\)). At zero,
\[
\Delta(0)=\frac12\mathbb E\bigl[e^{-A_2W/\sigma}-e^{-A_1W/\sigma}\bigr]<0.
\]
At \(h=A_2\), both amplitudes are entirely in the second branch, yielding
\[
\Delta(A_2)=I_0(A_2/\sigma)-I_0(A_1/\sigma)>0.
\]
The last inequality holds because \(I_0'(u)=\mathbb E[W\sinh(uW)]>0\) for \(u>0\). Also \(\Delta\) is constant and positive for \(h\ge A_2\). Continuity and strict increase on \((0,A_2)\) prove the sole crossing and both strict signs. Multiplication by \(e^{h/\sigma}>0\) preserves those signs.

**3. Exact cutoff identity.** With \(a=A/\sigma\) and \(x=h/\sigma\), the conditional formula can be rewritten as
\[
R_A(h)=I_0(a)-\tfrac12\mathbb E\bigl[(e^{aW}-e^x)_+\bigr],
\]
where \((z)_+=\max\{z,0\}\). Thus the crossing solves an explicit one-dimensional integral equation. Its uniqueness was established in step 2; no numerical root finding is used as proof.

**4. Weak-tide asymptotics.** Fix \(0\le\rho<1\), set \(A_2=\sigma a\) and let \(x=h_*/\sigma\), \(d=a-x\). For each fixed \(c\in(\rho,1)\), at \(x=ca\) the large-amplitude positive-part correction is of order \(a\), while \(I_0(a)-I_0(\rho a)=O(a^2)\); therefore \(\Delta(\sigma ca)<0\) for small \(a\). By the unique-crossing result, \(x/a\to1\) and eventually \(x>\rho a\). Hence the smaller-amplitude positive-part correction is zero and the exact crossing equation reduces to
\[
I_0(a)-I_0(\rho a)
=\tfrac12\mathbb E\bigl[(e^{aW}-e^{a-d})_+\bigr].
\]
The Bessel series gives the left side as \((1-\rho^2)a^2/4+O(a^4)\). On the right, substitute \(u=1-W\); only \(0<u<d/a\) contributes. The arcsine density becomes
\[
\frac{2}{\pi\sqrt{2u-u^2}}=\frac{\sqrt2}{\pi}u^{-1/2}\bigl(1+O(u)\bigr).
\]
Since \(d/a\to0\), the exponential difference is uniformly \((d-au)(1+o(1))\), and direct integration yields
\[
\tfrac12\mathbb E\bigl[(e^{aW}-e^{a-d})_+\bigr]
=\frac{2\sqrt2}{3\pi}\frac{d^{3/2}}{\sqrt a}\bigl(1+o(1)\bigr).
\]
Equating the two leading terms gives
\[
d=\left(\frac{3\pi(1-\rho^2)}{8\sqrt2}\right)^{2/3}a^{5/3}(1+o(1)),
\]
which is exactly the stated sharp law.

## Verification

Run `python3 check_tidal_exceedance.py` from the extracted file directory (Python standard library only). It tests separate direct-integral and Bessel-positive-part formulas, normalized differences and signs over several amplitudes, the exact derivative identity, the small-amplitude coefficient and a physical-dimension benchmark. This finite checker supplements, not replaces, the preceding proof.

For \(\sigma=1\) meter, \(A_1=0.5\) meter and \(A_2=1\) meter, numerical quadrature gives \(h_*\approx0.533675162946\) meter. At \(h=0.1\) meter the exceedance probabilities are approximately \(0.82999983\) for the smaller tide and \(0.74992348\) for the larger; at \(h=0.75\) meter the respective probabilities are \(0.50235397\) and \(0.55597361\). The fixed phase-pair approximation is different: it yields \(h_*=\sigma\log(2\cosh(A_1/\sigma)-e^{-A_2/\sigma})\approx0.63518564\) meter for these values.

## Relationship to prior work

The convolution of independent tide and surge distributions is established coastal-flood methodology, not a new claim. Sweet and Park (2014) analyze changes in level exceedances and the effects of tidal range using empirical/sigmoidal curves. Williams and colleagues (2016) study independence of large skew surges and high tides, providing a motivation for idealized independence but not a general assertion about instantaneous phase. The 2016 FEMA guidance specifically discusses sinusoidal density concentrated near extrema and approximating peaks by equal high/low pairs; that approximation leads to a different crossover and does not determine the arcsine near-crest asymptotic. Subsequent full-text studies in 2020 and 2021 give joint-probability convolution methods, and Palmer and colleagues (2024) quantify empirical contributions of changed tides and surges. These works make the input convolution familiar and support the problem's importance; no exact all-amplitude single-crossing theorem combined with its \(5/3\) weak-tide boundary-layer constant was identified in those inspected treatments. This does not establish historical uniqueness: classical stochastic-order and single-crossing theory may imply the qualitative part, and other coastal-flood studies may include an equivalent limit.

## Limitations

This is a stylized single-instant benchmark, not a calibrated coastal flood prediction, an annual return period, or a claim of physical tide–surge independence at every location. Real tides are multifrequency, storm surges may be negative and nonexponential, temporal dependence and hydrodynamic interaction can matter, and surge peaks have durations. Replacing the full sinusoid by binary high/low tides changes the threshold and eliminates the reported near-crest coefficient. No universality is claimed for non-exponential surge tails or for the \(5/3\) exponent under arbitrary tidal waveforms. Originality remains subject to more extensive historical review and independent scientific assessment.

## References

- Sweet, W. V., and J. Park (2014), *From the extreme to the mean: Acceleration and tipping points of coastal inundation from sea level rise*, Earth's Future. First public 18 December 2014. https://doi.org/10.1002/2014EF000272
- Williams, J., K. J. Horsburgh, J. A. Williams, and R. N. F. Proctor (2016), *Tide and skew surge independence: New insights for flood risk*, Geophysical Research Letters. First public 1 June 2016. https://doi.org/10.1002/2016GL069522
- FEMA (2016), *Coastal Flood Frequency and Extreme Value Analysis*, section 4.3. https://www.fema.gov/sites/default/files/2020-02/Coastal_Flood_Frequency_and_Extreme_Value_Analysis_Guidance_Nov_2016.pdf
- *Modeling dependence and coincidence of storm surges and high tide: methodology, discussion and recommendations based on a simplified case study in Le Havre (France)* (2020), Natural Hazards and Earth System Sciences. https://doi.org/10.5194/nhess-20-3387-2020
- *Trivariate copula to design coastal structures* (2021), Natural Hazards and Earth System Sciences, especially section 2.4.2. https://doi.org/10.5194/nhess-21-239-2021
- Palmer, K., et al. (2024), *Quantifying the Mean Sea Level, Tide, and Surge Contributions to Changing Coastal High Water Levels*, Journal of Geophysical Research: Oceans. https://doi.org/10.1029/2023JC020737
