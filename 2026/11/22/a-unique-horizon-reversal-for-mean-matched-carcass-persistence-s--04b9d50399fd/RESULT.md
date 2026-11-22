# A unique horizon reversal for mean-matched carcass-persistence survey calendars

## Finding

**Theorem (sharp survey-calendar reversal).** Consider carcasses arriving at a constant positive rate over a fixed monitoring horizon \(H>0\). A carcass has survival function
\[
 S(t)=\sum_{j=1}^{m}w_j e^{-\lambda_j t},\qquad
 0<\lambda_1<\cdots<\lambda_m,\quad m\ge2,\quad
 w_j>0,\quad\sum_{j=1}^{m}w_j=1.
\]
There are exactly two instantaneous, independently imperfect surveys, with identical per-survey detection probability \(0<p<1\) conditional on a carcass still being present, and no false detections. The aim is to maximize the expected number of distinct carcasses detected. The second optimal survey is always at \(H\). Define \(H_S\) by \(S(H_S)=p\). The first optimal survey is uniquely
\[
 t_S(H)=\begin{cases}
 H,&0<H\le H_S,\\
 \text{the unique }t\in(H/2,H)\text{ such that }S(t)=pS(H-t),&H>H_S.
 \end{cases}
\]
The same schedules maximize the probability of detecting at least one carcass when arrivals form a Poisson process with constant intensity.

Replace this heterogeneous lifetime distribution by a *single* exponential lifetime with exactly the same mean
\[
 M=\sum_{j=1}^{m}\frac{w_j}{\lambda_j},\quad S_E(t)=e^{-t/M},\quad L=-\log p,\quad H_E=ML.
\]
Its unique optimal first survey is \(t_E(H)=H\) for \(H\le H_E\) and \(t_E(H)=(H+H_E)/2\) otherwise. There is exactly one positive number \(u_0\) satisfying
\[
 S(u_0)=e^{-u_0/M},\qquad p_0=e^{-u_0/M}\in(0,1).
\]
The following comparison is complete, including equality cases:

1. For \(0<p\le p_0\), \(t_S(H)=t_E(H)\) when \(H\le H_E\), and \(t_S(H)>t_E(H)\) when \(H>H_E\): the mixture never prescribes an earlier first survey.
2. For \(p_0<p<1\), one has \(H_S<H_E\), and there exists exactly one \(H_*>H_E\) with \(t_S(H_*)=t_E(H_*)\). Equality also holds for \(0<H\le H_S\). The mixture prescribes a strictly *earlier* first survey for \(H_S<H<H_*\), but a strictly *later* one for \(H>H_*\).

The crossing is characterized without optimization over two dates: it is the unique \(H>H_E\) satisfying
\[
 S\!\left(\frac{H+H_E}{2}\right)
 =pS\!\left(\frac{H-H_E}{2}\right).
\]
In particular, replacing a heterogeneous disappearance process by its mean-matched exponential approximation can misplace the earlier of two equal-effort searches in opposite directions as the monitoring horizon changes, and such an error-direction reversal can occur **at most once**.

**Exact two-class illustration.** With \(S(t)=(e^{-t}+e^{-3t})/2\), \(M=2/3\), let \(z\approx1.83928675521416\) be the unique real root exceeding one of \(z^3-z^2-z-1=0\). Then \(p_0=z^{-3}\approx0.16071324478584\). At \(p=1/2\), the unique reversal horizon is
\[
 H_* =\frac23\log2-\log\left(2^{4/3}-2\right)
 \approx1.11632828814274.
\]
At \(H=0.6\), the mixture's optimal first date is \(0.502405145688\), earlier than the mean-matched value \(0.531049060187\); at \(H=2\), its optimal date is \(1.278012394648\), later than \(1.231049060187\).

## Assumptions and scope

