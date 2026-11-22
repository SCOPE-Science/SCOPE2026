# A three-regime symmetry-breaking law for spaced thermal-stress challenges

## Finding

**Theorem (complete fixed-endpoint three-challenge phase diagram).** Let \(0<\alpha<\beta\), \(P,D>0\), and \(T>0\). Consider three idealized identical instantaneous challenges administered in their stated order at \(t_1=0\), \(t_2=t\in[0,T]\), and \(t_3=T\). The log-hazard at challenge \(j\) is
\[
h_j=h_0+\sum_{i<j}\left[D e^{-\beta(t_j-t_i)}-P e^{-\alpha(t_j-t_i)}\right],\qquad h_0>2P.
\]
Conditional on reaching each challenge, the subject survives it with probability \(e^{-h_j}\). Therefore total three-challenge survival is \(\exp(-\sum_{j=1}^3h_j)\). Define the fast-injury/slow-priming ratio \(q=D/P\) and the exact boundaries
\[
q_{\mathrm e}(T)=\frac{\alpha}{\beta}\frac{1-e^{-\alpha T}}{1-e^{-\beta T}},\qquad
q_{\mathrm c}(T)=\left(\frac{\alpha}{\beta}\right)^2 e^{(\beta-\alpha)T/2}.
\]
For every \(T>0\), \(0<q_{\mathrm e}(T)<q_{\mathrm c}(T)\), and **all global survival-maximizing schedules** are as follows:

1. If \(0<q\le q_{\mathrm e}(T)\), exactly the two endpoint clusters \(t=0,T\) are optimal.
2. If \(q_{\mathrm e}(T)<q<q_{\mathrm c}(T)\), exactly two distinct interior times \(t=T/2\pm z_*\) are optimal, where \(0<z_*<T/2\) is the unique root of
\[
\frac{\sinh(\beta z_*)}{\sinh(\alpha z_*)}=
\frac{\alpha}{q\beta}e^{(\beta-\alpha)T/2}.
\]
3. If \(q\ge q_{\mathrm c}(T)\), exactly the midpoint \(t=T/2\) is optimal.

In particular, put \(q_0=(\alpha/\beta)^2\) and \(q_\infty=\alpha/\beta\). If \(q\le q_0\), endpoint clustering is optimal at every positive horizon. If \(q_0<q<q_\infty\), increasing \(T\) produces **exactly three successive regimes**: a unique midpoint until
\[
T_{\mathrm c}=\frac{2\log(q/q_0)}{\beta-\alpha},
\]
then two off-center interior optima until the unique \(T_{\mathrm e}>T_{\mathrm c}\) satisfying \(q=q_{\mathrm e}(T_{\mathrm e})\), then the two endpoint clusters. At \(T=T_{\mathrm c}\) the midpoint remains the sole optimum; at \(T=T_{\mathrm e}\) only the two endpoint clusters are optimal. If \(q\ge q_\infty\), the midpoint-to-paired-interior transition occurs at \(T_{\mathrm c}\), but there is no finite endpoint-clustering transition. For \(q>q_\infty\), the smaller interior optimum tends to \(\log(q\beta/\alpha)/(\beta-\alpha)\) as \(T\to\infty\), and for \(q=q_\infty\) it tends to zero.

The symmetry-breaking onset is quantitative: as \(T\downarrow T_{\mathrm c}\) from above for \(q>q_0\),
\[
\left|t_*(T)-T/2\right|=
\sqrt{\frac{3(T-T_{\mathrm c})}{\alpha+\beta}}+O\big((T-T_{\mathrm c})^{3/2}\big).
\]
Thus the two interior optima branch from the midpoint with a universal square-root coefficient depending only on the two memory-decay rates.

## Assumptions and scope

The two post-challenge memories are additive, identical after each challenge, independent of challenge order except through elapsed time, and exponentially relaxing. The faster decaying memory \(D e^{-\beta s}\) is harmful (injury/sensitization), while the slower decaying \(P e^{-\alpha s}\) is beneficial (priming/acclimation). The conditional log-hazard is an *assumed* mathematical link, not an empirically identified coral-survival law. The baseline \(h_0>2P\) ensures every conditional hazard is positive, including when two challenges are immediately successive. At \(t=0\) or \(t=T\), the order of the two immediate challenges is retained and their zero-rest limit is allowed. No constraint on a minimum interchallenge rest time is imposed.

The theorem concerns maximization of the probability of surviving **all three challenges**, not the health of survivors or the extinction risk of a coral population. Rates are measured in units reciprocal to the time coordinate; \(q\) is dimensionless. Species heterogeneity, genetic selection, interval-dependent dosages, seasonal temperature trajectories, slow non-exponential recovery, treatment harms beyond the three modeled hazards, and stochastic memory variation are outside the model.

