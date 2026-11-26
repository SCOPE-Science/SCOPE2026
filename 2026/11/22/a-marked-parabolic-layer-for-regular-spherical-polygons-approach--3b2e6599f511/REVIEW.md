# Independent mathematical audit

## correctness

PASS

Use normalized uniform area on the polygon as stated in the scope, so the denominator tends to 2π rather than the whole sphere's 4π. In a folded sector the gnomonic side line is at planar distance tan(R)cos(α); a ray at offset φ meets it at tan(r_max)=tan(R)cos(α)/cos(φ). Its minimum over a sector gives the centered incircle. The spherical inward unit normals to the supporting great circles have equal polar coordinate, with their horizontal directions opposite the side midpoint meridians. For an interior point the smallest signed margin, and hence smallest supporting-circle distance, is to the side of closest midpoint longitude. A shortest segment to a minimizing circle ends in the polygon: the open ball with radius the minimum of the circle distances is contained in every supporting hemisphere. This verifies the use of actual side arcs and the vertex-meridian folds up to area-null ties. Write δ=π/2−ρ=arctan(tan(ε)sec(α)). An independent spherical-excess calculation on 2n right triangles gives polygon area 2π−2n arcsin(sin(α)sin(δ)); subtracting the incircle area gives layer area 2π sin(δ)−2n arcsin(sin(α)sin(δ)). Expanding yields 2n C_α ε+O_n(ε³) before normalization, hence the stated ε coefficient and O_n(ε²) probability remainder. For total variation, the uniform expansions of arctan(tan(ε) cos(φ)/cos(α))/ε and δ/ε give O_n(ε²) boundary shifts; the Jacobian ε cos(εx) has relative error O_n(ε²) on the bounded layer. The limiting band area is exactly 2C_α, so changes in support, density and normalization give the stated L¹ error; rotational symmetry makes the sector index exactly uniform and independent. Vertical and horizontal slices give the displayed first-limit marginals with the proper supports. For the second limit, the transformed lower boundary (cos(αu)−cos α)/(1−cos α) equals 1−u²+O(α²) uniformly; the upper boundary stays 1 and the transformed area is 2/3+O(α²). The second L¹ bound and the density 3/2 follow. Integrating slice lengths gives the quoted two marginals, radial CDF, and mean 7/10. Independent bounded numerical quadrature agreed with spherical excess within 8.6×10^−16 in the tested cases, and direct integrations checked the marked marginal formulas. The numerical check is not a proof of either TV rate.

## originality

PASS

Provisional for the marked spherical conditional total-variation limits and accompanying sharp rarity, not for finite spherical polygon area, classical trigonometry, or a finite radial distribution. The local geometric calculation is elementary, but the compared work does not give the conditional joint law or its successive parabolic normalization under the same measure and geometry.

## value

PASS

The polygon and its canonical incircle approach the same hemisphere, so the last piece of area between them is a natural singular geometric object. The joint law shows where that area actually sits: it avoids the side midpoint and concentrates toward vertices, a distinction inaccessible from the scalar rarity. The second scale gives a quantitative and explicit parabolic law as the sectors shrink. This provides interpretable geometry beyond recomputing the area of a fixed polygon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
