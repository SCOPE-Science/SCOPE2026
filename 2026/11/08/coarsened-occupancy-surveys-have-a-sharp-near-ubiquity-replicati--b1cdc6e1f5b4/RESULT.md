# Coarsened occupancy surveys have a sharp near-ubiquity replication phase

## Finding

Repeated presence–absence visits at independent ecological sites may be retained as complete binary histories or compressed to a single flag indicating whether the species was ever detected. These reporting choices have different optimal replication laws, even with exactly calibrated test characteristics.

Fix true-positive detection probability \(p\), false-positive probability \(f\), and site occupancy \(\psi\), with \(0<f<p<1\) and \(0<\psi<1\). Put \(a=1-p\), \(b=1-f\), and \(\varepsilon=1-\psi\). For \(t\ge1\) independent visits per site, let \(t_{\mathrm{OR}}(\psi)\) denote **any** integer maximizing Fisher information per site-visit when only the ever-detected flag is retained. Let \(t_{\mathrm{full}}(\psi)\) analogously denote any maximizing integer when the full binary history is retained.

**Coarsening phase theorem.** The maximizing integers exist for every \(0<\psi<1\), and as \(\psi\uparrow1\):

1. If \(1-p\ge(1-f)^2\), all \(t_{\mathrm{OR}}(\psi)\) remain uniformly bounded. If \(1-p<(1-f)^2\), all diverge, with
   \[
   t_{\mathrm{OR}}(\psi)=\frac{\log(1/\varepsilon)}{\log((1-f)/(1-p))}+O(1).
   \]
2. For **every** \(0<f<p<1\), all \(t_{\mathrm{full}}(\psi)\to\infty\). In particular, when \(p\le2f-f^2\), retaining full histories changes a bounded near-ubiquity optimal replication count into a divergent one.
3. The divergent OR regime has a sharp, integer-lattice-sensitive variance law. Define
   \[
   \lambda=\log(b/a),\quad \mu=-\log b,\quad \nu=\log(b^2/a)>0,\quad L=\log(1/\varepsilon),
   \]
   and the continuous, positive, one-periodic function
   \[
   \Phi(\theta)=\min_{j\in\mathbb Z}\left(e^{\mu(j-\theta)}+e^{-\nu(j-\theta)}\right).
   \]
   If \(H_t\) is the exact variance coefficient per site-visit of the untruncated unbiased estimator based on OR flags, then
   \[
   \min_{t\ge1}H_t=\frac{L}{\lambda}\,\varepsilon^{\nu/\lambda}\left(\Phi(\{L/\lambda\})+o(1)\right).
   \]
   The additive error \(o(1)\) is uniform in the fractional lattice phase.

The threshold is equivalent to \(p>2f-f^2\) for diverging OR replication; equality belongs to the bounded regime.

## Assumptions and scope

Each site has an independent fixed latent occupancy state \(Z\sim\operatorname{Bernoulli}(\psi)\). Conditional on \(Z=1\), successive visits independently report positive with probability \(p\); conditional on \(Z=0\), they independently report positive with probability \(f\). Sites are independent. The rates \(p,f\) are known from external calibration and remain fixed as \(\psi\uparrow1\). All visits have identical unit cost; one compares information about \(\psi\) per visit while the number of sampled sites adjusts to the visit budget. Full histories retain each binary response; the OR flag retains only whether at least one response was positive. No estimator of \(p\) or \(f\) is included in the objective.

The statements concern finite \(t\) for each \(\psi<1\), followed by the near-ubiquity limit \(\psi\uparrow1\). A fixed finite field budget cannot support arbitrarily growing replication with a growing number of sites; the result is a local design/information limit, not a finite-budget performance guarantee.

## Proof

**1. Exact OR observation and information.** The probability of no positive response at a site is
\[
 u_t=\psi a^t+(1-\psi)b^t=b^t\bigl[\varepsilon+(1-\varepsilon)e^{-\lambda t}\bigr].
\]
The OR flag is Bernoulli with mean \(1-u_t\), and its derivative with respect to \(\psi\) is \(b^t-a^t=:\Delta_t\). Its Fisher information is therefore
\[
 I_t^{\mathrm{OR}}(\psi)=\frac{\Delta_t^2}{u_t(1-u_t)}.
\]
For \(N\) sites, the untruncated estimator \(\widehat\psi=(\overline Y_t-(1-b^t))/\Delta_t\) is unbiased and has exact variance \(u_t(1-u_t)/(N\Delta_t^2)\). Under a budget of \(B=Nt\) visits this equals \(H_t/B\), where
\[
 H_t=\frac{t u_t(1-u_t)}{(b^t-a^t)^2}.
\]
Thus minimizing \(H_t\) is exactly equivalent to maximizing information per visit. For every fixed \(\varepsilon>0\), as \(t\to\infty\), \(u_t\sim\varepsilon b^t\) and \(\Delta_t\sim b^t\), so \(I_t^{\mathrm{OR}}/t\sim b^t/(t\varepsilon)\to0\). A finite optimum exists.

