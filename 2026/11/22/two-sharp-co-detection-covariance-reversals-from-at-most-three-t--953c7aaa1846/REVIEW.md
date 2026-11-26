# Independent mathematical audit

## correctness

PASS

Replace both detections by complementary empty-box indicators, preserving covariance. Conditional on N=n, a specified box is empty with probability (1−t)^n and both are empty with probability (1−2t)^n. Hence C(t)=G(1−2t)−G(1−t)^2. Expanding G(1−t)=1−μt+vt²/2−wt³/6 gives the stated C(t)=t²F(t). For the entire allowed interval, F″≤−v(v−w)/2−2μw/3−w²t²/3, with v≥w≥0. If N can equal 2 or 3, this is strictly negative: for w=0 use v>0, and for w>0 use μ>0. Three distinct zeros would contradict strict concavity between the first and third. Two strictly interior zeros force negativity at both endpoints by the same strict chord inequality extended from either end and positivity between; those three signs conversely give two reversals. With N≤2 and b=P(N=1), c=P(N=2), F=2c−(b+2c−ct)² increases strictly when c>0; when c=0 it is constant −b², including the zero law. Independently expanding the two witness PGFs in integer coefficients gave 1024F=−57+680t−1558t²+504t³−81t⁴ and 100F=−44+120t−25t². Exact rational evaluation reproduced the five displayed three-copy signs (including zero at 1/9), and the two-copy root 2/5. No endpoint root is counted as a strict interior reversal. Read VERIFICATION.md and check.py as frozen evidence; the source program was not executed. The finite source tests do not substitute for the curvature bound.

## originality

PASS

The balls-in-bins routing model and the empty-box PGF identity are not new. What survives comparison is the sharp volume-driven sign-reversal bound for an arbitrary fixed law on {0,1,2,3}, its lower-support refinements and witnesses. The strongest same-model occupancy treatment supplies the fixed-n laws, not the sign classification after arbitrary count mixing; the closest indexed sign-window results change a different parameter or use different events. Priority remains best-of-knowledge.

## value

PASS

Under the simple finite-disjoint-stock detection model, the theorem identifies precisely how many items are needed for a reentrant covariance sign pattern. It proves a distribution-uniform cap and supplies realizable interior witnesses, showing that a positive window alone need not indicate a common measurement fault. This is more than computing a PGF or restating conditioned negative association. It is a population probability result, not a validation of an assay, an estimator, or a field detection claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
