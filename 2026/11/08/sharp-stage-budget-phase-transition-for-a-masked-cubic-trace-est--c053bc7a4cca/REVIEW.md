# Self-review

## Correctness — PASS
The factorization into independent mask-count and probe-coupled factors follows directly from the projector identity. Exact binomial and Rademacher fourth-moment calculations give the stated variance formula. Strict convexity plus the capped simplex KKT conditions prove existence, uniqueness and the output-stage saturation threshold; asymptotic substitution proves the limiting budget gain. The standalone program evaluates the original masked matvecs by finite enumeration and exact rational arithmetic independently of the moment formula. Tests are supporting evidence, not infinite-dimensional proof.

## Originality — PASS, qualified
The closest motivating full text is Ghosh et al. (2026, arXiv:2606.22629), sections 2–3 and conclusion: its equal-law incomplete-row estimator and general second moment do not state the distinct Bernoulli stage probabilities, globally optimal budget split, unique saturation boundary or strict asymptotic variance difference. Hutch++ (Meyer et al., 2020) and improved variants (Persson et al., 2022) allocate full matvecs across distinct estimation phases, not independent incomplete rows of a single cubic trace. No covering indexed claim was found in targeted searches. Existing general moment algebra may simplify the moment computation; the allocation theorem is the substantive claimed new result. Exhaustive historic priority is unproved.

## Value — PASS
When the last row mask is coupled to the same probe used in the terminal quadratic form, its variance cost differs from earlier masks. A communication-budget optimizer must therefore use stage-aware allocation even on a canonical low-rank spectral-moment test, and the exact saturation transition gives a useful nonasymptotic design boundary. The gain survives at fixed total sampling rate in arbitrarily high dimension. This is not a claimed triangle-count guarantee for graph adjacency matrices.

## Limitations and risks
The theorem is exact for one rank-one constant projector, independent Bernoulli masks, Rademacher probes, expected row budgets and variance loss. Higher rank, graph adjacency matrices, fixed mask sizes, correlated outages, adaptive rules, throughput costs, and distributional tails are unaddressed. Unindexed equivalent classical allocation results remain possible.

Self-review: passed. Independent audit: not yet performed.