**2. Sharp OR phase.** For fixed \(t\), as \(\varepsilon\downarrow0\), \(I_t^{\mathrm{OR}}/t\) tends to its boundary expression \(\Delta_t^2/[t a^t(1-a^t)]\), asymptotic for large \(t\) to \((b^2/a)^t/t\). If \(a<b^2\), these boundary scores diverge with \(t\). By their continuity in \(\varepsilon\) for each fixed \(t\), no uniformly bounded sequence of maximizers is possible.

If \(a\ge b^2\), then for \(0<\varepsilon\le1/2\), the inequalities \(u_t\ge\psi a^t\), \(1-u_t\ge1-b^t\ge1-b\), and \(\Delta_t\le b^t\) give
\[
 \frac{I_t^{\mathrm{OR}}}{t}\le\frac{(b^2/a)^t}{t\psi(1-b)}\le\frac{2}{t(1-b)}.
\]
The \(t=1\) score has a positive limit as \(\varepsilon\downarrow0\); hence all optimal \(t\) are bounded, also at equality \(a=b^2\).

**3. Sharp logarithmic/lattice law.** Suppose \(a<b^2\), so \(\nu=\lambda-\mu>0\). The exact algebraic rearrangement is
\[
 H_t=t\,\frac{\varepsilon e^{\mu t}+(1-\varepsilon)e^{-\nu t}}{(1-e^{-\lambda t})^2}
 \bigl[1-b^t\bigl(\varepsilon+(1-\varepsilon)e^{-\lambda t}\bigr)\bigr].
\]
Writing \(x=L/\lambda\), choose any integer \(t=x+O(1)\). Uniformly for bounded \(t-x\), both correction factors tend to one and
\[
 H_t=\frac{L}{\lambda}\varepsilon^{\nu/\lambda}
 \left(e^{\mu(t-x)}+e^{-\nu(t-x)}\right)(1+o(1)).
\]
To justify optimizing within this window rather than merely estimating candidate designs, fix sufficiently large \(T\). For \(t\ge T\), the exact expression is bounded above and below by fixed positive multiples of \(t(\varepsilon e^{\mu t}+e^{-\nu t})\). The candidate \(t=\lfloor x\rfloor\) has cost \(O(L\varepsilon^{\nu/\lambda})\). For \(t\ge x+R\), the first summand grows at least like \(L\varepsilon^{\nu/\lambda}e^{\mu R}\); for \(T\le t\le x-R\), choose \(T>1/\nu\), and the decreasing function \(t e^{-\nu t}\) shows that the second summand costs at least a fixed multiple of \(L\varepsilon^{\nu/\lambda}e^{\nu R}\), for \(R\) fixed and \(\varepsilon\) sufficiently small. Each \(t<T\) has a strictly positive boundary cost while the candidate cost vanishes. Taking \(R\) large excludes every point outside \(|t-x|\le R\) from the optimum. Thus each minimizing integer is \(x+O(1)\).

All minimizing integers now lie in this bounded window. Write \(t=\lfloor x\rfloor+j\); then \(t-x=j-\{x\}\). Minimize the uniform expansion over the finitely many relevant \(j\), equivalently over all integers because its two exponential tails diverge. This proves the displayed \(\Phi\) formula. The minimum of continuous functions with coercive tails is a continuous, positive, one-periodic function of the fractional part.

**4. Full-history phase.** For an observed binary history \(y\in\{0,1\}^t\) with \(k\) positives, write \(P_p(y)=p^k a^{t-k}\) and \(P_f(y)=f^k b^{t-k}\). The exact Fisher information about \(\psi\) is
\[
 I_t^{\mathrm{full}}(\psi)=\sum_{y\in\{0,1\}^t}
 \frac{(P_p(y)-P_f(y))^2}{\psi P_p(y)+(1-\psi)P_f(y)}.
\]
At the one-sided boundary \(\psi=1\), this is the chi-squared identity
\[
 I_t^{\mathrm{full}}(1)=\sum_y\frac{P_f(y)^2}{P_p(y)}-1
 =\left(\frac{f^2}{p}+\frac{(1-f)^2}{1-p}\right)^t-1=K^t-1,
\]
with \(K>1\) by strict Cauchy–Schwarz because \(p\ne f\). Thus \(I_t^{\mathrm{full}}(1)/t\to\infty\). For \(\psi\in(0,1)\), the latent Bernoulli occupancy state has information \(1/[\psi(1-\psi)]\), and the score of any observed history is the conditional expectation of the complete-state score. Jensen's inequality gives \(I_t^{\mathrm{full}}(\psi)\le1/[\psi(1-\psi)]\). So \(I_t^{\mathrm{full}}(\psi)/t\to0\) at fixed \(\psi<1\), proving a finite maximizer exists. Given any finite cutoff \(M\), choose a finite \(t>M\) whose boundary score per visit exceeds every boundary score at \(1\le s\le M\). Continuity at \(\psi=1\) carries the strict comparison to all sufficiently near-one \(\psi\). Every full-history maximizer therefore exceeds \(M\), proving divergence.

