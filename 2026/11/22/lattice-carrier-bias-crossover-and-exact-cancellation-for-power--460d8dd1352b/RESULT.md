# Lattice–carrier bias crossover and exact cancellation for power-DEGPD mean residual life

## Finding

Consider the *power-carrier* discrete extended generalized Pareto distribution, with parameters \(\sigma>0\), \(\kappa>0\), and \(\xi>0\):
\[
 \Pr(Y=j)=\left[1-\left(1+\frac{\xi(j+1)}{\sigma}\right)^{-1/\xi}\right]^\kappa-
 \left[1-\left(1+\frac{\xi j}{\sigma}\right)^{-1/\xi}\right]^\kappa,
 \qquad j\in\mathbb N_0.
\]
Put \(p=1/\xi\), \(c=\sigma/\xi\), and \(x=u+c\). For integer thresholds \(u\ge 1\), let \(m_u=\mathbb E[Y-u\mid Y\ge u]\).

**Theorem.** The mean residual life is finite exactly when \(0<\xi<1\), equivalently \(p>1\). For every fixed \(p>1,c>0,\kappa>0\), as integers \(u\to\infty\),
\[
\boxed{\quad m_u=\frac{x}{p-1}-\frac12+
 \frac{p}{12x}+
 \frac{(\kappa-1)c^p p}{2(p-1)(2p-1)}x^{1-p}
 +O\!\left(x^{-3}+x^{-p-1}+x^{1-2p}\right).\quad}
\]
Define the corrected bias \(B_u=m_u-x/(p-1)+1/2\). Its sign and leading order obey the following exhaustive fixed-parameter classification.

* For \(1<p<2\), \(\kappa\ne1\), the carrier term dominates: \(B_u\sim (\kappa-1)c^pp\,x^{1-p}/[2(p-1)(2p-1)]\). Thus the eventual sign is that of \(\kappa-1\). At \(\kappa=1\), \(B_u\sim p/(12x)>0\).
* For \(p>2\), the lattice term dominates for every \(\kappa>0\): \(B_u\sim p/(12x)>0\).
* For \(p=2\), \(B_u=C_1/x+C_3/x^3+O(x^{-5})\), with \(a=c^2\) and
\[
 C_1=\frac16+\frac{(\kappa-1)a}{3},\qquad
 C_3=-\frac1{30}-\frac{(\kappa-1)a}{12}
 +a^2\left[\frac{(\kappa-1)^2}{6}-\frac{2(\kappa-1)(\kappa-2)}{15}\right].
\]
If \(a\le1/2\), then \(C_1>0\) for all \(\kappa>0\). If \(a>1/2\), the unique admissible critical carrier parameter is
\[
 \boxed{\kappa_*(c)=1-\frac1{2c^2}\in(0,1).}
\]
For \(0<\kappa<\kappa_*\), \(B_u<0\) eventually; for \(\kappa>\kappa_*\), \(B_u>0\) eventually. On the cancellation curve itself, the order \(x^{-1}\) disappears and
\[
 \boxed{\quad B_u=\frac{1-4c^2}{60x^3}+O(x^{-5})<0
 \quad\text{for all sufficiently large }u.\quad}
\]
At the concrete rational parameter triple \((\xi,\sigma,\kappa)=(1/2,1/2,1/2)\), this simplifies to \(m_u=(u+1)-1/2-1/[20(u+1)^3]+O(u^{-5})\).

A zero-inflated extension with an independent structural zero of probability \(\pi\in[0,1)\) has exactly the same \(m_u\) for every \(u\ge1\), so the classification extends unchanged to that model.

## Assumptions and scope

The random variable is supported on \(\mathbb N_0\). Its CDF is \(\Pr(Y\le j)=[1-(c/(j+1+c))^p]^\kappa\), with \(\kappa,p,c>0\). Parameters remain fixed while the integer threshold tends to infinity. The estimate is *not* claimed uniform as \(p\downarrow1\), \(\kappa\downarrow0\), or \(c\to\infty\). Conditional expectation is defined using \(Y\ge u\), not \(Y>u\), and \(u\ge1\) in the zero-inflated case. For \(\xi\ge1\), every such conditional mean diverges to infinity.

