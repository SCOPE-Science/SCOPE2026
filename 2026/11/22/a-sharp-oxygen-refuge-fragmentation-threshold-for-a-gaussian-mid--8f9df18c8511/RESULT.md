# A sharp oxygen-refuge fragmentation threshold for a Gaussian midwater deficit

## Finding

**Theorem (complete vertical-connectivity phase diagram).** Fix a finite depth range \(0\le z\le H\), an oxygen-deficit centre \(0<z_c<H\), a width \(\sigma>0\), a thermal compensation slope \(\kappa>0\), and a relative deficit \(0<\rho<1\). Define the idealized, dimensionless aerobic-viability score

\[
\Phi(z)=e^{\kappa z}\left[1-\rho\exp\left(-\frac{(z-z_c)^2}{2\sigma^2}\right)\right].
\]

For a requirement \(\theta>0\), a viable depth band is a connected component of \(V_\theta=\{z\in[0,H]:\Phi(z)\ge\theta\}\) having positive length. Set

\[
a=\kappa\sigma,\qquad b=\frac{z_c}{\sigma},\qquad
u=\frac{\sqrt{a^2+4}-a}{2},\qquad
\rho_c=a\nu e^{\nu^2/2},
\]

and define the *sharp fragmentation threshold*

\[
\rho_{\mathrm{frag}}(a,b)=
\begin{cases}
\displaystyle \frac{a e^{b^2/2}}{a+b},&0<b<\nu,\\[6pt]
\displaystyle a\nu e^{\nu^2/2},&b\ge\nu.
\end{cases}
\]

Then \(0<\rho_c\le\rho_{\mathrm{frag}}<1\). The score \(\Phi\) is strictly increasing throughout the depth range if \(\rho\le\rho_{\mathrm{frag}}\), hence every \(V_\theta\) is connected or empty. If \(\rho>\rho_{\mathrm{frag}}\), the score has exactly one strict **interior minimum**, strictly shallower than the oxygen-deficit centre, and there is a nonempty open interval of requirements \(\theta\) giving **exactly two** positive-length viable bands. No requirement can give three such bands. In particular, there exists a requirement with two viable bands if and only if \(\rho>\rho_{\mathrm{frag}}\). The threshold is independent of the bottom depth \(H\) so long as \(H>z_c\).

More precisely, when \(\rho>\rho_{\mathrm{frag}}\), write \(z_m\) for that interior minimum, \(m=\Phi(z_m)\), and \(M=\max_{0\le z\le z_m}\Phi(z)\). Then the requirements giving exactly two positive-length bands are **exactly**

\[
 m<\theta<\min\{M,\Phi(H)\}.
\]

At either endpoint of this open range a band disappears or the intervening gap closes; zero-length isolated points are not counted as bands.

**Sharp near-onset law.** In the interior-fold case \(b>\nu\), take \(\rho=\rho_c(1+\varepsilon)\) with \(\varepsilon\downarrow0\), and put \(A=\sqrt{2/(1+\nu^2)}\). If \(z_-<z_+\) are the newly created local-maximum and local-minimum depths, respectively, then

\[
\frac{z_\pm-z_c}{\sigma}=-\nu\pm A\sqrt{\varepsilon}+O(\varepsilon),
\qquad
\Phi(z_-)-\Phi(z_+)=\frac{4aA}{3}e^{a(b-\nu)}\varepsilon^{3/2}+O(\varepsilon^2).
\]

Thus the separation of the extrema opens at square-root order but the interval of viable-score thresholds that can expose their gap opens at order \(\varepsilon^{3/2}\). The exponents are generic fold behaviour; the exact oxygen-depth threshold, location correction and coefficient are model-specific.

## Assumptions and scope

The score is an idealized product of normalized oxygen availability, represented by a Gaussian-shaped *deficit* from a strictly positive baseline, and exponential compensation for declining metabolic oxygen demand with depth. The latter approximates a linear-depth change in the logarithm of the Arrhenius thermal factor, not the full temperature-dependent Arrhenius law. It is not an empirical fit. The model concerns possible aerobic habitat defined by a fixed physiological cutoff, not observed species abundance, migration, animal fitness, or connectivity through a two- or three-dimensional ocean. It assumes a finite water column that extends below the deficit centre; no linear temperature profile is extrapolated to infinite depth. The assumptions permit all real positive \(\kappa,\sigma\), all \(0<z_c<H<\infty\), all \(0<\rho<1\), and all thresholds \(\theta>0\). The assertions are exact for every such parameter choice.

## Proof

