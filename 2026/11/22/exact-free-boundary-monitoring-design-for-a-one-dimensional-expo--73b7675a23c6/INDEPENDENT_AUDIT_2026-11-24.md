# Independent mathematical audit

## correctness

PASS

In the frozen finding, the verbal description of the small-X regime was reversed: theta L approaching zero means the transect is short relative to the correlation length, with strong correlation, not weak correlation. Also record 971795799fba's quadrature margins are shorter, not longer, than its interior gaps. Complete corrected affected files are in /workspace/repairs/2/. The repaired theorem follows by subtracting the known mean and conditioning the Gaussian Markov chain: the outer intervals condition on the nearest observed endpoint, whereas a bridge conditions on its two adjacent observations. Integrating the corresponding Schur complements gives G(u)=u-(1-exp(-2u))/2 and H(d)=d coth(d)-1 in units of sigma²/theta. Both costs extend to zero with zero marginal cost and are strictly convex, so moving length from any positive gap to a zero gap rules out boundary points of the compact simplex. The unique interior minimum equalizes the derivatives and forces symmetric positive margins and common interior gaps. The numerator of G'(d)-H'(d) after division by its positive prefactor vanishes at zero and has derivative 4(1-exp(-2d))², proving a<d. Expansion at zero gives a=d/3+O(X²). At fixed n, d≥X/(n+1) forces d and then a to diverge; e^(-2a)=(4d-2)e^(-2d)+O(de^(-4d)) proves both logarithmic expansions and their dimensionless interpretation. /workspace/evidence/reproduce_other_checks.py independently reproduced the two-station normalized optimum and 40.439557% improvement at X=1 with high-precision bisection; this is not the global proof or empirical evidence.

## originality

PASS

The corrected claim is for freely optimized terminal gaps and unweighted integrated pointwise simple-kriging variance over the whole interval. Neither the endpoint-constrained IMSPE theorem nor a free-node optimum for estimating the integral gives the terminal/interior marginal equation for this objective. Credit the earlier shorter-gap ordering in quadrature, not an alleged opposite ordering.

## value

PASS

Unconstrained monitoring design is a natural predictor benchmark. It shows precisely how and by how much boundary freedom changes a design ordinarily constrained to endpoints, explains the 1:3 strongly correlated limit and the logarithmic deficit at large dimensionless length, and provides a unique scalar design equation for all station counts in scope. Its substantive conclusion is about the specified model, not general environmental deployment efficacy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
