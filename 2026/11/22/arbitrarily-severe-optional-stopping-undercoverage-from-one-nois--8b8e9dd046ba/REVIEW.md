# Self-review

**Correctness — PASS.** The spectral-filter identity is derived from the exact Landweber recursion, the source-class bias bound follows from a scalar maximum, and the coordinate coefficient ratios vanish uniformly for each fixed finite number of examined scales. Joint Gaussian convergence and vanishing standardized bias establish the \((1-\alpha)^r\) selected-coverage limit. A bundled executable checks explicit matrices, recurrence and representative finite samples; these checks do not replace the proof.

**Originality — PASS, qualified.** Optional-stopping and familywise-coverage dangers are established ideas. The motivating Landweber paper states that its stopping indices are independent of the realized observations (arXiv:2610.00882v1, equations 3.20–3.21), so its guarantee neither addresses nor claims validity under the first-exclusion selection in this theorem. Adaptive-stopping risk results (arXiv:1606.07702) and simultaneous confidence calibration (arXiv:2510.11708) provide complementary principles, not this explicit Landweber one-coordinate multiscale near-independence construction. Bounded literature and published semantic-result searches identified no dominating theorem. Unindexed historical equivalent constructions remain possible.

**Value — PASS.** The precise multiplicative coverage loss, caused entirely by repeated reuse of one noisy dataset under a data-dependent iteration choice, gives a meaningful limitation and a concrete reason to seek simultaneous/anytime-valid uncertainty bands in iterative inverse problems. The setting uses engineered spectra and a significance-peeking rule, and makes no claim about the paper's observation-independent stopping or all adaptive schemes.

**Evidence and limits.** The all-parameter theorem is proved analytically; a finite Python test is corroborative. This is the exact-covariance Gaussian model, with source class exponent one. Historical priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
