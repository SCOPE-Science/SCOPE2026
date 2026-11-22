# Sex-ratio symmetry changes the optimal fragmentation scale for redundant mating sites

## Finding

Fix an integer \(r\ge 2\) and a sex fraction \(0<\theta<1\). A total Poisson founder pressure \(L>0\) contains independent male and female counts with means \(\theta L\) and \((1-\theta)L\); each founder independently selects one of \(k\) equally attractive sites. A site is **mating-capable** when at least one founder of each sex arrives. Let \(W_k\) count mating-capable sites and \(k_L^*\) be **any** integer maximizing \(\Pr(W_k\ge r)\) over \(k\ge1\). Then the optimum exists for each \(L>0\), and the following sharp asymptotic dichotomy holds as \(L\to\infty\):

- **Balanced sex composition**, \(\theta=1/2\): every maximizing integer obeys
  \[\frac{k_L^*}{\sqrt L}\longrightarrow\sqrt{\frac{r-1}{2\log2}}.\]
  Moreover, the optimized probability of failing to obtain \(r\) sites satisfies
  \[\log\Pr(W_{k_L^*}<r)=-\frac L2+\sqrt{2(r-1)L\log2}+o(\sqrt L).\]
- **Any fixed imbalance**, \(\theta\ne1/2\): with \(a=\min(\theta,1-\theta)\) and \(\delta=|1-2\theta|>0\), every maximizing integer obeys
  \[\frac{k_L^*\log L}{L}\longrightarrow\delta.\]
  The corresponding optimized failure exponent satisfies
  \[\log\Pr(W_{k_L^*}<r)=-aL+(r-1)\left(1+\frac a\delta\right)\log L+o(\log L).\]

In contrast, for the objective of **at least one** mating-capable site (\(r=1\)), the unique optimal choice is \(k=1\) for every \(L>0\). Thus a requirement for spatially redundant mating sites produces a discontinuous change from square-root to nearly linear optimal fragmentation when the founder sex ratio departs from one-half by any fixed positive amount. The distinct-site objective is essential: it is not total mating-pair count, and mating capability is not an assertion of successful reproduction or population persistence.

## Assumptions and scope

The sites have no carrying-capacity limits, no suitability differences, and no movement between sites after assignment. Male and female arrival processes are independent Poisson variables; all arrivals locate a site, and each selects among \(k\) sites uniformly. The condition of at least one individual of each sex is sufficient to designate a **potential** mating site. The reliability target \(r\ge2\) is fixed while total expected arrival \(L\) increases; the fixed sex fraction \(\theta\) is not permitted to approach \(1/2\) as a function of \(L\). The optimization permits every positive integer \(k\) and does not charge a cost per site. All statements concern the stated idealized stochastic model only.

Put \(t=L/k\) and \(b=1-a\). Independent Poisson splitting gives, exactly,
\[p_k=\Pr(\text{both sexes at a specified site})=(1-e^{-at})(1-e^{-bt}),\qquad W_k\sim\operatorname{Binomial}(k,p_k).\]
Write \(q_k=1-p_k\). The failure probability is
\[G_k(L)=\Pr(W_k<r)=\sum_{j=0}^{r-1}\binom{k}{j}p_k^j q_k^{k-j}\quad(k\ge r);\qquad G_k(L)=1\quad(k<r).\]
The parameter \(\delta=b-a\) is zero exactly in the balanced case.

## Proof

**1. Exact probability and attained optimum.** Independent Poisson thinning and allocation make the male and female counts independent at every site, hence the displayed binomial law. For \(k\ge r\), \(p_k>0\), so \(G_k<1\). Conversely \(p_k\le abL^2/k^2\) because \(1-e^{-x}\le x\). Markov's inequality gives \(\Pr(W_k\ge r)\le kp_k/r\le abL^2/(rk)\to0\). A maximizer therefore exists among finitely many \(k\), and none has \(k<r\). If \(r=1\), every success requires at least one male and female overall, an event equivalent to success at \(k=1\). For \(k>1\), positive probability exists that exactly one male and one female arrive and choose different sites; thus \(k=1\) strictly dominates.

