# An exact introduction-count staircase under two-founder thresholds and intermittent habitat receptivity

## Finding

Consider independent, equal-expected-size introduction episodes with a total expected viable-propagule budget \(B>0\) and episode receptivity \(0<s<1\). If a receptive episode establishes a founding population precisely when at least two viable propagules arrive, the probability of at least one successful episode under \(m\ge1\) introductions is
\[
P_m(B,s)=1-\left[1-s+s\left(1+\frac{B}{m}\right)e^{-B/m}\right]^m.
\]
There is a unique dimensionless \(\xi_s>1\) with the following properties:

1. For every budget \(B>0\), the only possible globally optimal integer release counts are \(\max\{1,\lfloor B/\xi_s\rfloor\}\) and \(\max\{1,\lceil B/\xi_s\rceil\}\).
2. For every integer \(j\ge1\), there is exactly one critical budget \(B_j(s)\) with \(j\xi_s<B_j(s)<(j+1)\xi_s\); these budgets are strictly increasing and are the *complete* set of changes of the optimal count. The count equals \(j\) for \(B_{j-1}(s)<B<B_j(s)\), with \(B_0(s)=0\), and exactly the adjacent counts \(j,j+1\) tie at \(B=B_j(s)\).
3. For fixed \(s\in(0,1)\), every maximizing count \(m_*(B,s)\) satisfies \(m_*(B,s)/B\to1/\xi_s\) as \(B\to\infty\), and differs from \(B/\xi_s\) by less than one for \(B>\xi_s\). No other count ever ties.

The continuous-optimum dose \(\xi_s\) is the unique positive solution of
\[
\frac{s\xi_s^2e^{-\xi_s}}{1-s+s(1+\xi_s)e^{-\xi_s}}
=-\log\left[1-s+s(1+\xi_s)e^{-\xi_s}\right].
\]
The critical budgets are the unique solutions in the specified intervals of
\[
j\ell_s\!\left(\frac{B_j}{j}\right)=(j+1)\ell_s\!\left(\frac{B_j}{j+1}\right),
\qquad \ell_s(x)=-\log[1-s+s(1+x)e^{-x}].
\]
In particular, the exact one-to-two-release threshold is \(B_1(s)=2t_s\), where \(t_s>0\) uniquely solves
\[
e^{t_s}=1+t_s\left(1+\frac1{\sqrt{1-s}}\right).
\]

## Assumptions and scope

For each fixed pair \((B,s)\) with \(B>0\), \(0<s<1\), choose a positive **integer** \(m\) of equal-size episodes. At each episode an independent Bernoulli receptivity variable has success probability \(s\). Independently, the number of viable arrivals is Poisson with mean \(B/m\); all episodes and their arrivals are mutually independent. One episode establishes exactly if it is receptive and has at least two viable arrivals. The overall goal is to maximize the probability of at least one such episode. There are no survival interactions or delayed rescue effects between episodes. The resource constraint fixes expected arrivals, not a deterministic total number of individuals. Arbitrarily unequal release sizes are **outside** the optimization domain. The primary mathematical subject is ecological colonization and founding success under a two-propagule cooperation threshold.

## Proof

**Reduction.** For a Poisson variable of mean \(x\), the probability of at least two arrivals is \(p(x)=1-(1+x)e^{-x}\). An episode therefore fails with probability \(q_s(x)=1-sp(x)=1-s+s(1+x)e^{-x}\). Since the episodes are independent, \(P_m=1-q_s(B/m)^m\). Defining \(\ell_s(x)=-\log q_s(x)\), maximizing \(P_m\) is equivalent to maximizing
\[
F_m(B,s)=m\ell_s(B/m)=Bf_s(B/m),\qquad f_s(x)=\frac{\ell_s(x)}x.
\]

