# Independent mathematical audit

## correctness

PASS

With c=sqrt(1−s²), compactness and full dimension ensure a unique Löwner ellipsoid; invariance under axial reflection and transverse orthogonal maps forces an origin-centered form xz²+u||y||²≤1. The maxima on the cylindrical and spherical portions reduce to the rim and poles, giving exactly x≤1 and c²x+s²u≤1. Maximizing log x+(d−1)log u sets u=(1−c²x)/s² and gives x=1/(dc²) for c²>1/d and x=1 otherwise, including c=0 where the objective increases directly in x. Below threshold u>x, so equality in x(z²+||y||²)+(u−x)||y||²≤x+(u−x)s²=1 requires both constraints active, exactly the two rim spheres. For the round branch, equality is all spherical points with ||y||≤s, including the larger contact set at the threshold itself. The resulting semiaxis product is the stated normalized volume. Its left logarithmic derivative vanishes at the threshold and its left second logarithmic derivative is −2d²; since F_d=1 there and the right branch is constant, the claimed C¹/not C² and second-derivative jump follow. The double-cap convex-hull identification follows by putting each allowed y between the two cap points at z=±sqrt(1−||y||²).

## originality

FAIL

The theorem is mechanically implied by the exact finite-cylinder solution of Güler–Gürtuna, §8, Theorem 8.1(i)–(ii), via two elementary containment arguments. The finite cylinder is a different body, but its known optimizer supplies a matching lower bound in the nonround regime and, at the critical aspect ratio, for the entire round regime. The contact and volume regularity statements follow directly from the resulting same quadratic form. No historical priority is inferred from catalogue dates.

## value

FAIL

The contact transition is geometrically natural and the formula is useful as a reference. But the exact prior cylinder solution yields the two branches by the elementary containment sandwich, and their equality sets and curvature are routine consequences of the same known form. This frozen claim does not establish a separate unknown invariant or covering result that survives that implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
