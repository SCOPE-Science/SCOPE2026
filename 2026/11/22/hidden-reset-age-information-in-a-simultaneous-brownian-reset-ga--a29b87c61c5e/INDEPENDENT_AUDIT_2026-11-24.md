# Independent mathematical audit

## correctness

PASS

At stationary common Poisson resets U=rT is unit exponential. Given U, the radius squared in units 4D/r is UB with B independent unit-rate Gamma(k), k=N/2; Gaussian angles are independent of U given the radius, including the sign at N=1. The Mellin product integral gives the stated Bessel-K density, with the extra Jacobian e^v for its log. Entropies are finite by the Bessel tails (the log-left tail at k=1 can carry a polynomial factor). Taking logs gives the difference of the output entropy and h(log B)=log Gamma(k)-k psi(k)+k, with all r,D scaling removed. The posterior density of U given any existing finite snapshot of nonzero radius is positive on (0,infinity), and the distinct conditional normal variances exclude conditional independence of the next coordinate and U. The information chain rule gives strict increase. The scalar Laplace marginal with scale sqrt(D/r) and E log U=-EulerGamma give the displayed I_1. For the delicate entropy correction, independently expanded the exact relative-entropy argument: f(w)=exp(w-e^w), Z=log B-psi(k), and for p=f*law(Z), h(p)-h(f)=E exp(Z)-1-D(p||f). On |Z|<=delta<log 2, write a=e^{-Z}-1 and a' for an independent retained shift. The likelihood overlap minus 1 is aa'/(1+a+a'), uniformly away from a zero denominator. Expanding the reciprocal as 1-(a+a')+(a+a')^2/(1+a+a') bounds the retained chi-square by O(k^{-2}), since Ea=O(k^{-1}), Ea^2=O(k^{-1}), E|a|^3=O(k^{-3/2}), and E|a|=O(k^{-1/2}). These follow from the centered second and fourth Gamma-log moments plus exponentially small truncation of the mean. Gamma Chernoff bounds give exponential tails for the omitted mass, and the exponentiated shift tail is bounded by the same estimate for a shape k+1 tilted Gamma law. Cauchy–Schwarz controls the omitted log moment. Convexity of relative entropy and the exact single-shift divergence exp(Z)-1-Z then give D(p||f)=O(k^{-2}) plus exponentially small terms. Digamma gives E exp(Z)-1=1/(2k)+O(k^{-2}); Stirling and digamma give h(log B)=0.5 log(2 pi e/k)+1/(6k)+O(k^{-2}). This verifies the positive difference 1/(3k)=2/(3N), with the stated leading constant and remainder.

## originality

PASS

Credit the already known mixture, Bessel-K input, generic log-noise reformulation and leading information order; strict monotonicity uses the standard information chain rule and is not a standalone general innovation. The supported distinct contribution is the evaluated age–snapshot information, especially its explicit first correction with a justified remainder for the changing log-Gamma perturbation. General results come close, but the inspected statements do not directly supply this correction with controlled remainder for this prior and triangular array.

## value

PASS

For a synchronous reset gas the latent time since reset is a physically meaningful common cause, and the full-snapshot information distinguishes recoverability of that variable from ordinary position or square-position correlations. The exact integral and finite-size term provide an information benchmark beyond the universal leading order, with a tail argument that matters for this non-Gaussian observation experiment. This motivates the precise coefficient without relying on a downstream theorem or a claim about an estimator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