For \(p>1\) an exact, convergent representation is
\[
 m_u=\frac{\displaystyle\sum_{j=1}^{\infty}(-1)^{j+1}\binom\kappa j
 c^{pj}\zeta(pj,x+1)}{1-[1-(c/x)^p]^\kappa},
 \qquad x=u+c>c,
\]
where \(\zeta(s,a)=\sum_{k=0}^\infty(k+a)^{-s}\) is the Hurwitz zeta function. This formula is useful for numerical reproduction, but its existence alone is not the central claim.

## Proof

**1. Tail normalization and existence.** Let \(Z\) be continuous with distribution function \(\Pr(Z\le z)=[1-(c/(z+c))^p]^\kappa\) for \(z\ge0\). Then \(Y=\lfloor Z\rfloor\) has precisely the given mass function. For integer \(u\ge1\), \(\Pr(Y\ge u)=S(x)\), where
\[
 S(x)=1-\left(1-\frac{c^p}{x^p}\right)^\kappa,\quad x=u+c.
\]
The tail-sum identity for nonnegative integer variables gives
\[
 m_u=\frac{\sum_{k=1}^\infty S(x+k)}{S(x)}.
\]
Since \(S(x)\sim\kappa c^p x^{-p}\), the tail sum converges if and only if \(p>1\). Multiplication of all positive-count probabilities by \(1-\pi\) proves the zero-inflated assertion for \(u\ge1\).

**2. Uniformly controlled expansion.** Write \(a=c^p\), \(d=(\kappa-1)/2\), and \(e=(\kappa-1)(\kappa-2)/6\). For \(x\to\infty\), Taylor's theorem yields
\[
 S(x)=\kappa a x^{-p}\left[1-da x^{-p}+ea^2x^{-2p}+O(x^{-3p})\right].
\]
The expansion is uniform over \(x+k\ge x\) for \(k\ge1\); the remainder is bounded by a constant times \((x+k)^{-4p}\) in the unnormalized survival. For every \(s>1\), let
\[
 A_s(x)=x^s\sum_{k\ge1}(x+k)^{-s}=x^s\zeta(s,x+1).
\]
Termwise summation is valid because \(p>1\). Dividing the numerator and denominator gives
\[
 m_u=A_p(x)+da x^{-p}[A_p(x)-A_{2p}(x)]
 +a^2x^{-2p}\big[(d^2-e)A_p-d^2A_{2p}+e A_{3p}\big]
 +O(x^{1-3p}).
\]
This equality uses the same \(x\) in every \(A_s\). The remainder is bounded by the total summable fourth-order Taylor tail and denominator inversion.

**3. Discrete correction.** Euler–Maclaurin summation, including its standard integral remainder for \((x+t)^{-s}\), gives for every fixed \(s>1\)
\[
 A_s(x)=\frac{x}{s-1}-\frac12+\frac{s}{12x}
 -\frac{s(s+1)(s+2)}{720x^3}+O_s(x^{-5}).
\]
In particular, \(A_p-A_{2p}=xp/[(p-1)(2p-1)]+O(x^{-1})\); its constant term cancels. The terms retained from step 2 produce
\[
 m_u=\frac{x}{p-1}-\frac12+\frac{p}{12x}
 +\frac{da p}{(p-1)(2p-1)}x^{1-p}
 +O(x^{-3}+x^{-p-1}+x^{1-2p}),
\]
which is the first boxed expansion. Comparison of \(x^{-1}\) and \(x^{1-p}\) now proves the \(p<2\) and \(p>2\) regimes. The special value \(\kappa=1\) removes every carrier correction exactly, leaving \(A_p\).

