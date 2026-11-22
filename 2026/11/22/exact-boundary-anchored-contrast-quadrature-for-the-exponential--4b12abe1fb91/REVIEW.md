# Mathematical review

## Correctness — PASS
The central claim is a complete global optimization of a single noisy contrast measurement for estimating an integrated stationary exponential-kernel Gaussian process. Exact covariance integration and one-dimensional Gaussian conditioning give the risk. Strict concavity of the kernel mean forces boundary anchoring, a symmetry/variance comparison excludes gaps above half the interval, and a strictly increasing root function gives uniqueness. Noise monotonicity and the long-correlation crossover follow from differentiation and uniform asymptotics. The separate deterministic numerical cross-check `verify.py` passed 20666 supplementary checks. The continuum theorem rests on the stated analytic proof, not finite grids.

## Originality — PASS, historically qualified
Karvonen–Kanagawa–Särkkä (2018) and related quadrature work analyze point-value measurements and general kernel weights. Longi et al. (2020) study spatial line-integral sensor placement; they supply linear-operator covariance methods but not this exact scalar contrast-only OU optimum. A related public OU quadrature record optimizes full point values, which is a distinct, more informative observation channel. The prior comparisons did not identify a theorem already establishing boundary anchoring, strict sub-half spacing, or the \(\eta\ell\) crossover. The 2017 derivative paper, one 2019 OU paper, and one related published record could not all be inspected in full; historical priority remains contingent on deeper literature verification.

## Value — PASS
A two-point difference is a natural relative measurement even when individual field values cannot be recorded. For an integrated exponential-correlated field, the widely tempting full-endpoint contrast supplies no information, while exactly one boundary-to-interior gap is optimal. Its monotone response to noise and its explicit long-correlation one-third-to-one-half transition provide a structural calibration law rather than a merely numerical example.

## Scope and limitations
The assertion is restricted to one scalar contrast, fixed gap-independent Gaussian measurement noise, stationary centered exponential covariance, unit marginal variance, a uniform integral, and known model parameters. It does not imply optimality for two separately observed values or unknown common offsets in the integral target. Numerical checks are finite and the review is not an independent historical-priority certification.

Self-review: passed. Independent audit: not yet performed.
