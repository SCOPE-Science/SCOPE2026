# Three isotope clocks identify an uncalibrated temporary diet excursion

## Finding

**Theorem (sharp three-tissue recovery of an uncalibrated return excursion).** Fix three *distinct* known tissue turnover rates \(\lambda_1,\lambda_2,\lambda_3>0\). An animal at isotopic equilibrium on a known baseline diet A briefly ate diet B and returned to A before a single simultaneous tissue sampling time. Let the two return-looking-back transition ages satisfy \(0<a<b<\infty\), and let the unknown common tissue-equilibrium difference between diets B and A be \(\Delta>0\). Under one-compartment first-order turnover, the three measured tissue residuals are
\[
d_i=\Delta\bigl(e^{-\lambda_i a}-e^{-\lambda_i b}\bigr),\qquad i=1,2,3.
\]
The mapping \((\Delta,a,b)\mapsto(d_1,d_2,d_3)\) is **globally injective** for every triple of distinct positive rates. In the strictly interior parameter family, no one- or two-tissue sampling design is locally identifying, so three tissues are sharp. This is structural identification from exact measurements, not a noise-robust estimation assertion.

If the rates are \((\gamma,2\gamma,3\gamma)\), \(\gamma>0\), write \(R=d_2/d_1\), \(S=d_3/d_1\), and \(K=4S-3R^2\). Then feasibility is characterized precisely by
\[
d_1>0,\quad K>0,\quad 0<\frac{R-\sqrt K}{2}<\frac{R+\sqrt K}{2}<1.
\]
For feasible data the **unique** solution is
\[
u=\frac{R+\sqrt K}{2},\quad v=\frac{R-\sqrt K}{2},\quad
 a=-\gamma^{-1}\log u,\quad b=-\gamma^{-1}\log v,\quad
\Delta=\frac{d_1}{\sqrt K}.
\]
The displayed closed inverse is included as an explicit illustration of the general injectivity result, not as a claim that three harmonic moment measurements were previously unknown. The Jacobian with columns ordered as \((\Delta,a,b)\) is exactly
\[
\det\frac{\partial(d_1,d_2,d_3)}{\partial(\Delta,a,b)}
=-\gamma^2\Delta^2uv(u-v)^4.
\]
Its strict nonvanishing proves local regularity for positive-duration excursions and quantifies a fourth-power loss of determinant as the two switch ages coalesce at bounded \(a\) and \(\Delta\). The quartic statement is about the Jacobian determinant, not an asserted statistical minimax rate.

## Assumptions and scope

The animal has previously reached isotopic equilibrium on diet A, and its tissue-specific baseline equilibrium readings are known and subtracted. Diet B differs by the **same unknown positive equilibrium contrast** \(\Delta\) in every tissue (or tissue-specific discrimination corrections have already been reliably calibrated). The animal consumes only A before age \(b\), only B at lookback ages in \([a,b]\), and A again from age \(a\) until sampling. Ages run backward from sampling; \(a\) is time elapsed since returning to A and \(b-a\) is the duration on B. Equilibrium isotopic response in tissue \(i\) obeys \(\dot x_i=\lambda_i(E_i(t)-x_i)\). Turnover rates are known, fixed, distinct, and positive, tissue measurements are contemporaneous and exact, and the contrast's sign is fixed a priori. Shared contrast, steady initial A equilibrium, and a **single** temporary B interval are substantive hypotheses. With a known negative common contrast, sign all residuals to reduce to the positive case. No general statement is made for tissue-specific unknown contrasts, multiple excursions, or uncertain initial equilibrium.

## Proof

**1. Forward equation.** With the baseline removed, the input is \(\Delta\) for lookback ages \(s\in[a,b]\) and zero elsewhere. Convolution of the stable linear turnover equation gives
\[
 d_i=\lambda_i\Delta\int_a^b e^{-\lambda_i s}\,ds
 =\Delta(e^{-\lambda_i a}-e^{-\lambda_i b}).
\]
Thus division by the known positive rate produces three Laplace moments of the unknown positive constant-height interval: \(d_i/\lambda_i=\int_0^\infty\Delta\mathbf1_{[a,b]}(s)e^{-\lambda_i s}\,ds\).

