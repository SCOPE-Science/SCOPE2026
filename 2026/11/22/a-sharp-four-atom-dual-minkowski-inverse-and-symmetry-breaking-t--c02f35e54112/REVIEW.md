# Independent mathematical audit

## correctness

PASS

In the normalization (q/2)∫cone |x|^(q−2)dx, the facet parameterization (as,bst) has jacobian ab·s; integration of s^(q−1) cancels q, and evenness in t gives the stated single-atom mass. At r=a/b these are rb^q I_x and rb^q I_y. The two averaged logarithmic derivative terms lie strictly on opposite sides of r²/(1+r²), so the derivative of log R_q has sign q−2. Coordinate exchange gives reciprocity. For q>1 divide by r^(q−2); the rescaled denominator integrand (t²+r^(−2))^((q−2)/2) is dominated by t^(q−2) for 1<q<2 and by a constant for q≥2. The latter corrects the stated dominator at RESULT.md l. 64 for q>2 without changing the limit 1/(q−1). For 0<q<1 use u=rt and finiteness of c_q to get R_q∼r^(q−1)/c_q; q=1 follows from asinh. This proves the open ranges, the unique scale given B for q≠2, the q=2 fiber ab=A, and the q=4 calculation. For an origin-interior body, the boundary pushforward density h_K(ν)|x|^(q−2)/2 is strictly positive and bounded above and below, so support is the ordinary area-measure support; finite four-normal support forces an axis rectangle. Differentiating the opposite-face mass at fixed span gives the integral with numerator (q−1)s²+y², strictly positive including q=1. Equality forces centering separately on both axes. Below q=1 the mass on a side at distance s against span [−1,1] is positive and goes to zero at both ends (s^q c_q near zero, s^(q−1) at infinity), so two unequal distances realize one level. Reflection balances the remaining two sides, and the centered inverse supplies a distinct second body. The proof is for the interior-origin convention, which should be stated explicitly in the Finding. Even for a boundary-origin extension via the cone formula, q≥1 admits no extra bodies: the only silent sides have supporting line through the origin, at most two, so such a body is its coordinate bounding box intersected with its tangent cone. A boundary supporting halfplane can be written y+kx≥0 with k>0 after coordinate reflections (an axial one forbids positive mass on one of the four sides). Seeing both negative sides forces b_+>k a_- and a_+>b_-/k and makes the cone contain the positive quadrant. Hence each positive side contains its entire nonnegative-coordinate span whereas the corresponding negative side covers a strictly shorter positive interval. The same pointwise side-mass monotonicity forces a_+<a_- and b_+<b_-, contradicting the two strict visibility inequalities. Inspected verify.py and VERIFICATION.md, not executed; their numerical quadratures are not certified error bounds and do not replace the all-parameter proof.

## originality

PASS

The defensible distinct contribution is the all-q strict inverse/fiber analysis together with sharp origin-symmetry rigidity and breaking for arbitrary realizers in this four-normal family. Centered existence alone at positive q is not a novelty basis: even the supercritical interval follows from Henk–Pollehn's strict bound and their own rectangle degenerations, as detailed below. The q=4 specialization is also overlapping; no priority claim is made for it. These overlaps do not determine the global fibers in the full parameter family.

## value

PASS

Four orthogonal facet normals are a natural minimal setting for testing how far symmetric dual Minkowski results determine unrestricted realizers. A one-dimensional strictly monotone inverse of actual side lengths at supercritical q and the exact transition at which origin symmetry becomes forced add useful information beyond the known attainable interval, even for this restricted family. The construction below q=1 is a witnessed distinction between uniqueness among symmetric candidates and uniqueness among all candidates, not a claim to classify every off-center fiber.

The dated certificate retains the supplied scientific assessment, sources and limitations.
