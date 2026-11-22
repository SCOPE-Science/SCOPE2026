# Reentrant equal spacing in a two-opportunity seed-bank rescue model

## Finding

Fix a positive horizon \(T\), rate \(\lambda>0\), and peak-success parameter \(0<\kappa\le4\). Two independent, exchangeable regeneration opportunities have durations \(t\) and \(T-t\), where \(0\le t\le T\). Their individual success probability is
\[
p_\kappa(u)=\kappa e^{-\lambda u}\left(1-e^{-\lambda u}\right).
\]
The probability that at least one succeeds is
\[
R_{\kappa,\lambda,T}(t)=1-\left[1-p_\kappa(t)\right]\left[1-p_\kappa(T-t)\right].
\]
A duration of zero denotes skipping the corresponding opportunity, not conducting two simultaneous fires. Define
\[
T_0=\lambda^{-1}\log(\kappa-2)\quad(\kappa>3),\qquad
T_1=2\lambda^{-1}\log\left(2-\sqrt{4-\kappa}\right)\quad(\kappa>3),\qquad
T_2=2\lambda^{-1}\log\left(2+\sqrt{4-\kappa}\right).
\]
The **complete global maximizer classification**, with every boundary included, is:

- If \(0<\kappa\le3\), exactly \(t=T/2\) maximizes for \(0<T\le T_2\). For \(T>T_2\), precisely two unequal, exchanged allocations maximize.
- If \(3<\kappa<4\), the maximizers are exactly \(t=0,T\) for \(0<T\le T_0\), exactly two distinct unequal interior allocations for \(T_0<T<T_1\), exactly \(t=T/2\) for \(T_1\le T\le T_2\), and exactly two distinct unequal interior allocations for \(T>T_2\). Here \(0<T_0<T_1<T_2\).
- If \(\kappa=4\), the endpoint and interior regimes above still hold with \(T_0=\lambda^{-1}\log2\) and \(T_1=T_2=2\lambda^{-1}\log2\). The equal allocation is optimal only at that isolated threshold in the subsequent interior range. In fact, every maximizer for \(T>T_0\) has one opportunity lasting \(\lambda^{-1}\log2\), giving success probability one.

The two interior allocations are explicit. Put \(q=e^{-\lambda T}\), \(s_*=(1+\kappa q)/2\) and
\[
x_\pm=\frac{s_*\pm\sqrt{s_*^2-4q}}2.
\]
Then \(t=-\lambda^{-1}\log x_+\) or \(t=-\lambda^{-1}\log x_-\); these are exchanged about \(T/2\). The second root is strictly positive and both correspond to positive durations whenever the solution is interior.

**Reentrance:** for every \(3<\kappa<4\), equal spacing first loses to a single nonzero opportunity, then is restored as the unique optimum on a nonempty intermediate interval, before breaking again at long horizons. For example, with \(\kappa=3.5\), \(\lambda=1\), the three boundaries are approximately \(0.4054651081\), \(0.5137650246\), and \(1.9917609123\). At \(T=0.45\), the optimal durations are approximately \((0.0716422124,0.3783577876)\); at \(T=1\), they are \((0.5,0.5)\); and at \(T=3\), approximately \((0.7249845563,2.2750154437)\). All numerical values are illustrative, not field estimates.

## Assumptions and scope

The two successful-regeneration indicators are independent conditional on the chosen durations and have identical probability law. The bell-shaped probability is an idealized product of a maturation-by-time factor \(1-e^{-\lambda u}\) and a viability-through-time factor \(e^{-\lambda u}\), scaled by \(\kappa\). Its maximum is \(\kappa/4\le1\). These are separate cohorts/opportunities, not a linked demographic population whose success at one fire changes the next. The total elapsed time is conserved, the environment is homogeneous, and the endpoint \(t=0\) means omitting one opportunity. The claim is only about this exact model and objective; no rate or parameter is fitted to a particular species.

## Proof

Let \(x=e^{-\lambda t}\), \(y=e^{-\lambda(T-t)}\) and \(q=e^{-\lambda T}\in(0,1)\). Then \(xy=q\), \(x,y\in[q,1]\), and \(s=x+y\) covers exactly the interval \([2\sqrt q,1+q]\). The lower endpoint occurs only at \(t=T/2\), the upper endpoint only at \(t=0,T\), and each strict interior value gives exactly two exchanged allocations. Since \(0<\kappa\le4\), each factor \(1-\kappa x(1-x)\) is a probability of failure.

The exact factorization is
\[
\begin{aligned}
1-R_{\kappa,\lambda,T}(t)
&=\left(1-\kappa x+\kappa x^2\right)\left(1-\kappa y+\kappa y^2\right)\\
&=\kappa s^2-\kappa(1+\kappa q)s+1+(\kappa^2-2\kappa)q+\kappa^2q^2\\
&=\kappa\left(s-\frac{1+\kappa q}{2}\right)^2+C_{\kappa,q},
\end{aligned}
\]
where \(C_{\kappa,q}=1+(\kappa^2-2\kappa)q+\kappa^2q^2-\kappa(1+\kappa q)^2/4\). Thus the unique minimizing value of \(s\) is precisely the projection of \(s_0=(1+\kappa q)/2\) onto \([2\sqrt q,1+q]\). This proves the root formula and excludes every unlisted global optimum without derivative heuristics or numerical search.

