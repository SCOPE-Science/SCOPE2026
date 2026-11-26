# Independent mathematical audit

## correctness

PASS

The maximum of the linear form on the fixed compact box gives exactly the stated feasible domain; strict convexity gives uniqueness. At strict slack, interpolate the base minimizer toward a maximizing box vertex to obtain comparison points feasible for all nearby data, then take subsequential limits and let the interpolation weight vanish. At equality the feasible set is the maximizing face, and any nearby feasible optimizer limit lies in it. For an arbitrary target on that face, assigning epsilon times its free coordinates to the originally zero coefficients and subtracting epsilon times their squared norm divided by a positive coordinate's cap from its coefficient preserves the positive threshold exactly. The target then minimizes the separable Lagrangian with multiplier 1/epsilon: positive base coefficients clip to their caps, negative ones to zero, and the new coefficients give the target's free coordinates. If the maximum is zero, shifting the threshold by epsilon times that squared norm instead gives the same certificate; at a fixed zero threshold the optimizer is always zero. These constructions give all and only the claimed cluster points and attain the jump using all free caps. For the strict-slack example the first coordinate clips to one iff epsilon <= 2/5, the second equals 1/2, and the maximum exceeds the threshold by epsilon/2. The one-dimensional positive-threshold boundary has no zero coefficient.

## originality

PASS

The supported distinct contribution is the exact feasible-domain discontinuity locus, full attainable face, sharp jump and fixed-positive-threshold strengthening for the particular fixed-box projection. Neither the clipped solver nor general loss of constraint regularity is claimed as new. The result qualifies a continuity assertion made for the abstract limiter optimization; it does not establish a discontinuity along any DG trajectory.

## value

PASS

The result corrects a useful continuity heuristic for an existing limiter and quantifies its exact failure under feasible perturbations. The full face and norm-sharp jump give actionable distinctions between strict feasibility, a nondegenerate boundary and a singular boundary. The fixed-threshold two-coordinate witness shows that positive right-hand side and unique minimizers do not prevent jumps, even when the approaching data have strict slack.

The dated certificate retains the supplied scientific assessment, sources and limitations.
