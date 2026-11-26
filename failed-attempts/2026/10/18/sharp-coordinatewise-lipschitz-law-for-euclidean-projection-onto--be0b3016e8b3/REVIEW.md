# Independent mathematical audit

## correctness

PASS

Moreau orthogonality gives the stated three branches. In the middle branch set u=z/||z||₂ and s=t/||z||₂; differentiation gives the symmetric matrix in RESULT.md line 36. Absolute row and column maxima agree, so the two global moduli agree by scalar direction tests and integration. Along a segment ||z||₂²−t² is quadratic; if identically zero the restricted projection is identity or zero according to the sign of t, and otherwise there are only finitely many crossings. The axial row gives T_d=(1+√d)/2. For a=|u_i| the spatial row is [1+a+s(1−a²)+|s|aΣ_{j≠i}|u_j|]/2, maximized in the limit s→1; equal absolute sizes of the other u_j attain the Cauchy–Schwarz bound. The spatial objective has negative second derivative and opposite derivative signs at the endpoints for d≥2. Substitution a=2/3 proves spatial dominance for d=2,3,4. For d=5 the tangent bound gives B_5≤89/40<√5, and √d−a√(1−a²)√(d−1) increases for d≥2; hence the comparison remains strict. In d=1 the nonzero branch row sums are one. Independent bounded bisection confirmed the signs of spatial-minus-axial maxima for d=2,3,4,5 (+0.15407,+0.09701,+0.04162,−0.00998). The frozen script was inspected, not run.

## originality

FAIL

A distinct indexed result contains the same sharp maximum-norm formula, unique scalar maximizer, and strict dimension-five switch. The only material-looking addition, equality of the sharp ℓ₁ constant, follows immediately from symmetry of the already-displayed Jacobians and the same integration and derivative-witness argument. The indexed path date is later; this determines no historical priority or dependence.

## value

PASS

The underlying exact switch in the norm of a standard projector answers a natural coordinatewise stability question and is not a generic consequence of Euclidean nonexpansivity. The extra ℓ₁ statement does not independently distinguish this record, as assessed under originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
