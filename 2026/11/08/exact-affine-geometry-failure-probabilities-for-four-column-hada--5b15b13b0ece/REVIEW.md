# Self-review

## Correctness — PASS

The two formulas follow by explicit, exhaustive-in-type occupancy decompositions, not Monte Carlo sampling. Rank is unchanged by column signs and common row-character factors. For the affine-plane case four Walsh row types each repeat \(N/4\) times and full rank is equivalent to hitting every type. For the affine-independent case the eight cube row types each repeat \(N/8\) times; exactly twelve four-corner supports are coplanar. Exact-support inclusion–exclusion yields the second formula. The asymptotics follow from fixed-fraction binomial-ratio products when \(m^2/N\to0\). Numerical edge cases and all \(N=8\) column supports were reproduced with integer arithmetic. The proof covers all \(d\ge3\), \(4\le m\le N\) and both affine orbits.

## Originality — PASS, qualified

The literature comparisons are at the level of logical implication. Tropp's SRHT concentration theorem and Balabanov et al.'s block-SRHT embedding bound do not state these four-column exact binomial laws. Ipsen–Wentworth's published abstract describes coherence-dependent rank and conditioning bounds, not exact affine-orbit formulas; full text was not accessible and thus is not certified as noncovering. A published four-sparse Walsh support theorem excludes the zero-coefficient null vectors that account for the coplanar cube rows, while a published eight-point Walsh spectral-partner census studies orthogonality rather than four-column sample-rank events. Relevant complete public mathematical statements and accessible full primary SRHT manuscripts were read. Publication precedence in older specialized minor-counting literature remains a residual risk.

## Value — PASS

The exact failure probability is a natural quantitative invariant of a widely used numerical sketch, and finite rank loss is an algorithmic failure mode for subspace embedding and preconditioning. The two laws separate coordinate subspaces with identical dimension, coherence and leverage scores. The explicit finite-size ratio \(9/2\) and asymptotic exponential separation show concretely why those summaries cannot determine sharp rank-failure performance. The classification does not claim a bound on condition numbers or general-purpose solver improvements.

## Limitations and independent assessment

Uniform distinct-row sampling and four coordinate columns are essential; the asymptotic regime is restricted. Specialist literature coverage remains incomplete. Independent scientific evaluation is outstanding.

Self-review: passed. Independent audit: not yet performed.
