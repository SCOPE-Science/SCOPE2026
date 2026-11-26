# Independent mathematical audit

## correctness

PASS

The transform is a copula: take componentwise maxima of independently sampled baseline pairs, with independent positive geometric sample size, and transform each maximum by its continuous marginal CDF g_p. In preimage coordinates put A=1+θz and F=xyA. Clearing the three positive denominators reduces K−uv to p[F(p+qz)−pxy], hence to pxyz(q+pθ+qθz). All z in (0,1) occur in the open square; the affine endpoint signs give both sharp thresholds, including their closed equality boundaries and the unique interior sign-contour coordinate in the mixed regime. At p=1,θ=0 both orders hold; at θ=−1 there is no PQD. For CDF-TP2, log(g_p(F)) has mixed derivative (log F)_xy/(1−qF)+qF_xF_y/[F(1−qF)^2], with (log F)_xy=θ/A². Substituting F_x=y[A−θx(1−y)] and F_y=x[A−θy(1−x)] gives numerator θ+q A[A(1−θ+2θz)+2θ²xyz] over the positive A²(1−qF)^2. It is nonnegative for θ≥0. For θ=−t the two factors 1−tz and 1+t−2tz are at least 1−t; the nonnegative remainder and the limit x,y→0 give the exact infimum (1−t)^3 for the product multiplying q. Thus the weak threshold includes equality; failure gives a negative mixed derivative on an interior rectangle. Integrating the mixed derivative establishes the determinant sign, extending it to the boundary by continuity. At t=1 the infimum is zero and necessity excludes all p>0. For t in (0,1), q<1 is why the root of (1−t)^3=t must be excluded from the existence range. Independent numerical evaluation gives 0.31767219617198067263 for that root. No density-TP2 assertion is involved, and no frozen script was used as proof.

## originality

PASS

The geometric PGF construction and geometric–FGM family are prior. The supported distinct result is the complete sharp phase diagram, in particular the sharp recovery of PQD and CDF-TP2 and the mixed-sign contour for negative baselines. Available comparisons did not establish an equivalent or broader theorem containing those thresholds. The original paper and author chapter were sought but their primary passages could not be retrieved in this audit, so historical coverage is not certified.

## value

PASS

This is an order-selection question in an already used copula family, not an arbitrary scan of parameter values. Exact thresholds tell which parameters produce global quadrant order, which afford the stronger CDF-TP2 property, and when no global quadrant order describes the same copula. The crossing contour and strict separation of the thresholds make the distinction usable even when simpler summaries such as rank correlation do not resolve it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
