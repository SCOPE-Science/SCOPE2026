# Review of the priced four-cycle spectral-gap result

## Correctness — PASS

Two independent analytic Rayleigh upper-bound mechanisms apply on the ranges \(0<d\le3\) and \(d\ge3\). Explicit feasible weights attain both bounds. Equality in two distinct mode certificates forces **every** maximizer in the first regime; equality in the path certificate yields the exact critical segment and the unique path solution past the threshold. The reflected eigenspace calculation verifies the stated multiplicities. The standalone exact-arithmetic verifier passed 12 symbolic identities, 27 rational spectra, four critical allocations and 1,440 rational competitor certificates. Finite checks corroborate, rather than replace, the all-real-parameter argument.

## Originality — PASS on inspected evidence, with residual priority risk

Sun et al. (2006), *The Fastest Mixing Markov Process on a Graph*, DOI 10.1137/S0036144504443821, is the principal antecedent: it covers the general SDP formulation, arbitrary edge prices and the complete priced-path problem. Its section 5.3 gives uniform-cost cycle formulas and a two-dimensional realization fact for priced cycles, but not the exact one-defect four-cycle optimum or all equality cases. Boyd et al. (2009), DOI 10.1137/070689413, and Gerencsér et al. (2015), DOI 10.1109/ECC.2015.7330635, optimize discrete-time cycle mixing under different constraints. The path endpoint of the present formula is not claimed as separately original. Specialist works not located by the inspected searches could still establish equivalent formulas.

## Mathematical value — PASS

The four-cycle is the smallest nontriangular network with alternative routes. Changing one edge price models the simplest departure from uniform network design. An exact global classification distinguishes a positive full-cycle optimum, a genuine interval of nonunique optima at the ninefold price threshold, and a unique path optimum above it; Fiedler multiplicity changes with these phases. The full characterization is a natural, reproducible benchmark for constrained spectral graph optimization, notwithstanding its intentionally limited network size.

## Limits

The statement excludes general cycle sizes, nonreversible chains and discrete-time mixing-radius objectives. The analytic result is complete only under the specified single-exceptional-price model. Exact computational replay is supplemental. Publication priority and mathematical verification have not been independently established.

Self-review: passed. Independent audit: not yet performed.
