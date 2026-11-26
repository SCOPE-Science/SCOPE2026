# Independent mathematical audit

## correctness

PASS

The three target inequalities on each image vertex suffice by convexity. Translating the two lower coordinate bounds to zero leaves a triangle scaled by 1−W, or an empty fiber. The W sublevel areas are r² times the footprint area, so integrating the fiber area (ab/2)(1−W)² gives ab/12 times the footprint area in ordinary Lebesgue coordinates. The gauge is coercive: a placement bounds the distance between the first two image vertices by the target diameter, so its unit sublevel is bounded, and continuity gives interior about zero. With a=t≤1=b, I checked the edge inequalities for the scaled polar normals via the exact minimum of each degree-at-most-two polynomial on [0,1], and checked eight strictly positive consecutive turns for 0<t<1. There are 25 distinct normals from the 27 indexed triples; 200 distinct edge tests therefore suffice. The supporting-line intersections and shoelace sum give the claimed area f(t) and five distinct limiting vertices of a genuine pentagon at t=1. Scaling gives V=t f(t)/12 in the normalized case and the stated formula in m,M; the increasing f(t)/t proves the unique fixed-area maximizer. At fixed b=1 the right branch minus the analytic extension of the left branch is a(a−1)^3(3a²−a+3)/[48(a+1)(a²+1)], so the first two derivatives match and the third jumps by 5/32. Zero-scale maps have measure zero; no reflected placements or Haar weighting are included.

## originality

PASS

The feasible four-polytope and its projection are known general objects, and the triangle self-containment gauge integral and equal-leg instance are known. The distinct claim is the exact fixed-source, all-right-target volume and multiplier polygon, the resulting fixed-area maximizer and the cubic derivative jump. The strongest inspected prior formulas and algorithms concern either different target/source families or a different invariant of the same polytope.

## value

PASS

Knowing the largest similarity does not quantify the size of the feasible set. The exact ordinary volume over a full one-parameter shape family yields a normalized measure of containment and a sharp area-constrained shape comparison. The loss of footprint vertices exactly at equality and a cubic, rather than first-order, smoothness break give a concrete geometric benchmark for parametric polytope volume calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
