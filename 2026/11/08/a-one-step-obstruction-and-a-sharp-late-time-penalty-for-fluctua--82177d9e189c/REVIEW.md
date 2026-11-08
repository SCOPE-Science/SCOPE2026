# Scientific self-review

## Correctness

**PASS.** The unit-rate killed transition kernel yields the exact Bessel survival formula, and its derivative is the first-passage density \(m e^{-u}I_m(u)/u\). Its Bessel ODE gives a weighted derivative with exactly one sign change for \(m\geq2\) and none for \(m=1\); this is the critical nonstandard step. Strict Jensen gives the one-step ordering. Exact short-time generator coefficients and the moment expansion for the integrated renewal clock prove the finite-disorder sign reversal and the positive \(t^{-3/2}\) correction. The 168 implementation checks are corroboration, not substitutes for these proofs. The argument assumes positive bounded iid rates and a fixed resampling period.

## Originality

**PASS with publication-priority qualification.** The directly motivating arXiv:2609.26925 supplies the general rate-clock representation and a heavy-tail first-passage mean transition, not the bounded-rate nearest-neighbor exception, explicit late penalty or weak-disorder one-inflection theorem. arXiv:1809.09186 already reports a qualitative early/late first-passage crossover for *continuum* diffusing diffusivity; that shared phenomenon is expressly not claimed new. arXiv:1812.07249 provides a general continuum clock-transform method, not the discrete Bessel sign theorem. Relevant public mathematical-result searches and the accessible preceding research claims produced no statement implying the entire theorem. The main risk is unlocated specialized literature on Bessel first-passage modes or stochastic-clock response coefficients.

## Value

**PASS.** A single spatial step changes the sign classification qualitatively: variance in an external jump-rate clock can never improve cumulative passage probability from distance one, while any nondegenerate bounded law must do so at sufficiently short horizons from distance two or more. The unique weak-response horizon separates these behaviors without dependence on the rate-resampling period, and a quantitative universal coefficient measures the residual late survival cost. This supplies a finite-horizon prediction for lattice transport that cannot be inferred from the infinite mean passage time or from continuum crossover plots alone.

## Boundaries and residual risks

The original motivation's broad unbounded-rate regime is not covered. The finite-disorder crossing is not proved unique. Independent validation and a full bibliographic priority determination remain outstanding. The proof and model statements are confined to the explicitly defined symmetric absorbed half-line chain.

Self-review: passed. Independent audit: not yet performed.
