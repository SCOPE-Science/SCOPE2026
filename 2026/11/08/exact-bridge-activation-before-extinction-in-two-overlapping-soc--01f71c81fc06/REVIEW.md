# Self-review

## Correctness: PASS

The theorem specifies the exact two-edge Poisson jump mechanism, threshold-one source, initially active overlap and inactive target-only vertices, and the first target-clock event. A renewal decomposition at source-group firings gives \(P=S/(S+E)\). Its critical computations are the success probability \(S=\mathbb E\int_0^{T_B}\beta e^{-(\alpha+\beta)t}dt\) and the extinction probability \(E=\mathbb E e^{-\alpha T_A-\beta T_B}\). A uniform death-order permutation and independent exponential spacings yield the binomial-weight products and finite sums. Expanding all \(a\) Laplace factors proves the universal coefficient, rather than relying on numerical extrapolation. An independently assembled full-state rational chain confirmed 56 instances, and a compressed rational chain 165 more; no unproved infinite extrapolation is made. Critical assumptions are independent exponential death and group clocks, two edges only, and fixed parameters in the asymptotic.

## Originality: PASS, with residual priority risk

The direct motivating full open article by de Arruda et al. presents the hyperedge Poisson rule, phenomenology of bridging groups, and exact one-hyperedge hyperblob analysis, but does not state or imply a finite expression for the target's first firing before extinction in two genuinely overlapping groups or the overlap-independent power law. St-Onge et al. use one-vertex activation by a group in their full-text Methods and therefore do not cover the simultaneous full-group event; their results concern approximate master equations, phase transitions, and seeding. Higham–de Kergorlay likewise employ nodewise SIS infection, with spectral extinction bounds rather than the target-event law. Queries for stochastic hypergraph bridge invasion and order-statistic first passage produced no covering mathematical records. A contemporaneous supplementary file to the direct article was not fully readable, and unindexed equivalent work remains a priority risk. Negative search results are not asserted as proof of uniqueness.

## Value: PASS

Hyperedge intersections are the mechanism behind cross-community activation in the motivating work, yet even the elementary two-group event is affected by both finite-population extinction and recovery-dependent erosion of bridge eligibility. The result provides an exact, polynomial-size expression in place of an absorbing microstate calculation, a precise zero-versus-positive overlap threshold, a concrete rational test case, and a non-obvious universal \(\alpha^{-(a-1)}\) bridge-failure law whose leading coefficient does not depend on how many overlap vertices are required. It can serve as an exact benchmark when selecting or evaluating bridge arrangements and internal reinforcement strengths. It is not presented as a general hypergraph phase-transition theorem.

Self-review: passed. Independent audit: not yet performed.