The projection lies at the upper boundary precisely when \((\kappa-2)q\ge1\). This occurs for a positive horizon precisely when \(\kappa>3\) and \(T\le\lambda^{-1}\log(\kappa-2)=T_0\). It lies at the lower boundary precisely when \(\kappa q-4\sqrt q+1\le0\). Setting \(r=\sqrt q\) gives \(\kappa r^2-4r+1\le0\), whose roots are
\[
r_-=(2+\sqrt{4-\kappa})^{-1},\qquad r_+=(2-\sqrt{4-\kappa})^{-1}.
\]
For \(0<\kappa\le3\), \(r_+\ge1\), hence the lower boundary applies exactly for \(T\le T_2\). For \(3<\kappa<4\), both roots lie strictly between zero and one, hence it applies exactly for \(T_1\le T\le T_2\). At \(\kappa=4\) the roots coincide at \(1/2\), giving a sole equal optimum at \(T=2\lambda^{-1}\log2\). For \(3<\kappa<4\), \(T_0<T_1\) because at \(T=T_0>0\), the vertex equals \(1+q>2\sqrt q\), while it first reaches the lower boundary at \(T=T_1\). Outside these disjoint ranges the vertex is strictly inside the admissible interval and yields exactly the two stated unequal allocations. No other ties exist, completing the classification.

As \(T\to\infty\) for fixed \(0<\kappa\le4\), the interior vertex tends to \(1/2\), the larger root tends to \(1/2\), and the shorter optimal interval tends to \(\lambda^{-1}\log2\). This limiting short interval is independent of \(\kappa\). At an equal-to-asymmetric threshold for \(\kappa<4\), the two solutions coalesce continuously, since the root discriminant vanishes there; the optimal set changes by a square-root splitting, not a jump.

## Verification

Run `python verify.py` with Python 3 and no third-party packages. The supplied checker tests the quadratic identity, boundary cases, all four qualitative regimes, exchanged roots and the optimization inequality against deterministic grids and seeded random allocations. It reported `ASSERTIONS_PASSED 204786`. These are supplementary finite arithmetic checks; the preceding algebra proves the uncountable-parameter statement. Boundary float computations do not replace exact root inequalities.

## Relationship to prior work

Plumanns Pouton et al. (2024) report seedbank occurrence patterns under different fire histories, documenting the need to account for both long and short return intervals. McCarthy, Possingham and Gill (2001) already optimize prescribed burning using a stochastic demographic dynamic program; their age/abundance-state-dependent objective is not this two-independent-cohort fixed-horizon failure-product problem. Tucker and Cadotte (2013) study how stochastic variation of fire returns affects coexistence of seeders and resprouters with a Gaussian seeder-recruitment response, not the exact two-opportunity Bernoulli optimization solved here. Tonnabel et al. (2012) optimize within-plant resource allocation given a fire regime rather than the optimal pair of fire intervals under this objective. Agne et al. (2022) measure seed supply and post-fire regeneration versus stand age, without a covering allocation theorem. None of those models or results implies the present explicit reentrant threshold classification without adding the new probability law and objective.

## Limitations

The equal maturation and viability rates are a special case, independence omits demographic inheritance and stochastic wildfire, and zero-duration opportunities are abstract skips rather than admissible actual fires. Exact threshold values are model-specific; the theorem does not establish optimal real-world prescribed fire schedules or empirical conservation outcomes. A broad historical mathematical priority claim is not made, and a highly relevant 2013 primary paper was accessible only through its abstract and indexed detailed excerpts rather than a fully retrieved standalone article. The finite checker is not an independent proof or external audit.

## References

- Plumanns Pouton, E., Kasel, S., Penman, T. D., Swan, M., and Kelly, L. T. (2024). *Soil seedbanks are shaped by the timing of fires in a Mediterranean-type ecosystem*. Journal of Applied Ecology. First published 10 September 2024. https://doi.org/10.1111/1365-2664.14759
- McCarthy, M. A., Possingham, H. P., and Gill, A. M. (2001). *Using stochastic dynamic programming to determine optimal fire management for Banksia ornata*. Journal of Applied Ecology. https://doi.org/10.1046/j.1365-2664.2001.00617.x
- Tucker, C. M., and Cadotte, M. W. (2013). *Fire variability, as well as frequency, can explain coexistence between seeder and resprouter life histories*. Journal of Applied Ecology. https://doi.org/10.1111/1365-2664.12073
- Tonnabel, J. et al. (2012). *Optimal resource allocation in a serotinous non-resprouting plant species under different fire regimes*. Journal of Ecology. https://doi.org/10.1111/j.1365-2745.2012.02023.x
- Agne, M. C. et al. (2022). *Fire interval and post-fire climate effects on serotinous forest resilience*. Fire Ecology. https://doi.org/10.1186/s42408-022-00145-4
