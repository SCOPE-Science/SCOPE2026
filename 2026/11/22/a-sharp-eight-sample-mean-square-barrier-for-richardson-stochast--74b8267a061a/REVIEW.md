# Scientific review

## Correctness — PASS

The stationary OU generator is explicitly applied to the quadratic observable and then twice; empirical action entries reduce to the exact ratio of the second and fourth Gaussian sample moments. A polar Gaussian decomposition proves independence of the chi-square radius and bounded angular fourth-power sum. Its radial inverse-moment condition is necessary and sufficient for *every* positive moment order; a nonzero leading polynomial coefficient transfers the condition to each update rule. Direct Gaussian integration of the true semigroup image converts coefficient-square integrability into prediction-risk integrability, and small-radius chi-square asymptotics give the constants and exponents. The special cancellation in the second-order Taylor method at unit step is treated separately. The rational-arithmetic checker tests 78,095 finite algebraic identities. Finite tests do not replace the analytic moment proof.

## Originality — PASS, qualified

The closest primary source is Xu, arXiv:2611.00793, particularly the scheme definitions (2.5)–(2.8), Theorem 3.3, Proposition 3.6 and Remark 3.7, and the distinct trigonometric OU example in Section 5.2. It establishes deterministic or high-probability finite-data bounds, not the sharp unconditional Gaussian inverse-moment cutoff or the precise rare-error tail constants for the one-observable quadratic OU dictionary. Llamazares-Elias et al., arXiv:2405.00539, analyze Monte Carlo convergence of Galerkin approximations under broader conditions, not this scheme-comparison threshold. Closest publicly indexed results concerning inverse-Gram moment barriers are on Anderson extrapolation, random quadrature, Fourier sketches and regression control variates, not SDMD. No search proves historical uniqueness; equivalent unindexed special cases remain a risk. The basic inverse-chi-square integrability calculation is classical and is not claimed as novel.

## Mathematical value — PASS

The source paper recommends second-order Richardson SDMD for its fixed-data accuracy while its finite-sample guarantees are probabilistic. Here, a natural and explicit unbounded dictionary proves that the Richardson step has an infinite unconditional squared Koopman error at sample counts where first-order and generator-Taylor steps already have finite risk, despite an almost-surely positive Gram. The sharp \(m/8\) versus \(m/4\) Pareto tails identify the statistical mechanism and exact sample budget at which mean-square reliability first exists. This addresses a genuine solver-design distinction rather than an arbitrary isolated numerical value. The phenomenon does not assert poor typical-case accuracy or refute conditional high-probability bounds.

## Scope and residual risks

The result is only for iid Gaussian training points, an unregularized scalar Gram, a noninvariant polynomial dictionary and a single fixed step; it does not apply to bounded trigonometric dictionaries or regularized inverses. Primary literature on operator estimation can contain related general moment phenomena under different names. No external expert audit has been performed.

Self-review: passed. Independent audit: not yet performed.
