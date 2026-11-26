# Independent mathematical audit

## correctness

PASS

The independent exact replay at review-evidence/2-klein-quintic.js used polynomial arithmetic over F_7, not the uploaded script. Substitution of the three quartics annihilates the Klein equation; their common affine gcd is 1, their leading coordinates are nonzero at infinity, and the six conic monomials have restriction rank 6. The product of image degree and generic mapping degree is 4; the rank excludes a line or conic, so the map is the birational normalization. The cross product with the derivative has precisely the three quintic coordinates claimed, no finite basepoint, nonzero leading ratios at infinity and linear restriction rank 3. It annihilates the asserted dual equation. The same degree argument, now with degree 5, proves an integral quintic with a degree-one normalization; generically the cross product gives the tangent on the smooth locus. At each coordinate cusp the local equation has the form a unit times a square plus a nonzero constant times a cube, with the unit absorbed into the square formally in characteristic seven. At the fourth point the leading ratios give [1:2:4], the gcd of B−2A and C−4A is 1, and separate series division gives u=s²+2s⁴+s⁵+… and v−3u−3u²−5u³=3s⁷+O(s⁸). Taking a formal square root so u=t², the even part of the second coordinate can be subtracted as a series in t², leaving t⁷ times a unit in t². Thus the completed branch ring is k[[t²,t⁷]], with gaps 1,3,5. The four delta invariants sum to the quintic arithmetic genus 6, exhausting the singularities. Normalization is defined over F_7 and induces a bijection on finite-extension points because every singular point has exactly one geometric preimage; the count and zeta follow. This is the dual of the reduced equation in the stated plane, not a claim about stable reduction. The frozen SymPy verifier and transcript were inspected, not executed.

## originality

PASS

The supported distinct claim is the dual quintic in characteristic seven, its complete cusp basket and the consequences for this dual model. The published characteristic-seven cusp and arithmetic on the original plane quartic are existing work, not credited as novel. The closest original-curve, Hessian, and classical Gauss-map results inspected do not establish the explicit dual and its local singularity calculation. The limited search is not a historical priority certification.

## value

PASS

The Klein quartic is a natural object with bad reduction at seven. In this reduction the explicit dual and the proof of its full singularity basket give more than a computed equation or repetition of the primal cusp. In particular, the wild transverse order seven and three additional ordinary cusps account for the entire genus defect and determine the geometry relevant to arithmetic on the dual model. The zeta function is a useful consequence rather than the sole basis of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
