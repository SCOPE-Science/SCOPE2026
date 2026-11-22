# A discontinuous fluctuation optimum for bounded quadratic thermal performance

## Finding

Normalize a thermal viability interval to \(0<T<1\). Instantaneous response is \(g(T)=T(1-T)\) inside this interval and zero outside. With a uniform daily phase, let
\[
F_m(A)=\frac{1}{2\pi}\int_0^{2\pi}g(m+A\cos\theta)\,d\theta,\qquad 0<m<1,\quad A\geq0.
\]
Here \(m\) is the fixed temperature mean and \(A\) is the nonnegative half-range. Write \(c=\min(m,1-m)\). Define for \(0<t<1\)
\[
s(t)=\sqrt{1-t^2},\quad \alpha(t)=\pi-\arccos t,\quad K(t)=\frac{t s(t)}{\alpha(t)},\quad
P(t)=(1-2t^2)\alpha(t)-t s(t),
\]
\[
R(t)=\frac{1}{\pi}\left[\alpha(t)+\frac{s(t)}{2t}-\frac{s(t)^2}{2\alpha(t)}\right].
\]
There is exactly one \(t_*\in(0,1)\) with \(P(t_*)=0\), and exactly one \(t_0\in(0,t_*)\) with \(R(t_0)=1\). Set
\[
c_{\mathrm{fold}}=\frac{K(t_*)}{1+K(t_*)}=0.1784650236211893\ldots,
\qquad c_{\mathrm{switch}}=\frac{K(t_0)}{1+K(t_0)}=0.1377302734044935\ldots.
\]
For every \(0<m<1\), the following is the complete global classification, over all \(A\geq0\):

* If \(0<c<c_{\mathrm{switch}}\), there is a unique positive global maximizer \(A_+(c)=c/t_-(c)\), where \(t_-(c)\) is the unique solution of \(K(t)=c/(1-c)\) in \((0,t_*)\).
* If \(c=c_{\mathrm{switch}}\), exactly two amplitudes, \(0\) and \(c/t_0\), are global maximizers. The positive optimal amplitude is \(0.4308921815739500\ldots\), so the optimum jumps discontinuously to zero as the mean crosses the switch.
* If \(c>c_{\mathrm{switch}}\), the unique global maximizer is \(A=0\).

The local structure has a second, distinct threshold. For every \(0<c<c_{\mathrm{fold}}\), \(F_m\) has precisely two strictly positive stationary amplitudes: a strict local minimum at \(A_-(c)=c/t_+(c)\), and a strict local maximum at \(A_+(c)\), where \(t_+(c)\in(t_*,1)\) is the second root of \(K(t)=c/(1-c)\). Thus for \(c_{\mathrm{switch}}<c<c_{\mathrm{fold}}\), the positive local maximum persists but is globally inferior to no fluctuation. At \(c=c_{\mathrm{fold}}\) the two stationary amplitudes coalesce into a horizontal inflection with no positive local maximum; for greater \(c\), the response strictly decreases with amplitude. This is a sharp bistability/metastability window for the idealized optimization, not a dynamical hysteresis theorem.

## Assumptions and scope

The thermal response is exactly the continuous hard-truncated parabola, with zero instantaneous growth outside the interval. The daily temperature follows the prescribed complete cosine cycle with fixed mean, variable amplitude and uniform phase. No constraints cap amplitude, and no lag, acclimation, mortality penalty, demographic feedback, or temperature-dependent duration effect is included. The observations describe a dimensionless average rate, not an empirically calibrated fitness function. Any interval \([L,U]\) and scale factor \(h>0\) are obtained by \(T=(\mathrm{temperature}-L)/(U-L)\), \(m=(\mathrm{mean}-L)/(U-L)\), and \(A=\mathrm{half\!\!\!\!-range}/(U-L)\), followed by multiplication by \(h\).

## Proof

