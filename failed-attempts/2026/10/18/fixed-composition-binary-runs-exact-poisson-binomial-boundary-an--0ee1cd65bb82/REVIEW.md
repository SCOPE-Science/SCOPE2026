# Independent mathematical audit

## correctness

PASS

The statistic is R−1 for R runs in a uniform word of fixed composition. When both counts are positive, two monochromatic blocks attain the minimum 1. Alternating the runs gives maximum M=2m for h>m and 2m−1 for h=m. Each intermediate value is possible by choosing alternating positive run lengths with the required totals. Sampling without replacement gives single-indicator probability 2ab/[N(N−1)], successive-pair probability ab/[N(N−1)], and disjoint-pair probability 4a(a−1)b(b−1)/[N(N−1)(N−2)(N−3)] when such pairs exist. Counting the two kinds of pairs gives the stated mean and V=μ(μ−1)/(N−1). A Bernoulli representation with endpoints 1,M has exactly one constant-one summand and M−1 nondegenerate summands. At that mean its variance ceiling is attained by 1+Binomial(M−1,(μ−1)/(M−1)); this follows by completing the square in the Bernoulli parameters. Subtracting the ceiling from V leaves (μ−1) times [μ/(N−1)−(M−μ)/(M−1)]. For h>m, the numerator of the bracket on denominator (N−1)(M−1) is 2m(m−1)(h−m)/N. For h=m, V=m(m−1)/(2m−1) while the ceiling is (m−1)/2. Both give the claimed positive gaps. A monochromatic word, including N=1, gives T=0; for m=1 the minority position gives the stated shifted Bernoulli, including the deterministic two-letter case. A fresh bit-word enumeration compared exact support, moments and gaps for all 119 compositions with 1≤N≤14. It corroborates the proof but does not replace it. The supplied checker was inspected, not run; its replay entry point is python3 verify.py in the frozen package.

## originality

FAIL

No direct earlier statement of this exact boundary was verified. The failure is instead by mechanical implication: the classical fixed-margin runs distribution already gives both endpoints, the mean and the variance, and the sharp variance ceiling for a sum of Bernoullis with those endpoints is immediate from equalizing the parameters at fixed mean. Their subtraction gives the exact gap without a new distributional calculation or inequality. At the two exceptional minority sizes the same distribution is deterministic or has consecutive two-point support. Neither of the similar same-day iid records is used as exact coverage.

## value

FAIL

There is a natural question here—dependent transition indicators may still have an independent-sum law—and the support-matched comparison is a useful explanation. But the exact gap and minority boundary follow routinely from the already available exact support and moments via a one-step sharp variance bound. The frozen claim does not establish a further structural result or a nonmechanical exact invariant; packaging the subtraction or its real-rootedness consequence does not meet that bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
