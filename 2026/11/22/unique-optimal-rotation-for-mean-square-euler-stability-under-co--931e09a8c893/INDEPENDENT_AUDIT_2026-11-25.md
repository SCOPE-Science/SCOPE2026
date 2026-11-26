# Independent mathematical audit

## correctness

PASS

The second-moment map is T(V)=CVC^T+tau*x*P V P with C=(1-x)I+sqrt(s)xJ. Testing every deterministic vector is equivalent to decay for all PSD starts by their finite rank-one decompositions. If q=(1-x)^2+s*x^2>=1, the noiseless second moment already fails to decay and positivity gives necessity. Otherwise put R=(I-T0)^(-1). If tau*x*(R(P))_11>=1, the nonzero PSD matrix R(P) satisfies T(R(P))>=R(P), including equality at the threshold. If the gain is <1, the positive rank-one resolvent gives V=(I-T)^(-1)I>=I, with T(V)=V-I<=rV for some r<1, proving decay by domination. I independently formed the symmetric-basis update and recovered F_s from the determinant ratio, including exact checks of both cleared derivative identities (`python /workspace/branches/review_recomputation.py`). In the transformed step coordinate t in (0,1), F_x is strictly positive, also at s=0, with the stated limits; thus strict inequalities give the entire stable interval. At fixed x, the numerator of F_s's frequency derivative is twice G_x, whose positive-degree coefficients are strictly positive and constant nonpositive. It yields at most one stationary point and makes any interior stationary point the strict profile minimum. For 2<tau<4 the continuous step ceiling vanishes at both s0 and infinity and attains a positive interior maximum. At its step, the fixed-step frequency profile is uniquely minimized; no larger step can be stable anywhere, by step monotonicity and the deterministic domain shrinking with step. This also establishes uniqueness of the stationary pair. The independent tau=3 sample gives x=0.0422474914026233618188663, s=5.00825714726004962531281 and sqrt(s)=2.23791357010498723713038. The frozen code and recorded output were read, not run; the numerical example is not the basis for uniqueness.

## originality

PASS

The covariance criterion and rank-one feedback technique are not new. The inspected prior results give a route to the stability inequality by model-specific specialization but do not supply the unique quantitative rotation optimum and its global two-equation characterization for this planar scheme.

## value

PASS

The natural contrast between normal rotational damping and anisotropic noise yields a usable stability trade-off: for 2<tau<4 no unrotated step works, while enough rotation restores stability, yet faster rotation eventually drives the sharp step to zero. The exact ceiling, its unique intermediate optimum and characterization resolve this trade-off beyond a generic spectral test or eventual small-step existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
