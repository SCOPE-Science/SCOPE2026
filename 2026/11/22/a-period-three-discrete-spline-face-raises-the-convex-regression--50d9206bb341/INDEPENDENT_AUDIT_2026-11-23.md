# Independent mathematical audit

## correctness

PASS

The curvature-active set is exactly the kernel of within-cell second differences. Interpolating k² at the knots makes the other second differences strictly positive; independent active rows and positive multipliers give an open projected region with local derivative P_m. The Gram matrix scaled by 9 has endpoint/interior diagonals 14/19 and off-diagonals 4. After normalizing by its diagonal, the largest absolute off-diagonal row sum is 8/19; finite Neumann powers of degree less than |i−j| cannot contribute to the (i,j) entry. This proves a uniform exponential bound. For a centered row, every coefficientwise subsequential limit solves the infinite tridiagonal equation with the source at the origin, and the bounded solution is unique by strict diagonal dominance on ℓ∞. Its coefficients are g_h=9r^{|h|}/(3√33), where 4r²+19r+4=0 and −1/2<r<0. The uniform bound applies also to the interpolated row, so dominated convergence justifies passing to the absolute sum. Each three-site block directed away from a knot h on one side contributes |g_h|, since the two interior weights have its sign and the next knot has the opposite sign. This gives (9+2√33)/11. On the whole infinite grid, shifts by three sites preserve the spline space, all knot rows have this same mass, and interpolating output rows cannot increase it; the sign input attains it in ℓ∞. The statement concerns shift invariance by a whole cell, not by one sample. The full convex cone projection is continuous piecewise affine, so its global coordinatewise constant is the maximum derivative norm on its full-dimensional regions. The second-difference map is onto: any active pattern with all other curvatures positive is realizable, and giving strictly positive active multipliers yields an open region. Appending a site with inactive final curvature extends each derivative by direct sum with the identity, proving L_{n+1}≥L_n. The result is an exact norm of the infinite face projector and only a lower bound for the full convex-regression sensitivity.

## originality

PASS

The closest exact convex-sequence result gives a weaker alternating-face lower bound and does not optimize this period-three face. Known continuous-spline bounds and constrained convex spline stability theory do not determine the exact discrete coefficient or the improved lower bound. This is a bounded comparison, not a claim of historical uniqueness or of a new general stability theory.

## value

PASS

The explicit realizable face produces an algebraic discrete spline benchmark and a substantially stronger constraint on any proposed global sup-norm bound. It connects the actual local derivative of convex regression to a sharp row-sign mechanism; it is neither merely an unmotivated sample-size example nor a claim that the unrestricted sharp asymptotic value has been determined.

The dated certificate retains the supplied scientific assessment, sources and limitations.
