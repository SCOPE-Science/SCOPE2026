# Scientific review: homophilic one-shot rewiring on bounded-degree trees

## Correctness — PASS

The claim is for a specified one-shot edge-replacement experiment, not for unbounded adaptive updates. On the original tree, the two seeded vertices activate only \(u\), leaving \(v\) at exposure \(1/4\). The proof partitions the only three initial mixed-status edges into two \(u\)-edges and one \(v\)-edge. Every legal recipient of a rewired \(u\)-edge becomes eligible after \(u\) adopts, and the threshold \(\theta<1/3\) transmits activation along the path; a rewired \(v\)-edge never produces additional adoption because \(v\) has at most one adopter among four neighbors. Hence the exact distribution is \(\{3:1/3,m+6:2/3\}\), with expectation \(5+2m/3\). An independent exact-rational exhaustive checker enumerated the complete allowed one-rewiring sample space for 20 sizes and three threshold choices (60 finite parameter instances), without numerical tolerances or sampling.

The proof handles the strict-threshold boundary \(\theta=1/4\), the terminal-path case \(m=1\), both edge orientations, and every legal recipient. Infinite sizes are covered by constructive local arguments, not extrapolated from these computations. No claim about ongoing rewiring or arbitrary graphs is made.

## Originality — PASS (best-knowledge, with priority risk)

Min and San Miguel's arXiv:2305.13965, Sections II–IV, defines the homophilic edge move and reports that network plasticity may increase cascade sizes in a large random-graph parameter regime. This earlier *qualitative* enhancement is expressly not claimed as new. Its equations and simulations do not state or imply that every eligible recipient of either of two specified edges in a connected bounded-degree tree triggers a global cascade, nor the exact two-point distribution and growing mean under a single sampled move. Eckles et al., arXiv:1810.03579, address long-tie interventions with noisy and absolute-threshold mechanisms on cycle-derived graphs, not the strict fractional threshold and status-directed edge replacement used here. Ebrahimi et al., arXiv:1404.2668, analyze absolute-threshold spread on growing preferential-attachment networks, not this one-step rewiring sample space. Published mathematical-results index hits on conversion/2-burning concern different operations, optimizing source numbers or static-graph closure, and do not dominate the stated law.

Search did not identify an exact covering result. This is **not** a proof of worldwide uniqueness. Priority uncertainty remains for unindexed manuscripts or equivalent formulations, particularly elementary sensitivity constructions in the broad Watts-threshold literature.

## Value — PASS

The natural question is whether homophilic adaptation—each individual rewiring away from an already adopting neighbor—must suppress a threshold contagion. Prior large-network work documents a complicated enhancement/suppression tradeoff but does not quantify how severe a gain can be with just one contact change and a connected initial network. This theorem provides a fixed-threshold, bounded-degree family showing an *unbounded* response to one such move with a nonvanishing \(2/3\) success probability and an exact mean, not an arbitrarily chosen finite computation. It separates the strength of topology-induced connectivity changes from mere joining of initially disconnected components and furnishes a reproducible worst-case benchmark for interpreting adaptive cascade simulations.

## Remaining limitations

The exact law applies only when the one mixed-status edge is selected uniformly, its susceptible endpoint chooses a uniformly random nonneighbor susceptible, and all later network evolution is frozen. It does not quantify the full ongoing-stochastic-rewiring model's terminal distribution, nor assert comparable growth for typical random networks. The scientific-priority risk above remains. Computational checks are finite and do not constitute independent certification.

Self-review: passed. Independent audit: not yet performed.
