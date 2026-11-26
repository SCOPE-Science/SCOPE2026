# Independent mathematical audit

## correctness

PASS

The factorial degree is the rectangular tableau hook product, and the even-dimensional Schubert cells give the ordinary Euler characteristic binom(n,k). Duality preserves both. For k=2 the degree is Catalan(n−2); the successive degree/Euler ratio multiplier is 2(2n−3)(n−1)/(n(n+1))>1 for n≥4. The consecutive ratios 14/15 and 42/21 prove the edge threshold. For fixed n and r=n−k≥k+2 the adjacent degree quotient is the product of (kr+j)/(k+j) for 1≤j≤r−k−1, all >1. The degree in three rows starts at 42>20 for n=6 and grows by a factor >2, since (3r+1)/(r+1)>2 for r=n−3≥3 and each of the other two quotient factors exceeds 1. The central binomial maximum grows at most by 2 by Pascal's rule. This proves all interior cases; the projective-space edge and dual cases exhaust the domain. Independent replay `python3 /workspace/checks/frozen_replay.py 4` verified 4950 comparisons via exact cellwise hook lengths, not the factorial expression in the frozen proof; finite regression only. Frozen support describes a checker but supplies no script for this record.

## originality

FAIL

The complete non-projective-space classification and exclusion of equality are explicitly covered by a distinct indexed record. The only added cases are projective spaces, with degree 1 and Euler characteristic n, so they give no distinct threshold.

## value

FAIL

The non-projective crossover is a meaningful classification, but the frozen submission does not add a new scientifically useful instance to it. The only scope expansion is the routine comparison 1<n on the projective-space edge, and the frozen claim supplies no further invariant or result supported by that addition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
