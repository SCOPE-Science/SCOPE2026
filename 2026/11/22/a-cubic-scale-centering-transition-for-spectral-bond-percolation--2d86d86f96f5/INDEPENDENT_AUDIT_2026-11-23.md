# Independent mathematical audit

## correctness

PASS

The positive eigenpair of the quotient [[0,ns],[1,s-1]] gives the exact Perron root; s=o(n) gives sp=o(1), nsp→∞ and sigma∼sqrt(c)(ns)^(1/4). Independent clique contributions and an independent conditioning calculation validate the bottleneck variance step: with K~Bin(s,p) open spokes in one clique, its oriented count Z conditional on K is Bin(K(s−K),p), since each edge between an open and a closed spoke appears only once. The independent-copy variance identity and |k(s−k)−l(s−l)|≤(s−1)|k−l| give Var Z_n≤ns(s−1)p²+ns(s−1)²p³. Multiple length-two arrivals cost at most ns*binom(s−1,2)p⁴(1−p) in expectation; every remaining indirect vertex has a simple path entirely inside its own petal, bounded by n(sp)^3/(1−sp). Thus the aggregate mean absolute error is o(s), E Z_n/s→c² for s→∞ and Var Z_n=o(s²) in that regime. E B_n=O(s) handles bounded or irregular sequences at t=0, including s=1 where B_n=0. The binomial CLT and convergence-in-probability shift need no independence between direct and indirect counts; tightness gives divergence in the last regime. The coefficient follows from c²s/sigma∼c^(3/2)(s³/n)^(1/4).

## originality

PASS

On the evidence inspected, the three-regime centered rooted limit and its coefficient are not previously supplied. This is a conditional best-of-knowledge finding, not a priority certificate.

## value

PASS

This addresses a natural fluctuation question left by order-level spectral bounds on a highly irregular family. The exact center at the actual spoke mean matters at the transition, and the theorem distinguishes invisible, finite and overwhelming drift produced by internal clique edges, including a usable mean-shift constant. It is not a claim of a new percolation threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
