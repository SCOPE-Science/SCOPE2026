# Independent mathematical audit

## correctness

PASS

The polar of the orthogonal free sum is the product of the polygon polars, with vertices given by pairs of outward edge normals divided by their polygon inradii. Every product edge changes exactly one factor; there are mn edges of each type, dual to distinct primal ridges even if the angle values coincide. With u=pi/m, v=pi/n, U=(a cos u)^(-2), V=(b cos v)^(-2), the primal exterior-angle cosines are 1-2t sin²u and 1-2(1-t) sin²v for t=U/(U+V). The interior angle pi-arccos(C) increases in C. The larger cosine is minimized at the unique interior crossing, t=sin²v/(sin²u+sin²v), giving the displayed minimax and a/b=tan u/tan v. The allowed t are exactly (0,1); uniqueness is up to overall scale. Unit radii balance the angles precisely when m=n. The inspected code checks normal dot products on five order pairs and three radii ratios, not the universal statement or independent recognition of facets; it was not executed. The argument and theorem are restricted to centered regular polygons in orthogonal planes.

## originality

PASS

The strongest inspected same-geometry results concern inscribed volume or vertex normal-cone probabilities. The strongest minimax analogues concern other feasible families. The product-angle literature concerns a different face dimension after duality. The bounded comparison supports the distinct radius minimax and its sharp equality classification, not novelty of polarity or of the volume-extremizer geometry.

## value

PASS

This exactly resolves angular balancing in the natural orthogonal regular-polygon family that occurs in sharp inscribed-volume problems. Both the unique scale and optimal maximum are useful: they distinguish the two known volume-extremizing examples and show concretely when the equal-radius volume geometry can fail the angle objective. The contribution is the complete restricted optimum and ridge census, not the standard product-polar identity or a claimed global four-polytope optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
