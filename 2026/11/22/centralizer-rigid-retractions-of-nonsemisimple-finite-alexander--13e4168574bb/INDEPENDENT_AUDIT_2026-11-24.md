# Independent mathematical audit

## correctness

PASS

For T=lambda+epsilon with lambda different from 0 and 1, both T and 1-T are units. For a zero-fixing quandle homomorphism, the identities from x*0 and 0*y therefore give additivity by writing any sum as Tx+(1-T)y. Linearity over F_p and commutation with T then give R-linearity. An affine map (A,b) is idempotent exactly when A is a projection and b belongs to its kernel. Its two summands are free over the local ring, so change of basis and translation conjugate it to P_r. The projection count is the ratio of the three GL orders; reduction modulo epsilon contributes p^((2d-2)r(m-r)), the field orbit contributes p^(r(m-r)) times the Gaussian binomial, and translations contribute p^(d(m-r)). A map commuting with P_r has arbitrary block-diagonal linear part and translation in its image, giving the asserted Z_r. Equality of two exponents implies (r-t)(2(r+t)-2m+1)=0, forcing r=t. This also covers the extreme ranks. In the mixed example, the two images are distinguished by the rank of epsilon but each centralizer has p^6 linear parts and p^2 translations. The ordered-pair formula sums disjoint strata. VERIFICATION.md and verify.py are finite corroboration, not the proof; the frozen script was inspected, not executed.

## originality

PASS

The supported distinction is the full endomorphism-centralizer invariant of retraction conjugacy in the equal-length nonsemisimple family, with exact multiplicities and a mixed-length collision. Affineness, orbit-counting identities and ordinary linear centralizers are not new. The closest retraction and endomorphism censuses inspected do not cover the combined invariant.

## value

PASS

The full endomorphism centralizer is an intrinsic, countable invariant that distinguishes every retraction conjugacy class of a connected nonsemisimple family. The translation factor breaks the rank-complement symmetry of the linear problem, and the equal-image-size mixed-block example shows a genuine obstruction rather than a mere size difference. The complete multiplicities support exact commuting counts; value rests on the rigidity and its boundary, not on the Gaussian count by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
