# Independent mathematical audit

## correctness

PASS

For a fixed multiplier the two translation intervals have lengths (a-w_x)_+ and (b-w_y)_+ (infeasible fibers contribute zero). The widths are maxima of the three projected unit edge lengths, so the integrand has twelve equivalent 30-degree sectors and, at height 1 in the first sector, widths s and (sqrt(3)s+t)/2. Independently computed the full signed integral on the height-feasible sector using t=ws, 0<=w<=1/sqrt(3) and 0<=s<=2/(sqrt(3)+w), with Jacobian s. Summed over the sectors, the integral is (8 sqrt(3)q-7)/12. Only q<rho=2/sqrt(3) cuts a negative tail; q>=1 puts that cut above the sector boundary switch at sqrt(3)/2. Removing the tail adds 9 times the integral of (s-q)(rho-s)^2 from q to rho, i.e. (3/4)(rho-q)^4, so the one-sided fourth derivatives are 18 and 0 and lower derivatives agree. Rotation of the target exchanges the axes and uniform dilation gives the m^4 factor. At fixed area the objective is S^2 V(q)/q^2. Its derivative below rho is (q^2-1)3(q-1/sqrt(3))(q-sqrt(3))/(2q^3); above rho it is -(4sqrt(3)q-7)/(6q^3), both negative for q>1 in their respective regimes. At q=1 the value is (15/2-4sqrt(3))S^2. Exact replay: python3 /workspace/review_evidence/algebra.py (SymPy; triangle block).

## originality

PASS

The specific contribution supported by comparison is the evaluated translation-weighted equilateral-source volume and its aspect-ratio consequences. The closest distinct catalog record has the same quartic-transition phenomenon for a right-isosceles source, but a different formula and threshold, and same-day chronology is not used to decide coverage. The earlier equilateral orientation law is same-object but uses a different measure; its square optimizer is not the claimed 4-volume optimizer.

## value

PASS

The four-volume is a natural quantitative invariant of the already studied similarity-placement polytope, and it accounts for translations lost by projecting to the known multiplier footprint. The near-threshold integration identifies how a geometric change in active width constraints becomes a fourth-order rather than a lower-order singularity. The exact profile resolves an independent fixed-area extremum and supplies its sharp constant; neither a square optimum for a different footprint statistic nor the prior shape transition settles it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