**1. Stationary-point classification.** Substitute \(x=(z-z_c)/\sigma\), so \(x\in[-b,(H-z_c)/\sigma]\) and

\[
\Phi=e^{a(b+x)}(1-\rho e^{-x^2/2}),\qquad
\frac{d\Phi}{dx}=e^{a(b+x)}\left[a-\rho(a-x)e^{-x^2/2}\right].
\]

Define \(g(x)=(a-x)e^{-x^2/2}\). For \(x\ge a\), \(g\le0\) and the derivative of \(\Phi\) is positive. For \(0\le x<a\), \(0<g\le a\), so \(a-\rho g>0\) since \(\rho<1\). On the negative half-line, \(g>0\) and

\[
 g'(x)=e^{-x^2/2}(x^2-ax-1).
\]

The unique negative critical point is \(x=-\nu\), since \(\nu^2+a\nu=1\); \(g\) increases from zero to \(g(-\nu)=(a+\nu)e^{-\nu^2/2}=e^{-\nu^2/2}/\nu\) and then strictly decreases to \(g(0)=a\). Thus \(a-\rho g\) has no zero for \(\rho<\rho_c=a/g(-\nu)\), one tangential zero for \(\rho=\rho_c\), and exactly two simple negative zeros \(x_-<-\nu<x_+<0\) for \(\rho>\rho_c\). At and below \(\rho_c\), \(\Phi\) is strictly increasing. Above \(\rho_c\) its derivative has signs \(+,-,+\), so \(x_-\) is a local maximum and \(x_+\) a local minimum. There cannot be more extrema.

**2. Effect of the surface.** Since \((H-z_c)/\sigma>0>x_+\), the local minimum is strictly interior to the physical depth range exactly when \(x_+>-b\). If \(b\ge\nu\) this holds for every \(\rho>\rho_c\). If \(0<b<\nu\), the surface lies on the decreasing branch of \(g\) between \(-\nu\) and zero. Because \(g(x_+)=a/\rho\), strict decreasingness of \(g\) on that branch gives

\[
 x_+>-b\quad\Longleftrightarrow\quad
\frac a\rho<g(-b)=(a+b)e^{-b^2/2}
\quad\Longleftrightarrow\quad
\rho>\frac{ae^{b^2/2}}{a+b}.
\]

At equality the minimum sits at the surface, and the profile is strictly increasing to its right. Consequently the displayed piecewise value is necessary and sufficient for an **interior trough**. Note that \(\rho_c<1\), because \(g(-\nu)>g(0)=a\); when \(b<\nu\), \(g(-b)>g(0)\) gives \(ae^{b^2/2}/(a+b)<1\). Also \(\rho_{\mathrm{frag}}\ge\rho_c\) because \(g(-b)\le g(-\nu)\).

**3. Exact connectivity of viable sets.** At or below the fragmentation threshold, any stationary points lie at/before the surface or are absent, so the score is strictly increasing on \([0,H]\). Above it, a strict interior trough \(z_m=z_c+\sigma x_+\) satisfies \(0<z_m<z_c<H\). Immediately to its left the score is strictly greater than \(m=\Phi(z_m)\), so \(M=\max_{[0,z_m]}\Phi>m\). To its right, \(\Phi\) increases strictly, so \(\Phi(H)>m\). For \(m<\theta<\min(M,\Phi(H))\), the shallow interval contains points above threshold and the deep interval contains points above threshold, while a neighborhood of \(z_m\) is below it. Each side has only one superlevel component by the derivative pattern \(+,-,+\). Hence there are exactly two components with positive length. Conversely, a positive-length gap between two positive-length components requires a strict interior local minimum, \(m<\theta\), a shallower value greater than \(\theta\), and a deeper value greater than \(\theta\). These are precisely the stated strict inequalities. No more than two components are possible because the derivative changes sign at most twice.

**4. Near-fold expansion.** Set \(u=\nu\), \(x_*=-u\), and \(\rho=\rho_c(1+\varepsilon)\). The logarithm of \(g\) has vanishing derivative at \(x_*\) and second derivative \(-1-u^2\). Taylor's theorem gives

\[
 g(x_*+\delta)=g(x_*)\left[1-\frac{1+u^2}{2}\delta^2+O(\delta^3)\right].
\]

The two solutions of \(\rho g=a\) therefore satisfy \(\delta_\pm=\pm A\sqrt\varepsilon+O(\varepsilon)\), where \(A=\sqrt{2/(1+u^2)}\). Between them, uniform Taylor expansion of the score derivative yields

