# Independent mathematical audit

## correctness

PASS

Corner maximization replaces each half-side h_i by h_i+|t_i| for center t; centering preserves feasibility and volume. For positive squared half-sides the log-product is strictly concave. The three-equality solution has W≥U≥V>0 for β≤γ<α+β, so the first two multipliers are positive. The third is (1/U+1/W−1/V)/2, equals 1/(2W)>0 at γ=β, and decreases strictly to negative infinity. Its unique zero satisfies 1/V=1/(α−V)+1/(β−V), which has one solution in (0,α) since the left side decreases strictly and the right side increases strictly from finite values to infinity. It is the smaller quadratic root v*. The proof’s other root is at or above α (equal when α=β), not strictly above in the equality case; it is still excluded. The two-first-equalities candidate has supporting multipliers (1/U,1/W,0) and is feasible exactly when γ≥α+β−2v*. In both branches the supporting-plane inequality and strict concavity give the unique triple, and the two saturated cylinder inequalities force all center offsets to vanish. The maximum of x²+z² over the first two cylinders is α+β at y=0, and scaling that maximizing point gives witnesses between any two third squared radii below redundancy. Thus contact ends strictly earlier, not merely at a redundant constraint. For log-volume f, f′ equals half the third multiplier below the threshold and zero above; f″ from the left is −(U⁻²+V⁻²+W⁻²)/8 and is zero from the right, so the second derivative at the threshold does not exist. A separate rational replay at α=β=1 and γ=6/5,4/3,3/2 recovered the active multipliers, the plateau volume 16/(3√3), and the left curvature −27/16. At γ=3/2, x²=z²=7/8 and y=0 witnesses nonredundancy. These are bounded checks, not the global proof; the uploaded script was read, not executed.

## originality

PASS

The supported distinct claim is the explicit two-phase law for the unique translated axis-parallel box, its contact threshold strictly before redundancy, and the resulting sharp sensitivity law, not the tricylinder itself, its volume, or the general optimization method. No available compared statement covers that classification; exact priority remains bounded by the inspection limits below.

## value

PASS

For a natural three-parameter convex family this distinguishes optimization contact from geometric redundancy and identifies a nonempty range over which the solid strictly changes while its unique packed box stays fixed. The exact support switch and loss of second differentiability describe a sensitivity effect that neither the solid’s volume nor generic algorithms quantify.

The dated certificate retains the supplied scientific assessment, sources and limitations.
