# Review: exact metric inballs of path matchable-subgraph polytopes

## Correctness — PASS
The object is the zero-inclusive perfectly matchable vertex-subset polytope, realized by the full-rank unsigned path incidence map from the path stable-set polytope. The metric is explicitly the Gram form with diagonal \(2\) and adjacent entries \(1\), not an unspecified affine-equivalent metric. Its exact inverse gives every facet's intrinsic Euclidean normal length. Combining two coordinate lower bounds with each adjacent upper bound proves a global ball-radius upper bound, and the weight-proportional center attains it. Equality conditions and a strictly feasible relative-interior perturbation prove the complete incenter affine dimensions, including the small cases. Checks on the actual delivered `verify.py` independently corroborate exact Gram inversion, vertex sets, facet distances, LP optima and optimizer constraints. The proof covers all integers \(n\ge3\); finite experiments are not substituted for an infinite proof.

## Originality — PASS (provisional priority)
The defining 2022 paper by Mori studies algebraic properties of these polytopes, not the metric claim. The 1983 foundational bipartite formulation is credited, though its publisher full text was not accessed. The closest published indexed stable-set result computes ordinary-metric facet areas, while the present Euclidean image has a nonorthogonal incidence Gram form. Full-text comparisons of path connected-block, path symmetric-edge and alternating adjacent-sum results show different bodies or metrics and no implication of this incenter theorem. Actual published-finding corpus alias and implication searches found no equivalent indexed claim. The residual risk is an earlier unindexed weighted-stable-set or network-polytope incenter formula; database absence is not novelty proof.

## Mathematical value — PASS
The natural vertex-subset embedding is the defining realization of perfectly matchable subgraph polytopes. Its complete maximum-ball and all-center calculation gives a geometrically motivated new invariant across a Fibonacci-size infinite family, including an odd/even optimizer-dimension split. The theorem also demonstrates a substantial geometric distinction: the very same combinatorial polytope has constant inradius and a unique optimal center in natural edge coordinates, yet radius \(\asymp n^{-1/2}\) and nearly full-dimensional center freedom in vertex coordinates. This comparison motivates why the precise metric answer matters beyond routine LP calculation.

## Remaining limitations
Priority is provisional, no publication is asserted, and independent mathematical audit has not been performed. The closed-form optimal center **set** is given by inequalities, not an enumerated face lattice.

Self-review: passed. Independent audit: not yet performed.
