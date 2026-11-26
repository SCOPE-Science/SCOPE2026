# Independent mathematical audit

## correctness

PASS

Subtracting adjacent clamped outputs gives exactly the three coefficients in RESULT.md (1): ell_i, 1-r_i-ell_(i+1), r_(i+1), on increments d_(i-1), d_i, d_(i+1) respectively. With q=rho(|d_i|), the sum r_i+ell_(i+1) is bounded by bq/(1+bq)+aq/(1+aq), and it is this upper bound that is at most 1 iff ab q^2<=1. Thus on the sufficient side the edge matrix is nonnegative, with column sum 1 except for the lost boundary terms r_0 and ell_(n-1); for n=2 both losses are in the same column. Splitting each row into positive and negative contributions before taking its absolute value gives exactly the two losses plus twice the rowwise minimum, proving (3). The step (0,0,1,...,1) has unchanged endpoints and nonnegative output increments for n>=4, so the gain of 1 is attained. For ab>1 select delta>0 with ab rho(delta)^2>1 by continuity at 0. For the proposed monotone six-entry input, the endpoints are fixed and the central output increment tends to delta[1-bq/(1+bq)-aq/(1+aq)]<0 as T grows, because T rho(T) vanishes. Thus at some finite T the fixed endpoints and a strict negative output edge give TV increase, and endpoint repetition preserves the witness for n>6. This proves the one-input iff for n>=6 and sufficiency for n>=2, not two-input Lipschitz contraction. Inspected the source proof and VERIFICATION.md/verify.py without executing the upload; the reported finite rational tests apply to one affinity and are not used for generality.

## originality

PASS

The novelty judgment concerns the sharp directed product boundary and matching converse for the same clamped, range-weighted map and one-input seminorm, together with the exact dissipation. Harten's general sufficient incremental-form criterion already covers the mechanism of sufficiency after the coefficient bound. The inspected literature and distinct indexed comparators do not supply the matching necessity criterion or an equivalent directed classification. This is a bounded coverage judgment, not a priority claim.

## value

PASS

The directed weights may be very asymmetric, so a sharp bound on their product is more informative than separately restricting both spatial weights. The theorem settles precisely when every signal loses no stability in the one-input TV sense, and the adverse example above the boundary is monotone and needs only six sites. The dissipation separates boundary leakage from interior cancellation and identifies attainable equality. The meaningful advance is the sharp classification and witness, not re-proving the generic sufficient incremental lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
