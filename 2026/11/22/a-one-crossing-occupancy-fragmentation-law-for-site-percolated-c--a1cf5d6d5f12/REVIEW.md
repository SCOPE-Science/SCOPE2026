# Independent mathematical audit

## correctness

PASS

Condition on the two independent binomial shore counts. Both positive gives C=1; otherwise C=N, including zero for the empty graph. This gives F=(1-q^a)(1-q^b)+apq^b+bpq^a. The Bernoulli score (N-np)/(pq) gives Cov(N,C)=pqF'(p), and differentiation factors F'=nq^(a-1)H. Endpoint covariance is zero by determinism. For r=b-a>0, replacing bq^(b-1) by its upper bound bq^r shows H_q≥u-(a-1)q^(r-1)[br(1-q)+aq]/n≥2b/n; the last inequality follows because q^(r-1)[r(1-q)+q] is increasing to one. At balance H_q=m+1-mq^(m-1)>0. In the p coordinate H(0)=1 and H(1)<0 except K_1,1, for which H=1-p. This proves the strict signs and the unique maximum above F(1)=1 in the nonexceptional cases. At p=t/n the limiting H is analytic, nonincreasing, equals one at zero and tends to minus infinity; two roots would force it to vanish on an interval. Positive-root bracketing proves the stated proportional limit, including c+exp(-c)=2 at balance. For fixed a the pointwise interior limit H→1-(a+1)p gives the fixed-side limit by the same bracketing. The supplied finite rational checker was inspected, not executed; the bounded independent transition and derivative verification is documented in branches/47ffd03c-78d1-4092-9b43-487eabe2e90b/ordinal-2-root-check.md.

## originality

PASS

The exact finite joint distribution and hence the displayed covariance formula are already covered by a closed complete-bipartite specialization of the subgraph component polynomial. The surviving contribution is the strict one-crossing/unique-maximum theorem over the full parameter family and the two critical-root regimes. Best-of-knowledge comparison found no source that establishes those claims or implies them by simple specialization.

## value

PASS

The globally unique expected-fragmentation maximum is a meaningful structural boundary for independently thinned bicliques. Its location is of order one over graph size for proportional shores and of order one for a fixed small shore. These uniform and asymptotic results go beyond prior finite enumeration; they do not extrapolate to arbitrary hosts, unequal retention or bond percolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
