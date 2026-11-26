# Independent mathematical audit

## correctness

PASS

The trace map is finite by the three monic quadratic equations, and its irreducible image has four distinct generic traces over (x2,x3). Indeed the four products of the inverse-coordinate choices are generically distinct and cannot pair by inversion of the derived first torus coordinate identically unless λ²=1. This proves birationality and identifies the monic quartic resultant as the equation; its top term is 4x1²x2²x3². The equality of traces changes only coordinate inversion signs: one inversion cannot change a preimage nontrivially with product fixed, all three require λ²=1, and a pair is inverted exactly at product ±1. The derivative drops rank only when two of the three torus coordinates are ±1. Finite local embedding off these loci proves smoothness. At a point on one line except its pinches, there are two immersive lifts with normals differing by two signs and with nonzero unchanged third component, so the two local images are transverse. Pairwise line intersections give exactly the four stated points; there λ⁴≠1 excludes the all-minus exponent branch, leaving exactly three lifts whose normal matrix has determinant 4 after scaling. At a rank-drop point the third trace is an analytic coordinate in the sum of the two logarithmic source coordinates. With V=2sinh(v/2) in their difference coordinate, the normalized sum gives V², and the normalized difference divided by the analytic unit √(1+V²/4) gives UV. This proves the Whitney form at all twelve points. Each double stratum is a line minus four points; the normalization-fiber excess contributes 6(−3)+4(2)=−10, so χc=10. Replay python3 /workspace/branches/frozen_exact_checks.py 1 checks the direct resultant, total degree, all six symbolic Jacobian restrictions and triple normal determinant; exhaustiveness and analytic types use the proof, not sampling.

## originality

PASS

The underlying triangle family, generic degree and resultant method are inherited. A broader same-day catalogue theorem covers the normalization and generic six ordinary double curves at weights (1,1,1); those parts are not distinct. The explicit complete exceptional-point census for every c≠0,±1, local analytic types and resulting Euler characteristic are not covered by the strongest inspected statements. The analogous c=0 theorem has a different fiber at its line intersection and does not settle this deformation.

## value

PASS

The affine local stratification of a minimal graphical Lissajous hypersurface distinguishes the multiple fibers from ramification of its normalization and separates the generic-phase four triple crossings from the special fourfold point. Knowing which exceptions occur on each line, and their exact normal forms, makes the Euler correction and a comparison across phases possible. It is more than an equation or a generic component count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
