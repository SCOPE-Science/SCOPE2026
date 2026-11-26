# Independent mathematical audit

## correctness

PASS

In RESULT.md:23–47, index the gaps clockwise from a specified sampled start, not from a fixed spatial cut; rotation gives uniform simplex spacings, and K and U are independent of the indexing convention. Translating the simplex gives the one- and two-spacing tails; integrating them recovers E[K U]=(1−a)^n+(n−1)(1−2a)_+^n and the stated covariance. For a<1/2, the sign of the derivative of the normalized covariance in x=(1−2a)/(1−a) is that of x^(n−1)(2−x)^n−1. This product has one interior maximum and falls to 1 at x=1; the resulting decrease-then-increase and endpoint signs give exactly one covariance zero for n≥3. For n=2 the sole zero is a=1/2; the a≥1/2 formula has the required signs. Expanding the powers to second order in 1/n before multiplying by n gives the displayed compact-uniform C_n(c/n) expansion. The increasing series (exp(c)−1−c)/c² gives a simple positive limiting root with f'_0(c*)=c*(c*−1)exp(−2c*); simple-root perturbation gives correction c*/2−c*². Independent bounded bisection gives a_3≈0.403330466414 and a_100≈0.017703229735. These diagnostics do not stand in for the proof. The frozen script was not executed.

## originality

FAIL

The 2026/10/18 Resultary result states the same finite-sample gap–vacancy covariance, full sign transition and second-order critical length for the same fixed-length uniform-arc model. The 2026/10/13 covered-fraction result independently covers the sign law and leading depth under sign reversal. This is positive statement-level prior coverage, not a failure due to inaccessible papers.

## value

PASS

As a structural statement the sign classification distinguishes fragmentation from total vacancy for every finite sample size and locates the change to two orders; it is not merely a numerical recomputation or a marginal statistic. That intrinsic value does not make a duplicate a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
