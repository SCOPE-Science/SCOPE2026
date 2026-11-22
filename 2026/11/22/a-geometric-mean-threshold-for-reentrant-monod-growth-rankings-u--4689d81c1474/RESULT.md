# A geometric-mean threshold for reentrant Monod growth rankings under two-level nutrient forcing

## Finding

Consider two positive populations with instantaneous per-capita growth laws
\[
\frac{\dot N_i(t)}{N_i(t)}=a_i\frac{c(t)}{K_i+c(t)}-d,
\qquad i=1,2,
\]
where \(a_i>0\), the common mortality \(d\geq0\), and the two half-saturation constants satisfy \(0<K_1<K_2\). Suppose a prescribed nutrient concentration spends half of each period at \(m-\sqrt v\) and half at \(m+\sqrt v\), for fixed \(m>0\) and variance parameter \(0\leq v\leq m^2\). Its time mean is exactly \(m\), independently of \(v\).

Define the relative long-run logarithmic growth exponent
\[
D(v)=\lim_{t\to\infty}\frac1t\log\frac{N_1(t)/N_2(t)}{N_1(0)/N_2(0)}.
\]
The limit exists and equals
\[
D(v)=a_1 M_{K_1}(v)-a_2 M_{K_2}(v),\qquad
M_K(v)=\frac{m(m+K)-v}{(m+K)^2-v}.
\]
Write \(R(v)=M_{K_1}(v)/M_{K_2}(v)\) and \(\theta=a_2/a_1\). The following classification is exact for **every** choice of the stated positive parameters:

1. If \(m^2\leq K_1K_2\), then \(R\) is strictly decreasing on \((0,m^2)\), so the two species' relative growth ranking reverses at most once as nutrient variance rises.
2. If \(m^2>K_1K_2\), then \(R\) first increases strictly and then decreases strictly. There is exactly one maximum at \(v_*\in(0,m^2)\). In this regime **exactly two strict ranking reversals occur if and only if**
   \[
   \frac{m+K_2}{m+K_1}<\theta<R(v_*).
   \]
   The signs are \(D<0\), then \(D>0\), then \(D<0\). Outside this open interval of growth-rate ratios, at most one strict reversal occurs. Equality at the upper limit creates a tangential tie without a reversal.

Thus \(m=\sqrt{K_1K_2}\) is the **sharp mean-concentration boundary for the possibility of two variance-driven growth-rank reversals**, even though both species have strictly concave Monod responses and identical mortality.

The maximum can be located without numerical integration: put
\[
A_i=m(m+K_i),\quad B_i=(m+K_i)^2,\quad W_i=K_i(m+K_i).
\]
Then \(v_*\) is the unique solution in \((0,m^2)\) of
\[
\frac{(A_2-v_*)(B_2-v_*)}{(A_1-v_*)(B_1-v_*)}=\frac{W_2}{W_1}.
\]

**Exact witness.** Let \(m=1\), \(K_1=1/5\), \(K_2=1\), \(a_1=1\), \(a_2=17/10\) and common \(d=1/10\). Then
\[
D(v)=-\frac{175v^2-162v+24}{10(v-4)(25v-36)}.
\]
The denominator is strictly positive throughout \(0\leq v\leq1\). Consequently the only two ranking-reversal variances are
\[
v_{\pm}=\frac{81\pm\sqrt{2361}}{175},\qquad
v_-\approx0.1851993003,\quad v_+\approx0.7405149854.
\]
Species 2 leads for \(0\le v<v_-\), species 1 for \(v_-<v<v_+\), and species 2 for \(v_+<v\le1\). Both species' mean per-capita growth exponents are positive throughout this entire variance range. The two variance thresholds correspond to nutrient half-amplitudes approximately \(0.4303479\) and \(0.8605318\).

## Assumptions and scope