**4. Critical index and rigorous cancellation.** If \(p=2\), keep terms through \(x^{-3}\). The extra terms from \(A_2-A_4=2x/3-1/(6x)+O(x^{-3})\) and the order \(a^2x^{-4}\) correction give \(C_1,C_3\) displayed above. Every further Taylor term contributes \(O(x^{-5})\); after division, there are no intervening even inverse powers, because the \(-1/2\) coefficient in each \(A_{2j}\) is common and cancels in the normalized quotient. Solving \(C_1=0\) yields \(\kappa_*=1-1/(2a)\), admissible exactly when \(a>1/2\). Substitution into \(C_3\) yields \((1-4a)/60\), strictly negative in that admissible region. Thus all strict eventual signs and the cubic cancellation follow, including the equality boundary. This finishes the proof.

## Verification

The separately supplied `verify_mean_excess.py` uses 70-digit arithmetic and the exact Hurwitz-zeta representation rather than summing a huge, slowly converging tail directly. It compares leading coefficients on both sides of \(p=2\), the untwisted baseline, both sides of \(\kappa_*\), and two distinct critical-cancellation parameters. Execute with `python verify_mean_excess.py` after installing `mpmath==1.3.0` from `requirements.txt`. The numerical checks are diagnostics only; the proof of the infinite-parameter assertions is in the analytic expansion and error bounds above.

## Relationship to prior work

Ahmad, Gaetan and Naveau (arXiv:2210.15253, first public 27 October 2022) define the DEGPD and ZIDEGPD power-carrier models, including the count CDF, quantiles and fitting methods. This note does **not** claim the family, its CDF, tail index, or the zero-inflation mixture as new. Ahmad and Arshad (arXiv:2409.18719) discuss mean residual life plots as a threshold diagnostic but do not give this sharp, three-regime second-order conditional-mean classification. Hitz, Davis and Samorodnitsky (arXiv:1707.05033) establish the discrete GPD and the classical half-unit continuity correction for its tail probabilities; that is the \(\kappa=1\) baseline, not the carrier-lattice interaction. Papastathopoulos and Tawn (arXiv:1111.6899) develop *continuous* extended-GPD families and penultimate tail-index expansions, not this integer conditional-mean phase boundary. Daouia, Stupfler and Usseglio-Carleve (2023) use empirical discrete mean excess plots and D-GPD inference; they do not evaluate the power-DEGPD carrier correction.

The contribution claimed here is only the combined sharp mean-residual bias phase diagram, its equality case, and the explicit cancellation curve. Existing continuous-model and one-term lattice formulas are acknowledged rather than recast as novel.

## Limitations

The results concern population mean residual life, not uncertainty bands or sampling error of an empirical mean-excess plot. The asymptotics are pointwise in fixed positive model parameters and require a finite conditional mean. They do not assert a uniform approximation at near-critical varying shapes, nor does the cancellation eliminate variance or estimation noise. A specialist historical-priority review could still identify an uncatalogued equivalent result. No independent mathematical audit has been performed.

## References

1. T. Ahmad, C. Gaetan, P. Naveau, *An extended generalized Pareto regression model for count data*, arXiv:2210.15253 (first posted 2022-10-27), https://arxiv.org/abs/2210.15253.
2. T. Ahmad, I. A. Arshad, *New flexible versions of extended generalized Pareto model for count data*, arXiv:2409.18719 (2024), https://arxiv.org/abs/2409.18719.
3. A. Hitz, R. A. Davis, G. Samorodnitsky, *Discrete Extremes*, arXiv:1707.05033 (2017), https://arxiv.org/abs/1707.05033.
4. I. Papastathopoulos, J. A. Tawn, *Extended Generalised Pareto Models for Tail Estimation*, arXiv:1111.6899 (2011), https://arxiv.org/abs/1111.6899.
5. A. Daouia, G. Stupfler, A. Usseglio-Carleve, *Extreme value modelling of SARS-CoV-2 community transmission using discrete generalized Pareto distributions*, *Royal Society Open Science* 10 (2023), https://doi.org/10.1098/rsos.220977.
6. P. Gamet, J. Jalbert, *A flexible extended generalized Pareto distribution for tail estimation*, *Environmetrics* 33 (2022), https://doi.org/10.1002/env.2744.
