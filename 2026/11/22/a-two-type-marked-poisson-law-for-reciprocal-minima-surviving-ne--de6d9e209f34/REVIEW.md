# Independent mathematical audit

## correctness

PASS

Reconstructed the simultaneous-event formula, not merely the mean limits. The atomless quantile transform preserves orders almost surely, even for a continuous CDF with gaps. One fresh competitor contributes (1-x)(1-y) and a retained one contributes 1-max(x,y), giving h=(1-max)(1-epsilon min). Integrating over a retained focal diagonal or the two replaced focal triangles gives the stated exact means with m=2n-2, including the full-retention and full-refresh endpoints. For r designated cells in distinct rows and columns there are 2(n-r) external competitors per cell and precisely two cross cells per focal pair, tested against the coordinatewise maxima. All other placements contribute zero. After rescaling, the rescaled retained mark density multiplied by n^2 is n(1-epsilon_n), tending to c, including c=0 where an asymptotic ratio should not be used. The analogous replaced density tends to 1. The external factors tend to exp(-4s) or exp(-2(s+t)), and all finitely many cross factors tend to 1. The exponential bound from 1-h >= (x+y)/2 dominates fixed-order integrals; Riemann sums exclude only an O_r(1/n) proportion of placements. For counts in disjoint continuity boxes and both types, tightness follows from first moments, all subsequential mixed moments pass by higher-moment uniform integrability, and the product Poisson law is moment determinate. First-moment mark tail bounds prevent escape and give total counts and the zero-count limit. Replay: RESULT.md lines 39–90; inspected VERIFICATION.md and verify.py (finite checks, not executed or used as an infinite proof).

## originality

PASS

The supported distinct claim is the finite-c retained/replaced, spatial and quantile-marked overlap law with exact finite means. One-array extrema laws, single-row perturbations, and independent geometric matching overlaps do not supply the two-copy shared-competitor calculation or the retained mark intensity. No equivalent or dominating result was found in the examined evidence; this is not a priority guarantee.

## value

PASS

Determines how the two mechanisms—retention of an unusually small observation and fresh rediscovery of the same minimum—coexist at the natural order-one overlap scale. Their calibrated rates and distinct value profiles quantify what a single total count would hide, in a basic iid coupled-matrix model. No claim of quantitative convergence or extension to geometric or dependent costs is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
