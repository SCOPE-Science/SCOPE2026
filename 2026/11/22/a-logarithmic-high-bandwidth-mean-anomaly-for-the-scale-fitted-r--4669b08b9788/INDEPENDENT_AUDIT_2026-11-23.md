# Independent mathematical audit

## correctness

PASS

Normalizing the iid Rayleigh squares by their sum gives the uniform Dirichlet simplex, with fitted coordinates Y_i=sqrt(2n U_i) and exact marginal density c_n y(1-y^2/(2n))^(n-2). Below the sample minimum the statistic's integrand before squaring is exactly t times the sample mean of Y_i-1/Y_i. Beyond this random positive cutoff the uniformly bounded kernels contribute an exponentially negligible piece for that sample. For W_i=1/Y_i, the marginal tail at r is c_n/(2r^2)+O_n(r^(-4)); the probability of two coordinates at any fixed positive fractions of r is O_n(r^(-4)), and is zero for large r when n=2. Inclusion-exclusion and the bound that a sum above r with maximum at most (1-delta)r requires two such coordinates give the sharp sum-tail constant. The bounded sum of Y_i does not change it; squaring and rescaling give c_n/z and the positive-moment threshold q<1. For the finite-bandwidth mean, the diagonal kernel contributes c_n t^2 log(1/t)+O_n(t^2): on Y<t the bounded kernel contributes O_n(t^2), and on Y>=t the reciprocal-square times the marginal density is c_n/y+O_n(y). The cross kernels contribute only O_n(t^2) since |g_y(t)|/t is bounded by a constant times 1+1/y and the exact Dirichlet mixed inverse moment for i!=j is pi(n-1)/(2n), including the n=2 beta-integral case. Tonelli and the integral of s^2 exp(-s), equal to 2, give the stated 2c_n coefficient, without an interchange of mean and samplewise limit. Fixed positive a has finite expectation by the uniform kernel bound; no joint n,a or nonpositive moment claim is needed. The packaged two-coordinate quadrature and deterministic sample checks were read as diagnostics, not executed or used as infinite-parameter proof.

## originality

PASS

The original statistic, fitting rule, and general fixed-point framework are established; the pointwise endpoint is a short consequence of the published definition. The contribution is the joint characterization of the sharp tail, positive-moment transition and logarithmic prelimit mean for that exact fitted statistic. Neither the opposite-order limit nor the other high-weight statistics located cover these null constants.

## value

PASS

The exact boundary behavior quantifies a failure of mean calibration for a published tuning family: an almost-sure finite scale limit coexists with logarithmically divergent normalized means, and rare near-zero observations set the constant and moment transition. Neither pointwise integration alone nor a finite power comparison addresses that phenomenon. The result is an idealized null calibration benchmark, not a choice of bandwidth, power theorem or simultaneous large-sample approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
