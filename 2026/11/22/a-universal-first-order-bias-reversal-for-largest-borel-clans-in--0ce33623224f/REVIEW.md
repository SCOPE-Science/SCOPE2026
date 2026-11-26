# Independent mathematical audit

## correctness

PASS

The pooled number of founders is Poisson with mean nμδ and the marks are Borel sizes. Thinning gives the exact no-exceedance probability with k>nx and includes the no-founder case. At y=k/n, the tilted Borel mass is e^(−ay/2)/(sqrt(2π) k^(3/2)) times [1+δ(1−ay/3)+R]. For y≥x0>0, the exact remaining exponential is e^(−by), b=aδ/3+O(δ²)≥0; |e^(−by)−1+by|≤(by)²/2. This and the factorial error O(1/k) bound the bracket remainder by O(δ²(1+y²)) on the whole upper tail. Riemann sums for both coefficient functions have uniform O(1/n) error, including flooring nx, since their derivatives are integrable away from zero. Changing variables and exponentiating gives c=μa/sqrt(2π) and the stated coefficient −cJ(ax) times the limiting CDF. J starts positive divergent, decreases up to 3 where its tail is negative, and increases thereafter to zero from below. This gives one coefficient zero, not one crossing of the exact lattice CDF. The sign claims apply to fixed positive x. Independent numerical cross-check: starting at p1=e^(−θ), use p_(k+1)/p_k=θe^(−θ)(1+1/k)^(k−1), with a=1.6, μ=1.2, n=1000,4000,16000, summing to ceil(110n/a); quadrature/bisection gives z*≈1.88898594352. The scaled errors approach the predicted signs and coefficients away from the root; bounded n-scaled residuals at the root are consistent with lattice effects. The supplied check_borel_max.py was inspected, not executed; its exact-mass tail is numerically truncated.

## originality

PASS

Pass for the compact-uniform signed first correction and its unique cancellation point, not for the Borel representation, thinning formula or leading inverse-Gaussian largest-jump law. The inspected exact distributions supply the terms to be expanded but do not supply the moving-tail first correction, its uniform remainder, or its sign law.

## value

PASS

The largest founder is the most severe single family in the Poisson–Borel model. The theorem gives a sharp leading error with opposite signs at different thresholds and identifies a parameter-rescaled point where the error drops from order n^(-1/2) to O(n^(-1)). This provides a concrete calibration for when a leading-limit CDF over- or under-estimates fixed-threshold risk, not merely another derivation of the limit. The statistic is latent under the specified founder representation, not an observed total.

The dated certificate retains the supplied scientific assessment, sources and limitations.