\[
\frac{d\Phi}{dx}=a e^{a(b-u)}\left[-\varepsilon+\frac{1+u^2}{2}\delta^2+O(\varepsilon|\delta|+|\delta|^3+\varepsilon^2)\right].
\]

Integrating the negative derivative from \(\delta_-\) to \(\delta_+\) shows that \(\Phi(z_-)-\Phi(z_+)=\frac{4aA}{3}e^{a(b-u)}\varepsilon^{3/2}+O(\varepsilon^2)\), as asserted. The condition \(b>u\) ensures that both stationary points lie in \([0,H]\) for sufficiently small positive \(\varepsilon\). This completes the proof.

## Verification

The standard-library script `CHECK.py` independently checks the exact phase boundary, stationary-root locations, existence of positive-length bands, boundary monotonicity, a numerical depth example, and the two fold exponents and coefficient. Run `python3 CHECK.py` next to this file; it reports 25,814 passing supplementary assertion groups. These finite computations are checks of examples and numerical evaluations, **not** proofs over the continuum of parameter values; the proof above supplies the general result.

An explicit dimensionless example is \(\kappa\sigma=0.5\), \(z_c/\sigma=2\), \(\rho=0.8\), and \(H/\sigma=4\). Here \(\rho_c\approx0.5295076091\), the local maximum is at \(z/\sigma\approx0.4627158766\), and the local minimum is at \(z/\sigma\approx1.8696692361\). With \(\theta=0.7\), the nonviable gap is \(1.3334064849<z/\sigma<2.2585179629\). The viable regions on either side are of positive length.

## Relationship to prior work

The metabolic index and its temperature-and-oxygen dependence are established (Deutsch et al., 2015; Fröb et al., 2024), and observed oxygen minimum zones have upper and lower oxyclines (Wishner et al., 2020). Essington et al. (2022) specifically document increased metabolic index at deep depths when oxygen rises and temperature falls. These provide strong physical and ecological antecedents. The result here does **not** claim discovery of metabolic viability, oxygen-minimum layers, two separated habitat bands in nature, or the square-root and three-halves fold exponents. The claim is the exact, finite-column phase boundary, the shallow-shifted bottleneck, and the model-specific fold coefficient for the stated Gaussian-deficit/exponential-compensation model. The inspected sources did not state this parameter-complete classification. Mathematical fold-catastrophe theory already covers the generic local exponents; the derived coefficient and surface threshold are the additional calculations. Wider historical priority remains subject to independent literature review.

## Limitations

A Gaussian oxygen deficit and exponential thermal compensation are simplified surrogates, not calibrated vertical ocean profiles. Ocean temperature is not exactly linear with depth and the Arrhenius factor in absolute temperature is nonlinear. The index ignores food, behavior, movement barriers, hydrostatic pressure, respiration adaptation, changing currents and spatial variation. A threshold-defined viable set measures potential physiological suitability rather than actual occupancy; two bands do not imply biological population fragmentation, disjoint geographic populations, or a dynamical tipping event. For a bottom depth at or above the deficit centre, additional finite-domain conditions are necessary; the theorem assumes \(H>z_c\). No priority or external validation beyond inspected materials is certified.

## References

1. Fröb, F., Bourgeois, T., Goris, N., Schwinger, J., and Heinze, C. (2024), *Simulated Abrupt Shifts in Aerobic Habitats of Marine Species in the Past, Present, and Future*, Earth's Future 12, e2023EF004141. First public version verified 2024-04-04. https://doi.org/10.1029/2023EF004141
2. Wishner, K. F., Seibel, B., and Outram, D. (2020), *Ocean deoxygenation and copepods: coping with oxygen minimum zone variability*, Biogeosciences 17, 2315–2339. https://doi.org/10.5194/bg-17-2315-2020
3. Essington, T. E. et al. (2022), *Advancing statistical models to reveal the effect of dissolved oxygen on the spatial distribution of marine taxa using thresholds and a physiologically based index*, Ecography 2022, e06249. https://doi.org/10.1111/ecog.06249
4. Maloney, C. E., and Lacks, D. J. (2006), *Energy Barrier Scalings in Driven Systems*, Physical Review E 73, 061106; arXiv preprint 2005. https://arxiv.org/abs/cond-mat/0508534
5. Deutsch, C., Ferrel, A., Seibel, B., Pörtner, H.-O., and Huey, R. B. (2015), *Climate change tightens a metabolic constraint on marine habitats*, Science 348, 1132–1135. https://doi.org/10.1126/science.aaa1605
