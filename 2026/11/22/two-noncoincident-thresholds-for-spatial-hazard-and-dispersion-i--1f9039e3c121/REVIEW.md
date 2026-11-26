# Independent mathematical audit

## correctness

PASS

In dimensionless units let K be the reset kernel and R the exponential-time Neumann resolvent with kernel (exp(-|r-y|)+exp(-r-y))/2. The pre-alarm chain has kernel KR. On the event B≤1 the reset point r lies in [0,1] for every previous position; R(r,y)≥exp(-1)/2 on [0,1]. This gives a uniform minorization and a unique invariant probability μ. The identity μ=μKR also gives arbitrary-time stationarity by the last-alarm renewal equation: e^(-s)μU_s is the tail from s to infinity of the exponential-age mixture μKR, where U_s is the reflected Brownian semigroup. Conversely a stationary measure satisfies this mixture identity in the infinite-time limit. The law has a density, even though the reset law includes an atom. With w=E[Y exp(-tY)], the reset tail is exp(-ty)[(1+ty)v+tw], so the atom is 1-v-tw and the source density is t² exp(-ty)(yv+w). Re-solving normalization and the two affine-exponential coefficient equations gives the stated A,C,E and the atom flux; a polynomial-exponential solution at t=1 gives g_1=exp(-y)(30y²+68y+191)/319. For t≠1, in g'S+g² the pure exp(-2ty) coefficient is E²/t² and the cross coefficient is A(K0+K1 y). The sign is that of F_t; F'_t is positive from K1+(t-1)K0>0 and (t-1)K1≥0. Its far-tail limit is strictly positive (or +infinity), so its origin sign alone decides the bathtub/increasing alternatives, including strict increase for y>0 at the transition. At t=1 the derivative reduces to a positive factor times 450y²+1920y−689, with one positive zero. Exact moments give CV²−1=−8P_v/M² and the origin slope is 4P_h/Q². Each polynomial has one sign variation, starts negative and has positive leading coefficient; P_v(1)=4051 and P_h(1)=−689 separate the roots. Independent replay: python /workspace/review_reproduction.py (section 2, SymPy and mpmath) solved the density and bracketed 0.5241620843734732 and 1.17158604349906. The replay corroborates algebra and decimals, not the continuum monotonicity proof or other reset laws.

## originality

PASS

The strongest inspected prior work already treats the general reflected reset process and solves the same subtraction-and-truncation map for exponential capacity. Credit both. The supported distinct claim is the sharp spatial-hazard/CV phase diagram with two ordered thresholds for Erlang shape two, not the reset map, the general stationary transform, or the generic possibility that dispersion and hazard shape disagree.

## value

PASS

Erlang shape two is a natural first nonmemoryless capacity for this reset mechanism. The separate exact thresholds show precisely when stationary underdispersion coexists with locally decreasing exceedance hazard, and the result determines the entire hazard shape rather than just its slope at the origin or an example. The value is specific to this stationary spatial model, not a general statement about failure times, arbitrary capacity laws or transient diffusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
