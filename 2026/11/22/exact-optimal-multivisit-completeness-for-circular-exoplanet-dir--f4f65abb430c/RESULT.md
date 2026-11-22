# Exact optimal multivisit completeness for circular exoplanet direct imaging

## Finding

For an ideal, known-period circular planetary orbit with isotropic orbital-plane orientation, uniform unknown initial orbital phase, and perfect detection whenever projected separation exceeds the inner working angle, **equally spaced observing phases maximize the probability of at least one detection for every integer \(n\ge3\)**. There is an exact classification of *every* maximizing schedule, a sharp number of visits sufficient for geometrically complete detection, and a closed-form detection probability.

Write \(\tau\in(0,1)\) for inner working angle divided by orbital radius, \(c=\sqrt{1-\tau^2}\), \(a_n=\sin(\pi/(2n))\), and \(u_n=\cos(\pi/(2n))\). The maximum over all \(n\)-visit calendars is

\[
\mathcal C_n(\tau)=\begin{cases}
1,&c\ge a_n,\\
1-\dfrac{2n}{\pi}\left[\arctan\!\left(\dfrac{\sqrt{a_n^2-c^2}}{u_n}\right)-c\arctan\!\left(\dfrac{\sqrt{a_n^2-c^2}}{cu_n}\right)\right],&0<c<a_n.
\end{cases}
\]

Observing phases are equivalent modulo \(\pi\), corresponding to time separations modulo half an orbital period. Let \(g_1,\ldots,g_n\ge0\) denote their cyclic gaps, with \(\sum_jg_j=\pi\). For \(c\le a_n\), the unique optimal gap vector is \(g_j=\pi/n\) for all \(j\), up to overall phase rotation and visit permutation. For \(c>a_n\), the entire family of optimizers is described by \(\max_jg_j\le2\arcsin(c)\); each produces certain geometric detection.

Consequently, complete detection is achievable precisely when \(\tau\le\cos(\pi/(2n))\), with the minimum visit count \(\lceil\pi/(2\arcsin c)\rceil\) (interpreting the two-visit case as known prior work). As \(\tau\downarrow u_n\) from above, the optimal missed-detection probability obeys

\[
1-\mathcal C_n(\tau)\sim\frac{4n\sqrt{2u_n}}{3\pi a_n^2}(\tau-u_n)^{3/2}.
\]

## Assumptions and scope

A single planet follows a circular orbit of known radius \(R>0\) and period \(P>0\). The observer's line of sight is isotropically distributed relative to the orbital plane, independent of a uniform orbital phase. The observer may select any \(n\ge3\) observing epochs, their phases taken modulo \(P/2\). An observation detects the planet if and only if the instantaneous projected planet-star separation is *strictly* greater than \(\tau R\). There is no flux limit, noise, exposure-time constraint, weather, orbital eccentricity, ephemeris uncertainty, or false alarm. The theorem optimizes the probability of at least **one** detection, not repeated confirmation or orbit estimation.

## Proof

Rotate coordinates so the orbit is an equator, with orbital-position directions at angles \(\theta_j\) modulo \(\pi\). Let \(z\) be the absolute cosine of inclination. Isotropy makes \(z\) uniform on \([0,1]\); put \(s=\sqrt{1-z^2}\). At a phase \(\phi\) uniformly distributed modulo \(\pi\), the projected separation divided by \(R\) is \(\sqrt{1-s^2\cos^2(\phi+\theta_j)}\). Detection is equivalent to \(s|\cos(\phi+\theta_j)|<c\). Thus each observing epoch covers a phase arc of length

\[
\ell(s)=2\arcsin(\min\{1,c/s\})\quad (s>0),\qquad \ell(0)=\pi,
\]

on a circle of circumference \(\pi\). For cyclic observing gaps \(g_j\), the uncovered phase proportion is exactly

\[
U(s;g)=\frac1\pi\sum_{j=1}^n (g_j-\ell(s))_+,\qquad (t)_+=\max(t,0).
\]

Since positive-part is convex, Jensen's inequality yields \(U(s;g)\ge\max(0,1-n\ell(s)/\pi)\) for every inclination. Equality holds simultaneously for all inclinations when \(g_j=\pi/n\), proving global optimality without assuming a restricted class of calendars.

For optimizer classification, note that \(\ell(s)\) increases continuously as \(s\) decreases. If \(c<a_n\), its range crosses \(\pi/n\) at \(s=c/a_n\). For inclinations on one side of that crossing the optimal arcs must cover the entire phase circle, requiring \(\max g_j\le\ell(s)\); arbitrarily near the crossing this forces \(\max g_j\le\pi/n\), hence every gap equals \(\pi/n\). The same conclusion follows at \(c=a_n\) by taking \(s\uparrow1\). In both cases any nonequal gaps cause strict loss over an interval of inclinations of positive probability. When \(c>a_n\), \(\ell(s)\ge2\arcsin c>\pi/n\) for every inclination. Thus all inclinations are completely covered precisely when \(\max g_j\le2\arcsin c\). If a gap exceeds this bound, positive-probability inclinations near \(s=1\) leave uncovered phases, so the condition is necessary as well as sufficient.

