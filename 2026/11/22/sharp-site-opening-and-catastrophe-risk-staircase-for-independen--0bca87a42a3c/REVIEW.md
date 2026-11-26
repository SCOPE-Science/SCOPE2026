# Independent mathematical audit

## correctness

PASS

In the stated independent-site model, Poisson thinning and conditioning on suitability give the product of site failure probabilities. The negative log of each factor has strictly positive first derivative and strictly negative second derivative for 0<c<1, giving budget exhaustion and the unique equal allocation by Jensen. The perspective score J(m) has J''=B^2 g''(B/m-h)/m^3<0, vanishes at the ends of the open relaxation (0,B/h), and has a unique maximizer. If the relaxation retains the bound m>=1, this maximizer is clipped at 1. Restricting to the actual integer interval gives the two adjacent candidates, clipped to the feasible endpoint when needed. The ratio of the marginal integrands v_r(t) for greater versus smaller r=(1-c)/c increases strictly with t, so the ratio of the two integrated scores for any larger and smaller positive efforts decreases strictly with c. Thus for every pair of counts the relative comparison moves strictly toward the larger count. Adjacent equality can occur only if the higher count wins strictly in the leading (1-c) score at c=1: equality only at that endpoint does not give an interior crossing. A tie of adjacent scores is global by strict concavity, which also prevents nonadjacent ties and skipped steps. For y=px, the equation G_r(y)/v_r(y)-y=ph has a left side strictly increasing in y and strictly decreasing in r. At r approaching zero it converges pointwise to exp(y)-1-y, and fixed brackets on either side of the limit root give convergence. At large r, z=r exp(-y) satisfies the exact rearrangement at RESULT.md:94; moving z log(1+1/r) to the left bounds z=O(log r), then the remaining terms give z~log(r)/(ph). This verifies both limits. Separately, python3 /workspace/branches/review-1-probability.py replays a 60-digit calculation of all nine feasible scores for each displayed example: 3 at c=0.1 (P=0.99343192921475848540), 5 at c=0.9 (P=0.27854962250500966199). These are examples only; the proof, not the packaged diagnostic assertions, establishes the quantified claims.

## originality

PASS

The supported distinct contribution is the exact risk-ordered integer policy with its strict endpoint criterion and relaxed-effort limits for the specified independent one-lineage model, not Poisson thinning, equal allocation via Jensen, or the general idea of opening several sites. There is identifiable structural overlap with quorum-based activation staircases, but the accessible statements do not establish equivalent coverage; primary and exact companion-record access limits remain.

## value

PASS

A positive opening cost and imperfect common site suitability pose a substantive diversification tradeoff not resolved by equal allocation for a fixed count. The theorem identifies exactly which successive counts can interchange, rules out reversal and skipped integer steps, and quantifies the limiting per-site allocation. It is useful as a solvable baseline for independent-site conservation models, without predicting a real species or claiming validity under correlated risks, discrete effort, or quorum effects.

The dated certificate retains the supplied scientific assessment, sources and limitations.
