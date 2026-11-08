# Scientific review of the full-clustering atom

## Correctness

**PASS.** With the precise capped Pareto model, the rescaled extreme weights converge to the intensity \(\lambda\alpha t^{-1-\alpha}dt\) Poisson process. For each fixed extreme cutoff, all hub-hub edges are deterministically present eventually. An explicit truncated-first-moment estimate bounds the fraction of roots adjacent to smaller weights; a conditional law of large numbers for edges to finitely many hubs gives empirical convergence. Poisson thinning yields the analytic mean. The unit atom equivalence is proved exactly by counting points above one and showing a positive chance of fewer than two incident edges when this count is at most one. Finite checks corroborate the algebra but do not establish the infinite theorem. Risk: limits are in distribution, not stronger coupling or almost sure convergence.

## Originality

**PASS on the currently inspected literature, with a material historical-priority risk.** The 2026 capped-model primary paper establishes random-environment limits for components and degrees, not an exact local-clustering atom in its abstract; its entire full text was inaccessible. The accessible full-text HTML of the highly relevant 2026 Catanzaro–van der Hofstad–Garlaschelli paper was inspected in its central model, main theorems, local clustering discussion, and non-self-averaging statements. It establishes that low-degree nodes are nearly cliques and that average local clustering can fail to self-average **for the exponential kernel**, so those phenomena are explicitly excluded from the originality claim. It cannot directly supply a positive endpoint atom, because exponential edge probabilities never equal one at finite arguments. The 2022/2025 Avena–Garlaschelli–Hazra–Lalli full HTML was inspected; it addresses the exponential model and says that local clustering is not considered. The exact hard-saturation atom remains a genuinely distinct sharp boundary, subject to possible coverage in inaccessible capped-model full text or other unlocated work.

## Mathematical value

**PASS.** Averages in strongly inhomogeneous graphs can concentrate or fluctuate, and the endpoint structure of their limiting law is a natural diagnostic. The exact positive probability of an empirical clustering coefficient tending to one has a direct mechanism: the existence of at least two universally adjacent extreme hubs. The exact mass \(1-e^{-\lambda}(1+\lambda)\) distinguishes two standard connection rules despite their shared heavy-tail regime and related typical clustering phenomena. This is a motivated invariant of the same natural critical random-graph model, not a numerical slice or a rebranding of general clustering.

## Closest sources and remaining uncertainty

- Andreis, Avena, Hazra, Matteini, arXiv:2610.29564: **same capped model**, full text unavailable; abstract read; cannot assert whole-document noncoverage.
- Catanzaro, van der Hofstad, Garlaschelli, arXiv:2603.13159v1: **closest substantive clustering result**, full HTML with supplementary discussion read; exponential kernel and non-self-averaging already covered; the exact saturation atom is not.
- Avena, Garlaschelli, Hazra, Lalli, arXiv:2212.08462 and journal article: full HTML read; exponential kernel, wedges/triangles, not local clustering.
- Public mathematical-result searches returned no claim concerning this exact atom; search absence is not uniqueness proof.

Self-review: passed. Independent audit: not yet performed.
