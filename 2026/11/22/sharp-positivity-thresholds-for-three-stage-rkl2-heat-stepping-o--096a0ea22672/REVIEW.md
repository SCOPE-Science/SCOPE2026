# Independent mathematical audit

## correctness

PASS

The normalized three-stage Legendre polynomial is 7/12 + (5/12)P3(1−2t/5), so r is in [1/6,1] through t=5 and strictly decreases to −∞ afterward. The quadratic in 1−r(t)=t(1−t/2+t²/15) is strictly positive. For N=p+q, the constant, class-contrast, and within-class zero-sum eigenspaces yield eigenvalues 0,N,q,p (omit zero multiplicities). For distinct vertices in the class of size p, the entry is [p+q r(Nh)−N r(qh)]/(Np) = qh²[1/2−(p+2q)h/15]. Swapping parts gives the other within-class entry, and cross-class entries are (1−r(Nh))/N. For p≥2, the smaller class's cutoff has Nh≤5, ensuring positive scalar terms in both diagonals; the smaller-class entry is negative at every larger step (both classes tie if p=q). For a star with q≥2 the hub diagonal (1+q r(Nh))/N crosses first: r(45/8)=−343/512<−1/q while the leaf-pair zero has Nh≥45/8. Leaf diagonals are positive to the hub cutoff since r(h)≥1/6 there. On K1,1 only the constant and contrast modes contribute, so positivity coincides with |r(2h)|≤1. In every case the full stability horizon follows from the largest eigenvalue N and the exact scalar interval [0,α]. This verifies all endpoints, h=0, and nonreentry. The two horizon ratios and star limit follow by scaling and continuity.

## originality

PASS

Best of the available evidence supports the distinct three-stage RKL2 complete-bipartite endpoint classification, not the polynomial, scalar stability calculation, or a general positivity principle. Known Taylor, directed-chain, and grid results are credited. The closest broad weighted-bipartite index result has a sharp star gain incompatible with applying its stated conclusion to RKL2; full-text coverage beyond that indexed conclusion was not established.

## value

PASS

A graph-specific sharp safe-step benchmark is useful because the scalar stability condition is strictly too weak on every nontrivial member of a standard graph family. The exact star versus nonsingleton split and the balanced tie locate different constraints that a scalar criterion cannot identify; the horizon and stability gap are meaningful for timestep selection. It is not a claim about stage positivity or error at the endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
