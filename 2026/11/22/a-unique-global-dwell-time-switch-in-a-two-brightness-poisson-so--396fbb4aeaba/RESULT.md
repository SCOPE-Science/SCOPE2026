# A unique global dwell-time switch in a two-brightness Poisson source survey

## Finding

An idealized wide-field source survey can have **two separated globally optimal exposure durations at one unique bright-source fraction**, even though each of its two source populations alone has a unique optimal duration. A field costs one time unit of overhead and an exposure of length \(t>0\). Each source is either bright, with Poisson photon rate \(100\), or faint, with rate \(1\); the bright fraction is \(p\). A source is recorded if at least two photons arrive during its exposure. Write
\[
Q(u)=1-(1+u)e^{-u},\qquad J_p(t)=\frac{pQ(100t)+(1-p)Q(t)}{1+t}.
\]
The objective is the expected fraction of sources detected per unit total clock time, proportional to \(J_p\). For every \(p\in[11/50,7/25]\), the function \(J_p\) has exactly two strict local maxima, a short one at \(s(p)\in(1/20,1/10)\) and a long one at \(\ell(p)\in(1,3)\), separated by exactly one strict local minimum in \((1/10,1)\). There exists exactly one \(p_*\in(11/50,7/25)\) for which these maxima are equally high. For \(p<p_*\) in this interval the long exposure is the unique global optimum, whereas for \(p>p_*\) the short exposure is the unique global optimum. At \(p=p_*\), precisely the short and long exposure durations are global optima. Thus the globally optimal duration jumps by more than nine-tenths of a time unit across the switch. Numerical diagnostics give \(p_*\approx0.249672945086573\), \(s(p_*)\approx0.0682260295171\), and \(\ell(p_*)\approx1.6971315286686\); these decimals are not needed for the proof.

A general structural bound is also proved: for *any* two strictly positive photon rates, mixture fraction and strictly positive overhead, the analogous yield has at most two local maxima. When the rate ratio does not exceed \(3+2\sqrt2\), the yield has exactly one positive critical point. The underlying equal-shape gamma-density modality boundary is already known [1, 2]; no novelty is claimed for that background density fact.

## Assumptions and scope

Fix independent fields with identical expected source density and identical two-class source fractions. Photon counts per source are conditionally Poisson with mean equal to rate times exposure duration. The two-photon threshold is a literal count threshold, without sky background, detector false positives, source confusion, saturation, weather, or nonstationarity. The overhead and exposure are both measured in arbitrary common time units; their ratio matters, not their absolute calibration. Each visited field contributes independently to expected source discoveries. Optimizing field throughput over a large number of visits is equivalent to maximizing the defined \(J_p\); this does not optimize individual scientific information or detection significance.

For the general bound, let \(0<a<b\), \(h>0\), \(0<p<1\), and set
\[
F_p(t)=pQ(bt)+(1-p)Q(at),\qquad J_{p,h}(t)=\frac{F_p(t)}{t+h}\quad (t>0).
\]
For the exact switch take \((a,b,h)=(1,100,1)\), with the indicated closed interval of fractions.

## Proof

**1. The root-count lemma.** Let \(D(t)=(t+h)F'_p(t)-F_p(t)\). Then \(J'_{p,h}(t)=D(t)/(t+h)^2\), and
\[
D(0)=0,\quad D'(t)=(t+h)F''_p(t),\quad\lim_{t\to\infty}D(t)=-1.
\]
Since \(Q'(u)=ue^{-u}\),
\[
F''_p(t)=pb^2e^{-bt}(1-bt)+(1-p)a^2e^{-at}(1-at).
\]
This is positive for \(0\le t\le1/b\), negative for \(t\ge1/a\), and has potential roots strictly between those endpoints only. In that open interval, the root equation is
\[
R(t):=\frac{bt-1}{1-at}e^{-(b-a)t}=\frac{(1-p)a^2}{pb^2}.
\]
Direct differentiation gives
\[
\frac{d}{dt}\log R(t)=(b-a)\left[\frac1{(bt-1)(1-at)}-1\right].
\]
The strictly concave quadratic \(g(t)=(bt-1)(1-at)\) vanishes at both endpoints and has maximum \((b-a)^2/(4ab)\). Consequently \(R\) has at most two turning points, so any positive horizontal level intersects it at most three times. This proves \(F''_p\) has at most three positive zeros. If \(D\) had four distinct strictly positive zeros, Rolle's theorem, applied to these and \(D(0)=0\), would produce four distinct positive zeros of \(D'=(t+h)F''_p\), a contradiction. Thus \(D\) has at most three positive zeros and \(J_{p,h}\) at most two strict local maxima. When \(b/a\le3+2\sqrt2\), the quadratic maximum is at most one; \(R\) is strictly increasing, so \(F''_p\) changes from positive to negative exactly once. The function \(D\) initially increases from zero, then decreases to \(-1\); hence exactly one positive critical point of \(J_{p,h}\), a strict global maximum. A single source rate is similarly unimodal by the one-component derivative formula.

