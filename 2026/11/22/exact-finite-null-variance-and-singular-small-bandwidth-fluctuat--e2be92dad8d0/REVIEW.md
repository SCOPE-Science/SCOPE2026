# Independent mathematical audit

## correctness

PASS

Verified the known-parameter, i.i.d. standard Cauchy result for every n >= 2 and a > 0. The real Fourier–Stein feature has mean zero by the transform of the Cauchy score. Its real and imaginary parts before the real-feature combination are odd and even in x, respectively; writing the complex product against the conjugate and using the transforms at s-t gives K(s,t) = (s^2+t^2+|s-t|+1) exp(-|s-t|)/2. Conditional degeneracy kills all unequal-pair covariances and diagonal/off-diagonal covariances. The diagonal contributes 1/(2na^2), and the identical unordered pairs contribute 2(n-1)/n times the weighted squared-kernel integral. The independent change to u=|s-t|, v=|s+t| gives that integral as (1/8) times the positive-quadrant integral of (u^2+v^2+2u+2)^2 exp(-2u-a max(u,v)); splitting at v=u and integrating the monomials gives the stated rational polynomial identically. The physical-space pair kernel is made of derivatives through order two of 2a/(a^2+(x-y)^2); distinct observations contribute O(a). For the squared expectation the second derivative term has size a^-3 times 4(1-3u^2)/(1+u^2)^3 at x-y=au, and the difference has Cauchy scale-two density, equal to 1/(2pi) at zero. Dominated convergence for its square gives the same 3/2 constant after multiplication by a^5; the lower derivatives are negligible there because |g| <= 1 and |g(x)-g(y)| <= 2|x-y|. This verifies the near-collision mechanism and the failure of L^2 convergence despite bounded almost-sure limit. Replay: python3 /workspace/independent_checks.py 5 (symbolic identity and spatial constant; requires SymPy). Frozen checker inspected only; the 60 sampled entries in its loop include repeats (57 distinct), a documentation slip that does not bear on the all-a identity.

## originality

PASS

Credit Ebner–Eid–Klar with the statistic, integration-free kernel, pointwise endpoint, arcsine score law, and the known-parameter component of the frequency covariance. The contribution is the explicit finite-sample centered variance for all positive bandwidths and the singular small-bandwidth variance/non-L^2 comparison for that same statistic. The inspected theorem on the fitted Gaussian-process limit is not an exact finite-sample variance theorem, and its asymptotic kernel and trace alone do not evaluate the required squared integral or establish the finite-n coefficient. No independent exact cover was found in the comparisons performed, not a priority guarantee.

## value

PASS

This is the variance of an existing test statistic under its basic known null, for all n and a, not a selected numerical moment. The scale and coefficient tell a user precisely why a bounded fixed-sample small-bandwidth approximation cannot be used to infer the untruncated variance: pairs at separation of order a dominate it. The statement does not promise fitted-parameter calibration or a bandwidth-selection rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
