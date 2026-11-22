# A sharp warmest-temperature window for amplitude-optimal cold-mean diurnal development

## Finding

Consider a prescribed sinusoidal temperature with fixed daily mean at or below the lower viable temperature for development, and an instantaneous nonnegative parabolic response supported on a finite thermal window. There is exactly one globally rate-maximizing diurnal temperature amplitude. At its optimum, the day's **highest temperature** lies strictly between \(2/\pi\) and \(3/4\) of the way through the viable thermal window (with the first inequality attaining equality when the mean is exactly the lower boundary). The constants are universal and sharp.

Specifically, write \(W=U-L>0\), \(\delta=L-\mu\ge0\), and
\[
 r(T)=\begin{cases}c(T-L)(U-T),&L<T<U,\\0,&\text{otherwise},\end{cases}\quad
 T_A(\theta)=\mu+A\cos\theta,\quad
 J(A)=\frac1{2\pi}\int_0^{2\pi}r(T_A(\theta))\,d\theta,
\]
where \(c>0\), \(A\ge0\), and \(0\le\theta<2\pi\). There is a unique global maximizer \(A_*\). If \(\delta>0\), then \(A_*\in(\delta,\delta+W)\) and
\[
 \frac2\pi<\frac{\mu+A_*-L}{U-L}<\frac34.
\]
If \(\delta=0\), the unique maximizer is \(A_*=2W/\pi\), attaining the left equality. As \(\delta/W\to\infty\), the fraction tends to \(3/4\), so neither bound can be improved uniformly. For \(\delta>0\) the maximizing amplitude has the equivalent exact characterization
\[
 A_*=\frac{\delta}{\cos t_*},\qquad
 \frac{t_*}{\sin t_*\cos t_*}=1+\frac W\delta,\qquad
 0<t_*<\frac\pi2.
\]

## Assumptions and scope

The temperature is prescribed, deterministic, sinusoidal, and acts instantaneously: no acclimation, developmental memory, lethal accumulation, or population feedback occurs. Its mean \(\mu\) is held fixed and is **not above** the response's lower viable boundary \(L\). Temperature amplitude \(A\) is the difference between maximum temperature and the mean, **not** the peak-to-trough swing. The rate is exactly zero at and outside both viability boundaries and strictly parabolic inside, with \(L<U\), \(c>0\). These conditions are mathematical model assumptions, not inferred physiology. The result optimizes the daily mean instantaneous development-rate proxy, not individual survival, time to completion with state dependence, or population fitness.

## Proof