Carcass arrival times form a homogeneous Poisson process of intensity \(q>0\) on \([0,H]\), initially with no carcasses. A new carcass independently receives an exponential removal rate \(\lambda_j\) with probability \(w_j\); its lifespan is then exponential at that rate. Equivalently the marginal survival is \(S\) above. Every carcass is available until removed. At each chosen time \(0\le t_1\le t_2\le H\), its conditional detection probability is \(p\) if available. Detections are independent given the latent lifetimes and arrival times. After being detected, a carcass is recorded once and removed from later counting. Attempts may coincide in time but then represent *two independent tests* of the same available carcass, not one duplicate record. Each survey has the same fixed logistical effort; timing itself is not charged. Parameters, survival mixture, and absence of preexisting carcasses are known for designing the experiment.

No equivalence with unbiased mortality estimation or information-optimal parameter inference is asserted. A deterministic constant arrival intensity suffices for the expected-value argument; the Poisson assumption additionally makes the probability-of-any-detection objective equivalent by Poisson thinning. We require all weights strictly positive and at least two *distinct* removal rates; the single-rate limit has no strict error reversal.

## Proof

**1. Expected distinct detections and the terminal survey.** Let \(C(x)=\int_0^xS(u)\,du\). For a carcass arriving at \(s\le t_1\), inclusion-exclusion gives its probability of ever being counted by the two surveys as \(pS(t_1-s)+pS(t_2-s)-p^2 S(t_2-s)\): the two detections can both occur only if the original carcass survives to \(t_2\). A carcass arriving in \((t_1,t_2]\) is counted with probability \(pS(t_2-s)\). Integrating over arrival times yields
\[
 \frac{\mathbb E N_{\mathrm{found}}(t_1,t_2)}{qp}
 = C(t_1)+C(t_2)-p\bigl[C(t_2)-C(t_2-t_1)\bigr]. \tag{1}
\]
For fixed \(t_1\), the partial derivative of the right side with respect to \(t_2\) is \((1-p)S(t_2)+pS(t_2-t_1)>0\). Hence \(t_2=H\) in every optimum, uniquely. Differentiating (1) with \(t_2=H\) gives
\[
 \frac{1}{qp}\frac{d}{dt_1}\mathbb E N_{\mathrm{found}}(t_1,H)
 =S(t_1)-pS(H-t_1). \tag{2}
\]
The right side is strictly decreasing on \([0,H]\) because \(S\) is strictly decreasing. It is positive at zero and has value \(S(H)-p\) at \(H\). Thus \(t_1=H\) is the unique maximum when \(S(H)\ge p\); otherwise there is one interior maximizer satisfying the equation in the finding. At that maximizer, \(S(t)=pS(H-t)<S(H-t)\), so \(t>H/2\). For a Poisson population of independent marked arrivals, the thinned count of carcasses eventually found is Poisson with mean (1); consequently \(\Pr(N_{\mathrm{found}}\ge1)=1-e^{-\mathbb EN_{\mathrm{found}}}\), with the same maximizer.

