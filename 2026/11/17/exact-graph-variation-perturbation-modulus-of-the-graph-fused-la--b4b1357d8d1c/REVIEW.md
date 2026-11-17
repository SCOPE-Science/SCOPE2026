# Mathematical review

## Correctness

PASS. The graph fused-lasso KKT condition, its locally affine connected-component averaging derivative, and the weighted coarea identity imply the finite partition-and-cut upper bound. Conversely, for any connected partition and input cut, a block-constant primal signal and a dual field zero on internal edges and saturated with the proper signs on exterior edges construct a valid proximal point. Small internal spanning-tree flows absorb any cut perturbation, realizing the block average exactly. The barbell witness then has one-edge input cut and \(t(q-t)\) output variation, giving a quadratic lower bound. The universal quadratic upper bound follows from oscillation contraction under averaging. Exact rational diagnostics reproduce the finite identities; the analytic argument handles arbitrary finite graphs.

## Originality

PASS, with bibliographic uncertainty. Tibshirani–Taylor (arXiv:1005.1971, Section 10, Lemma 3) already prove local affine projection structure, and their Section 6 gives connected fused blocks. The current result uses these established ingredients but asserts a new global graph-BV two-input constant through cut tests and *realizability of all connected partitions*, plus a quadratic barbell amplification law. Madrid Padilla–Scott–Sharpnack–Tibshirani (arXiv:1608.03384, Sections 1–3) study graph BV denoising, rates and DFS comparisons rather than input-to-input graph BV norms. Kirisits–Scherzer–Setterqvist (RICAM Report 2018-24, Sections 1 and 3) establish per-input convex minimality, not BV contraction of differences. Related tree projection calculations do not imply the all-graph formula or the cyclic barbell construction. Searches of relevant mathematical records and literature did not locate a stronger theorem already implying the full statement, but this absence cannot establish uniqueness. The major residual risk is an equivalent reformulation hidden in earlier polyhedral projection, generalized-lasso sensitivity, or submodular proximal literature.

## Value

PASS. The invariant controls perturbation stability in exactly the graph variation penalized by the estimator and is mathematically distinct from its ordinary Euclidean nonexpansivity or single-input smoothing. The exact finite combinatorial representation covers every positively weighted connected graph and every \(\lambda>0\), and the explicit quadratic growth family is a substantive warning about stability on clustered graphs with one bridge. No efficient algorithm or exact extremal leading coefficient is claimed. The tree cases may overlap other projection constants and are not the new motivation.

## Closest sources and limitations

The local projector formula is inherited from generalized-lasso theory; the quantitative cut maximum, its complete attainability and the barbell order law are the proposed contributions. Relevant papers inspected were arXiv:1005.1971 (Sections 2, 6 and 10), arXiv:1608.03384 (Sections 1–3), and RICAM Report 2018-24 (Sections 1 and 3, including Theorem 6). Historical equivalence remains possible. The theorem is restricted to finite positive-weight undirected graphs, unweighted Euclidean fidelity and anisotropic total variation.

Self-review: passed. Independent audit: not yet performed.