**2. Chebyshev uniqueness lemma.** For any three distinct positive exponents \(\lambda_1,\lambda_2,\lambda_3\), a nonzero linear combination of the functions \(e^{-\lambda_i s}\) has at most two real zeros, counting multiplicities. To prove it, order exponents increasingly, divide the combination by the slowest exponential, differentiate, and apply Rolle's theorem inductively to the remaining two exponential terms (including the multiplicity-counting version); the two-term base case is immediate. Consequently, for any \(r\in\{0,1,2\}\) prescribed distinct nodes, there exists a nonzero linear combination of the first \(r+1\) exponentials with simple zeros at those nodes and no other real zeros. For \(r=0\) take one positive exponential. For \(r=1\) solve one homogeneous equation with two coefficients. For \(r=2\) solve two homogeneous equations with three coefficients; a multiple root or an additional root would violate the zero bound, so the prescribed roots are simple and the combination alternates sign there.

Now suppose two distinct parameter triples produce the same three measurements. Their signed input difference is
\[
f(s)=\Delta\mathbf1_{[a,b]}(s)-\Delta'\mathbf1_{[a',b']}(s).
\]
Unless it vanishes identically, its nonzero values have at most two sign transitions, after zero intervals are ignored. This holds because two intervals are either nested, disjoint, or partially overlapping: in the nested case the signs can follow at most a \(+,-,+\) or \(-,+,-\) sequence, while in the other cases they change at most once. Let \(r\le2\) be its sign-transition count, and select one point in each transition (inside any intervening zero gap if needed). The lemma supplies a nonzero combination \(g(s)=\sum_i c_i e^{-\lambda_i s}\) with simple zeros precisely at these locations, whose overall sign can be chosen so that \(f(s)g(s)\ge0\) everywhere and is strictly positive on a set of positive measure. Therefore \(\int_0^\infty f(s)g(s)\,ds>0\). Yet each of its three component Laplace moments vanishes by equality of the observations, a contradiction. Hence the interval-height signals coincide almost everywhere. Positivity and finite nonzero intervals force \(a=a'\), \(b=b'\), and \(\Delta=\Delta'\). This proves **global** uniqueness for arbitrary distinct turnover rates, not merely generic local identifiability.

**3. Sharpness of three tissues.** For two distinct rates \(\lambda_1,\lambda_2\), put \(L=b-a>0\). Their measured ratio is
\[
\frac{d_2}{d_1}=
 e^{-(\lambda_2-\lambda_1)a}
 \frac{1-e^{-\lambda_2L}}{1-e^{-\lambda_1L}}.
\]
At any interior true \((a,L,\Delta)\), perturb \(L\) within a sufficiently small open interval and solve this equation explicitly and continuously for \(a\) (possible because \(\lambda_2-\lambda_1\ne0\)). Then set \(\Delta=d_1/[e^{-\lambda_1a}(1-e^{-\lambda_1L})]\). The resulting distinct feasible triples have the **same two exact readings**. Fewer readings plainly cannot resolve them either. A duplicated turnover rate adds no information. Therefore the minimum is exactly three distinct tissues.

**4. Closed inverse and collision behavior.** For rates \((\gamma,2\gamma,3\gamma)\), put \(u=e^{-\gamma a}\), \(v=e^{-\gamma b}\), with \(0<v<u<1\). The readings are \(d_i=\Delta(u^i-v^i)\), so
\[
R=u+v,\qquad S=u^2+uv+v^2,
\qquad K=4S-3R^2=(u-v)^2.
\]
The positive root \(u-v=\sqrt K\) yields the stated inverse and necessary/sufficient feasibility inequalities. Direct differentiation of the three forward equations yields
\[
\det\frac{\partial(d_1,d_2,d_3)}{\partial(\Delta,u,v)}=-\Delta^2(u-v)^4.
\]
Since \(\partial(u,v)/\partial(a,b)=\gamma^2uv\), the original-variable determinant is \(-\gamma^2\Delta^2uv(u-v)^4\). For fixed \(a\), \(\Delta\), \(\gamma\) and \(L=b-a\downarrow0\), \(u-v=u(1-e^{-\gamma L})\sim u\gamma L\), proving determinant decay proportional to \(L^4\) with nonzero proportionality factor. This final statement does not assert that every individual parameter's statistical error scales with the fourth power.

## Verification

The accompanying executable `check_isotope.py` has been run with Python, SymPy and SciPy. It reconstructs the inverse discriminant and Jacobian with exact symbolic algebra (2 assertions), confirms 513 positive rational examples by exact fractions, checks a specific unequal-duration example, and numerically recovers parameters for 24 non-harmonic rate/parameter/initialization tests. Output:

```text
ISOTOPIC_THREE_TISSUE_OK assertions=540 symbolic=2 rational=513 nonlinear_numeric=24
```

Example: with \(\gamma=1\), \(u=4/5\), \(v=1/5\), and \(\Delta=5\), measurements are \((d_1,d_2,d_3)=(3,3,63/25)\), and the inverse returns \(a=\log(5/4)\), \(b=\log5\), and \(\Delta=5\). Reproduce with `python check_isotope.py` after installing SymPy and SciPy. The theorem for *all* real positive rates and histories rests on the Chebyshev proof, not finite testing or a numerical solver.

## Relationship to prior work

Klaassen et al. (2010) formulate the *single*-diet-switch isotopic clock, using two tissues to recover one unknown switch age when a shared isotope contrast is uncalibrated. That single-switch situation does not give the two unknown endpoints of a temporary return excursion. Jouta et al. (first online 2016, journal year 2017) study two diet switches and explicitly discuss return-to-original-diet A–B–A excursions (their “ABBA switch”); their published two-tissue model presupposes known equilibrium signatures for *all three stages* and solves for two switch times. The contribution here is **not** the idea of a two-switch isotope model or an ABBA excursion: it is the sharp three-tissue identification theorem when the intermediate diet contrast is *unknown*, valid for any distinct positive turnover rates, with the harmonic closed inverse and coalescence Jacobian.

An earlier first-order uptake result already analyzes a one-rectangular-pulse versus two-rectangular-pulse discrimination problem with four harmonically spaced observation channels and the same one-pulse moment formula; its three-channel ambiguity is **between the one-pulse and two-pulse classes**, not within the promised one-pulse class. That result is not claimed new or superseded here. The present mathematical addition is the **arbitrary-distinct-rate** global and sharp one-interval identification theorem applied to three uncalibrated isotope tissues, rather than another four-harmonic-channel pulse-class test. The arithmetic-progression inverse is explanatory and its algebraic relation to the earlier single-pulse moment formula is acknowledged.

Batenkov, Sarig and Yomdin (2009) derive general algebraic/Prony methods for reconstructing piecewise signals from integral measurements. Batenkov and Yomdin (2013) analyze general Prony invertibility and colliding nodes. They supply important broader mathematical context; this result should be understood as a constrained positive-interval Laplace inverse problem, not a novel invention of Prony reconstruction or moment uniqueness. Their inspected results do not directly state the minimal arbitrary-rate three-measurement theorem in this specified isotope-clock model or the displayed positive-domain inverse; general method coverage remains a residual historical-priority risk.

## Limitations

The theorem does not establish practical precision under noise, recovery when different tissues have unknown distinct contrast factors, identifiability under an unknown pre-excursion baseline, multiple diet pulses, isotope fractionation or time-varying turnover rates, or an optimal choice of tissue rates. Near the zero-duration boundary, the Jacobian determinant collapses as the fourth power and inference is potentially ill-conditioned. A zero contrast, simultaneous switches, or indistinguishable tissue rates is excluded. Equilibrium isotope differences have to share a common signed scale after tissue discrimination corrections. This is a theoretical exact-data benchmark. Earlier broad moment-reconstruction or ecological monitoring publications not fully indexed might imply the narrow theorem; independent literature review and experimental validation have not been performed.

## References

1. Klaassen, M., Piersma, T., Korthals, H., Dekinga, A., and Dietz, M. W. *Single-point isotope measurements in blood cells and plasma to estimate the time since diet switches*. Functional Ecology **24** (2010), 796–804. First published July 13, 2010. https://doi.org/10.1111/j.1365-2435.2010.01689.x
2. Jouta, J., et al. *Ecological forensics: using single point stable isotope values to infer seasonal schedules of animals after two diet switches*. Methods in Ecology and Evolution **8** (2017), 492–500. First published October 27, 2016. https://doi.org/10.1111/2041-210X.12695
3. Batenkov, D., Sarig, N., and Yomdin, Y. *An “algebraic” reconstruction of piecewise-smooth functions from integral measurements*. arXiv:0901.4659, first posted January 29, 2009. https://arxiv.org/abs/0901.4659
4. Batenkov, D. and Yomdin, Y. *Local and global geometry of Prony systems and Fourier reconstruction of piecewise-smooth functions*. arXiv:1301.1187, first posted January 7, 2013. https://arxiv.org/abs/1301.1187
