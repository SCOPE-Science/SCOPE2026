# A sharp event-rate threshold for environmental fixation overshoot in a three-individual population

## Finding

A population with three individuals can show strictly higher one-mutant fixation probability under **every positive environmental-switching rate** than under either frozen environment, even though both frozen environments have the **same** fixation probability. In the reciprocal two-stage birth--death family defined below, the switching response is monotone precisely when the first transient-state event rate is at most twice the second. When it exceeds twice the second, the fixation probability crosses the neutral value and has one finite optimum. The threshold is independent of selection intensity.

Let \(a,c,d>0\), \(\kappa\ge0\), and put
\[
 A=a^2+a+1,\qquad H=(a+1)(a^2+1),\qquad G=(a+1)H,
\]
\[
 D(\kappa)=3H^2\kappa^2+(c+d)(a+1)AH\kappa+aA^2cd.
\]
For an initially uniform environment and one mutant, the fixation probability is
\[
 \boxed{\Phi(\kappa)=\frac aA+\frac{(a-1)^2G\kappa\,[cA+2(a^2+1)\kappa]}{2AD(\kappa)}.}
\]
Each frozen environment gives \(\Phi(0)=a/A\). For every \(a\ne1\), every \(\kappa>0\) improves strictly over both frozen possibilities. The comparison with neutrality is
\[
 \boxed{\Phi(\kappa)-\frac13=\frac{(a-1)^2[G(c-2d)\kappa-2aAcd]}{6D(\kappa)}.}
\]

If \(c\le2d\), the fixation probability is strictly increasing and approaches \(1/3\) from below. If \(c>2d\), there is exactly one crossing of neutrality, at
\[
 \kappa_0=\frac{2aAcd}{G(c-2d)},
\]
and exactly one finite global optimum, at the unique positive root of
\[
 H^2(c-2d)\kappa^2-4a(a^2+1)Acd\kappa-aA^2c^2d=0.
\]
The optimum lies above \(\kappa_0\). The neutral case \(a=1\) has \(\Phi(\kappa)=1/3\) for every switching rate. A population of two individuals cannot show a switching advantage over the best frozen environment, for any finite environmental switching dynamics. Thus size three is minimal for this specific phenomenon.

## Assumptions and scope

The population is a continuous-time birth--death chain with mutant count \(i\in\{0,1,2,3\}\). The states \(i=0\) and \(i=3\) are absorbing (extinction and fixation of the mutant). The environment \(e\in\{+,-\}\) changes independently at rate \(\kappa\) in either direction. Rates for count changes, conditional on environment, are

| Mutant count | Environment | Rate up | Rate down |
|---|---|---|---|
| \(1\) | \(+\) | \(ca/(a+1)\) | \(c/(a+1)\) |
| \(1\) | \(-\) | \(c/(a+1)\) | \(ca/(a+1)\) |
| \(2\) | \(+\) | \(d/(a^2+1)\) | \(da^2/(a^2+1)\) |
| \(2\) | \(-\) | \(da^2/(a^2+1)\) | \(d/(a^2+1)\) |

Thus \(c,d\) are the **total count-change event rates** at the two transient mutant counts, respectively, independent of environmental state. Initially \(i=1\), and the environment is uniform and independent. All count-change and environmental events are governed by competing exponential clocks. No specific Moran reproductive mechanism is claimed for these rates. When \(\kappa=0\), the initial environment is fixed forever. When \(\kappa\to\infty\), the count-change rates average to neutral up/down rates at each transient count.

## Proof

**1. Frozen environments.** For a birth--death chain on \(0,1,2,3\), starting at \(1\), the fixation probability is
\[
 \bigl[1+(w_1^-/w_1^+)+(w_1^-/w_1^+)(w_2^-/w_2^+)\bigr]^{-1}.
\]
In environment \(+\), the two downward-to-upward ratios are \(1/a\) and \(a^2\); in environment \(-\), they are \(a\) and \(1/a^2\). Either substitution gives \(a/(a^2+a+1)=a/A\). This equality is not a consequence of identical environmental selection: selection points in opposite directions at the two mutant counts.

**2. Exact switching solution.** Denote by \(h_{1+},h_{1-},h_{2+},h_{2-}\) the fixation probabilities conditioned on count and environment, with boundary values \(h_{0\pm}=0\) and \(h_{3\pm}=1\). The backward equations are
\[
 (c+\kappa)h_{1+}-\kappa h_{1-}-\frac{ca}{a+1}h_{2+}=0,
\]
\[
 (c+\kappa)h_{1-}-\kappa h_{1+}-\frac{c}{a+1}h_{2-}=0,
\]
\[
 (d+\kappa)h_{2+}-\kappa h_{2-}-\frac{da^2}{a^2+1}h_{1+}=\frac{d}{a^2+1},
\]
\[
 (d+\kappa)h_{2-}-\kappa h_{2+}-\frac{d}{a^2+1}h_{1-}=\frac{da^2}{a^2+1}.
\]
This strictly transient finite system has a unique solution. Eliminating the two variables \(h_{2\pm}\), solving the remaining two equations, and simplifying the average \(\Phi=(h_{1+}+h_{1-})/2\) yields
\[
 \Phi-\frac aA=\frac{(a-1)^2G\kappa[cA+2(a^2+1)\kappa]}{2AD(\kappa)}.
\]
All factors in the denominator are strictly positive for the stated positive parameters, so the gain is strict whenever \(a\ne1\) and \(\kappa>0\).

