# Scientific review: two-request Green-kernel quadrature with erasures

## Correctness — PASS

The conditional-variance decomposition is derived from the one-dimensional Dirichlet Green-kernel Markov property, and its gap cost is the integral of the unique Dirichlet solution of \((-\partial_t^2+\kappa^2)v=1\). Strict convexity yields a unique global optimizer in the entire ordered two-point triangle. Its symmetric stationary equation has exactly one root in \((0,1/3)\). Monotonicity in delivery probability follows by an interval-ratio argument; monotonicity in inverse lengthscale follows from a strictly decreasing derivative-kernel likelihood ratio, whose sign is proved explicitly. Exponential asymptotics prove the sharp logarithmic correction. The standalone numeric verifier passed 6,443 direct Green-kernel, Gaussian Schur-complement, root, comparison, and asymptotic checks. These checks do not substitute for the analytic infinite-parameter arguments.

## Originality — PASS, with residual priority risk

The closest inspected literature is Karvonen–Kanagawa–Särkkä (2018), which gives general Bayesian-quadrature variance and weight principles, and Santin (2022), whose full relevant statements optimize pointwise kernel interpolation error without erasures. A publicly accessible 2026 theorem for stationary exponential covariance solves noiseless integral-quadrature placement, but has a different terminal gap law, no pinned endpoints, and no erasures. The previously established Brownian-bridge formula at zero inverse lengthscale is acknowledged and excluded from the claimed novelty. The present continuum statement concerns strictly positive inverse lengthscale, strict migration of the optimal separation in two parameters and its high-tension asymptotic, none of which follows from the cited statements. Exact historical priority has not been independently established; more remote earlier optimal-design literature might contain an equivalent specialization.

## Value — PASS

Independent sensor erasures create a genuine choice between clustered redundant measurements and separated coverage. The theorem resolves this design continuously for every positive kernel inverse lengthscale and every intermediate reliability, showing that the optimal requests spread apart strictly as the kernel becomes more local, approaching trisection with an exact first-order rate. This is an actionable quadrature and sensing design distinction, not a relabeling of an exact known finite table. The theorem has a sharply stated two-sensor, pinned-covariance scope and is not claimed for noisy values or stationary unpinned models.

## Limits

Claims of global optimality assume known covariance, independent equal delivery probabilities, exact observed values and a scalar integral target. The Brownian limit is not asserted to be novel. No external mathematical validation or exhaustive historical priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
