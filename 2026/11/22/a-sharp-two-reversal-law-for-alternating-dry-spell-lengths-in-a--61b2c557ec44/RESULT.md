# A sharp two-reversal law for alternating dry-spell lengths in a lagged soil-carbon pulse model

## Finding

Consider identical, independent rewetting cycles whose pulse yield after a dry spell of length \(t\geq 0\) is
\[
P_2(t)=C e^{-bt}\bigl[1-(1+at)e^{-at}\bigr],\qquad a,b,C>0.
\]
Compare a regular sequence of dry spells of length \(m\) with a repeated alternating sequence of lengths \(m-d,m+d\), where \(d>0\) and \(m>d\). Both schedules have exactly two rewetting events per time \(2m\). Their mean rewetting-pulse release rates are, respectively,
\[
R_{\mathrm{regular}}(m)=\frac{P_2(m)}{m},\qquad
R_{\mathrm{alternate}}(m,d)=\frac{P_2(m-d)+P_2(m+d)}{2m}.
\]
There is a unique critical alternating half-gap \(d_c=d_c(a,b)>0\), determined by
\[
e^{-bd_c}\frac{1-(1+2ad_c)e^{-2ad_c}}{1-(1+ad_c)e^{-ad_c}}=2,
\]
with the following **complete classification** for each fixed \(a,b>0\).

* If \(0<d<d_c\), exactly two distinct values \(d<m_-(d)<m_+(d)\) yield equal rates. Alternation increases release for \(d<m<m_-\) and \(m>m_+\), but decreases it for \(m_-<m<m_+\).
* If \(d\geq d_c\), exactly one value \(m_+(d)>d\) yields equal rates. Alternation decreases release for \(d<m<m_+\) and increases it for \(m>m_+\). At \(d=d_c\), the excluded zero-length-spell endpoint \(m=d\) is also an equality.

All comparisons are strict away from the stated equality values. The two-reversal phenomenon requires at least **two successive maturation stages**: replacing the two-stage maturation factor by a one-stage factor gives exactly one crossover for every \(d>0\).

For \(a=b=1\), \(d_c=0.425304912003236\ldots\). Taking \(d=0.2\), the two rate-equality mean intervals are \(m_-=0.37255179702065\ldots\) and \(m_+=2.1603940203633\ldots\); at means \(0.25,1,3\), alternation changes predicted pulse release rates by approximately \(+19.33\%,-3.54\%,+1.00\%\), respectively.

## Assumptions and scope

At the beginning of each dry spell, a normalized precursor cohort is initialized independently of other cycles. Each precursor requires two successive independent exponential maturation steps, each at rate \(a\), to become rewetting-releasable. An independent exponential deactivation clock of rate \(b\) begins at the same dry-spell onset, and must not have fired by rewetting. Rewetting immediately releases a fixed amount \(C\) per viable and fully matured precursor. Thus the release probability is the product of an Erlang-two cumulative maturation probability and independent precursor survival, giving \(P_2(t)/C\). Release and reinitialization are instantaneous. In the one-stage comparison, maturation uses a single exponential waiting time at rate \(a\).

The theorem concerns the **rewetting-pulse component** of carbon release only. Dry-period baseline respiration, variations in rain volume, soil water balance, nutrient feedback, microbial adaptation across cycles, overlapping cohorts, saturation of substrate supply, and long-run carbon mass-balance constraints are outside the model. The parameter \(C\) affects the magnitude but not the comparison signs. The mathematical results hold for all positive \(a,b,C,d\) and all admissible \(m>d\), without approximations to the rate functions.

## Proof

Write \(G(x)=1-(1+x)e^{-x}\) and \(F(t)=e^{-bt}G(at)\); it suffices to work with \(C=1\). Set \(c=a+b\),
\[
B_d=\cosh(bd)-1,\quad J_d=\cosh(cd)-1,\quad S_d=\sinh(cd).
\]
For \(m>d\), direct expansion of the two event rewards shows
\[
\frac{F(m-d)+F(m+d)-2F(m)}{2e^{-bm}}
=B_d-H_d(m),\qquad
H_d(m)=e^{-am}\bigl[(1+am)J_d-ad S_d\bigr].\tag{1}
\]
The denominator and the cycle length \(2m\) are positive, so the sign of the difference in release rates is exactly the sign of \(B_d-H_d(m)\).