The resource time course is an **externally imposed** two-level periodic signal; it is not solved from a consumption or nutrient-balance equation. Both levels are nonnegative, and strictly positive for \(v<m^2\). The two levels occupy equal durations; their order within a period is immaterial to the per-period growth exponent. Species share the same mortality \(d\), and their populations obey linear equations with the prescribed, piecewise constant coefficient. The finding concerns relative exponential growth under this forcing, not competitive exclusion in a feedback-coupled chemostat.

All quantifiers include any positive period length, any \(a_i>0\), \(0<K_1<K_2\), \(m>0\), \(d\ge0\), and all \(v\in[0,m^2]\), with strict reversals counted only inside \((0,m^2)\). Reversing species labels reduces the case \(K_2<K_1\) to the stated ordering. If \(K_1=K_2\), relative ranking is independent of \(v\), so this distinct-constant condition is essential to the two-reversal assertion.

## Proof

**Exact integration.** Over one period, integration of the population equations yields the difference of the two time averages. For any \(K>0\), direct common-denominator simplification gives
\[
\frac12\left(\frac{m-\sqrt v}{K+m-\sqrt v}+\frac{m+\sqrt v}{K+m+\sqrt v}\right)
=\frac{m(m+K)-v}{(m+K)^2-v}=M_K(v).
\]
The mortality terms cancel from the log-ratio. Repetition of periods yields \(D(v)\), and any terminal incomplete period contributes \(O(1/t)\) to the normalized log-ratio.

