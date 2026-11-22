# A sharp storm-concentration crossover in periodic surface-pollutant wash-off

## Finding

For an idealized, periodically rain-washed urban surface with constant dry-weather pollutant accumulation and nonlinear fractional rain removal, the mean retained pollutant burden has an exact qualitative change as rainfall sensitivity varies. Consider two **prescribed comparison patterns** with the same total rain depth \(W>0\) each period \(T>0\): a single storm of depth \(W\) per period, or two storms of depth \(W/2\) separated by \(T/2\). If a storm of depth \(r\geq0\) instantaneously retains the fraction \(\exp(-\kappa r^p)\) of the pre-storm load, with \(\kappa,p>0\), define the normalized per-half-storm dose \(x=\kappa(W/2)^p\).

The periodic stationary average burdens of the equally split and concentrated patterns are, respectively,
\[
\overline B_{\mathrm{split}}=\frac{aT}{4}\coth\!\left(\frac{x}{2}\right),\qquad
\overline B_{\mathrm{one}}=\frac{aT}{2}\coth\!\left(2^{p-1}x\right),
\]
where \(a>0\) is the dry-weather accumulation rate. For every \(0<p\leq1\), splitting strictly lowers the mean burden for every \(x>0\). For each \(p>1\), there is exactly one \(x_p>0\) satisfying
\[
\coth(x_p/2)=2\coth(2^{p-1}x_p).
\]
Concentrating rainfall strictly lowers the mean burden for \(0<x<x_p\); both patterns tie exactly at \(x=x_p\); splitting strictly lowers it for \(x>x_p\). At the quadratic rain-response exponent \(p=2\), the crossover is explicit:
\[
\boxed{x_2=\operatorname{arcosh}\!\left(\frac{1+\sqrt5}{2}\right)=1.061275061905\ldots.}
\]
No other crossover occurs within these two specified patterns. The comparison is independent of \(a\) and \(T\). This is **not** a theorem that either specified pattern is optimal among all possible intermediate rain splits or arbitrary schedules.

## Assumptions and scope

A surface carries a single nonnegative, well-mixed pollutant mass \(B(t)\). Between instantaneous rain events it obeys \(\dot B(t)=a\), where \(a>0\) is constant; there is no other decay, erosion, inflow pulse, saturation cap, or redeposition during the storms. A rain pulse with event depth \(r\geq0\) updates \(B^+=\exp(-\kappa r^p)B^-\), for fixed \(\kappa>0\) and \(p>0\). A zero-depth event is the identity. A cycle of length \(T>0\) has two equally spaced possible event times, with depths either \((W,0)\) or \((W/2,W/2)\). Each pattern is repeated indefinitely. The mean is the exact time average of the unique attracting \(T\)-periodic trajectory. The parameters satisfy \(W>0\) and \(a>0\); no measured field fit of the power-law wash fraction is assumed.

The primary classification is MSC2020 86A05 (hydrological wash-off modeling). The motivating 2024 study of heterogeneous road-deposited sediment wash-off was publicly available on 2024-03-14; prior work on urban pollutant build-up and exponential wash-off provides an established starting point. The depth-exponent wash fraction is a **hypothetical extension**, not asserted to be the law fitted by those papers.

## Proof

**1. Existence and exact mean.** Let the two half-period rain retention fractions be \(s_1,s_2\in(0,1]\), with \(s_1s_2<1\), and put \(h=T/2\). Let \(b_0\) be the mass immediately following the second pulse and \(b_1\) the mass following the first. Successive dry intervals and impulses give
\[
b_1=s_1(b_0+ah),\qquad b_0=s_2(b_1+ah).
\]
The full return map has slope \(s_1s_2<1\), so it has exactly one globally attracting periodic solution. Direct solution gives
\[
b_0=\frac{ah\,s_2(1+s_1)}{1-s_1s_2},\qquad
b_1=\frac{ah\,s_1(1+s_2)}{1-s_1s_2}.
\]
Both dry intervals integrate to starting mass times \(h\) plus \(ah^2/2\), so the exact stationary time-average is
\[
\overline B(s_1,s_2)
=\frac{b_0+b_1}{2}+\frac{ah}{2}
=\frac{aT}{4}\frac{(1+s_1)(1+s_2)}{1-s_1s_2}.
\]
When the depths are \((W,0)\), this reduces to \((aT/2)\coth(\kappa W^p/2)\). When the depths are \((W/2,W/2)\), it becomes \((aT/4)\coth(x/2)\). Since \(\kappa W^p=2^p x\), the two formulas claimed in the finding follow.

