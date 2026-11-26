# Independent mathematical audit

## correctness

PASS

Positive-scale affine invariance gives the standard Cauchy normalization. To justify the key joint-density limit, put d=1/v and split the ordered density by the sample-minimum coordinate y at y=−d/2, so z=y+d. In the half y≥−d/2 retain the first n−1 order statistics, set x_c=x_b+g, and multiply their product density by d² f(y+d), with the indicator that y+d exceeds the last retained coordinate. The removed endpoint factor is bounded by 4/pi and tends to 1/pi. For each fixed tuple of the other n−2 coordinates the endpoint restrictions become automatic uniformly on bounded g intervals. The retained product is dominated by sup f times the product of densities in those free coordinates, an integrable bound. The other half is the same calculation by reflection, removing the minimum, with indices b−1,c−1 in the retained sample. This proves local uniformity of the two-term density H; the ordered factorials give n/pi. Integrating the r−1 coordinates between the two marked ranks yields the uniform O(g^(r−1)) bound. The same gap bound holds for the marginal small-gap law, and a union bound on absolute sample extremes gives P(V<s)=O(s). For adjacent ranks the small square integrates to H(0)t log(1/t) to leading order; its two exterior strips are O(t) at fixed square size. For r≥2 the compact region bounded away from zero gives the integral of H(g)/g; the g>M tail is O(t/M), and near zero integration of min(v0,t/g) against the gap bound plus the V>v0 strip gives O(t δ^(r−1)+t^r). The adjacent density at zero follows by integrating f² against the two order-statistic weights and substituting u=F(y). At n=4 the two three-sample densities are each 3/(2pi), giving 12/pi². At the other endpoint the two outer gaps lie in a simplex of area t²d²/2. For t≤1/4 one pair of translated endpoint densities has both arguments at distance at least d/4 from zero, according to the same y split, so the integrated four-density product is O(d^−4) for d≥1; it is bounded for d≤1. Dominated convergence and symmetry give 12(∫ f²)(∫ x² f²)=3/pi². Both moment thresholds follow by integrating these endpoint tails, including divergence at equality. The stated four probability levels do give (1,3,8,10) at n=10 under the record's own ceiling-rank convention.

## originality

PASS

The useful comparison is a fixed-size endpoint law for a raw affine-invariant spacing ratio, not priority for defining a quantile test. The accessible extreme-order Cauchy primary source uses a different statistic; the closest four-quantile source is reported to study null asymptotics and simulated cutoffs, but its full text and its interpolation convention could not be independently checked. The checked material does not supply the claimed coefficients or collapse-versus-escape transition. This is a bounded best-of-knowledge conclusion with the two specific access gaps below.

## value

PASS

The theorem resolves a natural fixed-sample rare-tail calibration question for an affine-invariant raw order-statistic ratio. It distinguishes the borderline adjacent collision coupled to an extreme range from the integrable inverse-gap case, with sharp constants and a contrasting quadratic endpoint at the minimal sample size. This gives precise moment thresholds and mathematically meaningful null-tail behavior, irrespective of which software quantile rule an existing test uses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