**One-maximum lemma.** For \(0\le v\le m^2\), all \(A_i-v\) and \(B_i-v\) are strictly positive. Differentiation gives
\[
\frac{R'(v)}{R(v)}=
-\frac{W_1}{(A_1-v)(B_1-v)}
+\frac{W_2}{(A_2-v)(B_2-v)}.
\]
Define \(H(v)=(A_2-v)(B_2-v)/[(A_1-v)(B_1-v)]\). Both component ratios \((A_2-v)/(A_1-v)\) and \((B_2-v)/(B_1-v)\) are strictly increasing because \(K_2>K_1\); hence \(H\) is strictly increasing. The sign of \(R'\) is the sign of \(W_2/W_1-H(v)\). It follows that \(R'\) can vanish at most once and can only switch from positive to negative.

At zero variance, exact simplification yields
\[
\operatorname{sign}R'(0)=\operatorname{sign}\bigl((K_2-K_1)(m^2-K_1K_2)\bigr).
\]
At the maximal nonnegative variance, the logarithmic derivative is
\[
\frac{R'(m^2)}{R(m^2)}=
-\frac{m+K_1}{mK_1(2m+K_1)}
+\frac{m+K_2}{mK_2(2m+K_2)}<0,
\]
because \((m+K)/[K(2m+K)]\) is strictly decreasing in \(K>0\). These facts prove the first two shape cases and the existence and uniqueness of the interior maximum when \(m^2>K_1K_2\).

**Sharp reversal criterion.** Since \(M_{K_2}(v)>0\),
\[
D(v)=a_1M_{K_2}(v)\bigl(R(v)-\theta\bigr).
\]
Furthermore
\[
R(0)=\frac{m+K_2}{m+K_1},\qquad
R(m^2)=\frac{2m+K_2}{2m+K_1}<R(0).
\]
For the single-hump case, a horizontal line at height \(\theta\) intersects both rising and falling branches exactly once each precisely when \(R(0)<\theta<R(v_*)\); all other levels have at most one strict crossing. In the monotonically decreasing case there is at most one crossing. This proves necessity, sufficiency, direction of signs and sharpness.

**Rational witness.** Substituting the displayed constants and combining fractions gives the stated rational \(D(v)\). The quadratic numerator has discriminant \(9444=4\cdot2361>0\). The elementary bounds \(48^2<2361<49^2\) place both distinct roots strictly between zero and one. The leading quadratic coefficient is positive, and the denominator is positive throughout the interval; the signs therefore alternate exactly as stated. Also \(M_K'(v)=-K(m+K)/[(m+K)^2-v]^2<0\). At \(v=1\), the witness's mean gross growth rates are \(5/11\) for species 1 and \(17/30\) for species 2, both exceeding common mortality \(1/10\). Hence their mean net growth rates remain positive for all \(0\le v\le1\).

## Verification

The companion `check.py` uses exact rational arithmetic to confirm the rational witness identity at 101 rational variances, the strict sign tests, the root-bracketing inequalities, and, over 1,800 seeded positive rational parameter sets, the two-level averaging identity, monotonicity of \(H\), the endpoint derivative sign, the geometric-mean threshold, and the endpoint ordering. It reports **10,906 passed exact-rational assertions**. These tests are diagnostics; the infinite-parameter theorem is proved by the identities and strict inequalities above.

Reproduce by running `python check.py` with Python 3; no nonstandard packages or data files are required.

## Relationship to prior work

The Monod saturation law is classical. Hsu (1980) studies two species coupled to a nutrient-balance equation with **sinusoidally varying supply**, proving extinction conditions and analyzing possible coexistence. Grover (1990) studies time-variable resource competition in the Monod framework. The present assertion is narrower about biological feedback but different mathematically: it classifies **relative exponential growth under prescribed, equal-duration two-level resource concentration**, provides an if-and-only-if geometric-mean boundary, and proves two ranking reversals with common mortality. It does not claim to solve or strengthen the chemostat coexistence problem.

Grover (2008) analyzes nutrient storage and spatial mixing in a coupled population-resource model. Yamamichi and Letten (2022) discuss two crossings of **instantaneous** species growth responses as nutrient concentration changes and fluctuation-mediated coexistence, including convex-response examples. Neither statement implies the two crossings of **time-averaged rank as the variance of an equal-mean two-level environment changes** with both responses concave. Stump and colleagues (2022) discuss sinusoidally forced Monod chemostat models but do not, in the inspected material, supply this two-point sharp threshold.

Publication-priority limitations remain: full text of Grover (1990) was not accessible for line-by-line comparison. General theory of ratios of fractional-linear functions may also imply the elementary shape lemma, although the specific ecological if-and-only-if result and rational reentrance example were not found in the inspected sources.

## Limitations

There is no feedback of the growing populations on nutrient concentration, no nutrient storage, no resource stochasticity, no unequal duty cycle, and no physiological response lag. The concentration jump is idealized. The theorem says which species has the larger **prescribed-environment long-run per-capita exponent**; it is not a theorem about exclusion, invasion into a self-regulated resident environment, or coexistence. Finite-duration measurements need not show the asymptotic ratio trend near a threshold. No empirical fit or independent experimental validation is claimed.

## References

1. Hsu, S.-B. (1980). *A Competition Model for a Seasonally Fluctuating Nutrient*. Journal of Mathematical Biology 9, 115–132. DOI: 10.1007/BF00275917. Author-hosted full text: https://www.math.nthu.edu.tw/~sbhsu/JMB1980.pdf.
2. Grover, J. P. (1990). *Resource Competition in a Variable Environment: Phytoplankton Growing According to Monod's Model*. The American Naturalist 136, 771–789. DOI: 10.1086/285131. Abstract inspected, full-text access limited.
3. Grover, J. P. (2008). *Is Storage an Adaptation to Spatial Variation in Resource Availability?* The American Naturalist 173. DOI: 10.1086/595751. Open full text: https://www.journals.uchicago.edu/doi/full/10.1086/595751.
4. Yamamichi, M., and Letten, A. D. (2022). *Extending the gleaner–opportunist trade-off*. Journal of Animal Ecology 91, 2163–2170. DOI: 10.1111/1365-2656.13813. Open full text: https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/1365-2656.13813.
5. Stump, S. M., Song, C., Saavedra, S., Levine, J. M., and Vasseur, D. A. (2022). *Synthesizing the effects of individual-level variation on coexistence*. Ecological Monographs 92, e01493. DOI: 10.1002/ecm.1493. Open full text: https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecm.1493.
