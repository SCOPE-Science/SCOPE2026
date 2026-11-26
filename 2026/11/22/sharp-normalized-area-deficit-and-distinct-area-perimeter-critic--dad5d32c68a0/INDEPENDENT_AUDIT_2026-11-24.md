# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 28–75 at a=1, restoring a² for area and a for length. The upper graph has a unique positive interior maximum at x*=√δ/2; outside it the second derivative of y² is negative and y is strictly concave. The symmetric upper graph capped by the horizontal chord between the two maxima is concave: it gives a convex containing set, and the new boundary chord belongs to the hull, so it is exactly the hull. At each contact x*²+y*²=1. The rationalized height deficit uses y*²−y²=(2−√(b⁴+4x²))²/4. Rescaling x=x*t yields the integral in lines 53–57: its denominator decreases strictly as δ grows while the numerator is fixed. For δ∈[0,3], hδ≥1/2 and Sδ≥1 give an integrable bound even at the lemniscate cusp. At zero the polynomial integral gives 1/120. At δ=3 the lobes have area 2 together, and the hull's first quadrant is a rectangle √3/4 plus sector minus triangle √3/4−√3/8, giving the asserted upper endpoint. For perimeter, y′=x(2/Sδ−1)/y is uniformly δ^(3/2)t(1−t²)/16+O(δ^(5/2)); expanding sqrt(1+y′²)−1 and integrating gives δ^(7/2)/3360 using the integral 8/105. The area expansion follows uniformly from its exact rescaled denominator, and the ratio constant is 120/3360=1/28. The supplied checker was read, not executed; its two area quadratures are distinct implementations of the rationalized integral rather than independent proofs. The limits are from within the connected nonconvex regime at fixed a.

## originality

PASS

The supported distinct claim is the globally strictly monotone Cassini area-deficit normalization with both optimal endpoint constants, presented together with the local perimeter comparison. Hull contact geometry and quadratures are credited background. An indexed general quartic-dimple result overlaps the two onset exponents and could account for their Cassini specialization via local jets; no novelty is assigned to the generic exponents. It does not establish the global normalized law throughout the connected Cassini regime in the statement available for comparison.

## value

PASS

The deficit measures the geometric cost of replacing a connected nonconvex oval by its hull. Normalizing by the critical area scale reveals a strictly ordered shape parameter across the entire regime and supplies sharp uniform constants, including the singular boundary limit. The distinct perimeter power and exact ratio explain why the length cost is smaller near convexity. The global statement is not a restatement of the contact geometry or a local exponent specialized to one oval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
