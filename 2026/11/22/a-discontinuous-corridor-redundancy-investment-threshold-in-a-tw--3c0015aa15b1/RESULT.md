# A discontinuous corridor-redundancy investment threshold in a two-route ecological network

## Finding

Consider two independent, edge-disjoint, two-corridor routes between a source and a destination habitat. Each corridor receives nonnegative investment and succeeds with probability \(p(x)=x/(1+x)\), where the reference failure clock has unit rate. A fixed positive total investment budget \(B\) is distributed over four corridors. The optimal probability that **at least one complete route succeeds** undergoes an exact discontinuous investment transition.

Let \(\sigma\) be the unique positive solution of
\[
2\sigma^3+\sigma^2-8\sigma-8=0,
\qquad B_*=2\sigma\approx 4.357355625886.
\]
When \(0<B<B_*\), the only optimal allocations are \((B/2,B/2,0,0)\) and \((0,0,B/2,B/2)\). When \(B>B_*\), the **unique** optimal allocation is \((B/4,B/4,B/4,B/4)\). At \(B=B_*\), exactly these three allocations tie; there are no additional optima. The balanced four-corridor allocation becomes a strict local, but non-global, optimum already at \(B=2\sqrt2\), creating a genuine metastable interval \(2\sqrt2<B<B_*\).

In contrast, optimizing only the most successful individual route always chooses a fully concentrated two-corridor investment for every \(B>0\). Hence the max-path connectivity proxy and the genuine two-route success probability disagree about restoration redundancy above a sharp budget.

## Assumptions and scope

Four directed corridors form exactly two internally disjoint length-two routes; no other routes or dependencies are present. The four corridor outcomes are independent conditional on investments. For a corridor allocated dimensionless investment \(x\ge0\), an independent success clock of exponential rate \(x\) races a unit exponential loss clock, giving \(p(x)=x/(1+x)\). An investment of zero gives zero success probability; arbitrary positive real investment is permitted. The loss-clock normalization fixes the unit and is essential to the numerical threshold. Intermediate habitat patches are perfect when reached, and success means at least one end-to-end two-edge route is viable. The total budget \(B>0\) is used completely: \(x_1+x_2+x_3+x_4=B\).

Define
\[
R(x_1,x_2,x_3,x_4)=1-[1-p(x_1)p(x_2)][1-p(x_3)p(x_4)].
\]
The claim concerns the **global and local maxima of this explicit reliability functional** on the closed budget simplex, not general colonization dynamics, population persistence times, correlated passages, or parameter-invariant ecology.

## Proof

**Step 1 (within-route balancing).** For a fixed route investment total \(v=a+b\), one has
\[
p(a)p(b)=\frac{ab}{1+v+ab}.
\]
For \(v>0\) this is strictly increasing in \(ab\), which by the arithmetic-geometric mean inequality is maximized uniquely at \(a=b=v/2\). The other route's factor \(1-p(c)p(d)\) is nonnegative, and at an optimal investment every funded route must be internally balanced. Indeed, if an unbalanced funded route can be improved, the objective strictly increases because the other route's failure probability is positive for finite budgets. Hence all global optima have the form \((t,t,u,u)\) with \(t,u\ge0\), \(t+u=S=B/2\).

**Step 2 (two-route failure landscape).** Define
\[
h(t)=1-p(t)^2=\frac{1+2t}{(1+t)^2},
\qquad F_S(t)=h(t)h(S-t),\quad 0\le t\le S.
\]
Maximizing \(R=1-F_S\) is minimizing \(F_S\). Since \(F_S>0\), its stationary points have the sign of the logarithmic derivative:
\[
\frac{d}{dt}\log F_S(t)
=\frac{2(S-2t)[1-2t(S-t)]}
{(1+t)(1+2t)(1+S-t)(1+2S-2t)}.
\]
The only interior stationary points are the central split \(t=S/2\) and, when \(S\ge\sqrt2\), the two solutions to \(t(S-t)=1/2\). The derivative is positive near \(t=0\), negative just to the left of \(S/2\) when \(S>\sqrt2\), and symmetric about the center. Thus every off-center stationary point, if it exists and is distinct from the center, is a *strict local maximum of failure*, never a global minimum. The only possible global minima of failure are \(t=0\), \(t=S\), and \(t=S/2\). When \(S>\sqrt2\), the center is a strict local minimum of failure, and when \(0<S<\sqrt2\) it is a local maximum. At \(S=\sqrt2\) the derivative sign still makes the endpoints the global minima.

