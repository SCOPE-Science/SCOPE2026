# Self-review

## Correctness — PASS

The exact preservation problem reduces to independent set: no retained coordinates may duplicate a new stratum, while arbitrary independent retained points can be completed using unused-coordinate-stratum pairings. Every new stratum is narrower than every original stratum; thus the two-coordinate conflict graph is the union of two matchings and has only paths and even cycles. The one-step collision indicators are independent except at neighboring positions, giving the exact expectation \(n(n-1)/(6(n+1))\) per axis and limiting matching incidence \(1/3\). Uniform permutation labels make the other colour's partial matching conditionally uniform; bounded alternating component explorations and independent two-root limits yield the displayed limiting odd-path densities. The exact component matching-number identity then gives deletion fraction \(1/4\), and the full-retention probability follows from summing all monotone binary strings. The standalone checker passed 46,948 assertions, including exhaustive small-instance independent-set comparisons; the infinite claim is analytic.

## Originality — PASS, with residual risk

Liu–Li–Yang (2015), https://doi.org/10.1155/2015/450492, supplies the maximum-independent-set formulation, not the two-coordinate two-matching specialization or the sharp random one-step retention fraction. Yang–Liu–Li (2017), https://doi.org/10.1080/00949655.2017.1368080, addresses faster extension by graph blocks and bounds, but full text remained inaccessible; its accessible abstract does not establish the present limit or exact one-step full-retention law. The full 2015 article's sections 2–4 were reviewed. The separate random-graph paper by Gamarnik–Nowicki–Świrszcz treats Erdős–Rényi or regular-graph ensembles rather than this Latin-hypercube re-stratification law. No claimed general graph-theoretic technique is represented as new.

## Value — PASS

The minimum retained-evaluation problem for increasing a Latin-hypercube size is specifically motivated by preserving expensive existing simulations. For planar designs the result replaces a general exponential-time search by a deterministic exact linear procedure at every larger target size. For unbiased random designs, adding just one target stratum nevertheless requires replacing a quarter of prior evaluations asymptotically; the exact exponentially small all-retained probability quantifies the complementary rare event. Both the computation guarantee and the sharp cost constant apply to the natural optimization objective, rather than an arbitrary statistic.

## Limits

The general structural theorem covers exactly two coordinate dimensions; the probability limit covers independent random jitter, random column pairing, and \(n\to n+1\) extension. It does not cover deterministic optimized designs, other dimensional regimes, or a central-limit rate. A relevant 2017 follow-up was available only as an abstract; independent historical-priority and mathematical audits remain outstanding.

Self-review: passed. Independent audit: not yet performed.
