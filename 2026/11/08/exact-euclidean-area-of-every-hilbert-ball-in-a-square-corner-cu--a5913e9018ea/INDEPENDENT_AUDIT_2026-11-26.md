# Independent mathematical audit

## correctness

PASS

The extrema of the four normalized facet functions along a line give the full-logarithm distance. The two opposite-facet bounds in each coordinate give J(w) with width 2t(1-w²)/(1-t²w²). For each cross-facet inequality its affine violation is largest at the corresponding rectangle corner. There, one within-coordinate inequality per coordinate is saturated, not both directions as the source's wording may suggest. Only the higher of the two corner high ratios can violate the opposite coordinate's low-ratio bound. Both center-coordinate lines satisfy every cross-bound strictly, so the two intercepts are on the adjacent half-edges and the cuts have disjoint interiors. Their intercept product divided by two gives T. The positive factor (1+min(a,b))(1−max(a,b)) makes the vanishing criteria exact, hence 4, 6 or 8 vertices. The width bound gives strict optimality away from zero; expanding the rectangle gives quadratic coefficient −4t²(1−t²) and the four cuts give −2t²(1−t²). The only nonsmooth numerator terms are proportional to |a−b|³, which are C², so the Hessian assertion follows. Area scales by the absolute determinant under affine transport, and normalized mass is unchanged. The frozen verifier was inspected but not run. Independent clipping and shoelace in /workspace/branches/460cc471-3f80-4ea2-a8c1-0dcfb8e28df9/area_reproduction.py compared 725 cases (maximum absolute difference 4e−15); this is diagnostic, not the proof. Scope is ordinary Euclidean area, finite r>0 and interior centers under the unhalved convention.

## originality

PASS

The supported distinct result is the all-center ordinary area law with sharp positional optimum and second variation for the square and its affine images. The ratio representation and generic polygonal-ball construction are known. Neither the construction nor the simplex mass result inspected gives the asserted area comparisons and Hessian for a parallelogram.

## value

PASS

Euclidean mass of metric balls is a natural invariant for uniform sampling on a square or parallelogram. An all-center area expression is usable even across degenerating corner cuts, and the exact nonzero Hessian answers how much mass is lost under a small displacement at any fixed positive radius. This is more than the existence of a polygon construction or a check of a symmetric center.

The dated certificate retains the supplied scientific assessment, sources and limitations.
