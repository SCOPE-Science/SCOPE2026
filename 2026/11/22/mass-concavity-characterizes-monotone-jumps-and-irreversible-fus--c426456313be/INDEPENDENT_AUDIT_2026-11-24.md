# Independent mathematical audit

## correctness

PASS

Strict convexity gives uniqueness. Summing the stated signed subgradient equations on a constant block gives its affine mean shift; cumulative flux at an internal edge must stay in [-lambda a_j,lambda a_j]. For each fixed signed partition those flux inequalities and the primal signs are linear in lambda, giving a finite piecewise-affine continuous path. At a nonzero middle gap the absolute-gap derivative is bounded by a_l/P+a_r/Q-a_i(1/P+1/Q) for the two block masses P,Q. Mass-coordinate concavity makes this nonpositive by the chord inequality; continuity covers simultaneous hits, ties and lambda=0. For a failed inequality, singleton blocks on strictly increasing data give the claimed strictly positive initial slope. For the split witness put c=(qA+pC)/(p+q)>B and K=pq delta/(p+q). Holding the failed pair fused requires internal subgradient c/B-K/(B lambda), which traverses [-1,1] from K/(B+c) to K/(c-B); beyond the latter the positive singleton gap slope is (p+q)(c-B)/(pq). Outside gaps can be chosen larger than the sum of adjacent uniform shift bounds lambda(a_j+a_{j-1})/m_j over any fixed interval ending after the split. This verifies the construction even at an end edge. The displayed three-site witness checks exactly: for example in its fourth piece the fluxes are lambda and 50+lambda/2, the latter admissible at and after 100/7, with first gap 49-3lambda/2. On the final block the fluxes 98/3 and 199/3 are admissible from 98/3. The four joins and all remaining signs and fluxes match.

## originality

PASS

The distinct contribution is the sharp three-way, all-data classification, in particular the necessity for irreversible fusion demonstrated by a positive-length split at every violated inequality. The sufficient direction is covered by prior generalized-lasso results, not just by the classical unweighted path theorem: after normalization the condition is diagonal dominance, and the known dual Lipschitz estimate gives absolute-gap shrinkage by complementarity. Prior unit-mass weighted-path work gives individual instances and a necessary condition on an actual event, not a construction at every failed mass-coordinate inequality. The condition itself also appears for other evolution/comparison problems; no novelty is assigned to the inequality in isolation.

## value

PASS

The converse gives a usable sharp criterion for deciding, from weights and fidelity masses alone, when all signals admit a merge-only path. Failure at any one edge is certified by actual positive-interval fusion and separation, not just by a dual boundary event. The gap-strengthening and cumulative-mass geometry connect the classical path algorithm to sharply separated stable and unstable parameter designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