Translate the lower viable boundary to zero: temperature relative to \(L\) is \(A\cos\theta-\delta\); the viable interval is \((0,W)\). For \(0\le A\le\delta\), this is never positive, so \(J(A)=0\). For \(\delta<A<\delta+W\), the cold truncation applies, but the hot cutoff has not been reached. Put \(x=\delta/A\in[0,1)\) and \(t=\arccos x\). Symmetry gives
\[
 J(A)=\frac c\pi\int_0^t(A\cos s-\delta)(W+\delta-A\cos s)\,ds.
\]
The integrand vanishes at the moving endpoint; differentiation under the integral gives
\[
 J'(A)=\frac c\pi\left[(W+\delta)\sqrt{1-\frac{\delta^2}{A^2}}-A\arccos\!\left(\frac\delta A\right)\right].\tag{1}
\]
If \(\delta>0\), substituting \(A=\delta/\cos t\) shows the sign of \(J'(A)\) equals that of
\[
 1+\frac W\delta-\frac{t}{\sin t\cos t}.
\]
The last ratio is strictly increasing on \((0,\pi/2)\): its derivative has the sign of \(\sin(2t)-2t\cos(2t)\), whose derivative is \(4t\sin(2t)>0\) and whose limit at zero is zero. This ratio grows continuously from \(1\) to infinity. Thus exactly one candidate \(A_*\) occurs above \(\delta\). It occurs **below** \(\delta+W\): at \(A=\delta+W\), equation (1) reads \((c/\pi)A(\sin t-t)<0\), whereas it is positive immediately after \(\delta\). Consequently \(J\) strictly rises to \(A_*\) and then decreases up to the first hot cutoff.

For every \(A\ge\delta+W\), the entire viable window is swept by the positive half of the sinusoid, so the change of variables \(u=A\cos s-\delta\) gives
\[
 J(A)=\frac c\pi\int_0^W\frac{u(W-u)}{\sqrt{A^2-(u+\delta)^2}}\,du.\tag{2}
\]
For each \(u\in(0,W)\), the integrand strictly decreases as \(A\) increases; hence \(J\) strictly decreases throughout this final regime, including right after the cutoff. Formula (2) also shows \(J(A)\to0\) at infinite amplitude. This proves the unique *global* maximum. It does not assert unique non-strict local maxima within the initial zero plateau.

If \(\delta=0\), in the first positive interval \(0<A<W\), equation (1) reduces to \(J'(A)=(c/\pi)(W-\pi A/2)\); hence \(A_*=2W/\pi<W\). The same strict decrease from (2) handles all larger amplitudes.

For the sharp bound when \(\delta>0\), stationarity implies \(W/\delta=[t-\sin t\cos t]/(\sin t\cos t)\). Consequently the fraction of the viable interval reached by the warmest daily temperature is
\[
 \frac{A_*-\delta}{W}=F(t),\qquad
 F(t)=\frac{\sin t(1-\cos t)}{t-\sin t\cos t}.
\]
An exact derivative factorization is
\[
 F'(t)=\frac{(1-\cos t)H(t)}{(t-\sin t\cos t)^2},\qquad
 H(t)=(1+2\cos t)t-(2+\cos t)\sin t.
\]
Since \(H(0)=0\) and \(H'(t)=2\sin t(\sin t-t)<0\) on \((0,\pi/2)\), \(F\) decreases strictly. Direct endpoint limits yield \(\lim_{t\downarrow0}F(t)=3/4\) and \(\lim_{t\uparrow\pi/2}F(t)=2/\pi\). For \(\delta/W\to\infty\), the stationarity equation forces \(t\downarrow0\), proving sharpness of the upper bound; as \(\delta/W\downarrow0\), \(t\uparrow\pi/2\), proving sharpness of the lower bound. This completes the proof.

## Verification

The standalone Python 3 script `check.py` requires only the standard library. Execute `python3 check.py` alongside this document. It checks numerical integration independently of the closed derivative and integral formulas; checks stationary amplitudes, interior/global inequalities, boundary cases, representative parameter grids, asymptotic fractions, and selected numerical values. It prints `PASS: 1835 numerical and independent-integral assertions` on the supplied script. These finite tests supplement, rather than certify, the analytical statements for all positive real parameters.

As a concrete dimensioned example, with \((L,U,\mu,c)=(10,20,0,1)\), the maximizing diurnal amplitude is \(17.13754563079678\); the warmest temperature is \(17.13754563079678\), only about \(71.3755\%\) into the viable \([10,20]\) interval. No hotter-than-upper-boundary hours are necessary at the optimum.

## Relationship to prior work

Baskerville and Emin (1969) introduced sine-based temperature aggregation and lower/upper degree-day truncation, rather than an exact quadratic instantaneous rate optimized over amplitude. Tian and Dong (2006) experimentally fitted a quadratic *growth versus amplitude* regression in shrimp at tested warm mean temperatures; this is neither the quadratic *instantaneous response versus temperature* considered here nor an all-offset sharp bound. Martin and Huey (2008) optimize the mean preferred temperature under a prescribed fluctuating thermal distribution; their optimizer is not an amplitude at a fixed subthreshold mean. Folguera et al. (2009) test a few thermal amplitudes experimentally, not an exact across-amplitude extremal characterization. Estay et al. (2014) give a broad nonlinear and Jensen-based theory for performance responses to temperature variance, but do not establish the strict unique amplitude maximum and universal warmest-day interval in this idealized model. These works motivate and constrain interpretation; none is treated as proof of this particular theorem or as evidence that the phenomenon of nonmonotonic variability response is newly discovered.

## Limitations

A symmetric parabolic instantaneous response is an idealization. Real ectotherm rate curves can be skewed, history-dependent, and negative for net fitness outside favorable conditions; body temperature may also lag air temperature. The constant bounds and unique optimum are not asserted for non-sinusoidal cycles, means above the lower threshold, alternative thermal curves, finite observational sampling, biological acclimation, or population-level outcomes. Neither the absolute amplitude nor upper viable boundary is empirically estimated here. No claim of first discovery is made: priority comparisons of additional historical physiological and applied mathematical literature, including inaccessible sources, remain independently revisable.

## References

- Baskerville, G. L., and P. Emin (1969), *Rapid Estimation of Heat Accumulation from Maximum and Minimum Temperatures*, Ecology **50**, 514–517, https://doi.org/10.2307/1933912 (first public online date verified as 1969-05-01).
- Tian, X., and S. Dong (2006), *The effects of thermal amplitude on the growth of Chinese shrimp*, Aquaculture **251**, 516–524, https://doi.org/10.1016/j.aquaculture.2005.05.031.
- Martin, T. L., and R. B. Huey (2008), *Why “Suboptimal” Is Optimal: Jensen’s Inequality and Ectotherm Thermal Preferences*, The American Naturalist **171**, E102–E118, https://doi.org/10.1086/527502.
- Folguera, G., D. A. Bastías, and F. Bozinovic (2009), *Impact of experimental thermal amplitude on ectotherm performance*, Comp. Biochem. Physiol. A **154**, 389–393, https://doi.org/10.1016/j.cbpa.2009.07.008.
- Estay, S. A., M. Lima, and F. Bozinovic (2014), *The role of temperature variability on insect performance and population dynamics in a warming world*, Oikos **123**, 131–140, https://doi.org/10.1111/j.1600-0706.2013.00607.x. Full-text open version: https://capes.cl/wp-content/uploads/2014/09/Estay-et-al-2014-Oikos-Thermal-Variability_2014.pdf.
- Allen, J. C. (1976), *A Modified Sine Wave Method for Calculating Degree Days*, Environmental Entomology **5**, 388–396, https://doi.org/10.1093/ee/5.3.388 (full text not inspected).
