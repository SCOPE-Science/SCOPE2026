# Independent mathematical audit

## correctness

PASS

For the corrected files in /workspace/repairs/3. The frozen Step 3 assumes an exact 2r slice-width upper bound for oblique projected bands (false for a sloping band), gives no uniform control at or just outside planar support, and gives no argument that excludes multiple passages from one branch at the inclinations used in its tail estimate. The blanket component-count sentence in its scope is not needed and is omitted. The corrected signed-distance proof resolves these issues: along a line the material criterion is g(q)=f(q)^2+(h+m q)^2<=r^2. For m>=A sqrt(r), any two hits bound an interval of length <=2r/m; bounded signed-distance Hessian gives |f|<=r+O((r/m)^2) throughout and g''>0, excluding multiple passages. At offsets within O(r) of either support, hit q varies within O(sqrt(r)) of the support point; the multiple-hit inclination cutoff gives allowed orthogonal offset width O(r) and measure O(r^(5/2)), including exterior offsets. At support distance delta>D r, the two planar band intervals are separated by at least c sqrt(delta), |f'|>=c' sqrt(delta) on both, and g is strictly convex within each. Thus multiple hits have exactly two components outside the strips and require mu<=C r/sqrt(delta) and s-width O(r). These yield boundary loss O(sqrt(eta)+sqrt(r)) and inclination tail O(1/M)+O(sqrt(r)) after scaling by r^-2. On compact interior subsets the offset overlap is trapped between intersections of corresponding intervals with half-widths alpha r and alpha r+O(r^2); the centers are exactly rv ell apart. This proves the marked limit and its mass J(K), including negligible higher multiplicity. For all hits the projected convex-curve tube area divided by r is dominated uniformly by the planar parallel-area bound; averaging projected tangent lengths gives pi L/2. The ellipse law follows by completing the quadratic and integrating a beta density. The frozen script was read, not run; it samples radii 0.2 and 0.5 and does not reproduce the stated 0.05 numerical benchmark, so that extraneous benchmark was not carried into the repair.

## originality

PASS

Classical invariant projection formulas and a qualitative four-crossing observation are prior, as are circular central-line and torus-shadow results. No inspected prior passage established the general arbitrary-oval offset-dependent thin-limit coefficient or marked law for invariant affine lines, which are unchanged by the proof repair.

## value

PASS

The repaired theorem quantifies a natural rare multiplicity event and identifies a geometrically nontrivial reciprocal-chord weighting, not a usual mean chord law. The joint law retains enough directional information to identify an ellipse's aspect ratio and axes, and the boundary estimates distinguish exactly two components from merely two candidate encounters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
