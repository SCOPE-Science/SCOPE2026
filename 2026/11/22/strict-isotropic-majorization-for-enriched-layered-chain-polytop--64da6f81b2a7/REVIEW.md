# Independent mathematical audit

## correctness

PASS

The signed antichains lie in individual layers and yield the convex hull of the embedded cubes, with gauge equal to the sum of the block sup norms. Differentiating block volume (2s)^m and block coordinate second-moment integral (2s)^m s²/3 gives the radial density and shell second moment (m+2)s²/(3m). Integrating against Dirichlet(m1,…,mr,1) gives the claimed volume and diagonal covariances; sign symmetry kills every off-diagonal term. In the log-profile, the second difference reduces to the stated log expression; m=3 gives log(2000/1944)>0, and for m≥4 the rational comparison between the two strict log bounds has numerator 2m−8 after taking the common denominator. Strict convexity of the integer potential gives the transfers and unique extremal orbits, including N=r and N=r+1. The phrase ‘equality only for permutations’ is read within the stated majorization comparison and the extremizer claims, not as injectivity on incomparable profiles. Indeed the profiles with multiplicities 6×7, 30×5, 50×3, 16×1 and 23×6, 31×4, 48×2 have equal constants at (N,r)=(358,102) but are incomparable (partial sums cross). Replay: python /workspace/audit_checks/reconstruct.py 2 reproduces the numerical examples and that exact distinction; the general result is analytic. Frozen code inspected, not executed.

## originality

PASS

Prior coverage includes the Hanner covariance/profile machinery. The distinct supported contribution is strict fixed-dimension, fixed-block-count majorization, which requires a separate sign inequality for the block potential. The bounded comparisons did not identify an earlier statement of that ordering or a stronger statement implying it without the discrete convexity step.

## value

PASS

For the canonical enriched layered geometry, this is a sharp answer to how redistributing a fixed number of coordinates among layers changes a natural affine invariant. The discrete convexity controls all comparable profiles and gives rigidity at both ends, not merely a computation of existing Hanner constants. Its value is specific to fixed N,r, not a new universal Hanner bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
