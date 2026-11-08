# Scientific review: exact two-period stability of reflected splitting

## Correctness — PASS

The two updates are defined on the same nontrivial maximally monotone skew inclusion with alternating positive scaled steps. Direct complexification gives explicit two-step monodromy matrices. A classical Schur–Cohn test produces strictly positive factors times, respectively, \(1-4ab\) and \(1-(a+b)^2\), so the proposed conditions are necessary and sufficient, not just numerical heuristics. The boundary eigenvalue is exactly \(-1\); the other multiplier lies inside the disk, whereas above the threshold exactly one multiplier lies outside. The equal-history initialization necessarily excites the nondecaying or growing mode because its first-iterate ratio has modulus one. A fresh symbolic and numerical checker confirms the algebra but is not used as a substitute for proof.

## Originality — PASS, with historical-priority reservations

The September 2026 sharp-step source analyzes constant steps on the identical matched-skew test and therefore yields only the diagonal case \(a=b\). The July 2026 variable-step linesearch source gives a previous-step-weighted reflection rule and a Lyapunov-based convergence theory, but not the arbitrary prescribed alternating-step phase boundary or its contrast with current-step weighting. The September adaptive reflected method requires a convex-subdifferential backward operator, which a nonzero skew operator is not. Searches for periodic/alternating reflected splitting, skew Floquet stability, and variable-step conventions did not identify a prior result that implies both exact thresholds. Such searches cannot establish absolute historical uniqueness; specialized unindexed stability calculations remain a residual risk.

## Value — PASS

The two algebraic frontiers answer a motivated design question: how to transport the stored-gradient correction across changing stepsizes. They show that ostensibly similar one-call schemes have qualitatively different admissible schedules, and that a very large individual step can be harmless under one convention yet destabilizing under the other. This is a nontrivial exact boundary for a canonical monotone inclusion already known to be extremal for fixed steps, not an arbitrary parameter tweak. The result is a reference test, not a general convergence theorem.

## Closest literature and limitations

- Y. Shehu (2026), arXiv:2609.18373: sharp constant-step matched-skew frontier.
- F. Muñoz García and F. Roldán (2026), arXiv:2607.20113: variable-step gradient-history convention and adaptive linesearch.
- H. Ou, A. Themelis, P. Latafat (2026), arXiv:2609.15936: adaptive reflected splitting with backward convex-subdifferential assumption; abstract examined, not the full document.
- The claim is for prescribed two-period positive steps, two-dimensional linear skew operators, and exact arithmetic. It does not cover arbitrary variable steps, nonlinear operators, or practical linesearch schedules.

Self-review: passed. Independent audit: not yet performed.
