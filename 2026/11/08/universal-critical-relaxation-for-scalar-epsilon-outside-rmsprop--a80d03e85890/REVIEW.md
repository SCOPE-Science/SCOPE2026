# Self-review

**Correctness — PASS.** The exact critical map is an amplitude contraction. Every orbit converges; non-finite-hit orbits have eventually alternating signs. The only nontrivial asymptotic step is controlling the memory relative to current amplitude. The explicit convolution bound with \(\sqrt{\beta}<\rho<1\) closes that step, after which reciprocal increments give the two constants. Rational and numerical verification from the bundled program supports, but does not replace, this analytic argument.

**Originality — PASS, subject to historical priority risk.** The close 2026 RMSProp paper proves strict subcritical convergence, supercritical instability, and critical boundedness but does not supply convergence at the equality \(h=2\varepsilon/a\) or its polynomial constants. A second 2026 stability paper and the 2025 sharp-rate analysis both impose strict step inequalities. Search of the research database for scalar RMSProp critical rates, memory asymptotics, and equivalent flip-boundary descriptions returned optimizer results on different algorithms rather than a covering theorem. The key full texts and their relevant theorems were inspected; a historical equivalence cannot be ruled out absolutely.

**Mathematical value — PASS.** This resolves the parameter left between strict global stability and strict instability for the primary model, proves the missing global behavior, and identifies sharp, universal rates that cannot be recovered from interior exponential-contraction estimates. The memory \(n^{-2}\) constant is independent of curvature and decay, a structural dynamical fact. The scalar restriction is deliberate: no result is asserted for coupled quadratic coordinates or general losses.

**Limitations.** All asymptotic claims exclude exact finite-hit orbits, which instead terminate. Finite experiments cannot prove convergence or novelty. No independent scientific validation has been performed.

Self-review: passed. Independent audit: not yet performed.