**2. A useful failure exponent.** Define for \(t>0\)
\[h_\delta(t)=\log\big(1+e^{-\delta t}-e^{-bt}\big)=\log\big(1+e^{-\delta t}(1-e^{-at})\big).\]
Then \(h_\delta(t)>0\), and exactly
\[q_k=e^{-at}e^{h_\delta(t)},\qquad\log q_k=-at+h_\delta(t).\]
Two individual terms of the binomial failure tail yield universal lower bounds
\[\log G_k(L)+aL\ge k h_\delta(t)\tag{1}\]
and
\[\log G_k(L)+aL\ge a(r-1)t+(k-r+1)h_\delta(t)+\log\binom{k}{r-1}+(r-1)\log p_k.\tag{2}\]
Here and below \(k\ge r\). For any sequence with \(k\to\infty\), \(t\to\infty\), and \(q_k\to0\), the last summand of the tail dominates: the ratio between each preceding summand and the following one is bounded by a constant depending on \(r\) times \(q_k/(kp_k)\). Therefore
\[\log G_k(L)=(k-r+1)\log q_k+\log\binom{k}{r-1}+(r-1)\log p_k+o(1).\tag{3}\]

**3. Balanced sex composition.** If \(\delta=0\) and \(a=b=1/2\), then \(h_0(t)=\log(2-e^{-t/2})\), which tends to \(\log2\) at infinity. Also there is an absolute \(c>0\) such that \(h_0(t)\ge c\min(t,1)\) for all \(t>0\), by its positive derivative at zero and continuity. At the trial value \(k=\lfloor x\sqrt L\rfloor\), fixed \(x>0\), formula (3) gives
\[\frac{\log G_k(L)+L/2}{\sqrt L}=\frac{r-1}{2x}+x\log2+o(1).\tag{4}\]
The error is uniform for \(x\) in compact subsets of \((0,\infty)\). No maximizing sequence has \(k/\sqrt L\to0\): since \(k\ge r\), (2), \(p_k\to1\), and \(t=L/k\to\infty\) make the normalized correction diverge (the first positive term suffices). No maximizing sequence has \(k/\sqrt L\to\infty\): (1) and \(h_0(t)\ge c\min(t,1)\) imply a normalized correction at least \(c\min(k,L)/\sqrt L\to\infty\). Thus all maximizers lie in a compact positive range after division by \(\sqrt L\). The right side of (4) is strictly minimized at \(x=\sqrt{(r-1)/(2\log2)}\), with minimum \(\sqrt{2(r-1)\log2}\). Uniform convergence, compactness and uniqueness prove both claims for **all** maximizing integers.

**4. Fixed sex-ratio imbalance.** Now \(\delta=b-a>0\). As \(t\to\infty\),
\[h_\delta(t)\sim e^{-\delta t},\qquad p_k\to1.\]
There is \(c_a>0\) such that \(h_\delta(t)\ge c_a t\) for \(0<t\le1\), and \(h_\delta(t)\ge c_a e^{-\delta t}\) for \(t\ge1\), directly from its logarithmic definition. Choose the integer trial \(k=\lfloor\delta L/\log L\rfloor\) (for sufficiently large \(L\)). Then \(t\sim\log L/\delta\), \(k h_\delta(t)=o(1)\), \(p_k\to1\), and (3) gives
\[\log G_k(L)+aL=(r-1)\left(1+\frac a\delta\right)\log L+o(\log L).\tag{5}\]
Fix \(\varepsilon\in(0,1)\). For every rival \(t\le(1-\varepsilon)\log L/\delta\), (1) implies \(\log G_k+aL\gg\log L\): for \(t\le1\), \(kh_\delta(t)\ge c_a L\); for \(1\le t\le(1-\varepsilon)\log L/\delta\), it is at least \(c_a L^\varepsilon/[(1-\varepsilon)\log L/\delta]\). These cannot beat the trial (5). For every rival \(t\ge(1+\varepsilon)\log L/\delta\), necessarily \(p_k\to1\) uniformly and \(\log\binom{k}{r-1}\ge(r-1)\log k-O_r(1)\) for \(k\ge r\). By (2),
\[\log G_k+aL\ge(r-1)\big[a t+\log L-\log t\big]-O_r(1).\]
For large \(L\), \(a t-\log t\) increases throughout this range, and the last lower bound exceeds the trial value (5) by at least \((r-1)a\varepsilon\log L/\delta+o(\log L)\). Consequently every maximizing sequence satisfies \(\delta t/\log L\to1\), or equivalently \(k\log L/L\to\delta\). Applying (2) and (5) on this localized range yields the stated optimal logarithmic failure expansion.

