# Scientific review

## Correctness — PASS

The exact recurrences are the equal-buffer specialization of the motivating article's EMA update. The two alternating EMA responses give the unique nonzero symmetric cycle and its fixed positive objective gap. After curvature/stepsize normalization, the two-step Jacobian has the cubic Floquet polynomial displayed in `RESULT.md`. Schur reduction gives four explicit exact factors; their strict signs prove attraction for \(0<\beta<4-\sqrt{15}\) and spectral instability for \(4-\sqrt{15}<\beta<1\). The critical case has a double multiplier \(-1\) and is excluded from the asymptotic-stability claim. The standalone symbolic and numerical checker succeeded. The finite checks support, but do not replace, the analytic all-parameter argument.

## Originality — PASS, with limitations

The core comparison is statement-level, not title-level. Barros, Defazio and Guigues (arXiv:2610.09203v1), Section 5, give the EMA recurrences and the non-expansive moment ratio, but not the exact quadratic orbit and Floquet classification; their stated convergence results concern the cumulative variant. Bock and Weiß (arXiv:2210.02070v1), Sections 2–3, prove Adam cycles with a square-root second-moment denominator and do not imply the linear-in-moment Floquet cubic. Fong and Yang (arXiv:2608.20638v1), Sections 2–3, study Adam's square-root normalizer; Itin (arXiv:2610.27321v1), Section 3 and Appendix A, studies momentum maps without an independently adapting second-moment state. Neither stronger theory covers the present map by an exhibited equivalence. Related published exact cycle and normalized-gradient findings were compared, so novelty is claimed for the **specific sharp equal-buffer EMA FlexGrad classification**, not the generic existence of two-cycles. Historical unindexed exact calculations remain a risk.

## Mathematical value — PASS

The source emphasizes the bound \(|s|\le\sqrt v\) for its optional EMA design but explicitly lacks convergence theory for that variant. The theorem shows why a bounded modulation does not ensure a vanishing step near even the simplest strongly convex minimum: a locally attracting cycle has objective floor \(\kappa\eta^2[(1-\beta)/(1+\beta)]^4/8\). The exact, dimensionless boundary \(4-\sqrt{15}\) separates local cycle attraction from instability and yields an interpretable tuning benchmark for the equal-buffer specialization. This is a motivated stability classification, not a routine first-step substitution. It does not cover the default practical EMA decay range or prove global behavior.

## Residual limitations

The critical boundary is nonhyperbolic and nonlinear critical stability remains open. The analysis excludes momentum mismatch, denominator regularization, bias correction, stochasticity, and general objectives. The local cycle basin is nonempty in full state space; a universal basin statement for prescribed initial buffer values is not proven. Priority cannot be certified against every unpublished calculation.

Self-review: passed. Independent audit: not yet performed.
