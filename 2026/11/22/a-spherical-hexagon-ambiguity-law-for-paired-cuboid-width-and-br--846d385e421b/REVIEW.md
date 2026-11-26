# Independent mathematical audit

## correctness

PASS

Width and projection area have coefficient rows v and w on the positive octant. Haar folding gives surface density 2/pi there, and the map on the row plane has area factor sqrt(det(LL^T))=N. Each lift from the disk to the sphere has Jacobian 1/sqrt(1-s); retain the positive lifts, giving twice the single-sheet factor near any positive point of the fold. The topological support is the image of the closed octant, with the formula specifying its density off null boundaries. The cross-product components and the positive difference (b^2-a^2)(c^2-b^2)(a^2+c^2) give q^2>1/2. To independently check the crucial hexagon, write d=2q^2-1>0. The two fixed vertices on the coordinate faces u1=0 and u3=0 have rays (0,r,q) and (q,p,0). On u1=0 and (Ru)2=0 there is the ray (0,2qr,d); its other constraints are strict, since (Ru)1=2pr and (Ru)3>0. On u3=0 and (Ru)2=0 use (d,2pq,0); reflection gives the other two vertices. No axis is feasible, and the three other mixed facet intersections have no nonzero nonnegative ray. The inward-normal dot products give the six stated exterior angles, so Girard's area formula divided by pi/2 gives the ambiguity probability. A positive fixed point gives positive mass, and directions near the middle axis are excluded because R22<0. Geometric progression sides have p=r tending to zero; adjacent-pair coalescence with the third distinct makes R a coordinate swap in the limit. The extrema are thus sharp limits only. The supplied numerical checker triangulates the spherical polygon and samples directions for six boxes; it was inspected, not executed, and is not the all-shape proof.

## originality

PASS

The distinct result is the explicit two-lift multiplicity and its all-triaxial-box arcsine probability, including the sharp shape dependence. General projection and area-formula methods, box width marginals, and recovering box edges from distributional moments are not new. The closest indexed comparison asks the same paired inverse problem for a triaxial ellipsoid, but is affine in squared direction coordinates and yields uniqueness, not octant reflection ambiguity. The original plausible full-text gap around Abas's broad paper has been narrowed by inspecting its decisive density and reconstruction statements. No equivalent or covering theorem for this triaxial cuboid geometry was established by these comparisons.

## value

PASS

Width and projected area are natural paired measurements. Their separate distributions cannot tell how often a single measured pair is insufficient even with noiseless data and known geometry. The explicit mass solves that inverse identifiability question for every triaxial box, and the sharp limits show that no uniform ambiguity guarantee follows merely from all edges being distinct. This exact invariant is useful independently of general coarea or simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
