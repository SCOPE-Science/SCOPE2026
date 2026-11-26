# Independent mathematical audit

## correctness

PASS

Modulo two both roots are simple. On each input parity the two valuations are distances to the lifted roots of f(n) and f(n+1), respectively. Writing A for the difference of the two roots of f, the within-parity center separations have valuations of 1+A and 1-A. One is exactly 1, and their product is R/a², giving the other depth d, also when R=0. In a parity of depth e, a distance valuation below e forces the same valuation at the other center; a valuation above e forces the other valuation to be exactly e; (e,e) is impossible since there are only two lifts at the next binary digit. Each listed event is one exact-valuation residue class at the larger exponent plus one. The two parities have disjoint cell supports. The one-center distribution is geometric with mean 2 and second moment 6. Independently, the conditional joint tail at thresholds i,j is 2^(1−max(i,j)) if min(i,j)≤e and zero otherwise. Relative to coincident centers the missing sum over min(i,j)>e is 6·2^(−e), which gives the asserted covariance on averaging depths 1 and d. Root congruence counts bound empirical tails by 2·2^(−k)+2/N and positivity and quadratic growth bound the maximum valuation by O(log N); summation controls the second moments and hence the mixed moment. The sign threshold and realizing triples check directly. The exact check in /workspace/reproductions/exact_checks.py 2 covers five triples, including R<0 and R=0.

## originality

PASS

The same-day odd-prime root-collision record has a nearly identical general mechanism and covariance sum, and its root-ball argument carries over to two. Its theorem as stated excludes two, however, and its sign conclusion for two common residue roots is false at two. The distinct contribution is the dyadic adjacent-quadratic reduction of both depths to a single coefficient invariant, and the resulting exact cells and negative-to-positive phase change. The general method is not original here.

## value

PASS

Neighbouring values introduce a natural dependence question beyond marginal quadratic trees. The classification gives an exact residue modulus for every possible transition, plus a coefficient criterion separating opposite signs even though the two marginal laws never change. It thus expresses a useful invariant of this family and a genuine limitation of the odd-prime sign rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
