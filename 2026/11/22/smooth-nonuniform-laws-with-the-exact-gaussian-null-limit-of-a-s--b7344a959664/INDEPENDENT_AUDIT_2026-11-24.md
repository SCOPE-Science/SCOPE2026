# Independent mathematical audit

## correctness

PASS

For the specified iid, complete-data kernel k=-min(x,y)+(x²+y²)/2, direct conditional integration gives the first projection (up to an additive constant) and multiplying its variance by four gives the asymptotic variance. I independently integrated the kernel split at x=y with polynomial densities in exact rational arithmetic. Replay: python3 /workspace/reproductions/five_projected_variance.py. This gives null mean 0 and variance 1/45, the two-by-two mean/variance Jacobian [[1/15,1/35],[0,4/945]], and along x+cH the exact pair (-c²/30,1/45-c²/420-c⁴/225). The determinant 4/14175 is nonzero, so the analytic implicit-function theorem gives the exact jointly constrained local solution, with zero linear terms and quadratic coefficients 29/112 and 9/16. Endpoints stay fixed, the derivative converges uniformly to one, and the midpoint displacement c/4 excludes the null and bounds Kolmogorov distance from below. The nondegenerate bounded-kernel U-statistic CLT and continuity of the normal tails give rejection probability tending to alpha at each fixed stated null cutoff; empirical-CDF convergence gives KS consistency. This proves a fixed-alternative asymptotic fact for the unstudentized test, not finite-sample equality or a censoring claim.

## originality

PASS

Zero-signal smooth alternatives, the original statistic, and its CLT/variance formula are not credited as new. The supported distinct content is an analytic nonuniform family with the asymptotic variance matched to the null exactly as well as its mean, converting scalar blindness into equality to size at every fixed asymptotic normal cutoff. The strongest available near-match statements describe conservative rather than size-equal power, and give no equivalent joint-level-set construction. Priority is qualified by unavailable full texts.

## value

PASS

A rigorously null-matched family is more informative than a zero-signal example: it exhibits a blind spot at every fixed nominal level for a published test, even for positive smooth alternatives independently detectable by an omnibus test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
