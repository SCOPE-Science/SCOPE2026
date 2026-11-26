# A discontinuous corridor-redundancy investment threshold in a two-route ecological network

## Finding

Consider two independent, edge-disjoint, two-corridor routes between a source and a destination habitat. Each corridor receives nonnegative investment and succeeds with probability \(p(x)=x/(1+x)\), where the reference failure clock has unit rate. A fixed positive total investment budget \(B\) is distributed over four corridors. The optimal probability that **at least one complete route succeeds** undergoes an exact discontinuous investment transition.

Let \(\sigma\) be the unique positive solution of
\[
2\sigma^3+\sigma^2-8\sigma-8=0,
\qquad B_*=2\sigma\approx 4.357355625886.
\]
When \(0<B<B_*\), the only optimal allocations are \((B/2,B/2,0,0)\) and \((0,0,B/2,B/2)\). When \(B>B_*\), the **unique** optimal allocation is \((B/4,B/4,B/4,B/4)\). At \(B=B_*\), exactly these three allocations tie; there are no additional optima. The balanced four-corridor allocation is a strict local optimum on the budget simplex if and only if \(B>2\sqrt2\). At \(B=2\sqrt2\) it is not a local maximum, even though the second derivative along balanced transfers between routes vanishes. Thus it is strictly locally optimal but globally inferior precisely on \(2\sqrt2<B<B_*\).

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
For \(v>0\) this is strictly increasing in \(ab\), which by the arithmetic-geometric mean inequality is maximized uniquely at \(a=b=v/2\). At zero route total both investments are zero. The other route's failure probability is strictly positive for any finite allocation. Therefore balancing a funded unbalanced route strictly increases \(R\); at a given pair of route totals the internally balanced allocation uniquely maximizes \(R\). In particular all global optima have the form \((t,t,u,u)\) with \(t,u\ge0\), \(t+u=S=B/2\).

**Step 2 (two-route failure landscape).** Define
\[
h(t)=1-p(t)^2=\frac{1+2t}{(1+t)^2},
\qquad F_S(t)=h(t)h(S-t),\quad 0\le t\le S.
\]
Maximizing \(R=1-F_S\) is minimizing \(F_S\). Since \(F_S>0\), its derivative has the sign of the logarithmic derivative:
\[
\frac{d}{dt}\log F_S(t)
=\frac{2(S-2t)[1-2t(S-t)]}
{(1+t)(1+2t)(1+S-t)(1+2S-2t)}.
\]
The only interior stationary points are the central split \(t=S/2\) and, when \(S>\sqrt2\), the two distinct off-center solutions to \(t(S-t)=1/2\). The failure function is symmetric about the center and its logarithmic derivative is antisymmetric. For \(S>\sqrt2\), the derivative changes from positive to negative at the off-center point to the left of center and from negative to positive at the center. By reflection the other off-center point is also a strict local maximum of failure. The center is then a strict local minimum of failure.

For \(0<S<\sqrt2\), the bracket \(1-2t(S-t)\) is strictly positive. For \(S=\sqrt2\), it equals \(2(t-S/2)^2\); thus the logarithmic derivative is positive to the left of the center and negative to the right, with a zero of order three at the center. In both cases the center is a strict maximum of failure along the balanced-split family, not a local maximum of success. At equality, arbitrarily small nonzero transfers along this family **increase** success despite the vanishing quadratic term. In all cases the only possible global failure minima are \(t=0\), \(t=S\), and \(t=S/2\).

**Step 3 (sharp global switch).** The respective failure probabilities of a concentrated route and a four-way balanced budget are \(h(S)\) and \(h(S/2)^2\). Clearing their strictly positive denominators gives the exact identity
\[
h(S)-h(S/2)^2
=\frac{S^2[2S^3+S^2-8S-8]}
{16(1+S)^2(1+S/2)^4}.
\]
Let \(P(S)=2S^3+S^2-8S-8\). Its coefficient signs have exactly one change, so Descartes' rule gives at most one positive root (counting multiplicity). Since \(P(0)=-8<0\) and \(P(S)\to+\infty\), there is exactly one positive root \(\sigma\). Moreover, \(P(\sqrt2)=-6-4\sqrt2<0\), so \(\sigma>\sqrt2\). It follows that \(h(S)<h(S/2)^2\) below \(\sigma\) and the reverse strict inequality holds above it. Step 2 excludes every other split; Step 1 excludes every unbalanced allocation. This gives all global optima and the three-way tie.

