# Independent mathematical audit

## correctness

PASS

For an integer diagonal gain q, integration of a test function of {q u+s} over u is the same as integration against uniform measure. Iterating this partial integration in x, then y, then z proves product Lebesgue invariance in the frozen modulus-one, fixed-translation setting. In the phase covariance, write u=(j+v)/q: summing j leaves 1/q times the unit-gain correlation. Splitting v at 1-{s} gives (1/12-{s}(1-{s})/2)/q=B_2({s})/(2q). The independent uniform forcing coordinate and even periodic B_2 give the stated absolute-amplitude dependence and factors 1/(2a), 1/(2c). The low-amplitude quadratic is (B-5/6)^2/5+1/36, including B=0 and B=1 up to a null endpoint. For B>=1, put K(B)=2 sqrt(B) J(B). Its first full period is 1/15; on each later full period twice integrating by parts gives a strictly positive integral because H(u)=u^2(1-u)^2/12 has H''=B_2 and both H and H' vanish at the endpoints, while the weight has positive second derivative. The possible final fragment subtracts at most sqrt(3)/(54 sqrt(k)) for k=floor(B)>=1, by integrating the negative part of (u-1/2)^2-1/12. This cannot erase 1/15. At infinity, the periodic primitive of the mean-zero B_2 is bounded, so the improper integral tail is O(B^(-1/2)). For the Fourier series one may integrate on finite intervals using absolute uniform summability and then take the limit: each frequency k has a tail bound O(1/(k sqrt(B))) by integration by parts. The Fresnel integral is 1/(2 sqrt(k)), giving K(infinity)=zeta(5/2)/(2 pi^2) and J(B)=zeta(5/2)/(4 pi^2 sqrt(B))+O(B^(-1)). The absolute convergence used is that of the Fourier series, not the unweighted-sign improper integral of absolute values. The frozen RESULT.md lines 34–76 give the analytic replay path. VERIFICATION.md and verify.py were inspected, not executed; finite diagnostics are not needed to establish the global sign or limit.

## originality

PASS

Best-of-knowledge pass for the exact map-specific continuous-coordinate lag-one law with strict all-finite-coupling sign and quantified coupling asymptotic. Product Lebesgue invariance of related triangular systems, Bernoulli Fourier expansions and the Fresnel/Gamma calculation are constituent results, not new claims. The classical identities also make the infinite-integral constant a straightforward consequence once the weighted-integral reduction is made; they do not establish positivity at every finite upper limit.

## value

PASS

Temporal dependence is a natural statistic for this map, independently of sequence entropy and one-time uniformity. The exact sign rules out elimination of lag-one real-coordinate covariance at any finite quadratic coupling, and the sharp leading term quantifies the remaining dependence as coupling grows. The result is about stationary real observables, not ciphertext or security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
