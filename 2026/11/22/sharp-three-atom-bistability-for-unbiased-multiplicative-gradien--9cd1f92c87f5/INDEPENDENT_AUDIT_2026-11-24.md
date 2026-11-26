# Independent mathematical audit

## correctness

PASS

At the first clipping knot the value is μ times the knot, and at the last it is cS. With at most two nonzero magnitudes positivity follows by interpolation; an atom at zero contributes nothing. With three distinct magnitudes a zero requires a nonpositive middle value. If the largest multiplier is negative, μ>0 makes the middle value strictly positive; if the smallest is negative, S>0 does the same. The remaining negative case has signs (+,−,+); the middle value c(p1−p2+p3a3/a2) gives the strict and touching cases, and solving on the two adjacent affine pieces gives the stated roots and stability by the drift sign. In the sample, scaling x by c gives successive positive-half slopes 7/5, −1, 1/5 and 0, with the claimed zeros. The complete clipped mean is globally 7/5-Lipschitz, so the mean update with η≤5/7 is nondecreasing, preserves intervals bounded by fixed points, and the signs give monotone convergence to the stated endpoints. For the sample recursion stopped at distance c/2 from c, the conditional drift is −η_n(X_n−c)/5 and the square increment budget is c²η_n²; the square and deterministic tail budget form a nonnegative supermartingale. Exit probability is at most 4 sum η_n²=π²/24 and the finite accumulated negative drift forces convergence on nonexit since sum η_n diverges. In the unclipped recursion E[A²]=65/2 and eventual squared-error contraction is at most 1−(7/5)η_n, yielding zero expectation limit and hence an almost-sure zero limit by supermartingale convergence. The frozen verifier is supplemental rational testing, not a stochastic proof; it was inspected, not executed.

## originality

PASS

Credit prior clipping bias and divergence examples. The distinct conjunction supported here is the minimal nonzero support classification with inward mean descent at both ends, and a concrete bounded wrong-limit event for diminishing steps with an almost-sure unclipped contrast. The available comparisons support this distinction provisionally, not publication priority.

## value

PASS

Sharp support minimality under positive curvature and positive signed mass separates transient clipping bias or far-field divergence from a genuine competing bounded attraction basin. The explicit same-oracle clipped/unclipped comparison makes the failure relevant even for a strongly convex true objective and decreasing steps. The signed sample curvature and specified oracle/steps are essential scope restrictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
