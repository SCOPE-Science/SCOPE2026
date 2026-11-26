# Independent mathematical audit

## correctness

PASS

Checked RESULT.md:4–27 and 29–61 on the full stated parameter range. Squaring the positive binomial series gives coefficients d_j>0 with d_0=m², so s^(2−r)K''(s) is a constant term m²r(r−1) plus a strictly increasing positive series. The wet-end leading curvature is 2m^(1−m)(1−m)(1−s)^(m−2); it dominates the derivatives of the square correction and the smooth prefactor. This proves strict convexity for r≥1 and exactly one concave-to-convex inflection for 0<r<1. The triangular integral for 2J is valid at a=h or 1−h: at the dry end T_h K'' is O(s^(r−1)), and at the wet end it is O((1−s)^(m−1)); corresponding boundary terms T_h K' vanish. For a_1<a_2 the ratio of the second translate to the first is strictly increasing on their common positive support by strict log-concavity; the earlier-only and later-only supports are ordered the same way. Whenever both means have both signs of curvature in their integration windows, the windows share an open neighborhood of s_*. The determinant is strictly positive on a product of intervals straddling s_* in that overlap, so the integrated determinant P(a_2)N(a_1)−P(a_1)N(a_2) is strictly positive. Windows lying on a single side have that strict sign. This verifies uniqueness, direction, and the mutual exclusivity of all endpoint tests, even when one test is zero. For small h the endpoint windows lie on opposite sides, ensuring an interior zero; any such zero has a window straddling s_*, giving |a_h−s_*|<h directly, without needing a compactness assumption at the endpoints. Direct scalar evaluation and bisection reproduce the illustrative left/right values −0.0224062230 and 0.2145644773, root 0.3209402594744, and positive left endpoint 0.00250377766 at larger contrast. VERIFICATION.md and checker.py were inspected, not executed; the 9,768 parameter-grid assertions are recorded diagnostics only. This is an exact result for equal-weight constitutive averages, not effective flow.

## originality

PASS

Qualified to the model-specific unique inflection in the nonconvex regime and resulting sharp finite-amplitude endpoint classification. The VGM constitutive relation, global convexity parameter threshold, and general triangular-kernel sign-variation method are credited as antecedents. The strongest unresolved historical risk is that the older constitutive literature contains a stronger all-parameter curvature theorem than was established by this check.

## value

PASS

For a fixed nonlinear hydraulic relation, this test decides the direction of exact two-class averaging bias at any feasible contrast by endpoint evaluations, without scanning mean saturation. Its single-reversal direction, equality cases, and link to the unique curvature change go beyond small-contrast Taylor reasoning; the larger-contrast example shows why the finite contrast is consequential. The value is constitutive and mathematical, not a prediction of effective conductivity or a claim that very negative exponents fit physical soils.

The dated certificate retains the supplied scientific assessment, sources and limitations.
