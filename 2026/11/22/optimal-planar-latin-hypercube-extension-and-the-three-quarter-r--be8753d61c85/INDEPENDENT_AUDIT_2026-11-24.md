# Independent mathematical audit

## correctness

PASS

A conflict-free retained subset can always be completed by pairing unused first-axis strata with unused second-axis strata and placing one point in each product rectangle. Each new interval is shorter than an old stratum and therefore can contain only points from at most two consecutive old strata. Each axis is a matching, so the simple union consists of paths, even cycles and isolated vertices; the alternating path/cycle formula computes the exact optimum in linear time given the old stratum order on each axis. For N=n+1 the offsets are independent Bernoulli bits with the stated rank-dependent probabilities; a collision is the adjacent pattern 10. The collision-free strings 0^k1^(n-k) have total probability 2^n*n!/(n+1)^n on an axis, by summing their binomial weights. The two coordinate-order bit arrays are independent, including after conditioning on the permutation, so the square and its Stirling equivalent follow. Adjacent collision indicators are one-dependent with mean sum n(n-1)/(6(n+1)) and variance O(n), so endpoint incidence tends to p=1/3 on each axis. Given the sizes, uniform relative relabeling of the two matchings has the graph statistics of two independent uniform partial matchings. For any fixed number of exploration steps, unexposed endpoint fractions are p+o(1) since only finitely many matched pairs and unmatched vertices have been revealed. Two bounded explorations at independent uniform roots are asymptotically independent: they intersect with vanishing probability and finite exposure changes the second exploration's probabilities by o(1). This gives a second-moment law for the truncated endpoint counts. Starting at an A-only endpoint, stopping at another A-only endpoint has limiting probability (1-p) times the geometric sum of p^(2k), namely 1/(1+p); the survival probability after a fixed even truncation tends to p^(2k), bounding the unclassified endpoint fraction via Markov and then k to infinity. Each such path has two A-only endpoints, giving T_A/n and T_B/n tending to 1/12. With doubled edges treated as two-cycles, deletion cost is (m_A+m_B+T_A+T_B)/2, hence D/n tends to 1/4 in probability and in mean. The target N=n+1 does not mean at most one new evaluation. Independent rational bit-pattern enumeration through n=7 corroborated the finite no-collision and mean collision formulas; for n=2,3,4 the one-axis no-collision probabilities were 8/9, 3/4, 384/625. The supplied checker was inspected, not executed, and no finite test is used to infer the limit.

## originality

PASS

The objective and maximum-independent-set reduction are directly covered by Liu–Li–Yang (2015) and are not credited as new. The strongest supported distinctions are the exact planar path/cycle specialization and the sharp random n-to-n+1 retention and no-deletion laws under independent jitter and random relative order. The 2017 full-text comparison remains incomplete.

## value

PASS

Exact retention of existing coordinates avoids throwing away usable evaluations. The planar specialization replaces a general graph search by two scans and a component traversal. Independently of that speedup, the probabilistic theorem shows that enlarging a randomly jittered design by just one target stratum typically costs re-evaluating about a quarter of its old points, and that full retention is exponentially unlikely. These are useful exact benchmarks for distinguishing this extension setting from nested designs constructed to preserve observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
