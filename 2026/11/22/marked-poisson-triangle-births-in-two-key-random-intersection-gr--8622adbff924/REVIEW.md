# Scientific assessment

## Correctness

**PASS.** Pairwise intersecting two-key sets admit an exhaustive deterministic classification as a common-key triple or a three-key cycle. Explicit union bounds at the first-triangle scale eliminate noncommon-key cycles, fourth key occurrences, and multiple witnesses. A coupling to independently sampled keys and independent Poisson clocks proves the marked Poisson process limit. Conditioning and Poisson concentration justify de-Poissonization. The displayed total-variation estimate follows from pair-coupling error, a Poisson occupancy coupling, Le Cam's inequality and the exceptional-event bounds, each explicitly of order at most \(m^{-1/3}\). All quantifiers are for fixed bounded rescaled horizons and \(m\to\infty\). Finite enumerations in `verify.py` test the structural identities without substituting for the infinite proof.

## Originality

**PASS (qualified).** Yağan and Makowski, arXiv:0910.0499v1, directly prove the threshold zero-one laws for triangle existence in the *same* uniform random key-graph model. These results do not imply the critical-window marked Poisson birth process or a quantitative marginal total-variation bound. Arratia, Garibaldi and Kilian, arXiv:1310.7055v1, supply occupancy/collision-process limit mechanisms but not their transfer to graph triangles under within-vertex key distinctness. Rybarczyk and Stark, arXiv:1609.01699v1, study Poisson clique/subgraph counts in the different binomial object-incidence model. The present theorem joins the source-specific third-occurrence process with a structural triangle reduction and controlled finite-scale errors. Related graph-count approximation literature is a historical-priority risk, and no exhaustive priority claim is made.

## Value

**PASS.** Zero-one triangle thresholds do not give the finite critical-window probability of remaining triangle-free, the distribution of the first triangle's witnessing key, or the joint timeline of the first few triangles. Those quantities are natural for clustered networks formed by shared attributes. The marked law and the explicit \(m^{-1/3}\) approximation rate supply a calibrated early-clustering null model without treating intersecting edges as independent.

## Closest literature and limits

The strongest directly comparable primary paper is Yağan–Makowski (2009), whose zero-one threshold and common-key mechanism are acknowledged. The next strongest comparison is the Rybarczyk–Stark subgraph Poisson approximation (2016), which uses independent Bernoulli key inclusion rather than a fixed two-key ring. The multiple-birthday literature already explains the underlying three-hit occupancy scaling, which is not claimed as novel. The theorem is confined to exactly two distinct keys and fixed rescaled horizons. Its quantitative statement is for one-time marginals, not pathwise total variation. Independent mathematical audit is not available.

Self-review: passed. Independent audit: not yet performed.