**2. Heterogeneous rates imply a strictly increasing optimal time skew.** For \(t\ge0\), define the survival hazard \(h(t)=-S'(t)/S(t)\). With tilted weights \(\pi_j(t)=w_j e^{-\lambda_j t}/S(t)\), differentiation gives
\[
 h(t)=\sum_j\pi_j(t)\lambda_j,\qquad
 h'(t)=-\sum_j\pi_j(t)(\lambda_j-h(t))^2<0. \tag{3}
\]
For \(H>H_S\), put \(\ell(H)=2t_S(H)-H>0\). The stationary equation (2) becomes
\[
 \int_{(H-\ell)/2}^{(H+\ell)/2}h(u)\,du=L. \tag{4}
\]
Let \(a=(H-\ell)/2\) and \(b=(H+\ell)/2\). Differentiating (4) by the implicit-function theorem gives
\[
 \ell'(H)=\frac{h(a)-h(b)}{h(a)+h(b)}\in(0,1). \tag{5}
\]
As \(H\downarrow H_S\), the interior optimum approaches \(t_S=H_S\), so \(\ell(H)\downarrow H_S\). Since \(h(t)\ge\lambda_1\), (4) implies \(\ell(H)\le L/\lambda_1\); since \(\ell\) is bounded and \(H\to\infty\) sends \(a\to\infty\), the hazard converges uniformly to \(\lambda_1\) across \([a,b]\) and therefore
\[
 \lim_{H\to\infty}\ell(H)=\frac L{\lambda_1}. \tag{6}
\]
The single-rate exponential comparator has constant hazard \(1/M\), hence constant post-activation skew \(H_E=ML\). The mixture always has \(\lambda_1<1/M\), so its long-horizon skew is strictly larger than \(H_E\).

**3. Exactly one detection-quality boundary.** Define
\[
 F(u)=e^{u/M}S(u)=\sum_jw_j e^{(1/M-\lambda_j)u}.
\]
We have \(F(0)=1\) and
\[
 F'(0)=\frac1M-\sum_jw_j\lambda_j<0,
 \quad F''(u)=\sum_jw_j(1/M-\lambda_j)^2e^{(1/M-\lambda_j)u}>0.
\]
Strict negativity follows from the strict harmonic-mean/arithmetic-mean inequality for distinct positive rates. Since \(\lambda_1<1/M\), its slowest component ensures \(F(u)\to\infty\). Strict convexity gives exactly one positive root \(u_0\) of \(F(u)=1\), and \(F(u)<1\) for \(0<u<u_0\), \(F(u)>1\) for \(u>u_0\).

At \(H_E=ML\), the sign of \(F(H_E)-1\) equals the sign of \(S(H_E)-p\). Since \(S\) decreases strictly, this yields \(H_S>H_E\) when \(p<p_0\), equality when \(p=p_0\), and \(H_S<H_E\) when \(p>p_0\).

**4. Global comparison and unique reversal.** When \(p\le p_0\), both first visits are terminal up to \(H_E\). For \(H_E<H\le H_S\), the mixture remains terminal, while the exponential first date is already earlier. Beyond \(H_S\), equation (5) gives \(\ell(H)>H_S\ge H_E\), so \(t_S(H)>t_E(H)\) for every \(H>H_E\).

When \(p>p_0\), \(H_S<H_E\): the mixture first date becomes strictly earlier than the terminal exponential first date on \((H_S,H_E]\). At \(H_E\), its skew \(\ell(H_E)<H_E\), since \(t_S(H_E)<H_E\). Equations (5) and (6) show that \(\ell(H)\) grows continuously and strictly, with limit \(L/\lambda_1>H_E\). It therefore crosses the constant comparator skew \(H_E\) at exactly one finite \(H_*>H_E\), and crosses it transversely. For \(H>H_E\), comparing the first dates is the same as comparing their skews, proving every stated sign and equality. Substituting \(\ell=H_E\) into (4) gives the equation characterizing \(H_*\). This completes the proof. \(\square\)

**5. Exact illustration.** For two equal weights and rates one and three, \(M=2/3\). Writing \(z=e^{u_0/2}>1\) in \(S(u_0)=e^{-3u_0/2}\) gives \(z^4-2z^3+1=0\). Removing the root \(z=1\) gives the displayed cubic. With \(p=1/2\), \(H_E=(2/3)\log2\). The equation for \(H_*\) reduces to \(e^{-(H_*-H_E)}=2^{4/3}-2\), giving the exact formula. The numerical values follow by evaluating the strictly monotone stationary equation, with no extrapolation from a finite grid.

## Verification

Run the accompanying `checker.py` with `python3 checker.py` using Python's standard library. On the packaged code, it reports `PASS 60064 supplementary numerical assertions; finite diagnostics are not a proof`. The checks include a numerically independent arrival-time integration of (1), direct finite two-dimensional grid challenges to the global optimizer, positive tilted-rate variances, random mixed-rate comparisons with the mean-matched exponential design, the explicit two-class crossover, and increasing optimal skew. No statistical experiments or finite grids are used to establish claims over all continuous parameter values; the proof above does.

## Relationship to prior work

Henry et al. (2021) document the practical cost–persistence tradeoff in roadkill surveys using multi-taxon data and frequency simulations; their publicly available revised manuscript was inspected through its methodological analysis and appendices. The present theorem fixes *exactly two* independent detection attempts and determines the optimal first date over a finite horizon; it does not assert a new discovery about heterogeneous carcass survival itself.

Korner-Nievergelt et al. (2015) develop estimators for carcass detection probabilities using survival curves, variable search effort, continuous arrivals, and irregular intervals, including retention of initially missed carcasses. Their general probability machinery subsumes the probability-accounting setup and is explicitly credited. Their inspected article does not state or imply the sharp mean-matched exponential **calendar-direction reversal** without additional mixture-hazard and convex-crossing analysis. Etterson (2013) also develops a general hidden-Markov estimation framework for irregular carcass-search intervals; the available repository abstract, bibliographic record, and public software documentation were inspected, but its complete article could not be read here, leaving residual historical priority uncertainty.

An independently published two-visit ecological-detection theorem for a colonization–extinction Markov state establishes a terminal-clustering threshold followed by a constant shifted survey time. That initially vacant but *recolonizing* habitat differs from permanent carcass disappearance, and its fixed-offset conclusion does not imply the strictly increasing mixture-survival skew or the mean-matched horizon reversal here. Other published survey-cap results concern Gamma-heterogeneous detection intensity and search cost, not two observations of latent carcass-removal lifetimes. General optimal inspection/survival theory could contain a broader equivalent statement; historical uniqueness is not asserted.

## Limitations

The theorem is an exact result within a homogeneous-arrival, finite positive-exponential-mixture, perfect-specificity, equal-detection-quality, two-visit model. It does not cover heterogeneous arrival intensity, postmortem detectability depending on carcass age, correlated or changing searcher efficiency, non-exponential persistence mechanisms, travel-time constraints, search intervals with finite duration, costs of revisits, or inference about actual mortality when parameters are unknown. Simultaneous independently effective tests may be impractical; if coincidence is prohibited, the terminal case is a limiting supremum, not an attained pair. The result recommends no particular survey interval without field calibration. Independent audit and field validation have not been performed.

## References

1. Henry, D. A. W., Collinson-Jonker, W. J., Davies-Mostert, H. T., Nicholson, S. K., Roxburgh, L., and Parker, D. M. (2021), *Optimising the cost of roadkill surveys based on an analysis of carcass persistence*, Journal of Environmental Management **291**, 112664. First public article date 2021-05-08. https://doi.org/10.1016/j.jenvman.2021.112664 ; public author manuscript https://repository.up.ac.za/bitstream/2263/83538/1/Henry_Optimising_2021.pdf
2. Korner-Nievergelt, F., Behr, O., Brinkmann, R., Etterson, M. A., Huso, M. M. P., Dalthorp, D., et al. (2015), *Mortality estimation from carcass searches using the R-package carcass — a tutorial*, Wildlife Biology **21**, 30–43. https://doi.org/10.2981/wlb.00094
3. Etterson, M. A. (2013), *Hidden Markov models for estimating animal mortality from anthropogenic hazards*, Ecological Applications **23**, 1915–1925. https://doi.org/10.1890/12-1166.1 ; public record https://digitalcommons.unl.edu/usepapapers/325/
4. Published research, *A sharp terminal-clustering threshold for two-visit ecological detection* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-terminal-clustering-threshold-for-two-visit-ecological-d--6b81ba3354e3
5. Published research, *A single reversal threshold for cost-optimal ecological survey duration under persistent Gamma detectability* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-single-reversal-threshold-for-cost-optimal-ecological-survey-d--6ade7c598511
