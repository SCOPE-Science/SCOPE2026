# Independent mathematical audit

## correctness

PASS

The statistic is a second factorial cumulant on the diagonal, not a variance. Write q=1−p and R=binom(n−a,b)/binom(n,b). Counting ordered disjoint pairs of connected components divides the product of the individual expected counts by the double counting of ab absent cross-edges and multiplies by the disjoint-set ratio R. Thus the normalized cumulant is R q^(−ab)−1 for a+b<=n and −1 when a+b>n; the means are positive for all in-scope sizes and 0<p<1. The unique feasible zero is π=1−R^(1/(ab)). The finite logarithmic average and positive Laplace representation are valid even at a+b=n. The strict log-convexity in size of (exp(tx)−1)/(x(exp(t)−1)) follows from 2 sinh(tx/2)>tx, giving the strict balancing comparisons, including the diagonal. Coordinate monotonicity is strict by adding a larger terminal row or column; the global extremes then give 1/n and 1−n^(−1/(n−1)), coinciding only at n=2. The ordering gives opposing ordinary covariances for (2,3) and (1,4) on an open interval for every n>=5. At n=5 and q=27/40, independent integer comparisons gave 40^6−10·27^6=221795110>0 and 5·27^4−40^4=97205>0 (replay: branches/review-exact-small-checks.js). The frozen verifier was inspected but not executed. The all-size conclusions were checked by proof, not inferred from finite enumeration.

## originality

FAIL

The exact finite-n distinct-size covariance sign law, the normalizing factorial ratio and its rectangular log average are explicitly covered in the October 18 matched result. The diagonal extension uses the same disjoint ordered-pair calculation already supplied by the general component-tuple law. Although the prior graph result does not state the fixed-total ordering, that ordering is a direct corollary of its exact formula and standard convex majorization: two applications of the fundamental theorem of calculus turn the factorial ratio into the expectation of a strictly convex function of an exchangeable weighted sum. The exact implication and strictness are shown below. This is a finding of derived coverage, not a claim to have located the exact comparison verbatim, and not a verdict based on inaccessible sources.

## value

FAIL

The dependence question is natural, and the same-total opposing signs are a useful illustration. For this submission, however, after crediting the already exact sign law and ordered moments, the remainder is the standard strict Jensen comparison of a symmetric convex integral mean. The global endpoints and opposing-sign example are immediate evaluations or consequences of that comparison. No additional substantive classification, independent obstruction, or nonroutine result survives this reduction; a different proof or a larger finite check would not change that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
