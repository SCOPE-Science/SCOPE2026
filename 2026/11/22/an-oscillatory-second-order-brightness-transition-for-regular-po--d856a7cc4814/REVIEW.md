# Independent mathematical audit

## correctness

PASS

Half the cross product of the two sides of a lateral triangle gives horizontal norm h sin(π/n) and positive vertical component s_n. The base vector is minus the lateral sum. Cauchy's formula thus reduces to the larger of the positive and negative lateral dot-product sums, equivalently max_S |u·a_S|. Maximization over u gives max_S ||a_S||, with equality only along ±a_S. At fixed 0<k<n the planar norm is maximized by taking the top k scalar projections in the direction of the sum; these are cyclically consecutive even if the cutoff is tied (the tie is at the ends of the arc). Their geometric sum has norm sin(kπ/n)/sin(π/n). Complementation strictly wins for k<n/2. For k<n, consecutive blocks give n axes; the tilt ratios h sin(kπ/n)/(k s_n) strictly decrease for k≥ceil(n/2), so distinct winning k contribute disjoint orbits. Crossing the vertical intercept gives exactly the stated threshold; at equality the vertical is still a maximizer, but no longer unique. Taking both signs of each extremal vector yields the 2m cap centers; disjointness and exclusion of smaller-norm vectors give the exact terminal formula. In the asymptotic, R'=-2f/sin²(πx), and with y=π(1-x), f' sin²(πx)=sin²y+2(π-y)sin y cos y-2πy+y², whose y-derivative is -4(π-y)sin²y. Thus f decreases from 1/2 to -1 and R has a unique nondegenerate minimum, with R diverging at 1. Comparing to a nearest grid point gives an O(1/n) bound on each minimizing grid point's distance from ξ; upper/lower Taylor bounds then give the d_n² term with O(n^-3) unscaled error. The prefactor is (n²/4)sin²(2π/n). Rational ξ would make cot(πξ) algebraic and nonzero, and the stationary equation would make π algebraic. Density for an irrational rotation then gives the full stated interval, including its endpoints. At ξ the stationary equation gives C/τ=π²-(1-ξ²)^(-2); hence A+C/4<0 exactly, not only numerically. Independent bisection and direct minimization checks agreed with the displayed constants and sampled asymptotics. In the proof the base and first lateral vector share the label a_0, and the oriented cap-center count uses both signs; these are notation issues, not changes to the finding.

## originality

PASS

Credit the known cone threshold and the previously used finite-polytope brightness and cap machinery. The supported distinct contribution is the explicit consecutive-face formula and axis classification at regular n≥5, the exact first crossing, and the irrational-grid second-order correction, with a family-specific tail coefficient. The closest original statements do not cover this combination.

## value

PASS

The finite formula resolves all brightest projections of a natural polygonal approximation of a cone. The nondegenerate interval of scaled errors pinpoints how integer facet counts affect the first shape transition and rules out a single second-order coefficient. This is more informative than the generic tail identity or convergence to a known constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