If \(c\ge a_n\), pointwise arc coverage is complete, so the displayed maximum equals one. Otherwise put \(z_0=\sqrt{1-c^2/a_n^2}\) and \(r=\sqrt{a_n^2-c^2}\). The optimized missed-detection probability is

\[
1-\mathcal C_n=\int_0^{z_0}\left[1-\frac{2n}{\pi}\arcsin\left(\frac{c}{\sqrt{1-z^2}}\right)\right]dz.
\]

Integration by parts, using \(\arcsin(c/\sqrt{1-z_0^2})=\pi/(2n)\), gives

\[
1-\mathcal C_n=\frac{2nc}{\pi}\int_0^{z_0}\frac{z^2\,dz}{(1-z^2)\sqrt{1-c^2-z^2}}.
\]

With \(z=\sqrt{1-c^2}\sin t\), the integral reduces to \(\int[(1-(1-c^2)\sin^2t)^{-1}-1]dt\). Evaluating its elementary antiderivative yields the stated arctangent expression. Completeness is one exactly when \(n\cdot2\arcsin c\ge\pi\), giving the threshold and minimum visit number. Finally, as \(\delta=\tau-u_n\downarrow0\), \(z_0\sim\sqrt{2u_n\delta}/a_n\). Expanding the last positive integral at \(z=0\) gives the displayed \(3/2\)-power coefficient. These arguments cover all \(n\ge3\), \(\tau\in(0,1)\), including the exact boundary.

## Verification

The included `checker.py` independently integrates phase coverage over inclination, compares it with the closed form for multiple visit counts and angles, tests random nonequispaced calendars against the optimum, probes uniqueness and plateau families, and checks the critical asymptotic coefficient. Its completed execution reported 577 passing assertions. These finite diagnostics check numerical consequences only; the all-parameter theorem rests on the proof above. As a benchmark, \(\tau=0.8\) and \(c=0.6\) allow geometric completeness with three evenly phased visits (but not two): the known two-visit formula gives probability approximately \(0.932449\).

## Relationship to prior work

Brown and Soummer (2010) analyze revisits and dynamic completeness for realistic exoplanet direct-detection programs. Stark and coauthors (2015), notably their optimized-revisits section, use numerical orbital populations and operational visit optimization. These studies motivate a noiseless exact benchmark but do not, in the material examined, give the full all-calendar \(n\ge3\) optimizer and equality classification above. An earlier indexed two-visit theorem already gives the quarter-orbit optimum and its closure exponent; **the two-visit case is not claimed as new**. An indexed theorem for coverage depths of regular equatorial spherical-cap arrangements is a close geometric dual that may already imply portions of the regular-calendar probability formula and critical exponent; those formula portions are not represented as individually novel. The claimed distinguishing content is optimization over arbitrary \(n\ge3\) calendars, complete equality conditions, and the resulting sharp observational coverage criterion. The extent to which general circle-coverage theory subsumes this specialized optimization remains a historical-priority risk.

## Limitations

This is a geometric visibility idealization, not a calibrated observing strategy for a telescope. Optimality is not asserted for eccentric or uncertain orbits, additional brightness and phase-angle constraints, nonzero false-positive/false-negative rates, variable exposure costs, multi-target allocation, or the requirement for multiple distinct detections. The elementary convex-coverage reduction means that general covering results could subsume some or all of the novelty, notwithstanding the specific prior comparisons recorded. Independent validation and exhaustive historical-priority certification have not occurred.

## References

1. R. A. Brown and R. Soummer, *New Completeness Methods for Estimating Exoplanet Discoveries by Direct Detection* (first posted 2010-03-24), arXiv:1003.4700, https://arxiv.org/abs/1003.4700 .
2. C. C. Stark et al., *Lower Limits on Aperture Size for an ExoEarth-Detecting Coronagraphic Mission* (first posted 2015-06-04), arXiv:1506.01723, https://arxiv.org/abs/1506.01723 .
3. *Exact two-visit direct-imaging completeness and its sharp quarter-orbit transition*, mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-two-visit-direct-imaging-completeness-and-its-sharp-quarte--26baa61dfac4 .
4. *Exact all-depth spherical-cap laws for regular equatorial point sets*, mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-all-depth-spherical-cap-laws-for-regular-equatorial-point--1f86ecf5421c .