For \(t\ge2\), the OR flag is a strict data processing of the history: positive histories with different numbers of detections have different likelihood ratios. Hence \(I_t^{\mathrm{full}}(\psi)>I_t^{\mathrm{OR}}(\psi)\) for every \(0<\psi<1\); equality holds for \(t=1\). This last point explains why the reporting choice has a genuine information effect.

## Verification

The standalone Python 3 script `checker.py` performs exact rational probability summation across all binary histories for several rational \((p,f)\), checks both Fisher formulas, the boundary chi-squared identity, the strict information inequality, and the unbiased estimator's exact variance. It also computes near-boundary optimizers and checks their logarithmic window and lattice-phase approximation in both regimes. Run with `python3 checker.py` from the directory containing this document. The completed test returned `PASS 191 exact and numerical assertions`. All global and asymptotic claims are supported by the proof above; finite tests are not substituted for it.

For illustration, with \(p=3/5\), \(f=1/10\), near-ubiquity values \(\varepsilon=10^{-4}\) and \(10^{-8}\) give optimal OR repetitions 13 and 25, respectively, from direct finite computation. With \(p=4/5\), \(f=3/5\), OR optimizers remain at one visit for those same two prevalence levels; full-history information can instead favor many repeats. These calculations are examples, not blanket finite-parameter design recommendations.

## Relationship to prior work

The Royle–Link false-positive occupancy model (2006) and later work on confirmed/unconfirmed observations establish the ecological relevance of missed and spurious detections. Guillera-Arroita, Ridout and Morgan (2010) analyze occupancy survey design and the site-versus-revisit tradeoff, in a different inference setting. Clement (2016) numerically optimizes more elaborate models with unknown detection characteristics and full detection histories, whereas the present result holds fixed calibrated detection rates and compares exact one-bit OR aggregation with full retention in the near-ubiquity limit. Ferguson, Conroy and Hepinstall-Cymerman (2015) study false-positive heterogeneity and confirmation protocols, rather than the stated coarsening phase. Recent repeated-test prevalence work gives general aggregation formulae, but the precise near-ubiquity integer-optimization transition, its logarithmic law and the contrast between full histories and OR flags are the investigated contributions.

The mathematically close McClish–Quade (1985) study of repeated screening tests and prevalence-estimation costs is a priority risk: only its bibliographic abstract was accessible, not its full paper. Its possible treatment of the precise near-boundary replication limit could not be excluded. No claim of exhaustive historical priority or independent certification is made.

## Limitations

This is an exact theorem for independent visits conditional on stable occupancy, with known, fixed \(p\) and \(f\), unit visit cost and independent sampled sites. Uncalibrated detection parameters, dependence between visits, changing site occupancy, site-specific heterogeneity, overhead travel costs, incomplete sampling, and finite-population correction can alter the optimal design. The estimator may fall outside \([0,1]\) at finite sample size because it is intentionally left untruncated for exact unbiasedness and variance algebra. The information limit near \(\psi=1\) is one-sided and does not imply one can collect infinitely many visits per site under a fixed budget. The work concerns information about prevalence, not classification accuracy at an individual site, nor direct management benefit. Historical priority remains provisional because the 1985 paper was not fully accessible.

## References

- Royle, J. A. and Link, W. A. (2006), *Generalized site occupancy models allowing for false positive and false negative errors*, Ecology 87, 835–841. https://doi.org/10.1890/0012-9658(2006)87[835:GSOMAF]2.0.CO;2
- Guillera-Arroita, G., Ridout, M. S. and Morgan, B. J. T. (2010), *Design of occupancy studies with imperfect detection*, Methods in Ecology and Evolution 1, 131–139. https://doi.org/10.1111/j.2041-210X.2010.00017.x
- Ferguson, P. F. B., Conroy, M. J. and Hepinstall-Cymerman, J. (2015), *Occupancy models for data with false positive and false negative errors and heterogeneity across sites and surveys*, Methods in Ecology and Evolution 6, 1395–1406. https://doi.org/10.1111/2041-210X.12442
- Clement, M. J. (2016), *Designing occupancy studies when false-positive detections occur*, Methods in Ecology and Evolution 7, 1538–1547. https://doi.org/10.1111/2041-210X.12617
- McClish, D. and Quade, D. (1985), *Improving estimates of prevalence by repeated testing*, Biometrics 41, 81–89. https://doi.org/10.2307/2530645 (abstract inspected; full text unavailable).
- Böttcher and collaborators (2025), *Determining the Optimal Sequence of Multiple Tests*, Statistics in Medicine. https://doi.org/10.1002/sim.70254 (relevant later general framework; full text partly accessible).
