# Independent mathematical audit

## correctness

PASS

PASS. The midpoint update has AR coefficient r(u)=(1-u)/(1+u) and Gaussian innovation variance 1-r(u)^2, so every step-mixture preserves N(0,1); the first two Hermite eigenvalues are E r and E r^2 and autocorrelations are geometric. Strict convexity of r proves that randomization worsens linear IACT. For f=r^2, its second derivative changes sign at u=2. The supporting chord from t_B=1+2/B to B is tangent at t_B and its difference from f factors as (B-u)(Bu-B-2)^2/[(B+1)^3(1+u)^2]. I independently checked the symbolic factorization, both contact points and tangency. Convex-envelope Jensen/equality proves the unique optimal step law; no claim for fixed physical-time cost.

## originality

PASS

PASS with priority qualification. Abdulle--Garegnani study random steps for ODE integration, geometric conservation and convergence rather than the stationary Gaussian OU midpoint Hermite observable IACT optimization under BOTH fixed arithmetic mean and cap. Earlier Resultary implicit-midpoint random-step damping studies optimize an equiprobable two-scale law or harmonic oscillator isotropization, different objective/feasible set. The new full-measure convex-envelope optimizer, exact t_B=1+2/B phase transition and opposing linear/quadratic IACT consequences are not implied by inspected results. General convex envelope/Jensen machinery is standard and credited.

## value

PASS

PASS. Correlation per numerical update under an exact-invariant Gaussian sampler is a natural sampling-efficiency objective. The globally optimal distribution subject to a mean and hard cap, exact transition, uniqueness and provable conflict of linear/quadratic observables form a useful design benchmark. The benefit does not extend to trajectory accuracy or all observables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
