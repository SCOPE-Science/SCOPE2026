# Independent mathematical audit

## correctness

PASS

PASS: For every stated (r,t) the disk and point fit in a common open hemisphere, making the minimal geodesic convex hull well-defined. Spherical right-triangle sine/cosine laws yield tangent angles u=acos(tan(r) cos(t)/sin(t)) and v=asin(sin(r)/sin(t)); the two triangle spherical excesses minus the facing spherical disk sector give added area Delta=2u cos r+2v-pi. Differentiation yields Delta′=2 sin r(cos r-cos t)/(sin t sqrt(sin^2 t-sin^2 r))>0, checked independently at multiple interior parameters with 1e-15 agreement. Expanding the positive denominator near t=r and t=pi-r and integrating gives Delta(r+h)=(2/3)sqrt(2tan r)h^(3/2)+O(h^(5/2)) and terminal deficit=4sqrt(2cot r)h^(1/2)+O(h^(3/2)); monotone inversion gives h~tan(r)*deficit^2/32. Sampled gnomonic spherical hulls in checker.py are corroboration, not a proof of the continuous hull.

## originality

PASS

PASS with access caveat: Assouline–Besau–Werner 2026 Section 5.2 Example 2 already proves concentricity, critical area and the radius defined implicitly by a geodesic hull volume; those are explicitly credited. Its full accessible Section 5.2 does not display the two-angle 2D spherical area evaluation or the two sharp endpoint coefficients. General Assouline–Schütt–Werner arXiv:2606.21112 treats Riemannian small-illumination asymptotics per available abstract, but full text could not be obtained from arXiv/OA and authorized Oxford retrieval returned vpn_disconnected; this is a real priority risk, not automatic fail. Euclidean R-ball illumination is a different convexity operation and geometry. The new scoped claim is explicit finite-level sphere geometry and its terminal square-root cusp, not prior qualitative radial symmetry.

## value

PASS

PASS: The complete radius-versus-illumination area profile for the canonical spherical disk is a natural geometric invariant of an established illumination-body construction. The sharp mismatch between onset delta^(2/3) and quadratic terminal inverse law with curvature-dependent coefficient describes an analytically meaningful regime not captured by a local small-area theorem. It is not an arbitrary isolated parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
