# Scientific assessment of critical product-hazard network relaxation

## Correctness — PASS

The statement fixes a connected finite undirected loopless graph, a positive unit Perron vector, exact critical transmission \(\beta=\delta/\rho\), and interior recovery probability. The analytic proof separately establishes all-vertex positivity, global extinction (using a uniform positive drift contradiction), Perron alignment (the primitive linearization and a forced contraction), the exact second-order coefficient, and the reciprocal-amplitude asymptotic. The coefficient is strictly positive even for bipartite graphs because the linear map has positive diagonal. The included checker confirms the quadratic identity across 3,084 small-graph/parameter tests and the predicted global profile on five topologies. Finite tests are not substituted for the proof.

## Originality — PASS, qualified

The exact nonlinear probability map and its threshold come from Chakrabarti et al. (2008), and Dung–Phuc (2026) contributes the community threshold set. The 2008 full text, including Theorems 2–4 and its appendices, covers strictly subcritical exponential decay, not the exact critical polynomial decay or its coefficient; the 2026 full text covers threshold comparisons, not temporal asymptotics at equality. The 2019 Prasse–Van Mieghem additive Euler NIMFA model and its 2020 continuous-time treatment have a distinct quadratic nonlinearity. The general \(t^{-1}\) phenomenon is standard for scalar parabolic dynamics and is not claimed as new. The distinctive claim is the globally valid network-specific constant and its explicit product-collision correction; an unindexed independent proof remains possible.

## Mathematical value — PASS

A spectral threshold alone does not quantify how slowly infection vanishes at the boundary: the theorem supplies the precise large-time coefficient for every connected finite network and any nonzero initial profile. It collapses a potentially neighborhood-dependent quadratic collision sum into the spectral pair \(\rho\) and \(\sum v_i^3\), and exhibits the quantitative discrepancy between different models with the same linear threshold. This makes a substantive, independently usable critical prediction, not a mere renaming of the strict-threshold results.

## Evidence and limits

Primary sources examined: Chakrabarti et al. 2008, https://www.cs.cmu.edu/~jure/pubs/virus-tissec.pdf (recurrence, theorem, and appendix text); Dung–Phuc 2026, https://arxiv.org/abs/2607.14048 (full article); Prasse–Van Mieghem 2019, https://arxiv.org/abs/1903.08027 (full HTML equation and assumptions); Prasse–Van Mieghem 2020, https://doi.org/10.1007/s00285-020-01542-6 (full OA article). Related searches did not locate a same-product-map, same-critical-coefficient statement, but no search can prove uniqueness. The model is deterministic and independence-closed, not the true finite SIS Markov process; directed networks, \(\\(\delta=1\)\), and infinite-network limits are excluded. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
