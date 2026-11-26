# Independent mathematical audit

## correctness

PASS

The cut at edge 1–2 starts two parts of size one. The next label joins a part with probability proportional to its size, so induction yields uniform S on 1,...,n-1. Fixing a membership sequence, each possible parent assignment within the parts has the same probability, and the allowed assignments form a product over arrivals; relabeling gives independent recursive trees. Only the complement root has its fringe size changed by the cut: it was n and becomes n-s. Thus exactly the term 1_{n-s=k} must be removed from the two induced counts. The insertion mean recurrence has the distinct root boundary f_{k,k}=1 and the stated leaf recurrence; at m=k the creation term gives 1/k for size k in the tree of size k+1, as required. The symmetric sum of component means has zero covariance with uniform S, leaving -((n-k)-n/2)/(n-1). This is valid at n=2,k=1 as well. Independently enumerated every parent sequence for 2≤n≤8 by walking ancestor chains and matched the conditional means and covariances in all cases.

## originality

FAIL

The arbitrary-k expression was not found verbatim, and global-global covariances alone do not imply it. But the exact conditional component split with independent recursive trees, already proved in a distinct indexed leaf-law result, and the established all-k fringe mean mechanically give the requested conditional regression and covariance. The only count correction is the already present root boundary with the size target changed to k.

## value

FAIL

The exact sign change is a natural illustration of the complement-root correction. In this case the known conditional product law and exact fringe means already give the regression by adding the two component counts and removing the one affected root. The sign then follows by symmetry and evaluation at one of the n-1 equally likely sizes. There is no further motivated unknown invariant or new structural argument surviving this mechanical implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
