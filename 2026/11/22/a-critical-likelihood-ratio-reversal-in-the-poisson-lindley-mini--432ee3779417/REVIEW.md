# Scientific review

## Correctness — PASS

The theorem is about the exactly specified stationary Poisson–Lindley minification chain with positive parameters and the explicit admissibility boundary. The geometric/negative-binomial mixture identity gives the innovation survival and allows admissibility to be verified independently by a single quadratic inequality. A shared-summands coupling proves strict stochastic monotonicity. The first two transition columns yield an exact adjacent-minor determinant; the crucial initial sign is supported by a rational identity with a finite polynomial of strictly positive evaluations for every positive parameter. Strict monotonicity of the determinant's scalar bracket supplies the unique real crossing and all integer-index signs. A separate boundary calculation and derivative give the critical escape-rate limit. The standalone checker confirms the finite identities and provides a rational positive/negative adjacent-minor witness; no inference from finite data is used to claim the infinite-index theorem.

**Residual correctness risks:** The algebra is lengthy and remains subject to independent review. The model's two-column theorem does not classify other output columns or establish global TP2 behavior at the admissibility endpoint.

## Originality — PASS, with qualified historical priority

The 2024 model paper already supplies the modified-negative-binomial operator, the stationary law, the innovation survival and the transition probabilities; none is claimed as new. The full-text theoretical and appendix portions of that article were compared with the newly proved global-in-state two-column minor sign law, its exact boundary and the critical escape-rate limit. The source does not provide these classifications. Qian and Zhu's 2022 explanatory-variable minification model addresses ergodicity and statistical inference; its accessible abstract provides no such statement, but its body was inaccessible. The 2026 Poisson-weighted-exponential minification article has a distinct marginal distribution and, in the inspected sections, treats transitions and estimation instead of this sign law. Published-literature searches for analogous conditional-ordering and total-positivity results did not identify a covering theorem. The related geometric NonLINAR model studied by Barreto-Souza et al. (2023) uses an alternative thinning operator and additive innovation, so it does not imply this Poisson–Lindley minification result.

**Residual originality risks:** A general minification theorem in inaccessible older full texts could subsume part of the calculation. Mathematical priority remains provisional; absence from search hits does not prove uniqueness. The published transition formula makes evaluation possible but does not itself establish the all-state sign classification without the positive-coefficient and monotonicity arguments.

## Value — PASS

The work resolves a natural structural distinction in a fitted count-series family: strict first-order stochastic monotonicity does not imply likelihood-ratio monotonicity, and the distinction has a sharp dependence on whether the thinning parameter is at the boundary or strictly interior. The unique crossing index tells precisely where comparisons between neighboring preceding counts fail even in the two most probable low-count output categories. The reciprocal-distance divergence quantifies why near-boundary finite state samples may conceal the failure. These properties inform order-constrained inference, reliability interpretation and likelihood-ratio-based arguments without asserting downstream empirical improvements.

**Scientific limits:** Results address adjacent preceding states and the first two output columns only. No empirical data analysis, full kernel minor census or reversibility classification is provided.

Self-review: passed. Independent audit: not yet performed.
