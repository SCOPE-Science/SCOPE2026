# Independent mathematical audit

## correctness

PASS

For E_{a,b}, a is the target and b the source. The forced edge a→b and external restrictions X_b≤X_a give the exact single-event weight. Two events with the same target require two forced edges and have five allowed assignments out of eight at every external vertex; the remaining internal edge is free. Reversal gives the same weight for the shared source. Counting unordered pairs yields B_n with half from each type. Reciprocal events conflict; a three-vertex chain forces a transitive triangle and allows four of eight external patterns; disjoint endpoints have two independent restrictions of weight 3/4 per outside vertex. For triples, reciprocal constraints enforce equality; a triangle allows at most four of eight assignments; a star with k arcs of one orientation has 2^k+2^(3−k)≤9 of sixteen. In the three-edge path, each failed implication has weight 1/4, the disjoint pair has 1/16, and each adjacent pair has 0 or 1/8. If both adjacent intersections are nonzero, the triple fails simultaneously with weight 1/16, giving valid weight 1/2; otherwise it is smaller. The remaining disconnected patterns have weights at most 15/32 and 27/64. The independent enumeration also confirms the sharp triple bound. Conditioning on internal edges leaves independent external blocks, giving S_3≤binom(N,3)(9/16)^(n−6) for n≥6. Bonferroni gives the claimed union error after subtracting the noncluster pair mass. The bound binom(w,2)−1_{w≥2}≤2 binom(w,3) gives the two-obstruction asymptotic. At W≥3 at most 3S_3 pair mass can contribute in expectation, so each shared-coordinate type accounts for B_n/2+o(B_n) among exactly-two cases; their overlap is impossible for two distinct events.

## originality

PASS

The supported distinct result is the second-exponential overlap correction, with its explicit smaller-base error and the conditional two-obstruction law. The one-pair probability, universal-kings prevalence, and the uncovered-set formulation are prior. A later indexed refinement expressly uses the correction and adds a different statistic. Reasonable access attempts did not yield Maurer's full text; that historical risk does not decide the review.

## value

PASS

The correction identifies the dominant dependence mechanism, not just a small improvement in the error term. It gives the leading probability of multiple failures, the exponential separation from other overlap patterns, and an exact description in the limit of how the two obstructions typically share an endpoint. The result refines a classical tournament property at a scale that the first moment cannot distinguish.

The dated certificate retains the supplied scientific assessment, sources and limitations.
