# Independent mathematical audit

## correctness

PASS

The Cauchy–Binet minors of rows (1,1),(e^{-at},e^{-bt}),(e^{-aT},e^{-bT}) give F=x²(1−u)²+q²(1−v)²+q²x²(u−v)². Its derivative in x is 2x Q_T(u), with Q(v)=(1−v)(1−rv) and Q(1)=q²(1−v)(r−v). The convex quadratic has one interior minimum when T≤Tc and two interior critical points (one unique global maximum) when T>Tc; endpoints exactly tie. Q(1/r)>0 with Q′(1/r)<0 gives t*<Tc, and the two critical limits equal Tc, so nonmonotonicity holds. For T→∞, F(t*)→r^{-2/(r−1)}(1−1/r)², while endpoint value decays as 2e^{-2aT}, giving the stated ratio. Independently checked 20 rate/horizon parameter pairs against 1001 grid points and exact quadratic candidates; finite grids are only diagnostics.

## originality

PASS

Published damped-Jordan pinned three-event design has an analogous transition at aT=1 for the confluent signal e^{-at}(A+Bt), but it does not give the distinct-rate bi-exponential determinant or exact Tc=log(b/a)/(b−a) and quadratic optimizer. Dette et al 2004 exponential regression concerns unknown rates, unrestricted approximate design/support and a different parameterization, not this three fixed-event problem. Semantic searches for the same known-two-rate fixed-endpoint schedule found no dominating theorem. Best-of-knowledge originality, not exhaustive priority.

## value

PASS

A complete D-optimal placement classification for the naturally constrained three-observation two-exponential estimation problem gives a sharp and useful duration threshold, explicit optimal event, and quantifies the high-horizon loss from endpoint replication. It directly answers sensor/measurement timing choices; not merely a reformulation of observability rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