**One continuous optimal dose.** Direct differentiation yields
\[
\ell_s'(x)=\frac{sxe^{-x}}{q_s(x)},\qquad
\ell_s''(x)=\frac{se^{-x}}{q_s(x)^2}\left[(1-s)(1-x)+se^{-x}\right].
\]
The bracket \(H_s(x)=(1-s)(1-x)+se^{-x}\) has \(H_s(0)=1\), derivative \(H_s'(x)=-(1-s)-se^{-x}<0\), and tends to \(-\infty\) as \(x\to\infty\). Hence \(\ell_s''\) is strictly positive until a unique \(c_s>1\), and strictly negative after it. Put \(N_s(x)=x\ell_s'(x)-\ell_s(x)\). By differentiation \(N_s'(x)=x\ell_s''(x)\), while \(N_s(0)=0\) (continuous extension), and \(N_s(x)>0\) for \(0<x\le c_s\). As \(x\to\infty\), \(x\ell_s'(x)\to0\) and \(\ell_s(x)\to-\log(1-s)\), so \(N_s(x)\to\log(1-s)<0\). Consequently \(N_s\) has exactly one positive zero \(\xi_s>c_s>1\). Since \(f_s'(x)=N_s(x)/x^2\), the function \(f_s\) strictly increases on \((0,\xi_s)\) and strictly decreases on \((\xi_s,\infty)\). Its limits are zero at both ends: \(\ell_s(x)\sim sx^2/2\) as \(x\downarrow0\) and \(\ell_s(x)\to-\log(1-s)\) as \(x\to\infty\). Its unique global maximum occurs at \(\xi_s\); the displayed defining equation is precisely \(N_s(\xi_s)=0\).

**Integer adjacency and every transition.** For fixed \(B\), \(F_m=Bf_s(B/m)\). As integer \(m\) increases up to \(B/\xi_s\), its argument decreases toward \(\xi_s\) from above and \(F_m\) strictly increases; as \(m\) increases beyond \(B/\xi_s\), its argument decreases below \(\xi_s\) and \(F_m\) strictly decreases. Thus a global maximum can occur only at the two adjacent integers bracketing \(B/\xi_s\), with the lower integer clamped to one. For each \(j\ge1\), compare \(F_j\) and \(F_{j+1}\). If \(B\le j\xi_s\), both arguments lie at or below the maximum and \(F_j>F_{j+1}\). If \(B\ge(j+1)\xi_s\), both arguments lie at or above the maximum and \(F_j<F_{j+1}\). On the intervening interval \((j\xi_s,(j+1)\xi_s)\), \(f_s(B/j)\) is strictly decreasing in \(B\), and \(f_s(B/(j+1))\) strictly increasing. Their continuous difference therefore has exactly one zero \(B_j(s)\), going from favoring \(j\) to favoring \(j+1\). Because the intervals \((j\xi_s,(j+1)\xi_s)\) are strictly ordered and disjoint, all \(B_j\) strictly increase. The adjacency result establishes the stated optimal-count ranges and uniqueness except at these exact crossings. The asymptotic count law and strict one-count error follow directly from adjacency.

**First budget threshold in closed implicit form.** Write \(B=2t\), \(t>0\). Expanding the two independent failure probabilities gives the exact identity
\[
P_2(2t,s)-P_1(2t,s)
=se^{-2t}\left[(1-s)(e^t-1-t)^2-t^2\right].
\]
The factor \(se^{-2t}\) is positive. Since \(e^t-1-t>0\), the sign is the sign of \(\sqrt{1-s}(e^t-1-t)-t\). Equivalently the positive transition solves \(e^t=1+t(1+1/\sqrt{1-s})\). The ratio \((e^t-1)/t\) is strictly increasing on \((0,\infty)\), from one to infinity, proving existence and uniqueness. This positive root is the already uniquely defined \(B_1/2\). At \(s=1\), excluded from the main theorem, \(q_1(x)=(1+x)e^{-x}\), and \(f_1(x)=1-\log(1+x)/x\) strictly increases, so one release is optimal for every finite budget. At \(s=0\), every count fails equally and no nontrivial optimum exists.

## Verification

The accompanying standalone `check.py` uses only Python's standard library. Run `python3 check.py` to verify 963 supplementary numerical checks across six receptivity parameters, up to 25 adjacent thresholds for each parameter, direct brute-force integer maximization, exact two-release identity checks, differential identities and high-precision probability calculations. These finite computations supplement, but do not substitute for, the analytic proof. An independent symbolic simplification of \(\ell_s''(x)\) and the two-release difference gave zero residuals. For \(s=1/2\), the calculations give \(\xi_s\approx2.24242709681353\), \(B_1\approx3.12625148548179\), and \(B_2\approx5.46548159364452\). The inequalities in the theorem and their strictness follow analytically, not by numerical enumeration.

## Relationship to prior work

Grevstad (1999) already established qualitatively, in stochastic simulations, that an intermediate release size can be optimal when environmental variability and Allee effects interact. Shea and Possingham (2001) optimized biological-control introductions using stochastic dynamic programming with a distinct sigmoid establishment law and evolving metapopulation states. Koontz and colleagues (2018) used experiments and demographic simulations to compare introduction sizes and numbers under fixed propagule pressure. Those contributions motivate the present question; the claim here is **not** that intermediate optima are newly discovered. The specific result proved here is the complete unique-continuous-dose and strictly ordered integer-count transition law for the independent, fixed-mean, two-founder Poisson model. None of the accessible, inspected source statements gives this formula or these all-budget uniqueness and equality classifications. Related exact index records on multi-habitat Poisson founding and two-site mate-limited establishment concern different resource domains and success criteria. Historical priority remains uncertain in inaccessible older texts.

## Limitations

This is a stylized, conditional mathematical statement. The stochastic number of arrivals is not an exactly controlled integer release. Environmental receptivity is independent between episodes; correlated conditions, demographic persistence, density dependence, temporal rescue, variable release sizes, nonzero per-release costs, different viable-arrival distributions, and different founding thresholds are not covered. The results are not empirical advice on actual introductions of invasive species or biological-control agents. Full text of Grevstad (1999), potentially related prior work, was unavailable for thorough theorem-level comparison; absence of an accessible result is not evidence of absolute novelty. No independent external audit has been performed.

## References

1. M. J. Koontz, M. F. Oldfather, B. A. Melbourne, and R. A. Hufbauer, “Parsing propagule pressure: Number, not size, of introductions drives colonization success in a novel environment,” *Ecology and Evolution* (first published 2018-07-20), https://doi.org/10.1002/ece3.4226. Main motivating source.
2. F. S. Grevstad, “Factors influencing the chance of population establishment: Implications for release strategies in biocontrol,” *Ecological Applications* 9 (1999), https://doi.org/10.1890/1051-0761(1999)009[1439:FITCOP]2.0.CO;2. Abstract inspected; full text unavailable.
3. K. Shea and H. P. Possingham, “Optimal release strategies for biological control agents: An application of stochastic dynamic programming to population management,” *Journal of Applied Ecology* (first published 2001-12-25), https://doi.org/10.1046/j.1365-2664.2000.00467.x. Accessible full text inspected.
4. P. Bajeux, F. Grognard, and L. Mailleret, “Influence of components of propagule pressure, Allee effects, and stochasticity on time to establish introduced populations,” *Journal of Theoretical Biology* (2019), https://doi.org/10.1016/j.jtbi.2019.03.012. Abstract-level contextual comparison only.
