# Independent mathematical audit

## correctness

PASS

The statement is for increasing, order-decreasing restrictions of translations, with the empty map counted once. For a fixed shift d>0, each rank-r domain gives r distinct edges in a residue-class forest, so there are 2^(n-r) partial identities with equal membership bits at the endpoints. The sum over d gives binomial(n,r+1) domains; reversing the factor order doubles the count. Normalizing at j=r+1 gives the asserted truncated Bin(n,1/3) law; the crossing event is empty at n=1, as the stated scope requires. In the concentration proof the selected positions exceed k+l, making all indicated bits admissible, and spacing K+1 makes the equations independent. The per-equation probabilities 3/4 and 5/8 account for coincident bits at zero shift; summing the geometric stratum sizes and tail is valid. With K=floor(sqrt(n)/2), each error is O(exp(-sqrt(n)/4)), and the normalizing size differs from 2^(n+1) by n+1. A separate composition replay matches all crossing ranks, the idempotent core, and complete ordered totals 4,21,102,449,1820,7033,26420,98245 for n=1..8.

## originality

FAIL

Both principal conclusions are covered at the statement/implication level by distinct same-day records. The parity-sensitive spectrum explicitly identifies the exact downward-translation summand before doubling for factor order. The broader signed-translation concentration theorem gives an exponentially small excess count over 4^n; restriction to the submonoid preserves the entire idempotent core and only removes excess pairs. Since the two sizes are both of order 2^n, this gives a stronger rate for this very probability and for conditional idempotent concentration. This is demonstrated coverage, not an inference of historical priority from the catalogue date or a claim that the result is false.

## value

FAIL

The monoid and crossing invariant are natural, but the submitted exact statistics are obtained by discarding other terms in a known rank sum (or by inversion and doubling); the concentration law follows from the larger monoid with a weaker advertised rate. No fixed-idempotent distribution, new estimate beyond the wider result, or additional statistic not obtained by these direct reductions is proved. A rewrite or an additional finite check would not change that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
