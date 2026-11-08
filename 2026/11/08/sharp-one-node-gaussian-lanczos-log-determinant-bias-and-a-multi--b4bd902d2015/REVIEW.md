# Self-review

**Correctness — PASS.** The one-node formula follows exactly from the first Lanczos Ritz value. Gaussian polar independence and the Dirichlet angular law give the expectation; Jensen proves the nonnegative bias, and strict coordinatewise convexity of logarithmic eigenvalues establishes the global two-endpoint extremizers with no missing interior cases. Beta integration proves the finite optimum, and beta moments and dominated convergence prove the two limiting regimes and multiplicity change. The optional executable replay checks formulas numerically, but no universal assertion relies on finite testing.

**Originality — PASS, with residual historical risk.** The nearest primary works provide general stochastic Lanczos quadrature, a one-probe strategy that still uses multiple Lanczos nodes, and general trace/determinant error analyses. None of the inspected full-text portions states the exact all-spectrum one-node Gaussian expectation-bias extremum or its conditioning-dependent multiplicities. Database searches found no equivalent claim. The complete manuscript of the 2026 motivating preprint was inaccessible, and an older equivalent log-sum-exp extremal theorem remains a plausible priority risk; no uniqueness of discovery is claimed.

**Value — PASS.** The natural one-node approximation is the cheapest nontrivial Lanczos log-determinant rule. A sharp spectral-condition-number risk law quantifies its worst systematic overestimation in every finite dimension, identifies extremizing spectra, and exposes a transition from balanced to singleton high-eigenvalue groups. These are useful calibration targets for sketch-based determinant estimation; generic Jensen positivity or a crude smoothness inequality does not determine them.

**Limits.** Exact arithmetic, one Gaussian probe, one quadrature node, fixed SPD matrices, expectation rather than concentration; no floating-point or multi-step stability claim. Mathematical priority is provisional pending broader literature inspection.

Self-review: passed. Independent audit: not yet performed.
