# Independent mathematical audit

## correctness

PASS

The maximum of the two factor supports gives the join support. At fixed planar directions let a be the square support and m≤M the polygon's opposite support values. With t=a‖u_E‖/‖u_F‖, the width is a[max(t,m)+max(t,M)]/√(a²+t²). It decreases up to m, increases past M, and the derivative sign in between is that of a²−tM, so its minimum is at m or M. Both endpoint values strictly increase with a, which excludes off-edge square directions; pure-component normals cannot be minimizing. For even q, m=M is minimized exactly at outward edge normals. For odd q use δ=π/q and 0≤θ≤δ/2 from a vertex radius after reflection/reversal: m=cos(δ−θ), M=cos θ. With a²=1/2, mM≥cos δ≥a², so the endpoint at m has derivative strictly negative for θ>0 (the sign is that of m′(a²−mM)+M′(a²+m²)); the endpoint at M also strictly decreases. Even in the triangle boundary case both minimize only at θ=δ/2. Then a‖u_E‖=γ_q‖u_F‖ uniquely; both components are nonzero and the oriented counts 4q and 8q halve to the stated line counts. The minimum of the single support instead balances at cos(π/q); symmetry averaging of admissible centers makes the origin optimal for the unrestricted inradius. Expanding 2z/√(1+2z²) at z=1 verifies the asymptotic coefficients and the odd gap. Independent evaluation on actual vertices gives widths 1.095445115010, 1, 1.134904029214, and 1.095445115010 at the predicted directions for q=3,4,5,6. The q=5 radical agrees. The recorded checker was inspected, not executed; its sampling cannot prove the continuum or equality assertions.

## originality

PASS

The even-width identity and single-support inradius are standard consequences of symmetry and free-sum support; credit those as background. The supported distinct contribution is the sharp odd minimum-width classification, including every equality line and the separation from twice the inradius, in the parity comparison. Neither the motivating volume theorem nor the closest directional comparators supplies the necessary two-sided optimization on the accessible evidence.

## value

PASS

This is an exact Euclidean invariant of a natural one-parameter family including the distinguished inscribed nine-vertex maximizer. Odd parity changes the extremizing construction, doubles the line count relative to the even pattern, and separates width from diameter of the insphere. The full equality set and sharp asymptotic gap are more informative than a numeric width for one example or the symmetric inradius identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
