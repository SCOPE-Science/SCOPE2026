# Independent mathematical audit

## correctness

PASS

Reflection symmetry makes the covariance diagonal and centered. Independently decomposing into the base rectangle, side strips and four quarter-disks gives A and both unnormalized moments: the x moment of one translated quarter-disk is a²πt²/4+2at³/3+πt⁴/16. Normalization is MxMy/A⁴. The expansion of 4A′MxMy−A(MxMy)′ has no constant term or terms above degree seven and agrees with all seven frozen coefficients. The first is positive by π<4; for the others the rational shift π=157/50+u gives positive monomial coefficients, establishing the sign for every a,b,t>0, including unequal sides and no aspect-ratio restriction. The endpoint values follow from the constant and leading terms. The coefficients of t and t⁷ in the derivative numerator give the stated quadratic corrections after division by A⁵ and integration at the respective endpoints; they also show the linear corrections vanish. Continuity gives strict decrease on the closed half-line despite J′(0)=0. Replay: python /workspace/audit_checks/reconstruct.py 1. The uploaded checker was inspected, not executed.

## originality

PASS

Pass for strict all-radius monotonicity of the nonsquare rectangle family and its sharp quadratic responses. The unit-square onset is demonstrably prior and the square profile is not counted as new. No retrieved stronger theorem supplies the unequal-rectangle all-radius inequality.

## value

PASS

Euclidean outer rounding is a natural path from a rectangle to the disk, and the determinant normalized by area is an intrinsic affine shape statistic along it. The result controls the ordering at all radii and arbitrarily large aspect ratio, not just near the initial body; the common onset in units of √(ab) exposes a simple aspect-independent response. It makes no assertion for arbitrary planar bodies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