**5. Quantifiers and boundaries.** All asymptotic limits hold with \(r\) and \(\theta\) fixed. The balanced and imbalanced regimes do not assert uniformity when \(\theta\to1/2\) simultaneously with \(L\to\infty\). Integer maximizers need not be unique for finite \(L\); the theorem specifies the asymptotic location of **every** maximizer. The expressions for failure probabilities characterize relative rare-event errors, not observations of established populations.

## Verification

The accompanying executable `verify.py` uses only the Python standard library. Run \`python3 verify.py\` from its directory. It checks the exact binomial tail against a separate probability-generating-polynomial recurrence, compares stable and direct expressions for \(q_k\), tests strict one-site dominance for the \(r=1\) objective, verifies finite optimization against a conservative tail bound, and displays the finite-size optimizer trends and asymptotic rescalings. Numerical tests do not constitute the proof of the infinite-parameter statements, which is the analytic argument above.

## Relationship to prior work

Chase, Kelly, Liebhold and Brockerhoff (first publicly available 2022-11-01) experimentally document propagule pressure and Allee effects in bark beetle colonization; they do not optimize the count of distinct two-sex sites. Cuddington, Hull, Currie and Koops (2015) study mate-finding at landmarked sites, including the exact finite distribution of pairs and the effects of landmark count on mating; they do not give the present fixed-Poisson-pressure \(r\)-distinct-site rare-event optimizer or its balanced-to-imbalanced asymptotic transition. Koontz, Oldfather, Melbourne and Hufbauer (2018) compare temporal introduction number and size in experiments and simulations, a different objective and model. Dupuis, Nuzman and Whiting (2007) prove a colored-ball occupancy large-deviations principle in a proportional ball-to-box asymptotic regime, not the optimized rare-event site-count scaling here. The binomial-thinning calculation, elementary entropy bounds and asymptotic optimization tools themselves are standard; this theorem is not a claim to invent those ingredients.

## Limitations

A site with founders of both sexes need not yield offspring, and achieving at least \(r\) such sites need not produce \(r\) self-sustaining populations. No allowance is made for density-dependent recruitment, dispersal mortality, mate-search distance, habitat quality, finite site capacities, predation, environmental correlation, mating system or intervention cost. A small sex-ratio bias that shrinks with \(L\) has an unexamined crossover regime. Historical mathematical priority remains provisional pending wider comparison, particularly literature on extreme occupancy tails and spatial mating kernels. This result should not be used as a quantitative field recommendation without model validation.

## References

- Chase, K. D., Kelly, D., Liebhold, A. M., and Brockerhoff, E. G. (2023), *The role of propagule pressure in experimental bark beetle invasions*, Journal of Applied Ecology 60, 342–352; first public accepted manuscript 2022-11-01. https://doi.org/10.1111/1365-2664.14326
- Cuddington, K., Hull, Z. T., Currie, W. J. S., and Koops, M. A. (2015), *Landmarking and strong Allee thresholds*, Theoretical Ecology 8, 333–347. https://doi.org/10.1007/s12080-015-0254-z
- Koontz, M. J., Oldfather, M. F., Melbourne, B. A., and Hufbauer, R. A. (2018), *Parsing propagule pressure: Number, not size, of introductions drives colonization success in a novel environment*, Ecology and Evolution 8, 8043–8054. https://doi.org/10.1002/ece3.4226
- Dupuis, P., Nuzman, C., and Whiting, P. (2007), *Large deviations principle for occupancy problems with colored balls*, Journal of Applied Probability 44, 115–141. https://doi.org/10.1239/jap/1175267167
