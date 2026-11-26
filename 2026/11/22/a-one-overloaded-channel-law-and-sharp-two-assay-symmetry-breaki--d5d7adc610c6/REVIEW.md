# Independent mathematical audit

## correctness

PASS

The independent Poisson events yield f=1−a+a^p with a=exp(−μw) and p=1+λ/μ. Differentiating log f gives the stated H, strictly increasing in a with endpoint values −1 and 2(p−1). Thus log f is strictly convex below h and strictly concave above h. The strict derivative inequality g'(w)>g'(0) for w>0 excludes every face of the compact simplex; the common marginal derivative and a two-coordinate second variation exclude two coordinates above h, and strict monotonicity below h forces the remaining coordinates to agree. At W>mh the equal point has a negative second variation. Comparison to small coordinates held at w0 forces s→w0 uniformly across minimizers since the large-coordinate factor tends uniformly to 1. The stationarity equation first gives s−w0=O(exp(−μW)), then division by g''(w0)=λμ exp(−μw0)/f0 gives the claimed coefficient; the small-coordinate factors change only to second order. For two matched-rate channels the feasible sum of the two exponential variables is [2√z,1+z]. The failure product is the stated strictly convex quadratic there; the vertex crosses the lower endpoint at exp(−V/2)=2−√3 and is never above the upper endpoint. This proves equality and uniqueness at the threshold, and precisely two ordered optima above it. The discriminant derivative 2√3 z_c and expansion of the log root ratio give the stated square-root law. A separate arithmetic evaluation at V=5 gave (0.71415220088,4.28584779912) and probabilities 0.26007287055 versus 0.14501692506 for equal loading. RESULT.md lines 9–66 give the all-parameter proof. Packaged check.py is supplemental, was inspected but not executed for this review, and its finite grids are not a global proof. No uniqueness of a general unequal finite-volume branch, or validity outside the stipulated model, is inferred.

## originality

PASS

Provisionally passes for the quantitative fixed-total failure model, not for generic two-level structure of separable objectives. Checked environmental sources motivate the trade-off but do not deliver these optima. Nearby published allocation results have distinct feasible designs or objective functions. The exact global transition, its coefficient and the large-load correction are not consequences of a generic curvature sign change alone.

## value

PASS

The mandatory-use constraint gives a motivated mathematical benchmark: optimal designs can sacrifice one channel while the other loads remain bounded. Knowing the sharp onset and growth of the unequal branch, and the rate at which the optimized probability approaches its large-load limit, is more informative than diagnosing nonconcavity or displaying one counterexample to equal allocation. This is theoretical design evidence only, not an empirically calibrated assay recommendation; allowing discard, dependent channels or nonfatal inhibition can change the conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
