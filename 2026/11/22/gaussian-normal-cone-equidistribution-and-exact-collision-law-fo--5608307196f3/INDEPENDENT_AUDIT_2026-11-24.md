# Independent mathematical audit

## correctness

PASS

The clique half-integral vertex list follows from tight pair equations and perturbation of unanchored bipartite components; positive half-support of size at least three is uniquely fixed by its tight pairs, with zero coordinates fixed separately. Under continuous Gaussian directions ties have probability zero. On sign support S the best half-support score is half the positive sum if |S|≥3; no other half-support can equal it. A singleton wins iff its positive weight exceeds the sum of the other positive weights, also for one or two positive coordinates. Thus independent fair signs and half-normal magnitudes give the displayed angles, and independent repetitions give the sum of squared angles. The exponential Markov bounds sum to a relative collision error O(n(0.9)^n), since (1+ρ)/2≈0.7615783 and 2m²≈0.8927206, independent of n. Conditioning on the successful half-support classifier and comparing to the sign support gives the first total-variation bound. For the collision-conditioned bound, multiply unnormalized collision weights by 2^n and push the integral vertices to the empty support. Before normalization the half-support weights are 2^−n q_k². Their deficit relative to uniform subsets, plus the omitted k<3 mass and the entire added integral collision mass, is O(n(0.9)^n); normalization preserves this order and pushing forward to cardinality contracts total variation. A binomial CLT then applies. Independent finite cross-check: at n=3 the three disjoint half-normal failure cones have one representative with rays (1,0,0),(1,1,0),(1,0,1), giving via the three-ray solid angle q_3=1−(12/π)arctan(3−2sqrt(2))≈0.3509593122 and angle q_3/8≈0.0438699140. This tests normalization, not the asymptotic. No supplied script was executed and no replay of its full LP count is claimed.

## originality

PASS

The polytope and half-integral vertex list are known. The distinct result evaluates its Gaussian exposure law, leading collision constant and collision-conditioned support law. The plausible normal-cone and collision matches use different polytopes and probability laws; standard conic projection/angle formulas do not by themselves give these full-clique asymptotics.

## value

PASS

The fractional stable-set clique relaxation is a standard polytope. Exact exposure weights describe the bias of a natural random objective, while the coincidence probability and rare-event-conditioned law distinguish whether its normal-fan mass is diffuse or concentrated. The collision metric is sensitive to overweight exceptional vertices; showing such weights are negligible on the collision scale is more informative than ordinary total-variation equidistribution alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