**2. Three separated critical points for a rational fraction interval.** Specialize to \(a=h=1\), \(b=100\). For \(c>0\) put
\[
D_c(t)=\big[1+ct+c^2t(1+t)\big]e^{-ct}-1.
\]
Then \(D(t)=pD_{100}(t)+(1-p)D_1(t)\). For each of the two fractions \(p=11/50\) and \(p=7/25\), the strict signs of \(D\) at the four rational times
\[
 t=1/20,\quad1/10,\quad1,\quad3
\]
are respectively \((+,-,+,-)\). This is independently established by exact-rational alternating-Taylor bounds in the accompanying \(\texttt{check.py}\). Because \(D\) is affine in \(p\), the same signs hold throughout the entire fraction interval. By continuity \(D\) has a zero in each of the three disjoint open intervals. Step 1 excludes any additional positive zero. Moreover these three crossings are simple: if any one were also a zero of \(D'\), Rolle's theorem between \(0\) and the three distinct zeros would give three additional distinct zeros of \(D'\), contradicting the at-most-three-zero bound. It follows that the short and long roots are strict local maxima, the middle one a strict minimum, and the roots depend smoothly on \(p\) in the open and closed parameter interval.

**3. Opposite global preferences at the endpoints.** At \(p=11/50\), every short-branch candidate \(1/20<t<1/10\) obeys, by monotonicity of \(Q\) and \(Q\le1\),
\[
J_p(t)\le\frac{p+(1-p)Q(1/10)}{1+1/20}<0.21300,
\]
whereas \(J_p(2)>0.22777\). The strict comparisons have exact rational enclosures in the checker. As the only other maximum is the long branch, the long one is globally superior at this endpoint.

At \(p=7/25\), for \(t\ge1\) the inequality \(Q(100t)\le1\) yields
\[
J_p(t)\le \frac1{1+t}-\frac{18}{25}e^{-t}<\frac14.
\]
For \(t\ge3\) the last strict inequality is immediate. On \(1\le t\le3\), it is equivalent to
\[
 e^t\frac{3-t}{1+t}<\frac{72}{25}.
\]
The expression on the left decreases on \([1,3]\): its logarithmic derivative for \(t<3\) is \(1-4/[(3-t)(1+t)]\le0\), since \((3-t)(1+t)=4-(t-1)^2\le4\). Its maximum is \(e\) at \(t=1\), and \(e<49/18<72/25\), with the first bound obtained from a geometric majorant for the exponential series. On the other hand, \(J_{7/25}(7/100)>0.26134>1/4\), certified with rational enclosures. Hence the short branch is globally superior at the upper fraction endpoint.

**4. Strictly increasing height difference.** Let \(H(p)=J_p(s(p))-J_p(\ell(p))\). Because both branches are stationary, differentiation using the envelope theorem gives
\[
H'(p)=\frac{Q(100s)-Q(s)}{1+s}-\frac{Q(100\ell)-Q(\ell)}{1+\ell}.
\]
Here \(1/20<s<1/10\), \(\ell>1\), and \(Q\) is increasing. The first term is bounded below by
\[
\frac{Q(5)-Q(1/10)}{11/10}>\frac12
\]
(by exact rational bounds in the checker), whereas the second is strictly less than \(1/(1+\ell)<1/2\). Therefore \(H'(p)>0\) throughout the interval. The strict endpoint preferences from step 3 give \(H(11/50)<0<H(7/25)\), and the intermediate-value theorem yields exactly one zero \(p_*\). All other times have strictly smaller yield than one of the two maxima by step 2 and \(J_p(0)=\lim_{t\to\infty}J_p(t)=0\). The announced uniqueness and discontinuous optimizer transition follow.

## Verification

Run \(\texttt{python check.py}\) using Python 3 and the standard library. The code checks signs at the eight rational parameter–time endpoints, strict endpoint height inequalities, the exponential majorant, and the strict envelope slope separation, using rational alternating Taylor bounds with positive-power propagation. It reports 61 successful rational assertions. An optional SciPy section computes diagnostic approximations to the transition and both optimal durations, but the mathematical conclusions do not use these floating-point calculations. The root count, uniqueness and envelope arguments are analytic, not finite-test claims.

## Relationship to prior work

The exact modality properties of finite gamma mixtures are established background. In particular, Ahmed, Goria and Hussein [1] study bimodality and inflections in two-component gamma *densities*, while Došlá [2] gives a two-gamma shape criterion which, for equal shape two, yields the rate-ratio boundary \(3+2\sqrt2\). The root-count step is a self-contained derivative argument using that known structural setting; the source-density bimodality condition is not claimed as a new discovery. What is claimed is the **global, unique fraction-driven equality of two separated maxima of the Poisson two-count *CDF-per-clock-time* throughput objective**, including explicit strict endpoint certificates and a monotone height-difference proof. Gamma-density bimodality alone does not determine how the two throughput maxima compare as the population mixture changes.

Kashyap and collaborators [3] formalize source-detection probability and power for photon counts, and Nemiroff [4] and Macquart [5] analyze survey dwell-time, depth-versus-area tradeoffs and observational overhead under other source populations and detection functions. Their inspected material does not state or imply the above unique two-count, two-brightness global switch. A related indexed mathematical result on gamma-mixture log-concavity [6] concerns a *density* curvature threshold and cannot be substituted for a theorem about \(J_p\)'s globally optimal exposure. That indexed record's complete text could not be recovered, so priority remains provisional. The same is true of unindexed literature on general renewal reward optimization; absence of a search hit is not a proof of priority.

## Limitations

The theorem is exact only within the specified Poisson detection-and-overhead model. The two-photon threshold is not a realistically calibrated astronomical detection-significance criterion, and photometric background, nuisance rates, changing observing conditions, finite fields, source blending and sky-location correlations are excluded. Changing those assumptions may remove or shift the switch. The interval result proves uniqueness of the transition **within** \([11/50,7/25]\), not across all mixture fractions; it proves no claim about multiple switches outside that interval. The approximate decimals are diagnostic and not certified to all printed digits. Originality assessment is literature-limited and independent audit has not been performed.

## References

1. S. E. Ahmed, M. N. Goria and A. Hussein, "Gamma Mixture: Bimodality, Inflexions and L-Moments," *Communications in Statistics—Theory and Methods* **37** (2008), 1147–1161, DOI: 10.1080/03610920701713286. Full text: https://stat.ethz.ch/pipermail/r-help/attachments/20080702/0db0ac8e/attachment.pdf . Cover identifies online publication 2008-01-01.
2. Z. Došlá, "Conditions for bimodality and multimodality of a mixture of two unimodal densities," *Kybernetika* **45** (2009), 279–292. Full text: https://dml.cz/bitstream/handle/10338.dmlcz/140075/Kybernetika_45-2009-2_6.pdf .
3. V. L. Kashyap et al., "On Computing Upper Limits to Source Intensities," arXiv:1006.4334 (2010), https://arxiv.org/abs/1006.4334 .
4. R. J. Nemiroff, "Tile or Stare? Cadence and Sky Monitoring Observing Strategies that Maximize the Number of Discovered Transients," *Astronomical Journal* **125** (2003), https://arxiv.org/abs/astro-ph/0301583 .
5. J.-P. Macquart, "Optimization of Survey Strategies for Detecting Slow Radio Transients," *Publications of the Astronomical Society of Australia* **31** (2014), https://arxiv.org/abs/1406.5790 .
6. "A sharp log-concavity threshold for equal-shape Gamma rate mixtures," indexed mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-sharp-log-concavity-threshold-for-equal-shape-gamma-rate-mixtu--e45ac4ab94e8 .
