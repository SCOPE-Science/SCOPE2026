# Independent mathematical audit

## correctness

PASS

For scalar strongly convex quadratics with independent static unbiased weighted sampling, e_{t+1}=(1−ηa_i/(mp_i))e_t−ηr_i/(mp_i), with Σr_i=0. The stationary mean is zero in the mean-square-stable region, and its exact variance is V(p)=(Σr_i²/p_i)/(2m²ā/η−Σa_i²/p_i). Cauchy–Schwarz gives the sharp stability frontier η<2/ā and unique root of (Σsqrt(r_i²+V a_i²))²=(2m²ā/η)V. Strict root monotonicity and Cauchy equality prove the unique full-support minimizer, including residual-zero components. Independently reconstructed multipliers and stationary variances exactly: a=(1,1,10),r=(1,−1,0),η=2/9 yields p*=(2/9,2/9,5/9), V*=1/15 versus uniform 1/3. General analytic root and inequality, not grid scans, establish global optimum.

## originality

PASS

The sharp Cauchy optimum for instantaneous residual-gradient variance is prior art, as are resampling techniques, stochastic quadratic covariance equations and small-step approximations. But this claim optimizes exact **unaveraged invariant iterate MSE** for arbitrary fixed stable nonzero step, where the sampling law controls both multiplicative Hessian contraction and innovation variance. Défossez–Bach explicitly discuss averaged constant-step LMS and approximate optimization for small step, distinct from this objective. No primary or database source inspected supplies this exact scalar root solution; best-of-knowledge PASS with substantial alternate nomenclature risk.

## value

PASS

Stationary error is an intrinsic optimization-quality measure for a constant-step method, and the exact optimizer shows a counterintuitive concrete effect: a zero-residual but high-curvature component receives most samples and improves final risk fivefold. This distinguishes finite-step optimal sampling from familiar instantaneous gradient-norm importance sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
