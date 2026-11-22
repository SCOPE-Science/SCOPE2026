# Scientific review

## Correctness — PASS

A complete proof covers all \(n\ge2\), \(0<p<1\), \(\lambda>0\), \(H>0\): the affine exponential survival recursion, strictly negative-definite objective Hessian, adjacent stationarity identities, explicit unique root, and the equality and subthreshold boundaries. In particular, equality of adjacent marginal returns forces equal pre-search stocks before the final visit. Global optimality is proved by strict concavity, not by the numerical search. The standalone checker passes 15,020 tests including exact-rational agreement of two constructions of expected discoveries and independent numerical evaluations.

## Originality — PASS, qualified by accessible evidence

The closest directly relevant sources are Korner-Nievergelt et al. (2011), which calculate detection corrections at regular intervals; Etterson (2013), which establishes estimation schemes handling irregular search intervals; the 2015 *carcass* tutorial that discusses such calculations; and Wolpert (2015), which gives a generalized mortality estimator. These sources establish portions of the stochastic model, but the inspected full primary material does not state the strict-concavity optimizer, its arbitrary-\(n\) equal-middle-gap structure, constant first–last offset, or exact collision threshold. Relevant indexed optimal ecological snapshot and Markovian-availability results have different state and objective definitions; none was found to imply the present all-\(n\) result. Important limit: Etterson's complete 2013 text was not accessible, despite an open repository attempt, so its full historical priority remains a residual risk; a broader unindexed inspection theorem is also possible. No claim of exhaustive priority or independent certification is made.

## Value — PASS

Repeated missed-carcass detection and scavenger loss are recognized determinants of monitoring quality. A complete global maximizer at every sufficiently long finite horizon, an exact boundary at which independent visits cease to be separated, and the horizon-independent endpoint offset are actionable analytical benchmarks for the detection-count objective. The theorem is not a restatement of a known correction factor or a tiny numerical optimization gain. It illuminates why equal-interval designs, often used to represent changing mortality over calendar time, need not maximize detection under strictly homogeneous arrivals. It is not a field protocol: heterogeneity, uncertainty, visit costs and estimator variance can change the optimum.

Self-review: passed. Independent audit: not yet performed.
