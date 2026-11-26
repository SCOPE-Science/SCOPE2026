# Independent mathematical audit

## correctness

PASS

RESULT.md lines 50–71: the probability integral transform preserves almost-sure endpoint ranks even for a continuous non-strictly-increasing CDF. Sorted pairs have density 2. Disjoint windows and the multinomial Laplace functional give independent limiting PPPs in the three specified corner charts. A tagged degree is conditionally Bin(n−1,p), with p=2b−b²−a². For a+b≤1, a²≤b(1−b), so p≥b, and reflection gives p≥min(b,1−a). A uniformly exponential lower-tail bound outside the two fixed rescaled corners beats a union bound over n vertices. Inside either corner the normalized conditional variance is O(n^(−1/2)); the chance that a particular vertex lies there is O(1/n), so summing conditional Chebyshev bounds over all tags makes the maximum degree replacement error vanish in probability. This does not assume independent degrees. The Jacobian for (u,v)=(qd/2,d/2) gives intensity (d/2) dd dq per side. PPP simplicity and absence of fixed-time atoms justify the counts and fixed-order/mark limits, including at t=0. For each vertex universality is exactly the two constraints L_i≤min R_j and R_i≥max L_j (the self constraints are automatic); the exceptional common-intersection probability computed in the source is correct but is not needed for this identity. The two rescaled thresholds are tight and have limiting survivals e^(−x²); conditional on them, no point of the independent spanning cloud hits the clipping boundary. This gives joint, not separate marginal, convergence. The covariance is 4 Cov(AB,min(A,B)); polar integration uses 2∫₀^{π/4}cos²θ sin³θ dθ=4/15−7/(30√2), giving 0.73451467980251 for the displayed expression. The conditional no-count tail gives the double integral, which at zero reduces via s=a+b to (2/3)∫₀∞s³e^(−s²)ds=1/3. These are limiting moments only. The frozen checker was read, not executed.

## originality

PASS

Credit the separate indexed clipping result for the full jointly convergent raw three-corner process, both gap minima, the conditional universal point-measure law and the mixed-Poisson count. At the level of raw point fields, it already determines the limiting construction. The supported distinct contribution is the transfer to the actual interacting vertex degrees throughout bounded windows, giving the full marked degree process jointly with the universal count. That transfer needs quantitative control of graph degrees in and out of the corners; it is not a restriction or coordinate map on the finite raw corner clouds. The covariance and conditional statements are consequences of this transfer and the credited limit, not separately novel universal-count theorems. No ordering is inferred from shared catalogue dates.

## value

PASS

The transfer from endpoint proxies to degree observations answers a natural question about a dense geometric graph: it gives the multiplicity, marks and ordered low-degree spectrum and relates that actual graph statistic to the opposite degree extreme. The uniform localization step is essential because omitted vertices could otherwise contribute low degrees; the resulting shared-boundary law gives a concrete dependence statement beyond either known scalar marginal. It is not sold as a new general Poisson convergence technique or a finite-size covariance asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
