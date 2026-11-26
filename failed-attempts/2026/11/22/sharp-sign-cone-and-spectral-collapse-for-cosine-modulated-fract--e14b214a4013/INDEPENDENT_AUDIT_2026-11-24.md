# Independent mathematical audit

## correctness

PASS

The Fourier coefficients are u_n(1+bD_n/2), with D_n=(u_{n-k}+u_{n+k})/u_n and u even. Positivity on finite sites is equivalent to nonnegative Fourier coefficients. For 0<α<1, D_n rises strictly for 0≤n≤k. Beyond k the backward increments a_n=n^α−(n−k)^α are strictly decreasing and convex (they integrate the strictly convex derivative of x^α). Thus a_n−a_{n+1}≥a_{n+k}−a_{n+k+1}>0, and the decrease of exp(ta_n) is larger than the increase of exp(−ta_{n+k}). Only ±k saturate. At α=1, D_n is constant at 2cosh(tk) for n≥k; direct substitution gives the stated positive coefficients on |n|<k and no tail. Consecutive frequencies yield ordinary Vandermonde rank, both for this finite band and for the infinite positive block when α<1. For α>1, the backward increment tends to infinity, so D_n→∞ and every b<0 creates negative modes eventually. The exact threshold and its jump follow. Independent rational multiplication of the finite Laurent polynomial by the Poisson denominator confirmed the linear endpoint; replay with python3 -I -B branches/frozen_review_checks.py from /workspace.

## originality

FAIL

The significant claimed boundary classification on 0<α≤1 is covered by the available statement of the distinct Poisson-mixture result 969b187a914f. For 0<α<1, classical positive-stable subordination represents e^(−t x^α) as ∫e^(−sx) μ(ds), with a nondegenerate probability measure on positive scales. On the integer spectrum, absolute summability follows from ∑_n e^(−t|n|^α)<∞, exactly the mixture hypothesis. At α=1 the measure is the single scale t. In the same signed stationary harmonic modulation, the indexed mixture theorem's sharp saturation at k gives b=−2u_k/(u_0+u_{2k}), its nondegenerate case gives exactly the two holes and strict finite Gram positivity, and its single-scale case gives the same 2k−1 collapse. The superlinear branch left outside that theorem follows immediately from the standard Fourier sign test and u_{n-k}/u_n→∞. The reason for failure is this mathematical domination and the routine remainder, not failed source access or an inferred same-day priority order.

## value

FAIL

A sharp covariance cone and exact interpolation capacity would be useful, but the nontrivial saturation, reopening and rank phenomena are already part of the broader Poisson-mixture result. Outside its parameter range, the surviving statement b≥0 is an immediate high-frequency consequence of convex exponential decay, with strict definiteness following from full Fourier support. Combining that observation with the covered endpoint introduces no new structural bound or geometry that warrants a scientific repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
