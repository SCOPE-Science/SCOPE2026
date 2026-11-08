# Scientific review

## Correctness — PASS

**Defined model.** Every edge is a distinct good worth exactly one to each of its two endpoints, all agents compare their own value plus external payment to everyone else's allocated goods plus payment, and each edge must be given to an endpoint. Isolates are included. The deterministic subsidy identity is derived directly by a tree-indegree deficit and globally propagated cash envy, then achieved by constructive orientations. The stochastic proof has the exact exponent for tree-component counts, separate bounds on all component sizes, all factorial moments for isolated edges, and second-moment concentration for isolated vertices. The scaled distribution and expectation follow from the exact finite identity, not from simulation. Small enumeration checks: 81 graph cases, two numerical expectation examples. Finite verification cannot certify the infinite limits.

**Risk and boundaries.** The result is false without globally comparing monetary payments, or if isolates are excluded; it does not cover nonunit or asymmetric edge values. The sparsity window is fixed in \(c\); no uniformity in \(c\) is asserted. Independent validation has not occurred.

## Originality — PASS (best knowledge)

The stochastic Bernoulli mixture and the critical window are the exact contribution assessed. The 2025 binary graph-orientation subsidy algorithm covers closely related deterministic component reasoning; the 2026 IJCAI paper already describes an isolated edge amplifying subsidies to isolated agents. These are *not* independently claimed as new. The 2026 arXiv paper of Wu studies random continuous agent-good valuation matrices and thus has a distinct sampling law and feasible allocation set. The new statement cannot be obtained by taking a direct corollary, renaming variables or choosing parameters in the latter paper. Searches for Poisson isolated edges and rare tree components on the one hand and random envy-subsidy orientation on the other, including the indexed research corpus, returned no matching combination. Classical isolated-edge Poisson counts are acknowledged as background, not mathematical priority claimed here.

**Risk.** Novelty remains a best-knowledge judgment: a random-graph extension hidden in an unindexed chapter or appendix, or a general theorem covering this compound stochastic invariant, could imply the statement. The statement deliberately narrows novelty to the combined distribution and mean law and does not claim uniqueness of mathematical discovery.

## Value — PASS

Sparse resource networks frequently contain many inactive agents, and subsidized fairness uses comparisons across the entire agent set. A single nontrivial tree forces a monetary transfer to all isolates. It is not evident a priori at what density this rare shock occurs, whether higher-order trees matter, or what the exact total-payment distribution is. The theorem gives a natural parameter window, an explicit Poisson defect intensity, a nondegenerate two-point limiting law for the *optimized* subsidy and its limiting mean, and a complete structural bridge from individual instances to stochastic network planning. These are quantitative, consequential results in the graph-orientation envy-with-subsidy setting, not a merely renamed count or arbitrary small-parameter computation.

**Risk.** The theorem is specialized to symmetric unit-valued sparse graphs; alternative market models may behave differently. Its proof builds on standard graph enumeration and known deterministic subsidy ideas; the value is in their exact, nontrivial joint transition rather than a new probability technique.

## Closest literature and limitations

- Li, Sun, Suzuki and Xing, arXiv:2502.13671 (19 February 2025), sections on binary additive graph-oriented subsidies, full primary transcription checked.
- Li, Sun and Xing, IJCAI 2026/387, full primary text checked; isolated-vertex propagation is a known example.
- Wu, arXiv:2610.10272 (7 October 2026), full HTML primary sections checked; different iid continuous value model.
- Index searches on exact claim, aliases, broader randomized subsidy models and graph tree counts had no dominating recorded claim; absence in an index is not a proof of originality.

Self-review: passed. Independent audit: not yet performed.