**Step 3 (sharp global switch).** The respective failure probabilities of a concentrated route and a four-way balanced budget are \(h(S)\) and \(h(S/2)^2\). Clearing their strictly positive denominators gives the exact identity
\[
h(S)-h(S/2)^2
=\frac{S^2[2S^3+S^2-8S-8]}
{16(1+S)^2(1+S/2)^4}.
\]
Let \(P(S)=2S^3+S^2-8S-8\). Its coefficient signs have exactly one change, so Descartes' rule gives at most one positive root (counting multiplicity). Since \(P(0)=-8<0\) and \(P(S)\to+\infty\), there is exactly one positive root \(\sigma\). Moreover, direct substitution gives \(P(\sqrt2)=-6-4\sqrt2<0\), so \(\sigma>\sqrt2\). Hence \(h(S)<h(S/2)^2\) for \(S<\sigma\) and the reverse strict inequality holds for \(S>\sigma\). Together with Step 2 and symmetry, this gives all global optima and the three-way tie at \(S=\sigma\).

**Step 4 (strict local trap and proxy disagreement).** At \(S>\sqrt2\) the center is a strict local minimum of failure, hence a strict local maximum of success. For \(\sqrt2<S<\sigma\), however, the concentrated endpoints have strictly lower failure probability. Finally, the single-best-path surrogate \(\max\{p(x_1)p(x_2),p(x_3)p(x_4)\}\) can be improved by placing all budget into whichever route has higher product and balancing it. Strict increase of \(p\) shows that no split-budget strategy can tie a concentrated one. This proves the stated disagreement.

## Verification

A standalone standard-library script `verify.py` reproduces the exact rational comparisons. Running `python verify.py` gives `PASS 36044 exact-rational assertions; unique positive root bracket 2178677/1000000 2178679/1000000`. The tests check all quarter-unit budget allocations through total budget seven, eighty exact rational values of the candidate-comparison identity, and four examples straddling the transition. None of these finite tests is used to infer an infinite claim; Steps 1–4 supply the complete analytic proof. With \(B=4\), the concentrated optimum has reliability \(4/9\), exceeding the four-way balanced value \(7/16\). With \(B=5\), the four-way balanced reliability \(3425/6561\) exceeds the concentrated value \(25/49\).

## Relationship to prior work

Hamonic et al. (arXiv:2109.06622, first public 2021-09-14) study budgeted habitat and corridor restoration through a maximum-product **single-path** connectivity proxy and discrete improvement choices. The surrogate-optimum statement above is compatible with their metric; the new exact threshold concerns the **probability of success along at least one of two independent routes** with continuous investments. Rushdi and Hassan (2015) already provide symbolic reliability analysis of ecological corridor networks including independent alternative routes, and therefore the reliability expression itself is **not** claimed as new. The claim is the exact optimization classification and the structural distinction between connectivity objectives. Barrera et al. (arXiv:2107.13333) address exact reliability optimization in series-parallel graphs with discrete/interval design variables and convex-envelope algorithms; their inspected statements do not give this continuous rational-rate closed-form threshold. Classic series-parallel allocation and reliability literature supplies broader background; historical priority beyond inspected sources cannot be guaranteed.

## Limitations

The finding assumes edge independence, two routes of exactly two edges, identical clock normalization, a rational passage law, and a divisible linear total budget; different success laws, network geometries, real habitat costs, or ecological dependencies can change the threshold or remove it. It is a stylized benchmark, not an empirical restoration prescription. Independent verification by external researchers has not been performed. Related older resource-allocation papers were accessible only by abstracts, so undiscovered stronger coverage remains a priority risk.

## References

1. F. Hamonic, C. Albert, B. Couëtoux and Y. Vaxès, *Optimizing the ecological connectivity of landscapes with generalized flow models and preprocessing*, arXiv:2109.06622 (first public 2021-09-14), https://arxiv.org/abs/2109.06622 ; journal version DOI:10.1002/net.22131.
2. A. M. A. Rushdi and A. K. Hassan, *Reliability of migration between habitat patches with heterogeneous ecological corridors*, Ecological Modelling 304 (2015), 1–10, DOI:10.1016/j.ecolmodel.2015.02.014.
3. J. Barrera, E. Moreno, G. Muñoz and P. Romero, *Exact reliability optimization for series-parallel graphs using convex envelopes*, arXiv:2107.13333, https://arxiv.org/abs/2107.13333.
4. E. El-Neweihi, F. Proschan and J. Sethuraman, *Optimal allocation of components in parallel-series and series-parallel systems*, Journal of Applied Probability 23 (1986), 770–777, DOI:10.2307/3214014 (abstract consulted only).
5. M. Shaked and J. G. Shanthikumar, *Optimal allocation of resources to nodes of parallel and series systems*, Advances in Applied Probability 24 (1992), DOI:10.2307/1427718 (abstract consulted only).
