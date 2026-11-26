# Independent mathematical audit

## correctness

PASS

Integration of the bridge kernel gives the integral-point covariance t(1−t)/2 and integral variance 1/12. Updating on the low site after the high site gives residual covariance (b−k)/2 and residual variance b−k²/((1+d)a); the latter is positive in the interior since k²≤ab and d>0. The formula extends correctly when y is an endpoint: the low correction is bounded by (1+1/d)b/4. When x tends to an endpoint and y stays interior, k=O(a), so the correction tends to b/4, the correct low-only result. On the diagonal it is zero, and the separated quarter-point design gives the exact positive gap stated. Uniformly on the square the low correction differs from g/4 by at most 1/(16d). This first forces every maximizing x to the midpoint and then forces every limit of y to be a maximizing y of g at the midpoint. The two distinct maximizers on that slice are obtained from the sign of the derivative on the two reflection halves; at them g_yy=−10+4√5<0. On two disjoint small interior rectangles away from x=y, the smooth remainder is O(1/d) through second derivatives. The Hessian has a negative yy entry bounded away from zero, xx=−d/2+O(1), and bounded xy; it is negative definite for sufficiently large d. Hence each rectangle contains at most one optimizer, and compactness and reflection give exactly two in total. The x gradient gives x−1/2=O(1/d); the nonzero y curvature then gives y−y₀=O(1/d). Inserting these estimates in the x gradient gives the specified high-site coefficient with O(d⁻²) error. The leading quadratic loss from x costs O(d⁻¹) in value, so the limiting correction is g(1/2,y₀)/4. Independent symbolic checks of finite separation and the golden constants: python3 /workspace/replay/checks.py 2. No finite check certifies uniqueness or an explicit d₀.

## originality

PASS

Standard Gaussian conditioning and additive-discrepancy covariance modeling are not novel. The supported difference is the exact strict non-collocation for the labeled budget at every d>0 and the eventual reflected optimizer pair with golden-ratio locations and quantified gain. The closest distinct indexed Brownian-bridge theorem has another observation model and asymptotically vanishing separation. The closest primary multifidelity comparisons are limited by full-text access.

## value

PASS

In a minimal exact two-fidelity integration problem, zero residual low-fidelity information at co-location leads to strict suboptimality at every nonzero discrepancy ratio, with a surviving strictly positive absolute gain even as the discrepancy dominates. The exact location asymmetry and the optimizer count quantify a natural design phenomenon beyond a Gaussian conditioning exercise. This does not claim a result for other kernels, costs, or budgets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
