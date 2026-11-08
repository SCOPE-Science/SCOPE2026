# Scientific review: A sharp reentrant stability window for implicit Euler with Gaussian coefficient error

## Correctness — PASS

The scalar update is exactly the inverse of a shifted normal. The proof reconstructs the centered Gaussian log-potential, derives its differential equation by a justified Gaussian integration by parts, proves the unique positive crossing of \(tw(t)=1\), and obtains the unique global minimum in noise amplitude. The strong law and the law of the iterated logarithm settle exponential and boundary regimes; local density positivity settles all divergent moments. Fractional-moment stability is equivalent to positive mean log denominator by differentiability at the origin and Jensen's inequality. The checker reproduced 824 deterministic consistency tests, including singular-integral numerical comparisons; no infinite claim rests solely on finite experimentation.

## Originality — PASS, subject to priority risk

Bosch (arXiv:2606.08203, 2026) constructs stable scalable ODE filters using exact Jacobian-vector products and stochastic covariance estimators; it does not implement independent Gaussian perturbations of the implicit drift coefficient. Bochacik–Przybyłowicz (arXiv:2104.15071, 2021), Section 5, treats stability under **exact information** for random-time Euler rules on a different test problem. Higham–Mao–Yuan (DOI:10.1137/060658138, 2007), Sections 2, 4 and 6, treats numerical Itô SDE forcing, with deterministic implicit drift denominators. The known iid-log-product stability criterion is not asserted to be new; the claimed increment is the closed Gaussian-denominator phase classification and unique drift cutoff. Targeted published-result searches and comparison with accessible historical findings showed no covering statement. Unindexed random-affine-recurrence results, and reformulations in classical normal logarithmic-potential theory, remain potential priority risks.

## Value — PASS

The result supplies a sharp, analytically characterized failure region for a directly interpretable type of operator-estimation error in a classical stiff ODE integrator. The distinctive open interval of noise-driven almost-sure instability, with restored stability at sufficiently large noise and simultaneous absence of all first and higher moments, goes beyond a generic textbook multiplicative-noise observation. The numerical cutoff is universal across timestep and decay-rate scalings in this model; it can serve as a reproducible diagnostic benchmark. Its value does not require assuming the motivating ODE-filter algorithms introduce such noise.

## Boundaries and outstanding risks

The perturbations must be independent standard Gaussians and can reverse the effective drift sign; changing those assumptions changes the result. Singular denominators occur only on null events but produce heavy tails and huge transients. Numerical constants are not formally interval-certified. Independent mathematical validation and exhaustive historical priority searches have not been performed.

Self-review: passed. Independent audit: not yet performed.