**Step 4 (strict local optimum and proxy disagreement).** For \(S>\sqrt2\), a sufficiently small nonzero change in route totals lowers the best success probability for those totals, since the balanced family has a strict local success maximum at the center. If neither route total changes, any nontrivial within-route perturbation lowers success by Step 1. Hence the center is strictly locally optimal on the full simplex. For \(S\le\sqrt2\), the feasible balanced transfers of Step 2 already show that the center is not locally optimal. For \(\sqrt2<S<\sigma\) the concentrated endpoints have strictly lower failure than the center.

Finally, for the best-path surrogate \(\max\{p(x_1)p(x_2),p(x_3)p(x_4)\}\), a route with total \(v\) has product at most \(p(v/2)^2\). This upper bound is strictly increasing in \(v\ge0\), so tying the concentrated value \(p(B/2)^2\) requires one route with total \(B\) and its investments balanced. This proves the stated disagreement.

## Verification

The frozen source package's standalone standard-library script `verify.py` checks exact rational comparisons. Its documented output is `PASS 36044 exact-rational assertions; unique positive root bracket 2178677/1000000 2178679/1000000`. The tests check all quarter-unit budget allocations through total budget seven, eighty exact rational values of the candidate-comparison identity, and four examples straddling the transition. None of these finite tests is used to infer an infinite claim or the irrational local boundary; Steps 1–4 supply the analytic proof. With \(B=4\), the concentrated optimum has reliability \(4/9\), exceeding the four-way balanced value \(7/16\). With \(B=5\), the four-way balanced reliability \(3425/6561\) exceeds the concentrated value \(25/49\).

## Relationship to prior work

Hamonic et al. study budgeted habitat and corridor restoration through a maximum-product **single-path** connectivity proxy and discrete improvement choices. The surrogate-optimum statement above is compatible with their metric; the exact threshold here concerns the **probability of success along at least one of two independent routes** with continuous investments. Rushdi and Hassan give symbolic reliability analysis of migration between habitat patches; the underlying reliability expression is **not** claimed as new. The contribution here is the exact optimization classification and the structural distinction between connectivity objectives. Barrera et al. study **all-terminal** series-parallel reliability and give a mixed-integer convex-envelope formulation for edge selection, not this two-terminal continuous rate-budget theorem. Shaked and Shanthikumar discuss spares and repair resources in the accessible abstract. Historical priority beyond inspected material cannot be guaranteed.

## Limitations

The finding assumes edge independence, two routes of exactly two edges, identical clock normalization, a rational passage law, and a divisible linear total budget. Different success laws, network geometries, real habitat costs, or ecological dependencies can change the threshold or remove it. It is a stylized benchmark, not an empirical restoration prescription. Independent empirical validation has not been performed. Related older resource-allocation papers were accessible only in part, so broader mathematical coverage remains a priority risk.

## References

1. F. Hamonic, C. Albert, B. Couëtoux and Y. Vaxès, *Optimizing the ecological connectivity of landscapes with generalized flow models and preprocessing*, https://arxiv.org/abs/2109.06622; journal DOI:10.1002/net.22131.
2. A. M. A. Rushdi and A. K. Hassan, *Reliability of migration between habitat patches with heterogeneous ecological corridors*, Ecological Modelling 304 (2015), 1–10, DOI:10.1016/j.ecolmodel.2015.02.014.
3. J. Barrera, E. Moreno, G. Muñoz and P. Romero, *Exact reliability optimization for series-parallel graphs using convex envelopes*, https://arxiv.org/abs/2107.13333.
4. E. El-Neweihi, F. Proschan and J. Sethuraman, *Optimal allocation of components in parallel-series and series-parallel systems*, Journal of Applied Probability 23 (1986), 770–777, DOI:10.2307/3214014.
5. M. Shaked and J. G. Shanthikumar, *Optimal allocation of resources to nodes of parallel and series systems*, Advances in Applied Probability 24 (1992), 894–914, DOI:10.2307/1427718.
