# Independent mathematical audit

## correctness

PASS

Normalize the parallelogram affinely; normalized arclength on the selected straight side is the uniform affine parameter and the area Jacobian cancels. For a centered ellipse written with a positive definite shape matrix, the support distances in the coordinate directions are square roots of its diagonal entries. Equal opposite supporting distances force center zero and tangency forces both entries one. With off-diagonal k, positive definiteness is |k|<1 and support in the first direction is attained at (1,k), proving the required classification and measure. The coverage quadratic in k is (k−xy)²≤(1−x²)(1−y²); the full interval lies in [−1,1] by Cauchy–Schwarz. Its normalized length is the square root of the right-hand side. Taking the mth power by independence, Tonelli and the substitution r=x² give the square of B(1/2,1+m/2) divided by 4, yielding π²/16 and 4/9. The gamma quotient with z=m/2 has correction −3/(8z); squaring gives the advertised −3/(2m) relative correction. Independently, rotate to principal coordinates U,V and integrate vertical slices in the positive quadrant: the l ellipse has the smaller height up to U₀=√[(1+k)(1+l)/2], after which k has the smaller height until U=√(1+k). In each integral set U=√(1+c) sin ψ. At the switch ψ_l=(π−α)/2 and ψ_k=(π−β)/2; the sinψ cosψ terms cancel, leaving the stated kernel, also continuous at k=l. Subtracting the two conic equations gives (x+y)²=(1+k)(1+l) and (x−y)²=(1−k)(1−l); their two independent sign choices give four points even for k+l=0. All contacts on the square boundary differ, so the four crossings are interior. Their gradient determinant is 4(l−k)(x²−y²) up to sign, nonzero since the product (x+y)(x−y) is nonzero. These exact checks resolve the claims; inspected frozen quadratures were not executed and are not needed for proof.

## originality

PASS

Credit the classical tangent-family equations and point-incidence theory, standard sector overlap computation, and the previously available congruent-perpendicular subfamily of the kernel. The distinct contribution supported here is the contact-uniform all-m mean and full two-parameter exact overlap, with a family-wide crossing count as a geometric consequence of the classical pencil.

## value

PASS

Natural sampling on the complete affine family gives an exact shape-independent hierarchy for every sample size, not just an example, and a sharp quantitative decay law. The full deterministic kernel is useful independently of random sampling and goes beyond the known congruent case or an individual overlap computation; four transverse crossings explain the integration geometry. The result is a mean-area law, not a claim about the whole area distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
