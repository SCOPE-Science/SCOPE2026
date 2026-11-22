# A sharp amplitude ceiling for beneficial fluctuations under Brière-I development

## Finding

For the Brière-I arthropod development-rate curve, symmetric temperature fluctuations can improve the time-averaged instantaneous development rate only below a **sharp finite amplitude**, and only for a lower interval of mean temperatures. Both the amplitude cutoff and the mean-temperature crossover are determined exactly, without small-variance approximations.

Let \(0<a<1\), \(f_a(x)=x(x-a)\sqrt{1-x}\), and
\[
\Delta_a(m,d)=\frac{f_a(m-d)+f_a(m+d)}2-f_a(m),
\qquad 0<d<\frac{1-a}{2},\quad a+d\le m\le1-d.
\]
All statements below hold for every admissible real choice of the parameters, including the two allowed endpoints of the mean interval.

**Theorem (complete sign classification).**

1. If \(2/3\le a<1\), then \(\Delta_a(m,d)<0\) for every admissible \(m,d\).
2. If \(0<a<2/3\), put
\[
 d_*(a)=\frac{3-9a+\sqrt{9+2a-3a^2}}{14}.
\]
Then \(0<d_*(a)<(1-a)/2\). For every \(0<d<d_*(a)\), there is exactly one \(m_*(a,d)\in(a+d,1-d)\) such that \(\Delta_a(m,d)>0\) for \(a+d\le m<m_*(a,d)\), \(\Delta_a(m_*(a,d),d)=0\), and \(\Delta_a(m,d)<0\) for \(m_*(a,d)<m\le1-d\). At \(d=d_*(a)\), equality occurs only at \(m=a+d\); every larger admissible mean has a negative gap. At \(d>d_*(a)\), the gap is strictly negative throughout the admissible mean interval.
3. The cutoff \(d_*(a)\) decreases strictly as \(a\) increases, and
\[
\lim_{a\downarrow0}d_*(a)=\frac37,
\qquad\lim_{a\uparrow2/3}d_*(a)=0.
\]

The cutoff therefore describes when **any** benefit from equal warm/cool excursions disappears throughout the complete feasible range of baseline temperatures.

## Assumptions and scope

The original rate is \(R(T)=\kappa T(T-T_{\min})\sqrt{T_{\max}-T}\) for \(T\in[T_{\min},T_{\max}]\), with \(\kappa>0\) and \(0<T_{\min}<T_{\max}\). Temperature is measured on the numerical scale on which this empirical rate curve is defined; an arbitrary shift of the temperature origin changes the model and its parameters. The normalized variables are \(a=T_{\min}/T_{\max}\), \(x=T/T_{\max}\), and \(R(T)=\kappa T_{\max}^{5/2}f_a(x)\). The two temperatures \(T_{\max}(m-d)\) and \(T_{\max}(m+d)\) each occupy exactly half the observation time and remain inside the response's viable interval. There is no thermal adaptation, acclimation, lag, mortality, seasonality, or history dependence: development is accumulated by integrating the instantaneous rate. In physical temperature units, the largest half-amplitude admitting a positive gap is \(T_{\max}d_*(a)\) whenever \(a<2/3\).

## Proof