## Proof

**Step 1: Exact cost reduction.** The log of total survival differs by an overall negative sign from the sum of three nonnegative hazards. Expanding the three pairwise histories and removing the constant \(3h_0+D e^{-\beta T}-P e^{-\alpha T}\), maximizing survival is exactly equivalent to minimizing
\[
F_T(t)=D\left(e^{-\beta t}+e^{-\beta(T-t)}\right)
-P\left(e^{-\alpha t}+e^{-\alpha(T-t)}\right)
\]
over \(0\le t\le T\). The function is symmetric under \(t\mapsto T-t\).

**Step 2: One-crossing derivative on a half-interval.** Write \(z=|t-T/2|\in[0,T/2]\). Then
\[
F_T(z)=2D e^{-\beta T/2}\cosh(\beta z)-2P e^{-\alpha T/2}\cosh(\alpha z)
\]
(up to the already omitted constant). For \(z>0\), its derivative has the sign of
\[
R(z)-K_T,\qquad R(z)=\frac{\sinh(\beta z)}{\sinh(\alpha z)},\qquad K_T=\frac{\alpha}{q\beta}e^{(\beta-\alpha)T/2}.
\]
Crucially \(R\) increases strictly for every \(z>0\). Indeed,
\[
\frac{R'(z)}{R(z)}=\beta\coth(\beta z)-\alpha\coth(\alpha z)>0,
\]
since \(u\mapsto u\coth(uz)\) has derivative \(\big(\sinh(uz)\cosh(uz)-uz\big)/(\sinh^2(uz))>0\). The numerator is positive because its derivative with respect to \(uz\) is \(2\sinh^2(uz)>0\) and it vanishes at zero. Thus the derivative of \(F_T\) on \((0,T/2)\) changes sign **at most once**, and only from negative to positive. The limits are \(R(0+)=\beta/\alpha\) and \(R(T/2)=\sinh(\beta T/2)/\sinh(\alpha T/2)\).

**Step 3: Exact global regime boundaries and equality cases.** The derivative is nonnegative throughout the half-interval exactly when \(K_T\le\beta/\alpha\), equivalent to \(q\ge q_{\mathrm c}(T)\); then the center is the unique minimizer, including equality. It is nonpositive throughout exactly when \(K_T\ge R(T/2)\), equivalent to \(q\le q_{\mathrm e}(T)\); then the outer edge is the unique half-interval minimizer, including equality. Otherwise it changes from negative to positive exactly once at \(z_*\in(0,T/2)\). Reflection proves the two distinct interior global minimizers and that there are no further ones. Since \(R(T/2)>R(0+)\) for \(T>0\), \(q_{\mathrm e}(T)<q_{\mathrm c}(T)\).

**Step 4: Horizon classification.** The function \(q_{\mathrm c}\) increases strictly from \(q_0\) to infinity. Also \(q_{\mathrm e}\) increases strictly from \(q_0\) to \(q_\infty\), because
\[
\frac{d}{dT}\log q_{\mathrm e}(T)
=\frac{\alpha}{e^{\alpha T}-1}-\frac{\beta}{e^{\beta T}-1}>0.
\]
The last inequality follows from strict decrease of \(u/(e^{uT}-1)\) in \(u>0\). Its derivative has numerator \(e^{uT}-1-uT e^{uT}<0\), the latter inequality following from the derivative of \(1-e^{-v}-v<0\) for \(v>0\). The two strict ranges and \(q_{\mathrm e}(T)<q_{\mathrm c}(T)\) establish every stated horizon transition, including \(T_{\mathrm c}<T_{\mathrm e}\) where the second exists.

**Step 5: Symmetry-breaking and far-horizon limits.** For small positive \(z\),
\[
R(z)=\frac{\beta}{\alpha}\left[1+\frac{\beta^2-\alpha^2}{6}z^2+O(z^4)\right].
\]
At \(T=T_{\mathrm c}+\varepsilon\), \(K_T=(\beta/\alpha)e^{(\beta-\alpha)\varepsilon/2}\). Equating and using analyticity in \(z^2\) gives \(z^2=3\varepsilon/(\alpha+\beta)+O(\varepsilon^2)\), and hence the claimed square-root law. For \(q\ge q_\infty\), the smaller optimum \(t_*(T)\) is unique on \((0,T/2)\) for all large \(T\). The derivative of \(F_T\) at fixed \(t>0\) tends to \(-D\beta e^{-\beta t}+P\alpha e^{-\alpha t}\), whose sign changes once at \(t_\infty=\log(q\beta/\alpha)/(\beta-\alpha)\) when \(q>q_\infty\). For every fixed \(\varepsilon>0\), the derivative is eventually negative at \(t_\infty-\varepsilon\) (when positive) and positive at \(t_\infty+\varepsilon\); uniqueness confines the optimizer between them. When \(q=q_\infty\), the limiting derivative is positive at every fixed \(t>0\), so the smaller optimum tends to zero. This completes the global classification.

## Verification

A standalone Python 3 script, `checker.py`, reproduces the exact witness and explores boundary and interior cases using only the standard library. It tested 7,000 independent parameter designs against 455,000 grid comparisons; it also checked the exact transition identities, square-root onset, long-horizon location, and positivity of illustrative hazards. These finite computations supplement but do not substitute for the analytic uniqueness proof above.

For \(\alpha=1\), \(\beta=3\), and \(q=1/5\), the sharp horizon thresholds are exactly
\[
T_{\mathrm c}=\log(9/5)\approx0.587786664902119,\qquad
T_{\mathrm e}=\log\left(\frac{6}{\sqrt{33}-3}\right)\approx0.782137734269056.
\]
At \(T=0.3\), only \(t=0.15\) maximizes survival; at \(T=0.7\), the two optima are \(t\approx0.055825985792\) and \(t\approx0.644174014208\); at \(T=1\), only the two endpoint clusters \(t=0,1\) maximize survival. With \(h_0=3\) and \(P=1\), all illustrative conditional hazards are positive.

Run: `python3 checker.py` from the extracted standalone artifact directory. The script is not a formal proof certificate or independent validation.

## Relationship to prior work

The field study by Brown and colleagues (2023, *Ecology and Evolution*) documents both ecological memory/thermal tolerance and the possibility of sensitization and trade-offs after repeated marine heatwaves. Brown and colleagues (2023, *PNAS*) document divergent acclimatization and recovery in individual coral colonies. Neither inspected study states the artificial two-exponential three-challenge survival model or its global three-regime timing classification. Wesener and Tietjen (2019) analyze earlier, faster, or stronger microbial stress-priming responses with a nonlinear population ODE; their optimization questions and objective differ. McLachlan and colleagues (2020) review experimental heat-stress design variability, not the present global extremum. Pla-Mauri and Solé (2026) examine a single-memory genetic-circuit massed-versus-spaced effect, using a thresholded gene-expression observable, not a competing fast-injury/slow-priming pair with fixed endpoints. These analogies motivate the question but do not establish priority; mathematical hyperbolic-function monotonicity and the exponential-memory ansatz themselves are standard.

## Limitations

The finding is conditional on the stated hazard law, not a claim that any real coral species obeys it. It does not infer numerical ecological parameters from the empirical studies. Multiple responses, adaptation shifts across genotypes, selection by earlier events, delayed or non-exponential damage, noisy observation, and fixed minimum rest times could change the optimum. The boundary schedules may be physically unrealizable as separate heatwave exposures; they are mathematically well-defined immediate-sequence limits. A full historical search outside the accessible papers remains necessary before making an absolute priority assertion. No independent audit or experimental validation has been performed.

## References

1. Brown, K. T., Genin, A., Mello-Athayde, M. A., et al. (2023). *Marine heatwaves modulate the genotypic and physiological responses of reef-building corals to subsequent heat stress*. Ecology and Evolution 13, e10798. First published 2023-12-13. https://doi.org/10.1002/ece3.10798
2. Brown, K. T., Lenz, E. A., Glass, B. H., et al. (2023). *Divergent bleaching and recovery trajectories in reef-building corals following a decade of successive marine heatwaves*. PNAS 120, e2312104120. Published 2023-12-19. https://doi.org/10.1073/pnas.2312104120
3. Wesener, F. and Tietjen, B. (2019). *Primed to be strong, primed to be fast: modeling benefits of microbial stress responses*. FEMS Microbiology Ecology 95, fiz114. https://doi.org/10.1093/femsec/fiz114
4. McLachlan, R. H., Price, J. T., Solomon, S. L. and Grottoli, A. G. (2020). *Thirty years of coral heat-stress experiments: a review of methods*. Coral Reefs 39, 885–902. https://doi.org/10.1007/s00338-020-01931-9
5. Pla-Mauri, J. and Solé, R. (2026). *Engineering basal cognition: minimal genetic circuits for habituation, sensitization, and massed–spaced learning*. ACS Synthetic Biology 15, 716–727. https://doi.org/10.1021/acssynbio.5c00766