The identity \(g(T)=g(1-T)\) and cosine-phase symmetry give \(F_m=F_{1-m}\); it suffices to assume \(0<m\leq1/2\). For \(0\leq A\leq m\), all temperatures remain viable, so
\[
F_m(A)=m(1-m)-\frac{A^2}{2}.
\]
When \(m<A<1-m\), only the lower viability limit is exceeded. With \(t=m/A\), the positive part of the cycle is \(0<\theta<\alpha(t)\), up to reflection. Direct integration yields
\[
F_m(A)=\frac{1}{\pi}\left[\alpha(t)\left(m(1-m)-\frac{A^2}{2}\right)+A\left(1-\frac{3m}{2}\right)s(t)\right],
\]
\[
F_m'(A)=\frac{(1-m)s(t)-A\alpha(t)}{\pi}.
\]
The moving integration boundary contributes nothing because \(g(0)=0\). Consequently, in this interval \(F'_m(A)>0\) if and only if \(K(t)>m/(1-m)\). For \(A>1-m\), the arcsine change of variables gives
\[
F_m(A)=\frac1\pi\int_0^1\frac{x(1-x)}{\sqrt{A^2-(x-m)^2}}\,dx,
\]
whose derivative is strictly negative. This also gives a strictly negative left derivative as \(A\uparrow1-m\) by continuity of the one-sided integral; hence no further maximum can occur beyond this boundary. If \(m=1/2\), the unconstrained quadratic region and the same full-support integral suffice to show strict descent for all positive amplitudes.

Differentiation gives
\[
K'(t)=\frac{P(t)}{s(t)\alpha(t)^2},\qquad P'(t)=-4t\alpha(t)<0.
\]
As \(P(0+)=\pi/2\) and \(P(1-)=-\pi\), \(P\) has exactly one root \(t_*\), and \(K\) grows strictly to its unique maximum \(K(t_*)\), then decreases. If \(m<c_{\mathrm{fold}}\), there are exactly two stationary points: the strict minimum occurs first as \(A\) increases (the root \(t_+>t_*\)), followed by a strict maximum (the root \(t_-<t_*\)). The threshold is interior: \(c_{\mathrm{fold}}<t_*/(1+t_*)\), since \(K(t_*)<t_*\), and the strictly negative derivative at \(A=1-m\) places the small root above \(m/(1-m)\). At equality the two derivative roots merge without changing sign; above equality no positive critical amplitude exists.

At a positive stationary point, write \(t=m/A\). The equation \(K(t)=m/(1-m)\) implies \(m=K(t)/(1+K(t))\). Substitution into the preceding exact integral gives
\[
\frac{F_m(A)}{F_m(0)}=R(t),
\qquad R'(t)=-\frac{P(t)[\alpha(t)+t s(t)]}{2\pi s(t)t^2\alpha(t)^2}.
\]
Therefore \(R\) decreases strictly on \((0,t_*)\) and diverges to infinity as \(t\downarrow0\). Moreover, \(P(1/2)>0\) so \(t_*>1/2\), and
\[
R(1/2)=\frac23+\frac{\sqrt3}{2\pi}-\frac9{16\pi^2}<1.
\]
Thus exactly one \(t_0\in(0,t_*)\) has \(R(t_0)=1\). Since \(K\) grows strictly on \((0,t_*)\), the positive local maximum exceeds, ties, or falls below \(F_m(0)\) precisely when \(m\) is below, at, or above \(c_{\mathrm{switch}}\). Together with strict descent in the other regions, this proves the global classification. Reflecting the mean handles \(m>1/2\). All uniqueness statements include the equality boundaries.

## Verification

Run \(\texttt{python check.py}\) with Python 3 and the arbitrary-precision \(\texttt{mpmath}\) package. The checker evaluates the two uniquely characterized roots by high-precision bisection, verifies the derivative identities, compares exact segment integrals with closed forms, and checks the predicted local-minimum/local-maximum and winner regimes at multiple means. Its reported decimal values are numerical representations, not the proofs of uniqueness. For \(m=0.1\), it gives the positive optimal amplitude \(0.49714781594104\ldots\), average response \(0.11280709248261\ldots\), versus constant-temperature response \(0.09\).

## Relationship to prior work

Rate averaging and the relevance of temperature variance to ectotherm performance are established. Martin and Huey (2008) optimize the mean body-temperature preference under variability and asymmetric curves, not amplitude at a fixed mean for a symmetric clipped quadratic. Paaijmans and colleagues (2013) use empirical and numerically rate-summed thermal curves and a daytime-sinusoid/nighttime-exponential temperature model; they do not state this exact first-order global amplitude switch or the distinct local-fold boundary. Bozinovic and colleagues (2011) report an interaction between mean and variance experimentally; the accessible abstract does not support a whole-document exclusion. Kingsolver, Higgins and Augustine (2015) examine nonlinear and time-dependent growth effects, rather than the exact mathematical benchmark here.

An earlier result for this same instantaneous response treats only means at or **below** the lower viability endpoint. The interior-mean domain here is disjoint: it exhibits a positive-amplitude local minimum, an abrupt optimal-amplitude switch, and an additional fold, none implied by the exterior-mean single-optimum classification. The Jensen concavity deduction for an untruncated quadratic gives \(F_m(A)=m(1-m)-A^2/2\), which likewise does not cover crossing a viability boundary.

## Limitations

The transition constants are exact for the stated stylized response and sinusoidal forcing, not universal physical temperature constants. The switching phase is in the optimization landscape, not real-time abrupt ecological evolution or experimental hysteresis. Outside the thermal range, the model sets growth to zero without imposing physiological damage or memory; adding those effects, asymmetric performance, other waveforms, or an externally capped amplitude may alter or eliminate the transitions. A broad mathematical treatment of arcsine convolutions or parametric truncated response optimization could contain equivalent results; historical priority requires independent specialist scrutiny.

## References

1. Martin, T. L. and Huey, R. B. (2008), *Why “Suboptimal” Is Optimal: Jensen’s Inequality and Ectotherm Thermal Preferences*, The American Naturalist 171(3), DOI: https://doi.org/10.1086/527502, first available online 2008-01-24.
2. Paaijmans, K. P. et al. (2013), *Temperature variation makes ectotherms more sensitive to climate change*, Global Change Biology 19, 2373–2380, DOI: https://doi.org/10.1111/gcb.12240, first online 2013-04-30.
3. Bozinovic, F. et al. (2011), *The Mean and Variance of Environmental Temperature Interact to Determine Physiological Tolerance and Fitness*, Physiological and Biochemical Zoology 84(6), DOI: https://doi.org/10.1086/662551, online 2011-10-13.
4. Kingsolver, J. G., Higgins, J. K., and Augustine, K. E. (2015), *Fluctuating temperatures and ectotherm growth: distinguishing non-linear and time-dependent effects*, Journal of Experimental Biology 218, 2218–2225, DOI: https://doi.org/10.1242/jeb.120733, online 2015-05-18.
