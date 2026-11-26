# Independent mathematical audit

## correctness

PASS

Weighting by Z is exactly the marginal from planting an increasing subsequence at a uniform k-set of positions. Under the base law, permuting entries inside each consecutive block preserves the restricted count of increasing subsequences using at most one position per block. Hence its conditional expectation on prescribed internal orders is unchanged. On the descent events this restriction contains every increasing subsequence: the cases have one block of length 2, one block of length 3, or two disjoint blocks of length 2. Excluding forbidden marked-position sets by elementary counting gives all stated one- and two-point probabilities. For separated positions y/x is zero when k=2 or 3, and for 4≤k<n is the product (k-2)/(n-2) times (k-3)/(n-3), strictly below x=k(k-1)/(n(n-1)); hence the separated covariance is strictly negative unless k=n, when the permutation is the identity. The variance sum uses n-2 adjacent pairs and (n-2)(n-3)/2 separated pairs. Independent symbolic factorization gave the submitted variance, and exact planted position/value enumeration checked all probabilities, means and variances for 4≤n≤7, 2≤k≤n (python3 /workspace/branches/independent-checks/check_descents.py). The variance/n limit follows by scaling the polynomial as n tends to infinity, including α=0,1. These finite checks do not replace the general proof or give a CLT.

## originality

FAIL

The primary comparison that determines the verdict is not Pinsky's model identity alone. Gessel–Zhuang's classical exact shuffle product, applied to Pinsky's planted-card construction after complementing values, yields the entire descent-set distribution in this model. Its elementary monomial coefficient specializes directly to the one-point, adjacent and disjoint-pair formulas. Covariance and variance then follow by subtraction and summation. No identical standalone statement was found, but it is a mechanically covered specialization.

## value

FAIL

The change in separated-descent dependence is a meaningful interpretation, and the formulas are convenient. But the exact pair probabilities are routine coefficient specializations of a known stronger descent distribution principle, and the covariance sign, total variance and variance limit then require only elementary arithmetic. The submission does not isolate a further nonmechanical statistic or structural conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
