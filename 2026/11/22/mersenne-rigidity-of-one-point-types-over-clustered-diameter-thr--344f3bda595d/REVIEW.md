# Independent mathematical audit

## correctness

PASS

A nonalgebraic one-point type is specified by its distances in {1,2,3} to the named finite base: the Katětov inequalities give precisely the metric extensions, universality and homogeneity give realizations and equality of the type for a given vector, and extending by multiple new points with the same old-distance vector and mutual distance 1 gives arbitrarily many realizations. For old distance 2 both inequalities hold for every assignment; for old distance 1 only the unordered pair {1,3} violates them. In a cluster of size a, combine the two palettes {1,2} and {2,3}, subtracting the all-2 assignment once; the factors are independent between clusters and weights are on named assignments. At (1,1,1) this gives M_{a+1}=2^{a+1}−1 per cluster. For an equality of scalar products, subtract multiplicities and choose the largest nonzero index J among finitely many exponent differences e_j. A primitive prime for M_J forces e_J=0 unless J=6, by Bang–Zsigmondy for (2,1). If J=6, prime 31 occurs only at j=5 and prime 5 only at j=4 among j=2,…,6, so e₅=e₄=0. The 3- and 7-adic valuations then give e₂=−2e₆, e₃=−e₆. Conversely that generator gives a true equality 63=3²·7. The signed changes in total base cardinality and cluster count are e₆ and −2e₆; hence either matching statistic forces e₆=0, implying identical profiles and base isometry. Every unequal profile pair has a common scalar of at least 63, since after canceling common cluster factors its value is 63^{|e₆|}. Equality at 63 uses precisely (5) and (1,1,2). The frozen checker and recorded log were read, not executed. Replay: python3 -B /workspace/review_evidence/independent_checks.py 5, a product-budget DFS independently checked 706 nonempty profiles and 558 attained scalars through one million, including 125 ambiguous scalars, both fixed-statistic injectivities and the first collision 63. DFS is exhaustive in the stated budget because factors increase with cluster size and exceed 1. It does not certify the infinite primitive-divisor theorem.

## originality

PASS

The full scalar inverse and the two fixed-statistic rigidity results are the supported distinct contribution. The type-polynomial factorization is already covered by a stronger graph-metric formula, and neither primitive divisors nor the numeric equality 63=3²·7 is new. The inspected sources did not state a stronger inverse theorem covering all the metric scalar fibers.

## value

PASS

A natural inverse problem is whether a scalar count of possible extensions can distinguish parameter metrics, instead of retaining the full polynomial or individual types. The answer here completely characterizes what information that scalar loses and shows two distinct readily available ways of recovering the whole profile. The contribution is limited but exact: it locates the sole all-size obstruction, rather than merely exhibiting the collision at 63 or evaluating a known count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