**One strict maximum, exceeding the comparison level.** Differentiate the explicit expression:
\[
H_d'(m)=a^2e^{-am}(d S_d-m J_d).
\]
Thus \(H_d\) is strictly increasing up to
\[
m_*(d)=d\frac{S_d}{J_d}=d\coth\frac{cd}{2}>d,
\]
and strictly decreasing thereafter, with \(H_d(m_*)=J_d e^{-a m_*}\) and \(H_d(m)\to0\) as \(m\to\infty\). To show that this maximum is strictly above \(B_d\), put \(z=cd/2>0\) and \(r=b/c\in(0,1)\). Since \(\coth\) is strictly decreasing on positive arguments,
\[
\begin{aligned}
\frac12\log\frac{J_d}{B_d}
&=\log\frac{\sinh z}{\sinh(rz)}
=\int_{rz}^{z}\coth v\,\mathrm dv\\
&>(1-r)z\coth z=\frac{a m_*}{2}.
\end{aligned}
\]
Consequently \(J_d e^{-a m_*}>B_d>0\). Thus the equation \(H_d(m)=B_d\) always has exactly one solution above \(m_*\), and it has another within \((d,m_*)\) exactly when \(H_d(d)<B_d\). If \(H_d(d)=B_d\), the lower equality is only at the excluded boundary \(m=d\).

**Exactly one transition in the alternating half-gap.** By (1), the sign of \(B_d-H_d(d)\) is the sign of
\[
F(2d)-2F(d)=F(d)\left[\frac{F(2d)}{F(d)}-2\right].\tag{2}
\]
Because \(G(x)>0\) for \(x>0\), define \(E(x)=xG'(x)/G(x)=x^2/(e^x-1-x)\). It is strictly decreasing on \((0,\infty)\): its logarithmic derivative is negative precisely when \((2-x)e^x<2+x\), which follows by defining \(h(x)=(x-2)e^x+x+2\). Indeed \(h(0)=h'(0)=0\) and \(h''(x)=xe^x>0\) for \(x>0\).

It follows that \(G(2x)/G(x)\) strictly decreases with \(x>0\), since its logarithmic derivative with respect to \(\log x\) is \(E(2x)-E(x)<0\). Therefore
\[
\frac{F(2d)}{F(d)}=e^{-bd}\frac{G(2ad)}{G(ad)}
\]
is strictly decreasing for \(d>0\). Its limiting values are \(4\) as \(d\downarrow0\) (because \(G(x)\sim x^2/2\)) and \(0\) as \(d\to\infty\) (because \(b>0\)). Hence equation (2) changes sign exactly once, at the uniquely defined \(d_c>0\). For \(d<d_c\), \(F(2d)-2F(d)>0\), so \(H_d(d)<B_d\) and there are two interior crossings. For \(d\geq d_c\), the lower crossing lies at or below the admissible boundary, and there is only the upper interior crossing. Together with the unique strict maximum of \(H_d\) and its positive-limit gap, this gives every strict sign regime in the finding.

**Sharpness in the number of maturation stages.** For a one-step maturation clock the event reward is \(F_1(t)=e^{-bt}(1-e^{-at})\). The same expansion becomes
\[
\frac{F_1(m-d)+F_1(m+d)-2F_1(m)}{2e^{-bm}}
=B_d-e^{-am}J_d.
\]
The right side is strictly increasing in \(m\), approaches \(B_d>0\), and at \(m=d\) is strictly negative, because
\[
\frac{F_1(2d)}{F_1(d)}=e^{-bd}(1+e^{-ad})<2.
\]
It therefore has exactly one root \(m_1(d)=a^{-1}\log(J_d/B_d)>d\), with negative comparison before and positive comparison after. The two-root case is impossible with one stage but is attained with two stages whenever \(0<d<d_c\).

