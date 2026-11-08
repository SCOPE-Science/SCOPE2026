# Scientific review: one-node stochastic Lanczos log-determinant orientation law

## Correctness — PASS

The estimator is exactly the normalized first-Lanczos Rayleigh quotient for independent Rademacher probes. In two dimensions each output has a two-point distribution; direct algebra gives its expectation and variance. The risk formula is the exact bias-squared plus independent-probe variance, not a concentration approximation. Differentiating the exact formula gives a sign controlled by the increasing function \(H(t)\); the power-series proof establishes monotonicity for every \(0<r<1\), hence both transitions, uniqueness, and endpoints for every integer \(N\ge1\). The scalar equal-eigenvalue boundary is stated separately. A standalone standard-library program checks the direct finite distributions and the derived risk/threshold laws across a finite parameter grid (80,540 comparisons). The analytic derivative proof, not the grid, proves the universal claim. No unfinished lemma or external computational certificate is required.

## Originality — PASS, with documented precedence risk

The foundational SLQ algorithm and general log-determinant bounds are due to Ubaru–Chen–Saad (2017, Algorithm 1 and section 4.3). Cortinovis–Kressner (arXiv:2005.10009, theorem-level trace concentration and determinant application), Chen–Trogdon–Ubaru (arXiv:2204.01941, uniform spectral quadrature), and Li–Han–Huang–Wathen–Zhu (arXiv:2307.00847, sections 3–4, asymmetric quadrature bounds and allocation of iteration/probe budgets) address broader but different guarantees. Source statements and material full-text sections were inspected. None of those inspected statements implies *as a stated result* the exact orientation-dependent two-point MSE, its two distinct transition counts, or the complete extremizer classification; general sufficient high-probability bounds cannot yield sharp equalities or exact extremizers without additional analysis. Current relevant mathematical-record searches found no same statement. Searches do not prove uniqueness, and an older specialist two-point-sampling or SLQ calculation may have already supplied an equivalent classification. The benchmark claims this particular exact phase diagram, not invention of SLQ or of elementary Rademacher moment identities.

## Value — PASS

There is a concrete numerical-analysis gap between controlling stochastic trace variance and controlling finite-depth quadrature bias: the worst orientation changes at an explicit probe budget, after which extra probes cannot improve the uniform one-node guarantee. The separate best-orientation transition identifies a nontrivial tradeoff rather than merely computing the risk at two endpoints. Together these give a complete sharp finite-dimensional benchmark for log-determinant probe-budget and quadrature-depth decisions. The two-dimensional setting is intentional as the smallest nontrivial case and the result does not purport to optimize a practical high-dimensional implementation. No general downstream theorem is required for this exact motivated classification.

## Prior-work comparisons and limitations

The closest explicit prior analyses are Ubaru–Chen–Saad (2017), Cortinovis–Kressner (2020/2021), Chen–Trogdon–Ubaru (2022), and Li–Han–Huang–Wathen–Zhu (2023). The last paper optimizes a global error budget and is not a competing optimal-*orientation* calculation. The result only addresses \(2\times2\) SPD inputs, distinct eigenvalues, independent fair sign probes, exactly one node per probe and MSE, not finite-precision or unknown-basis rotation costs. Specialist equivalence remains the chief originality risk. The record is internally checked and independently unaudited.

Self-review: passed. Independent audit: not yet performed.
