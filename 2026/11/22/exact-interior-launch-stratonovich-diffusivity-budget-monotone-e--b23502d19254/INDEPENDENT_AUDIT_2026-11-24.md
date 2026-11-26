# Independent mathematical audit

## correctness

PASS

For reflected Brownian motion in the intrinsic coordinate with generator ∂², the normalized time is S1 S2+S2²/2. It strictly increases in S1 and S2, so strict Jensen at each fixed interval mean proves the global reduction and the equality condition. The reduced derivative is ab(bt³−at−b)/t³; the cubic decreases once then increases from negative values to infinity and its sole positive root is above 1. Substitution gives a=(t³−1)/(t³+t−1). In the corrected proof the residual ratio R satisfies R′<0 by the displayed factorization (the quartic factor is positive) while a′>0. The added exact identity for 1−R factors its numerator as (t−1)³(2t⁴+2t³+3t²+t+1), so 1−R~9(t−1)³ and a~3(t−1). At infinity, R~2/t and b~t^−2. Smooth approximations preserve the infimum by budget normalization and convergence of intrinsic lengths, with no attained smooth optimizer. A separate bounded symbolic script verified the central rational and limit identities: /workspace/branches/d4c6303d-b329-4f1a-81f0-ed6ee89007a1/record3_independent_check.py. The supplied check.py was inspected, not executed; the proof, not profile sampling, establishes the gain theorem.

## originality

PASS

For the corrected claim, the exact sign of the Stratonovich gain over all launch fractions and the leading onset and target constants are distinct from the inspected primary stationarity theorem and numerical gain plot. The same-method optimizer and its straightforward allocation corollary are excluded from the claimed contribution.

## value

PASS

Strict monotonicity settles whether the relative gain monotonically grows rather than merely improving absolutely. The cubic onset and square-root relative deficit show that the design helps on very different scales at the two ends, information neither a stationary profile nor a sampled plot provides.

The dated certificate retains the supplied scientific assessment, sources and limitations.
