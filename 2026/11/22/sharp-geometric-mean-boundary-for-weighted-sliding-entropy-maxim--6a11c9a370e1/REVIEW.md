# Scientific review

**Correctness — PASS.** The gradient is a positive row-stochastic three-site kernel. Every input step generates a profile with at most one negative increment. A sharp two-by-two overlap comparison yields the geometric-mean defect, and step decomposition plus segment integration proves the all-input bound. The interior-cut concentration construction gives its exact supremum, while positive boundary masses rule out finite equality in the expansive regime. The standalone checker passed 9,800 randomized inequalities and 60 additional sharpness/equality tests. Finite tests are corroboration, not an infinite proof.

**Originality — PASS, qualified.** Direct searches of indexed public research records for weighted sliding entropy maxima, log-concavity, geometric-mean thresholds, and BV two-input stability found no same-operator result. Nesterov's smoothing theory supplies the derivative formula; Saumard–Wellner's log-concavity theory implies related qualitative stochastic ordering but no exact expansive norm. A directly relevant published cyclic-window result keeps weights fixed by absolute site, whereas the current position-dependent stencil changes overlap weights, allowing expansion. A prior moving weighted isotonic result shares a threshold but has a different nonlinear map and coefficient. An unindexed equivalent theorem is a residual risk.

**Value — PASS.** The result gives an exact robustness design criterion for a natural weighted entropy-smoothed maximum, identifies the precise amplification penalty for violating log-concavity, and exposes a finite-attainment discontinuity between contracting and expanding parameters. Temperature and signal length independence are operationally meaningful, and no comparable exact sensitivity follows from general log-concavity alone.

**Limits.** Real open-path length at least six; strictly positive fixed three-tap position weights; adjacent unweighted variation; no assertion for other filters or topologies. Historical priority remains conditional on accessible literature.

Self-review: passed. Independent audit: not yet performed.
