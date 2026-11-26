# Independent mathematical audit

## correctness

PASS

For an unglued radius-one planar sector and independent area-uniform sampling, the radial densities are 2r and the independent gap density is 2(theta-delta)/theta². Strict separate convexity of the squared distance in the two radii puts all maximizers at radial corners, with distances 1 for tip–arc pairs and 2 sin(theta/2) for the two ordered arc-endpoint pairs. They are disjoint types at theta=pi/3. Compactness localizes near-maximal configurations (also for moving angles after normalizing the angles by theta). In small fixed neighborhoods the positive linear loss bounds the local coordinates up to constants, so dominated convergence on bounded rescaled coordinates applies. At a tip–rim pair the loss is V+U cos(delta); the two orders together have density 8 epsilon³ U/theta² in rescaled radial and original angular variables. The radial simplex integral is 1/(6 cos²(delta)), and the double-angle secant-square integral equals -2 log cos(theta). The result is -8 log cos(theta)/(3 theta²), including at pi/3. At the rim endpoints the loss is s(U+V)+cT with s=sin(theta/2), c=cos(theta/2), and density 8 epsilon⁴ T/theta². The unit simplex T-moment after scaling is 1/24, giving 4/(3 theta² sin²(theta)). The normalized losses and slack have the two stated Dirichlet limits by their U and T density weights; the tip loss coordinate is U cos(delta) and the gap mark density is (theta-delta) sec²(delta)/[-log cos(theta)]. The rim orders are symmetric. For fixed lambda, the moving diameter raises the threshold relative to 1 by (sqrt(3) max(lambda,0)/2-1) epsilon plus O(epsilon²); the tip simplex weight has homogeneity three and its volume yields exactly the stated positive-part function. At lambda=2/sqrt(3) the threshold is 1-epsilon²/6+O(epsilon³), so the tip term is at most order epsilon⁶; for larger lambda there is no tip event for sufficiently small epsilon. In both cases the rim has a quartic contribution with coefficient 16/pi². The logarithmic derivatives/weighted secant-square identity establish the monotonicity assertions; more precisely the two-preimage range of the wide coefficient is strictly between its minimum and 16/pi², its excluded left-endpoint value. The exact polar survival disintegration follows by integrating the triangular angle law above the cosine-rule threshold. All limits used here are pointwise in the stated parameters. I inspected sector_verifier.py but did not execute it; its selected fixed-angle quadratures do not check the critical window or prove the limits, which are reproduced by the local integrals above.

## originality

PASS

The same planar sampling object is already studied, with exact mean distances at selected openings and exact moment formulas. The sharp upper tail, critical profile and conditional shapes are distinct from those statistics. The strongest near-diameter comparisons use the intrinsic cone metric with glued boundary rays. Mixing their exact integral representations gives the planar integral, which the frozen text does not claim is novel. Their fixed-parameter asymptotic statements do not evaluate that mixture near a moving support endpoint or give the planar angular marks. The unread original referenced by MathWorld is an explicit residual risk. This is a bounded evidence judgment, not a historical priority certification.

## value

PASS

The sector is a standard line-picking domain, and the upper-endpoint law reveals something the diameter and moments alone miss: at the exact contact transition a continuum of tip–arc maximizers still dominates, whereas just above it a suppressed angular endpoint weight changes the exponent. The explicit critical profile resolves when that competition disappears at leading order, and the conditional shapes quantify the geometry of the rare pairs. These address a natural gap in the same-object distribution problem despite not giving a full CDF.

The dated certificate retains the supplied scientific assessment, sources and limitations.
