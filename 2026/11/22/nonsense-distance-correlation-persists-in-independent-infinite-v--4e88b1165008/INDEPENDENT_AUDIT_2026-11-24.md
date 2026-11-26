# Independent mathematical audit

## correctness

PASS

The replacement RESULT.md removes the original unproved assertion that the limiting distribution actually varies across stable-index pairs. The fixed-index theorem alone establishes a parameterized representation, not nonuniversality. The replacement also specifies weak convergence and the exact conditional permutation convention, and fills in the zero-diagonal step of the strict upper bound. Re-audit: on the product-J1 coupling, boundedness and a.e. convergence give L2 distance-kernel convergence, and replacing index 0 with n affects only one row and column. Nonconstant occupation marginals have positive distance variances. Given the first path, the ordinary occupation covariance is the integral of a continuous nonzero deterministic anti-derivative against the other stable motion; by independence of increments its characteristic function is nondegenerate stable (step sums converge by integration by parts). It therefore vanishes with conditional probability zero, ruling out zero distance covariance. Proportional centered kernels give a separable difference of raw kernels. The a.e. identity extends at simultaneous continuity points, permitting use of the diagonal; the resulting scaled line isometry forces affine dependence, excluded by the joint density of evaluations at two fixed interior times. The trace and off-diagonal sums of the centered matrices yield the exact conditional permutation mean for n>=2; the normalized observed covariance converges to a strictly positive variable and the normalized grand-mean product is tight, proving p_n tends to zero in probability. The frozen CHECK.py was inspected, not replayed; its small-array and seeded samples are diagnostics, not a theorem about stable laws. No cross-index law comparison or finite Monte Carlo calibration is claimed in the corrected files.

## originality

PASS

The exact permutation identity, common-time occupation mechanism and finite-variance Brownian conclusions are prior. The repaired target is the strict, fixed-index stable occupation limit for infinite-variance independent levels, with the resulting inconsistency of the exact permutation calibration. The comparison credits the shared algebra and the stable invariance principle; it does not claim a new proof of that principle or a law comparison across indices.

## value

PASS

The main scientific distinction survives the repair: ordinary level-based distance correlation and exhaustive permutation testing can systematically indicate dependence for independent heavy-tail processes even where fixed-time population distance correlation is not defined under its usual moment condition. The occupation-law argument identifies common time as the source of the positive statistic and gives a usable warning about permutation calibration in the infinite-mean regime. No unsupported claim of index-dependent laws is needed for that conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