**2. Strict monotonicity of the comparison ratio.** Set \(c=2^{p-1}>1/2\) and
\[
G_p(x)=\frac{\coth(x/2)}{\coth(cx)}.
\]
The sign of \(\overline B_{\mathrm{split}}-\overline B_{\mathrm{one}}\) is exactly the sign of \(G_p(x)-2\). Elementary differentiation gives
\[
\frac{d}{dx}\log G_p(x)=-\frac{1}{\sinh x}+\frac{2c}{\sinh(2cx)}<0.
\]
The final inequality holds for every \(x>0\) because \(z\mapsto\sinh z/z\) is strictly increasing for \(z>0\), and \(2c>1\). Moreover,
\[
\lim_{x\downarrow0}G_p(x)=2^p,\qquad
\lim_{x\to\infty}G_p(x)=1.
\]
Thus if \(0<p\leq1\), then \(G_p(x)<2\) for every positive \(x\). If \(p>1\), continuity and strict monotonicity give exactly one crossing of \(2\), with the stated signs on either side. All strict boundary cases, including \(p=1\), are covered.

**3. Exact quadratic exponent.** Put \(p=2\), so \(c=2\). The tie identity \(\coth(x/2)=2\coth(2x)\) is equivalent, after multiplying the positive quantity \(\sinh x\cosh x\), to
\[
(\cosh x+1)\cosh x=\cosh(2x)=2\cosh^2 x-1.
\]
Consequently, \(\cosh^2x-\cosh x-1=0\), whose unique solution with \(x>0\) is \(\cosh x=(1+\sqrt5)/2\). This proves the claimed exact threshold and completes the proof.

## Verification

The accompanying standalone \(\texttt{checker.py}\) independently evaluates the two-step stationary affine recurrence, the integrated mean, the hyperbolic formulas, the one-crossing inequalities on sampled parameters, and the exact quadratic crossover. It uses the Python standard library and a fixed random seed. Run it with \(\texttt{python3 checker.py}\); the test output is reproducible and reports 38,553 assertions passed. These finite tests supplement but do not replace the complete analytic proof above. Source dates and the primary MSC designation were verified against the linked bibliographic records and MSC2020 descriptions.

## Relationship to prior work

Mao et al. (2024) analyze heterogeneous road-sediment wash-off and employ an exponential wash-off response for runoff pollutant modeling. Vinck et al. (2023) explicitly model constant dry-weather buildup and exponential wash-off depending on rain intensity and stored surface pollutant load. Neither is here interpreted as furnishing the two-policy nonlinear power-exponent comparison or its sharp universal bifurcation. The published mathematical result *Two sharp patch-allocation transitions for a generalized Type III feeding response* concerns a different saturating response family and prey allocation, not the stationary wash-off recurrence or the hyperbolic crossover. Published stormwater sequencing work concerns order effects or runoff hydrographs with fixed stage rates, not the equal-versus-concentrated **rain-depth allocation** comparison here.

The natural hydrological reason for this comparison is that high-intensity runoff can increase effective removal during a storm, while separated events reduce the dry period available for accumulation. A superlinear effective storm-dose response creates a competition between those two effects. The theorem isolates an exact, testable phase diagram for the two canonical regimes; it does **not** establish the physical response exponent at any site, nor the globally optimal split among all rain schedules. An exact field law must be measured before the theoretical transition is used operationally.

## Limitations

All rain is idealized as instantaneous; rainfall event duration and intensity trajectories are discarded, and the power-law dose exponent is not calibrated. Dry-weather accumulation is linear and unbounded and lacks sediment-size dependence, other degradation pathways, transport delays, or hysteresis. The cycle-average retained surface mass is **not** the total runoff export: in this no-other-loss periodic model, mass conservation makes the total pollutant washed away per period exactly \(aT\) in either pattern. The result does not compare peak runoff concentration, site-specific risk, or arbitrary intermediate storm splits. Noise, parameter uncertainty, nonstationary weather and field validation remain outside scope. Historical priority is provisional because some highly related full texts were inaccessible.

## References

1. J. Mao, J. Li, L. Li and H. Zhao, “Characterization of road-deposited sediment wash-off and accurate splitting of initial runoff pollution in heterogeneous urban spaces,” *Environmental Pollution* 347 (2024), 123766. First online 2024-03-14. https://doi.org/10.1016/j.envpol.2024.123766
2. E. Vinck, B. De Bock, T. Wambecq, E. Liekens and R. Delgado, “A New Decision Support Tool for Evaluating the Impact of Stormwater Management Systems on Urban Runoff Pollution,” *Water* 15 (2023), 931. https://doi.org/10.3390/w15050931
3. M. He et al., “Particle Size Effect in Urban Road-Deposited Sediment Wash-Off Process: Physical Experiments and Cellular Automata-Based Modeling,” *ACS ES&T Water* 4 (2024), 2906–2917. First online 2024-06-11. https://doi.org/10.1021/acsestwater.4c00105
