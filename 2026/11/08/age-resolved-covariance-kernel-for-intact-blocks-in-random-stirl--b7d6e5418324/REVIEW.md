# Review of age-resolved covariance kernel

**Correctness — PASS.** Uniform increasing-label gap insertion proves the subset-survival product exactly; this gives all pair covariances. Harmonic-sum estimates and a summable inverse-index bound justify all two-parameter covariance limits, including the axes. All 6,375 exact rational assertions in `verify.py` passed. Exhaustive tests are corroboration only, not the proof of the limit.

**Originality — PASS, with explicit priority risk.** Janson's earlier paper covers aggregate plateau statistics and increasing-tree bijections. Janson–Kuba–Panholzer treat generalized Stirling permutations and plateaux indexed by occurrence number. The strongest comparison is Haglund–Visontai (2012), whose full value-indexed stable generating polynomial already implies a finite labelled joint distribution and negative-dependence properties. That prior work substantially covers the qualitative background; the present assessed claim is specifically the explicit two-parameter birth-prefix covariance kernel and closed variance profile, not the discovery of labelled plateau statistics. No matching quantified kernel was identified in the completed comparisons. The stable polynomial may permit an earlier implicit derivation and is a serious priority risk.

**Value — PASS.** This resolves a motivated exact limiting second-order statistic for arbitrary birth-age windows in a canonical random growth model. The full-count variance is a known specialization; the nonconstant two-parameter covariance kernel is the contribution. It is potentially useful for age-profile inference and subsequent functional limit theory without asserting such a theorem.

**Limitations.** Only finite exact identities and covariance convergence are proved. There is no Gaussian-process limit or uniform rate. Independent bibliographic and mathematical assessment has not been performed.

Self-review: passed. Independent audit: not yet performed.
