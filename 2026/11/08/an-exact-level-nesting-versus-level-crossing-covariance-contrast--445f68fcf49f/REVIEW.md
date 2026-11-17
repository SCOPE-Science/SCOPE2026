# Independent mathematical audit

## correctness

PASS

Marked adjacent arc (i,i+1) contracts bijectively to a partition on n-1 points. It cannot introduce a crossing, but it is nested by each contracted arc (a,b) with a<i<b; old crossing/nesting pair order is preserved. Because E[N-C]=0 by 2-arc equidistribution, covariance gap is sum over contractions of h_i divided by B_n, namely D_{n-1}/B_n where D_m=sum_arc(b-a-1) over m-partitions. Aggregate dimension identity D_m=(m+4)B_{m+1}-2B_{m+2} follows from marking blocks and cut counting, so final gap n+3-2B_{n+1}/B_n. Exact rational Bell recurrence independently checked gap 0,0,1/15,5/26,73/203,490/877 for n2..7. Positivity follows from d>=0 and a nontrivial arc spanning one point for m>=3; Bell ratios B_{n+1}/B_n=O(n/log n) yield normalized limit 1.

## originality

PASS

Kasraoui-Zeng establish marginal crossing/nesting pair equidistribution, and Chern-Diaconis-Kane-Rhoades supply dimension sum and general shifted-Bell moment framework. Neither directly asserts the level-weighted covariance gap or its exact all-n sign: the marked-level contraction exposes a further nesting contribution absent from marginal equidistribution. Earlier Resultary block-versus-crossing covariance studies a different local statistic and displays another sign law. Best-of-knowledge PASS, with residual possibility that general mixed-moment appendices encode this identity implicitly.

## value

PASS

Crossings and nestings are exactly equidistributed marginals, so a strictly positive linear-order covariance asymmetry with the natural adjacent-arc count is a motivated dependence invariant invisible from the one-statistic enumerators. The marked-arc contraction identity is a substantive structural explanation and gives exact finite and asymptotic answers, not just a numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
