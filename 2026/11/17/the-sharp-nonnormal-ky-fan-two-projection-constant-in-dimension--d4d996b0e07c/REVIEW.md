# Independent mathematical audit

## correctness

PASS

For singular values s1>=s2>=s3 the identity A=(s1-s2)R1+2(s2-s3)R2+2s3R3 has nonnegative coefficients summing to s1+s2, with partial-isometry R1=UE1V*, R2=UE2V*/2, R3=UE3V*/2, all Ky Fan-two norm1. Rank2 is bounded by ||C(R2)||_(2) <=sqrt(2)||C(R2)||_F <=1. Rank3 is U/2 with unit-circle eigenvalues; pairwise separation and quadratic (10+2c-8c²) give <=3/(2sqrt2)<1/2+sqrt6/4. Any rank1 partial isometry is unitarily conjugate, up to phase, to matrix first row (r,sqrt(1-r²),0); centred top block has sum of two singular values1 and the discarded smaller singular value <=r/3, giving ||C(R1)||_(2)=(1+sqrt(1-8r²/9))/2+r/3, uniquely maximized at r²=3/8. This real rank1 witness gives equality. Averaging arbitrary real-linear traceless projection over O(3) or U(3) conjugation kills its traceless value on identity/complex scalar trace, yielding C without increasing norm, proving minimality. On Hermitian matrices scalar eigenvalue triples reduce to finite signed extreme points; centering norm<=1, equality at (1,0,0). Independently checked explicit witness and 1200 real/complex random partial isometries; finite sampling is not the operator norm proof.

## originality

PASS

Best-of-knowledge comparison of the exact mathematical statement/implications with named primary sources and published research; no independently earlier equivalent or dominating theorem found among inspected material. Same-day matching Resultary entries were excluded as independent prior evidence. Specific inaccessible texts and older alias risks are retained; negative searches are not treated as proof of uniqueness.

## value

PASS

The first genuine intermediate Ky Fan rank in the first eligible dimension has a natural exact minimum projection constant. It strictly separates nonnormal full-matrix trace removal (about 1.11237) from its Hermitian counterpart (1) and improves the earlier 4/3 intermediate-rank bound to an attained value. This is a useful sharp finite-dimensional stability invariant even without higher-dimensional generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
