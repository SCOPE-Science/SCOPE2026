# Independent mathematical audit

## correctness

PASS

After any positive number of draws at most two coupons can remain unseen. For any k≥1, the probability of one specified missing coupon is q^k and the probability of two specified missing coupons is p_ij^k, giving exactly nq^k−Σp_ij^k. Strict Jensen minimizes the pair power sum uniquely at uniform for k≥2. After scaling by q, independent positive-support incidence columns characterize vertices of the row-sum-one polytope. A support leaf forces a unit isolated edge; otherwise, the number of edges is both at least the vertex count by minimum degree and at most that count by column independence. Hence the remaining components are cycles, necessarily odd and half-weighted. Strict convexity forces every maximum of the power sum to be a vertex. If r vertices lie in odd cycles its value is n/2−r(1/2−2^(−k)), strictly decreasing in r. The smallest r is zero for even n and three for odd n, with exactly the stated supports. k=1 gives tail 1 regardless of p; the means include the k=0 tail 1 and follow by geometric summation, with strictness inherited from k=2. Exact-rational independent checks of n=4 through 8, including direct omission-sequence enumeration for horizons at most 3, agree. Replay: /workspace/branches/ee948815-2b18-48fe-aa70-c19773757914/check_independent.py. The uploaded checker was inspected but not executed; the finite tests do not establish the arbitrary-n result.

## originality

FAIL

The full sandwich with equality is recoverable from verified existing exact results, including the odd case. An indexed coupon-moment theorem gives the very survival reduction and its unique uniform upper extremum in the two-omission model. An earlier indexed geometric result treats the identical fractional matching polytope, classifies all its vertices, and gives precisely the parity extremizers of the square objective. On those vertices, every k-power sum is a strictly increasing affine function of the square sum (shown below), so strict convexity transfers exactly that classification to all horizons. This is an implication assessment, not a claim of copied work or publication priority.

## value

PASS

The balanced package constraint is natural and the horizon-by-horizon optimizer classification is stronger than one mean comparison. In particular the odd obstruction identifies a concrete parity difference in feasible optimal sampling, not an isolated table value. The useful probabilistic formulation does not override the coverage assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