**1. Strict decrease with the mean.** Differentiation on the open interval \(a<x<1\) gives
\[
f_a'''(x)=\frac{-15x^2+(36-3a)x+6a-24}{8(1-x)^{5/2}}.
\]
The numerator is increasing in \(x\in(a,1)\), since its derivative is \(36-3a-30x>3-3a>0\); its value at \(x=1\) is \(3(a-1)<0\). Consequently \(f_a'''(x)<0\), so \(f_a'\) is strictly concave. Midpoint strict concavity now yields
\[
\frac{\partial\Delta_a}{\partial m}=
\frac{f_a'(m-d)+f_a'(m+d)}2-f_a'(m)<0
\]
for \(a+d<m<1-d\). Continuity extends strict monotonicity to the closed feasible mean interval, even though derivatives of \(f_a\) need not be finite at \(x=1\).

**2. The upper-mean endpoint is always negative.** At \(m=1-d\), the warm temperature reaches the upper viability threshold and contributes zero. Since \(0<a\le1-2d<1-d<1\),
\[
\frac{f_a(1-2d)}{f_a(1-d)}=
\sqrt2\,\frac{(1-2d)(1-a-2d)}{(1-d)(1-a-d)}
<\sqrt2<2.
\]
Thus \(\Delta_a(1-d,d)=f_a(1-2d)/2-f_a(1-d)<0\).

**3. The lower-mean endpoint has an exact quadratic sign.** At \(m=a+d\), the cold temperature reaches the lower viability threshold, so
\[
\Delta_a(a+d,d)=d\big[(a+2d)\sqrt{1-a-2d}-(a+d)\sqrt{1-a-d}\big].
\]
Both factors in brackets are nonnegative, so squaring preserves their comparison. The difference of their squares is exactly
\[
(a+2d)^2(1-a-2d)-(a+d)^2(1-a-d)
=-dG_a(d),
\]
where
\[
G_a(d)=7d^2+(9a-3)d+a(3a-2).
\]
Therefore \(\operatorname{sgn}\Delta_a(a+d,d)=-\operatorname{sgn}G_a(d)\).

If \(a\ge2/3\), the constant term of \(G_a\) is nonnegative, the linear coefficient is positive, and its quadratic coefficient is positive. Thus \(G_a(d)>0\) for every \(d>0\). If \(0<a<2/3\), the constant term is negative and the leading coefficient positive. Exactly one root is positive, namely the displayed \(d_*(a)\), while
\[
G_a\left(\frac{1-a}{2}\right)=\frac{(1+a)^2}{4}>0.
\]
This locates the unique positive root strictly inside the permitted amplitude interval. Its sign divides the amplitudes as stated.

**4. Classification and endpoint cases.** The strictly decreasing continuous function \(m\mapsto\Delta_a(m,d)\) starts positive, zero, or negative according to Step 3, but always finishes negative by Step 2. The intermediate value theorem yields exactly one crossing precisely in the positive-start case; a zero start gives equality only at the lower endpoint. If the start is negative, every feasible mean is negative. These exhaust all admissible parameter values.

**5. Monotonic cutoff.** For \(0<a<2/3\),
\[
 d_*'(a)=\frac{-9+(1-3a)/\sqrt{9+2a-3a^2}}{14}<0,
\]
as the fraction on the right is strictly less than \(1\) in magnitude for this interval. Direct evaluation of the radical at its two endpoints gives the asserted limits.

## Verification

The attached standalone \(\texttt{CHECK.py}\) executes without third-party dependencies and checks the exact rational polynomial identity, quadratic root and boundary expressions, sampled monotonicity and sign regimes, and a numerical case. It reports 33,560 passing diagnostic assertions in a direct run. These finite tests check arithmetic and implementation, not the theorem's universal quantifiers, which follow from the proof above.

For a purely illustrative calibration \(T_{\min}=10\) and \(T_{\max}=50\) on the numerical temperature scale, \(a=1/5\) and
\[
d_*(1/5)=\frac{3+\sqrt{58}}{35}
=0.3033078030\ldots.
\]
The corresponding half-amplitude is approximately 15.1654 temperature units. At \(d=0.1\) there is a unique mean cutoff \(m_*=0.5247407404\ldots\). At \(d=0.31\) every feasible mean gives a strictly smaller averaged rate than constant exposure at the same mean.

## Relationship to prior work

Brière and coauthors (1999) supplied the empirical temperature-dependent development curve underlying this theorem. Worner (1992) established the ecological importance of nonlinear rate summation under variable temperatures; Ruel and Ayres (1999) developed Jensen-inequality reasoning for ecological variation. Martin and Huey (2008) examined asymmetric thermal fitness curves and temperature preferences, while Estay, Lima and Bozinovic (2013 online) examined interactions of mean and variance in thermal performance. Rebaudo, Struelens and Dangles (2017 online) reviewed temperature-rate curve models, including the Brière family; von Schmalensee and coauthors (2021) investigated thermal variation and growth implications. These works motivate the comparison but the accessible complete material does not provide this exact Brière-I two-temperature **all-means, all-amplitudes** classification or its radical cutoff. A general Jensen or concavity statement alone does not imply the polynomial critical-amplitude formula or its endpoint characterization.

## Limitations

The result applies only to the Brière-I functional form with strictly positive lower and upper thresholds, an in-range equal-duration two-temperature profile, and rate summation with no memory. It does not compare arbitrary temperature distributions, mean-shifted empirical rate curves, thermal mortality, population growth, seasonality, or finite-time development completion. The temperature ratio is defined on the response's calibrated numerical scale. Historical priority is not finally settled: relevant earlier primary material, including the complete Brière (1999), Worner (1992), and Estay (2013 online) papers, was not fully accessible in this review. Independent validation has not been performed.

## References

- Brière, J.-F., Pracros, P., Le Roux, A.-Y., and Pierre, J.-S. (1999). *A Novel Rate Model of Temperature-Dependent Development for Arthropods*. Environmental Entomology 28, 22–29. https://doi.org/10.1093/ee/28.1.22 (first publicly dated 1999-02-01).
- Worner, S. P. (1992). *Performance of Phenological Models Under Variable Temperature Regimes: Consequences of the Kaufmann or Rate Summation Effect*. Environmental Entomology 21, 689–699. https://doi.org/10.1093/ee/21.4.689.
- Ruel, J. J., and Ayres, M. P. (1999). *Jensen's inequality predicts effects of environmental variation*. Trends in Ecology & Evolution 14, 361–366. https://doi.org/10.1016/S0169-5347(99)01664-X.
- Martin, T. L., and Huey, R. B. (2008). *Why “Suboptimal” Is Optimal: Jensen's Inequality and Ectotherm Thermal Preferences*. The American Naturalist 171, E102–E118. https://doi.org/10.1086/527502.
- Estay, S. A., Lima, M., and Bozinovic, F. (first online 2013-09-05). *The role of temperature variability on insect performance and population dynamics in a warming world*. Oikos 123, 131–140. https://doi.org/10.1111/j.1600-0706.2013.00607.x.
- Rebaudo, F., Struelens, Q., and Dangles, O. (first online 2017). *Modelling temperature-dependent development rate and phenology in arthropods: the DEVRATE package for R*. Methods in Ecology and Evolution. https://doi.org/10.1111/2041-210X.12935.
- von Schmalensee, L., et al. (2021). *Thermal performance under constant temperatures can accurately predict insect development times across naturally variable microclimates*. Ecology Letters 24, 1633–1645. https://doi.org/10.1111/ele.13779.
- Roitberg, B. D., and Mangel, M. (2016). *Cold snaps, heatwaves, and arthropod growth*. Ecological Entomology 41, 653–659. https://doi.org/10.1111/een.12324.
