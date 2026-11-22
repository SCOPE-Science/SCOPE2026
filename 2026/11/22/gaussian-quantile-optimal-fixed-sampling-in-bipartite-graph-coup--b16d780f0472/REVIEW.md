# Self-review

**Object and conclusion.** The single assessed theorem concerns i.i.d. fixed class-source selection on complete bipartite graphs. It proves a binomial-strip completion law, a piecewise-normal asymptotic profile, the exact asymptotic optimizing Gaussian quantile, and the linear-waste distinction for uniform-vertex sampling.

## Correctness — PASS

The key coupling is exact: an \(A\) source covers one \(B\) vertex until the target class is exhausted, and vice versa. Thus the completion event is a binomial count interval for all finite positive class sizes. The proof gives a conditional negative-binomial expectation identity, a triangular-array binomial CLT and uniform-integrability argument. Strict positive curvature of the normal mean profile and quota waiting-time lower bounds prove the asymptotic claim for every finite optimizer. The packaged exact-rational state-space checker passed 1,470 assertions. Finite checks are corroborative rather than a substitute for proof.

## Originality — PASS against inspected material, with residual risk

The closest primary source is Deng–Wang, arXiv:2611.11345v1 (2026-11-08). Its Corollary 4.2 concerns fixed-degree biclique survival tails, Proposition 5.1 a repeated-coupon reduction for unions of bicliques, and Proposition 5.2 a balanced-binomial lower bound for two cliques. These contain no optimized nonuniform source-class choice or the present nonzero quantile correction. Dimitrov–Plaxton (2013) study uniform source vertices and optimize the covered-neighbor decision. published-finding corpus records on biased biclique random walks address dependent path-constrained sources, not i.i.d. class choices. General two-quota sampling theory remains a possible priority risk; failure to locate a match is not a claim of absolute novelty.

## Value — PASS

The structural gap is a practical and mathematical one: a degree-imbalanced biclique requires quotas of source appearances opposite to vertex proportions. The theorem characterizes the best stationary sampling design to square-root precision, including an asymmetric non-Gaussian limit and a specific nonzero quantile correction, while uniform vertex sampling wastes a positive linear proportion of all rounds when class fractions differ.

## Scope and limitations

The optimum excludes adaptive/periodic/dependent source selection and requires limiting proportions in \((0,1)\); it is not an all-graph cover-time statement. No explicit convergence-rate bound or independent mathematical audit is asserted. The published published-finding corpus matches were compared using accessible scientific summaries; the inaccessible full text is disclosed in the structured audit.

Self-review: passed. Independent audit: not yet performed.