## Verification

The accompanying `checker.py` is a self-contained Python standard-library diagnostic. It independently evaluates direct event-rate differences and their hyperbolic forms over positive rationally expressed floating-point parameter grids, brackets the unique half-gap threshold and all admissible rate crossings, checks the two-stage sign patterns, and tests the sharp one-stage boundary. It reports 2,504 passed deterministic numerical assertions, \(d_c(1,1)=0.425304912003236\), and the three displayed example rate comparisons. Run it with `python3 checker.py` in the same folder as this document. These finite diagnostics do not establish the universal conclusions; the analytic inequalities above do.

## Relationship to prior work

Fierer and Schimel (2002) experimentally demonstrate that the frequency of soil drying and rewetting changes respiration and soil microbial response history; their full paper treats regular experimental cycling and does not assert a two-stage Erlang-survival pulse law or this alternating-gap classification. Zhang et al. (2014) introduce and compare mechanistic carbon/enzyme-pool models in which degraded carbon accumulates in dry soil and is accessible after rain; their accessible full article contains detailed simulated and field-calibrated dynamics rather than a theorem for the present explicit minimal-response law. Borken and Matzner (2009) review the biological importance of precipitation timing and wetting pulses. Manzoni et al. (2020) derive random-rainfall-driven pulse statistics using a soil-moisture-dependent pulse equation, different from the present precursor-survival and deterministic alternating-interval reward law. General renewal-reward division by mean cycle length and the usual local curvature heuristic are already standard; neither alone gives the global two-crossing count, the sharp half-gap threshold, or the one-stage obstruction proved here.

The result is an exact benchmark **conditional on its stated minimal model**, not a derivation of that model from the cited field experiments. Published stormwater sequencing and leaching optimizations use different state variables and event responses and have not been found to imply this statement; a global priority claim beyond inspected sources is not made.

## Limitations

The fresh-precursor, independence and exponential-clock assumptions are restrictive, particularly because soil carbon may carry across many cycles. An Erlang-two maturation probability times precursor survival is a deliberately transparent mechanistic hypothesis, not a fitted kinetic law. The result does not determine signs of total soil respiration, which includes dry-period flux and additional carbon pools, and it makes no field calibration or climate prediction. Alternative substrate-development kinetics can have different curvature patterns, and the crossover count need not survive arbitrary changes of this response function. Publication priority is conditional on accessible literature and semantic search rather than an exhaustive theorem census.

## References

1. Fierer, N., and Schimel, J. P. (2002). *Effects of drying–rewetting frequency on soil carbon and nitrogen transformations*. Soil Biology & Biochemistry 34, 777–787. https://doi.org/10.1016/S0038-0717(02)00007-X. Full text: https://static1.squarespace.com/static/6335d20acf80c5162c7e37fe/t/6362cf37dd45810293f5b7f9/1667419959577/FiererandSchimel2002dryingrewetting.pdf.
2. Borken, W., and Matzner, E. (2009). *Reappraisal of drying and wetting effects on C and N mineralization and fluxes in soils*. Global Change Biology 15, 808–824. https://doi.org/10.1111/j.1365-2486.2008.01681.x.
3. Zhang, X., Niu, G.-Y., Elshall, A. S., Ye, M., Barron-Gafford, G. A., and Pavao-Zuckerman, M. (2014). *Assessing five evolving microbial enzyme models against field measurements from a semiarid savannah—What are the mechanisms of soil respiration pulses?* Geophysical Research Letters 41, 6428–6434. First published 2014-09-11. https://doi.org/10.1002/2014GL061399. Full text: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014GL061399.
4. Manzoni, S., Chakrawal, A., Fischer, T., Schimel, J. P., Porporato, A., and Vico, G. (2020). *Rainfall intensification increases the contribution of rewetting pulses to soil heterotrophic respiration*. Biogeosciences 17, 4007–4023. https://doi.org/10.5194/bg-17-4007-2020. Full text: https://bg.copernicus.org/articles/17/4007/2020/.
