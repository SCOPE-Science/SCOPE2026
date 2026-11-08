# Exact finite-step importance sampling for stationary scalar SGD

## Finding

Let \(m\ge2\), \(f_i(x)=a_i x^2/2+b_i x+c_i\) with \(a_i>0\), and \(F=m^{-1}\sum_i f_i\). Write \(x_*\) for the unique minimizer of \(F\), \(r_i=f_i'(x_*)\), and \(\bar a=m^{-1}\sum_i a_i\). Assume \(\sum_i r_i^2>0\), so this is the noninterpolating case. Sample indices independently with fixed probabilities \(p_i>0\), \(\sum_i p_i=1\), and apply the unbiased importance-weighted SGD update

\[
x_{t+1}=x_t-\frac{\eta}{m p_{I_t}}f'_{I_t}(x_t),\qquad \Pr(I_t=i)=p_i.
\]

For each fixed step size \(0<\eta<2/\bar a\), there is a **unique** full-support sampling distribution minimizing stationary mean-square error over all mean-square-stable fixed distributions. Define \(C_\eta=2m^2\bar a/\eta\). There is a unique positive solution \(V_*\) of

\[
\left(\sum_{i=1}^m\sqrt{r_i^2+V_*a_i^2}\right)^2=C_\eta V_*,
\]

and the unique optimizer and its minimum risk are

\[
\boxed{p_i^*=\frac{\sqrt{r_i^2+V_*a_i^2}}{\sum_{j=1}^m\sqrt{r_j^2+V_*a_j^2}},\qquad \min_p\lim_{t\to\infty}\mathbb E[(x_t-x_*)^2]=V_*.}
\]

A sampling law is mean-square stable precisely when \(\sum_i a_i^2/p_i<C_\eta\). No mean-square-stable law exists when \(\eta\ge2/\bar a\). Even an index with \(r_i=0\) receives **strictly positive optimal sampling probability** whenever \(\eta>0\), because its curvature affects stability.

For an exact three-component demonstration, take \(f_1(x)=x^2/2+x\), \(f_2(x)=x^2/2-x\), and \(f_3(x)=5x^2\), with \(\eta=2/9\). Then \(p^*=(2/9,2/9,5/9)\), the exact optimal stationary mean-square error is \(1/15\), and uniform sampling yields \(1/3\): a factor-five improvement. The third component has **zero gradient at the minimizer**, yet is sampled more often than the other two combined. Uniform sampling is mean-square stable only for \(\eta<4/17\), whereas suitable importance sampling is stable for every \(\eta<1/2\).

## Assumptions and scope

All computations are over real scalars. The fixed component functions are strongly convex quadratics, with no additional observation noise or momentum; stochasticity is solely from independently sampled component indices at successive steps. The index probabilities are time-independent, strictly positive, and attached to an unbiased importance weight \(1/(mp_i)\). The initialization is deterministic, or more generally independent of future indices with a finite second moment. The stationary risk refers to the unaveraged iterate, not a Polyak–Ruppert average. The noninterpolation hypothesis \(\sum_i r_i^2>0\) excludes a zero-variance degenerate case in which the uniqueness assertion changes.

## Proof

1. **Exact error recursion.** Because \(\sum_i r_i=0\), with \(e_t=x_t-x_*\),

   \[
   e_{t+1}=q_{I_t}e_t+\zeta_{I_t},\quad
   q_i=1-\frac{\eta a_i}{mp_i},\quad
   \zeta_i=-\frac{\eta r_i}{mp_i}.
   \]

   The indices are independent of \(e_t\), \(\sum_i p_i\zeta_i=0\), and \(\sum_i p_iq_i=1-\eta\bar a\). Set \(Q(p)=\sum_i p_iq_i^2\). Direct expansion gives

   \[
   Q(p)=1-2\eta\bar a+\frac{\eta^2}{m^2}\sum_i\frac{a_i^2}{p_i},\qquad
   \sum_i p_i\zeta_i^2=\frac{\eta^2}{m^2}\sum_i\frac{r_i^2}{p_i}.
   \]

2. **Exact stationary risk and admissibility.** If \(Q(p)<1\), the affine iid random recursion contracts in \(L^2\) under a common-noise coupling; its perpetuity has a unique stationary law with finite second moment. Its mean is zero because \(\lvert 1-\eta\bar a\rvert\le\sqrt{Q(p)}<1\). The mixed term in the stationary second-moment recursion therefore vanishes and yields

   \[
   V_\eta(p)=\frac{\sum_i r_i^2/p_i}{C_\eta-\sum_i a_i^2/p_i}.
   \]

   Here \(Q(p)<1\) is equivalent to the denominator being strictly positive. If \(Q(p)\ge1\), the centered innovations have strictly positive second moment, so no invariant law can have finite variance and mean zero. More directly, any stationary integrable mean must be zero unless \(\eta\bar a=0\), and a finite-second-moment stationarity identity would assert \((1-Q)V=\mathbb E\zeta^2>0\), a contradiction. Cauchy–Schwarz gives \(\sum_i a_i^2/p_i\ge(\sum_i a_i)^2=m^2\bar a^2\), with equality for \(p_i=a_i/(m\bar a)\); hence admissibility is possible exactly for \(0<\eta<2/\bar a\).

3. **Existence and uniqueness of the scalar root.** Define

   \[
   H(V)=\left(\sum_i\sqrt{a_i^2+r_i^2/V}\right)^2,\qquad V>0.
   \]

   Since at least one \(r_i\ne0\), \(H\) is continuous and strictly decreasing, with \(H(V)\to\infty\) as \(V\downarrow0\), and \(H(V)\to(\sum_i a_i)^2\) as \(V\to\infty\). Our step-size interval gives \(C_\eta>(\sum_i a_i)^2\), so a unique \(V_*>0\) solves \(H(V_*)=C_\eta\), which is the displayed root equation.

4. **Global optimality and unique optimizer.** For every probability vector \(p\) with positive coordinates, Cauchy–Schwarz gives

   \[
   \sum_i\frac{r_i^2+V_*a_i^2}{p_i}
   \ge\left(\sum_i\sqrt{r_i^2+V_*a_i^2}\right)^2=C_\eta V_*.
   \]

   For any stable \(p\), rearrangement and division by its positive stability denominator imply \(V_\eta(p)\ge V_*\). Equality in Cauchy–Schwarz is possible only for the displayed vector \(p^*\), and then \(\sum_i r_i^2/p_i^*=V_*(C_\eta-\sum_i a_i^2/p_i^*)\). The numerator is positive, hence the latter denominator is positive, so \(p^*\) really is stable. Strict equality conditions prove uniqueness, including when some residuals vanish.

5. **Three-component exact witness.** For \((a_i)=(1,1,10)\) and \((r_i)=(1,-1,0)\), \(\bar a=4\). At \(\eta=2/9\), \(C_\eta=324\), and \(V_*=1/15\) makes the optimal probabilities exactly \((2/9,2/9,5/9)\). At these probabilities, the sums \(\sum_i r_i^2/p_i\) and \(\sum_i a_i^2/p_i\) are respectively \(9\) and \(189\), yielding \(V=9/(324-189)=1/15\). Uniform sampling instead gives sums \(6\) and \(306\), yielding \(V=6/(324-306)=1/3\). The uniform stability threshold follows from \(2\eta\bar a>\eta^2\sum_i a_i^2/(m^2p_i)\), namely \(\eta<4/17\). For arbitrary \(0<\eta<1/2\), the exact optimal third probability simplifies to \(p_3^*=5\sqrt{\eta}/(3\sqrt2)\); the remaining two probabilities are equal. This explicitly shows positive probability assigned to a zero-residual component.

## Verification

The self-contained Python program `verification/check.py` uses standard-library rational arithmetic to check the exact stationary second-moment identities, global-inequality instances, the optimal three-component formula, and the fivefold improvement. Executing `python verification/check.py` reports 11 exact example identities; 9,053 rational sampling-grid candidates (4,164 stable); 288 additional exact covariance identities; and 99 floating-point root-consistency checks. Those finite checks corroborate, but do not replace, the general analytic proof of the scalar-root and global-optimality claims.

## Relationship to prior work

El Hanchi and Stephens (2021), *Stochastic Reweighted Gradient Descent*, introduce importance-weighted component-gradient sampling and optimize instantaneous gradient-estimator variance using tracked component gradients. The new question here is not instantaneous variance: it is the exactly minimized **invariant mean-square error of the unaveraged iterate at a fixed, nonvanishing step size**, including the sampling-dependence of its random multiplicative curvature. Their associated *Adaptive Importance Sampling* work has an empirical fixed-step appendix, but no corresponding exact optimizer for invariant quadratic risk. Défossez and Bach (2014/2015) investigate optimal resampling for **averaged** constant-step least-mean-squares, and explicitly treat the small-step approximation when optimizing sampling, rather than this finite-step unaveraged objective. Liu, Ziyin and Ueda (2020) provide finite-step stationary covariance formulas for additive-noise quadratic SGD without optimizing the resampling law under a component-dependent multiplier. Gruhlke, Nouy and Trunschke (2024) study sampling of projected gradients in a different setting. The formula may be independently derivable from classical fractional programming and Cauchy–Schwarz; publication precedence under a different nomenclature remains to be checked by an independent subject expert.

## Limitations

The theorem is for scalar strongly convex quadratics, iid **static** component sampling, and unaveraged stationary second-moment error. It does not give an implementable estimator of the optimal law without knowing component gradients and curvatures at the true minimizer, and does not claim analogous uniqueness in multiple dimensions or for adaptively varying sampling laws. Its proof requires a nonzero aggregate squared residual, and does not identify a Gaussian invariant distribution. The exact global-optimality result has been checked against accessible relevant literature, not independently certified for publication precedence.

## References

1. A. El Hanchi and D. A. Stephens, *Stochastic Reweighted Gradient Descent*, arXiv:2103.12293, first posted 2021-03-23, https://arxiv.org/abs/2103.12293.
2. A. El Hanchi and D. A. Stephens, *Adaptive Importance Sampling for Finite-Sum Optimization and Sampling with Decreasing Step-Sizes*, arXiv:2103.12243, first posted 2021-03-23, https://arxiv.org/abs/2103.12243.
3. A. Défossez and F. Bach, *Constant Step Size Least-Mean-Square: Bias-Variance Trade-offs and Optimal Sampling Distributions*, arXiv:1412.0156 (2014); revised published work in AISTATS (2015), https://arxiv.org/abs/1412.0156.
4. K. Liu, L. Ziyin and M. Ueda, *Noise and Fluctuation of Finite Learning Rate Stochastic Gradient Descent*, arXiv:2012.03636, first posted 2020-12-07, https://arxiv.org/abs/2012.03636.
5. C. Gruhlke, A. Nouy and L. Trunschke, *Optimal sampling for stochastic and natural gradient descent*, arXiv:2402.03113 (2024), https://arxiv.org/abs/2402.03113.
