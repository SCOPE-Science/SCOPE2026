# Independent mathematical audit

## correctness

PASS

For P(n)=n(n+1)(2n+1)/6 and a=563,b=11, square-cobalancing is precisely 574P(n)=11P(n+r). Direct integer evaluation gives P(5)=55, P(20)=2870, P(142)=964535, P(532)=50331190, so 574·55=11·2870=31570 and 574·964535=11·50331190=553643090; r=15,390. gcd(563,11)=1 and both indices >1. Setting X=2n+1,Y=2(n+r)+1 gives 11Y(Y²−1)=574X(X²−1) and rational integral points (11,41), (285,1065). Homogenized cubic is nonsingular: at Z=0 derivatives imply X=Y=0, impossible; for Z≠0 derivatives impose X²=Y²=Z²/3 and 11Y=574X, a contradiction. Thus smooth plane genus-one curve with rational point. The bounded scan n≤10000 in checker cannot prove global completeness, which is not claimed.

## originality

PASS

Best-of-knowledge PASS only for explicit *nontrivial* primitive coefficient collision with b>1 and both indices n>1, not broad existence of any nonunique pair. Cui et al. Definition 5.2 and Figure 2 record no multiple cases for a,b≤120 and speculate uniqueness; present a=563 lies outside the search. OEIS A374500 square-pyramidal product P(115)=P(11)P(14) yields weaker b=1 / index1 collisions and does not imply the given 574:11 ratio. Direct ratio equations are checked; Resultary searches found only the same record for exact parameters, not a dominating table or Diophantine classification.

## value

PASS

A concrete exact counterexample to the published apparent one-solution phenomenon in the natural square-cobalancing problem, satisfying stronger nondegeneracy b>1 and two non-unit indices; a specialized but mathematically motivated witness to an explicit open experimental conjecture. The independent exact cubic rational-point structure makes the pair useful for further Diophantine analysis. No misleading claim of global uniqueness, minimal coefficients, or an exhaustive integral-point census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
