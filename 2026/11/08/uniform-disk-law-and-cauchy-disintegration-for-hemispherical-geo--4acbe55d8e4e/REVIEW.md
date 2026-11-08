# Scientific review: hemispherical geodesic-midpoint law

## Correctness — PASS

The proof uses a one-to-one, almost-everywhere midpoint/separation/tangent parameterization of an ordered spherical endpoint pair. For two unrestricted points on the round sphere, its joint Jacobian is spherical area times uniform tangent angle times \(\sin(2t)\,dt\). The condition that both endpoints lie north of the equator is exactly \(0<w<z^2/[z^2+(1-z^2)\cos^2\phi]\) for \(w=\sin^2t\). Normalizing by the \(1/4\) hemisphere-endpoint event gives the constant density \(1/(2\pi^2)\). Integrating \(w\) and \(\phi\) gives the midpoint surface density \(z/\pi\), which cancels the orthogonal projection Jacobian and gives uniform Euclidean area in the disk. A tangent-variable transformation gives the conditional Cauchy law. Direct spherical-lune counting gives the separation density and moment formulas; pole-density comparison and strict monotonicity of a gamma ratio prove dimension uniqueness.

The executable independent sample checks of 660,000 directly generated hemisphere endpoint pairs and 340,000 factorized samples completed successfully. The finite simulation checks are auxiliary only; the infinite statements rest on the explicit calculations. Probability-zero antipodes, equator and singular reference frames are correctly excluded.

## Originality — PASS on accessible evidence, provisional historical priority

Bárány–Hug–Reitzner–Schneider, *Random points in halfspheres*, arXiv:1505.04672v1 (2015), studies convex hulls/facets/mean width/volume and approximation for independent hemisphere samples, not their pairwise geodesic midpoint pushforward. Gille, *Chord Length Distributions of the Hemisphere* (2005), DOI 10.3844/jmssp.2005.24.28, evaluates straight-line chord distributions of a solid hemisphere sampled by invariant lines, not a midpoint of geodesics whose endpoints are surface-uniform. Both primary PDF texts were inspected: the first by sections and targeted midpoint terminology, the second across all five pages. The paper-level comparison is one of mathematical objects, sampling models and implications, not titles.

Searches for spherical midpoint, orthogonal projection, uniform hemisphere, Lambertian disk, geodesic endpoint-pair laws, and conditional Cauchy angles returned no equivalent complete identity in the checked literature or accessible earlier mathematical records. Previous related studies of hemisphere geodesic containment concern endpoint visibility, not the pushforward midpoint. This is positive *best-knowledge* originality only, not an independence or all-literature guarantee. An older directional-statistics/disintegration identity could dominate the calculation; independent historical verification remains appropriate.

## Mathematical value — PASS

The result determines the full midpoint pushforward and an exact endpoint-pair disintegration for a natural curved sampling space. The Euclidean-area-uniform disk law is an unexpectedly simple geometric transform; the conditional Cauchy/uniform coordinates permit exact reconstruction and sampling of ordered endpoint pairs; the sharp dimension-three rigidity shows this simplicity is not a generic consequence of hemispherical symmetry. These are structural distributional statements rather than just a numerical probability or a special-case normalization check. No claim is made for arbitrary caps or projections.

Self-review: passed. Independent audit: not yet performed.