**3. Neutral crossover and switching-rate derivative.** Subtracting \(1/3\) from the exact expression gives the second boxed identity. The sign of \(\Phi'\) for \(a\ne1\) is the sign of
\[
 P(\kappa)=AH^2(2d-c)\kappa^2+4a(a^2+1)A^2cd\kappa+aA^3c^2d.
\]
More precisely, differentiating the gain in Step 2 yields
\[
 \Phi'(\kappa)=\frac{(a-1)^2G\,P(\kappa)}{2A D(\kappa)^2}.
\]
If \(c\le2d\), every term of \(P\) is nonnegative and its constant term is positive, so \(\Phi'>0\) for every finite \(\kappa\ge0\). If \(c>2d\), \(P\) is a downward-opening quadratic with positive value at zero and negative limiting sign. Its product of roots is negative, so it has exactly one positive root: the unique strict maximum. Dividing \(P=0\) by \(A\) gives the displayed equation for that root. Independently, the neutral gap has numerator increasing linearly from a negative intercept, with positive slope exactly when \(c>2d\); hence its unique crossing is \(\kappa_0\), and the maximum is beyond that crossing. The leading quadratic terms in \(\Phi\) give \(\lim_{\kappa\to\infty}\Phi=1/3\). If \(a=1\), every count change has equal up/down rates, and the exact expression is identically \(1/3\).

**4. Minimal population size.** A mutation-free two-individual birth--death population has only one transient mutant count, \(i=1\). For each environmental state \(e\), let the upward/downward absorption rates be \(u_e,v_e>0\). Condition on the environment at the first count-change event. Given that environmental state, the probability the event fixes the mutant is \(u_e/(u_e+v_e)\), independently of the past environmental trajectory. Consequently the overall fixation probability under any independent finite-state environmental switching process and any initial environmental distribution is a convex combination of the frozen one-mutant probabilities \(u_e/(u_e+v_e)\); it cannot exceed their maximum. The three-individual construction in Steps 1--3 attains a strict improvement for all positive switching rates when \(a\ne1\). The trivial one-individual case has no transient mutant count.

## Verification

`verify.py` uses only the Python standard library and independently solves the four-state backward equations by exact rational Gaussian elimination. It compares the result with the displayed formula, neutrality gap and derivative-sign polynomial on a deterministic grid of positive rational parameters. It also checks the exact illustrative instance below and the two-individual upper bound using rational matrices. These finite tests are reproducibility checks, not a substitute for the parameter-uniform algebraic proof above.

For \(a=2\), \(c=3\), \(d=1\), the two frozen fixation probabilities are \(2/7\), while
\[
 \Phi(\kappa)=\frac{150\kappa^2+285\kappa+56}{2(225\kappa^2+420\kappa+98)}.
\]
The neutral crossing is \(\kappa_0=28/15\), and the maximizing rate is \(\kappa_*=(28+7\sqrt{34})/15\). The maximum is \(31/84-\sqrt{34}/168\approx0.334339572\), strictly greater than \(1/3\), even though either fixed environment has probability \(2/7\approx0.285714286\).

Reproduce from the folder containing the result and verifier with `python3 verify.py`.

## Relationship to prior work

Ashcroft, Altrock and Galla (first public preprint dated 2014-06-21) establish a general fluctuating-environment birth--death framework, including a backward fixation equation and numerical switching-rate effects in a population with \(50\) individuals. The present result uses that established framework but proves a separate **sharp, all-parameter, minimal-size classification** for a reciprocal two-stage family: equal frozen fixation probabilities, strict all-rate switching improvement, the event-rate boundary \(c=2d\), and the unique neutral crossing and finite optimizer. These statements are not asserted as new model mechanics.

Cvijović and colleagues (2015) analyze fixation in fluctuating selection, primarily in large-population regimes; their fluctuating fitness model and asymptotic questions differ from the exact finite four-transient-state generator here. Cheong and colleagues (2016) study selection on environmental sensing accuracy with switching, rather than this mutant-count fixation objective. The generic birth--death matrix equations in the first paper cover the computation in principle, so independent priority verification remains important; the proposed contribution is the sign classification and minimality rather than mere rational inversion.

## Limitations

The model is stylized: environmental states have exactly symmetric switching rates; count-change rates are reciprocal between environments and have the specified count dependence; initial environment is uniformly distributed. Rates need not arise from a single biological fitness payoff matrix or a canonical Moran update. No global conclusion is given for arbitrary population sizes, asymmetric environmental switching, alternative initial environmental distributions, fixation times, or ecological field data. A prior general linear-system formula permits the finite calculation, and historical priority of the specialized sharp phase diagram remains provisional pending independent review. No independent audit has been performed.

## References

1. P. Ashcroft, P. M. Altrock, T. Galla, *Fixation in finite populations evolving in fluctuating environments*, arXiv:1406.5619v1 (public 2014-06-21), later *Journal of the Royal Society Interface* 11, 20140663 (2014), https://arxiv.org/abs/1406.5619 and https://doi.org/10.1098/rsif.2014.0663.
2. I. Cvijović, B. H. Good, E. R. Jerison, M. M. Desai, *Fate of a mutation in a fluctuating environment*, *PNAS* 112, E5021--E5028 (2015), https://doi.org/10.1073/pnas.1505406112.
3. K. H. Cheong, Z. X. Tan, N.-g. Xie, M. C. Jones, *A paradoxical evolutionary mechanism in stochastically switching environments*, *Scientific Reports* 6, 34889 (2016), https://doi.org/10.1038/srep34889.
