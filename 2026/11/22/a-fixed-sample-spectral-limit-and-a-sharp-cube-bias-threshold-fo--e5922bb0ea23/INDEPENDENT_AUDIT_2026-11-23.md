# Independent mathematical audit

## correctness

PASS

The source max of the squared centered Rayleigh quotient is n times the squared operator norm. With d≥2n the bottom deviation is −1/d and tr(G)=n gives λmax(G)≥1, so the positive top deviation λmax(G)/n−1/d is at least 1/d even for rank-deficient samples. This gives (1) exactly. The Haar off-diagonal Gaussian products have covariance identity (a singleton Gaussian index makes cross-products between distinct pairs vanish); norm ratios tend jointly to one. In the cube model, pair-products have means μ_d², shared-index covariance μ_d²−μ_d⁴, diagonal 1−μ_d⁴ and disjoint covariance zero. Boundedness and covariance convergence justify the centered joint triangular CLT; λmax stays continuous and the expansion around the identity gives the stated factor n√d/2. For exact finite Haar calibration, the unnormalized Gaussian cross-product matrix has positive Wishart density on positive definite matrices (d≥2n); diagonal normalization is a smooth change of variables with the positive diagonal scales, and the Haar Gram thus has positive density on the open unit-diagonal elliptope. Its λmax is atom-free by the determinant polynomial, and the available positive equicorrelations give positive mass in every open subinterval of (1,n). In the Gaussian limit and all finite shifts the determinant polynomial is likewise nonzero: specialize the total off-diagonal entries to zero at t≠0 and to J−I at t=0. Full support and scaling give the null's strictly increasing CDF on (0,∞). These facts justify converging quantiles and strict thresholds even for lattice alternatives. In the large-bias regime the all-ones Rayleigh quotient gives √d(λmax(G)−1)≥(n−1)√dμ_d²+O_P(1); the exact monotone spectral formula yields consistency. Subcritical power is nominal only for the stated upper-tail rule, not all tests. For n=2 the null |r| cutoff was independently obtained from z=t_(d−1,0.975) by z/√(d−1+z²); with h=√d integral at the four recorded d, the alternative tails were evaluated by the exact integer sum of binom(d,k)(h+1)^k(h−1)^(d−k)/(2h)^d over |2k−d|>d b. Rejection boundaries were k≤24 or ≥40, ≤112 or ≥144, ≤480 or ≥544, and ≤1985 or ≥2111, respectively. Powers 0.191249632841830, 0.175465797543167, 0.167714211420906, 0.171808101288575 and limiting power 0.17007504575308752 match the record. The n=2 derivative is positive for c>0 since |z−c²|<z+c². The source checker was only inspected: 751 is its scalar-check counter, including grouped checks on seeded simulation, not 751 distinct assert statements or proofs of the CLT. Discreteness versus nonatomic Haar proves TV=1 throughout the stated d≥2n scope.

## originality

PASS

Best-of-knowledge pass for the singular product-cube detection boundary and explicit Haar-calibrated local and two-observation laws for this statistic. The source test, its scatter operator-norm identity, the two-angle marginal and generic fixed-size multivariate Gaussian covariance limit are not new ingredients.

## value

PASS

This makes a precise operational statement about an established test in a low-data, high-dimension regime. Even a TV-one alternative can yield nominal asymptotic power under its upper-tail calibration, and the exact bias scale and local matrix power law explain when that ceases. The n=2 lattice-vs-continuous tail is a useful exact benchmark rather than an isolated numerical check. Novel mathematical value lies in the test-specific comparison, not the standard multivariate CLT or a minimax claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
