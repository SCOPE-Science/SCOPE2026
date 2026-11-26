# Independent mathematical audit

## correctness

PASS

Independently differentiated the perimeter in polar gap coordinates after fixing the central point and the first ray. For a radius-two chord, the derivative in either endpoint radius is sin(alpha/2), and the angular derivative is 2 cos(alpha/2). Thus each adjacent chord has derivatives (1/2,1/2,sqrt(3)); the closing chord, with angular gap 2pi minus the four adjacent angles, has derivatives (sqrt(3)/2,sqrt(3)/2,1). Eliminating the four angular differentials gives the nine coefficients in RESULT.md lines 17–20. The reduced Cartesian gap Jacobian is block lower triangular when the rows are ordered by the added outer vertices; each two-row block has positive determinant sqrt(3)/2. The stated row order differs by an even permutation, so its determinant is 9/16. Hull membership and the six strict inequalities persist. The smooth inverse chart gives a uniform quadratic residual and a feasible single-rim coordinate ray, which attains the sharp coefficient. Separately, the five cyclic gaps in a five-spoke flower are at least pi/3, sum to 2pi, and are thus at most 2pi/3; their strictly concave chord sum has minima only at the simplex vertices. The convex hull of the equal disks is the center hull plus the unit disk, so the shift in perimeter is 2pi. No unrestricted six-disk global minimum is asserted. Independent bounded replay: python /workspace/branches/replay_frozen.py 2; law-of-cosines reconstruction of 68 vectors including single-rim rays gave maximum scaled Taylor residuals near 0.1925 over four scales. The frozen verify.py checks pointwise algebra, not the 160 perturbations separately reported in the frozen narrative. The diagnostics are not used as proof.

## originality

PASS

Best-knowledge pass for the explicit nine-gap differential and sharp ambient stability coefficient. General finite-packing optimization and constraint calculus are prior context, and the separate concavity result in the five-spoke class is not the main originality basis. No exact or dominating quantitative match was established. Independent inspection of older primary packing sources was limited; that is a real priority risk, not negative coverage evidence.

## value

PASS

A five-spoke contact cluster is a natural explicit candidate in finite hard-disk perimeter minimization. The exact first-order penalty diagnoses which opening directions are weakest, and certifies stability even when the contact graph is not frozen. This is useful as a benchmark for classification or variational methods without presenting a local certificate as a global one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
