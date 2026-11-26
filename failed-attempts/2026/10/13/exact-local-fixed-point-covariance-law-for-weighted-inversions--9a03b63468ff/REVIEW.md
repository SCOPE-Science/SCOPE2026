# Independent mathematical audit

## correctness

PASS

Given Pi(i)=i, the remaining bijection is uniform. Nonincident comparisons stay fair; an incident comparison has conditional success probability (n-i)/(n-1) if its right endpoint is i, and (i-1)/(n-1) if its left endpoint is i. Subtracting 1/2 and multiplying by 1/n proves the basis identities and hence the real-weight formula, also at n=2. Setting weights to one gives the negative square and summing it gives -(n+1)/6. The fixed-point factorial moments give variance one; the independent insertion ranks of a uniform permutation give inversion variance n(n-1)(2n+5)/72. These yield the stated correlation and asymptotic. Independent replay: python3 -I -B /workspace/audit_replays/frozen_math.py 1, with 322 exact basis-weight tests plus marginal variances and aggregate covariance for n=2 through 7.

## originality

FAIL

The central arbitrary-weight formula has demonstrable coverage in the distinct indexed Ewens mixed-tensor result, at theta=1 and by linearity for n>=3. Conditional means, the unweighted profile, aggregate and correlation follow at once; the additional n=2 case only enumerates the two permutations. The matching indexed entries are dated later than the frozen entry: this is a coverage judgment at review, not a claim that those entries had earlier priority or that the frozen proof was derived from them. Earlier count-conditioned sources do not independently establish that designated-location formula.

## value

FAIL

The local left/right imbalance is a useful diagnostic on its own, and the frozen exchangeability proof is short and clear. For the claim as assessed against existing mathematical coverage, however, the only additions to the indexed exact tensor specialization are a two-permutation boundary case and a routine normalization by standard variances. They do not supply a distinct useful exact invariant or a new mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
