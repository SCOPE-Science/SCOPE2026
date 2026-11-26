# Independent mathematical audit

## correctness

PASS

The verified normalization has one rational branch above Q_infinity. On the T!=0 chart the three local coordinates have values m,m+2,m+6, where m=2g-5 is odd. In homogeneous degree n the possible numerator degrees are exactly 0 and 2 through 3n: all nonconstant numerators are multiples of the monic quadratic phi, and the intervals [2j,3j] provide a triangular basis in each allowed degree. This gives E_n and union H=<m,m+2,m+6>. Modulo m, representing residue 2j by the two non-m generators reduces to minimizing the cost of coins 1,3; at total j+lm the least cost is controlled by floor((j+lm)/3) plus the remainder, which cannot decrease as l increases for these m. The Apéry representative is thus the stated A_j, and taking its maximum and summing its entries give the stated conductor and gap count. In particular c<=(ceil(m/3)+2)m-1. Two different homogeneous degrees with matching leading values must have the same parity and differ by at least two, so a collision forces n>=ceil(m/3) and value >=(ceil(m/3)+2)m>c. Consequently no polynomial can obtain a new below-conductor value by cancellation; division by a local unit preserves valuation. Above the cutoff all values are already in H. The residual degree is one, so the filtration by valuation identifies delta with the gap count. Independent shortest paths in the residue graph, reachability and collision enumeration matched all 197 genera 4<=g<=200; the separate monic-quadratic span check over F_101 covered degrees 1 through 25. The general proof, not those finite tests, establishes uniformity.

## originality

PASS

This is an exact refinement of the same model, not a different parametrization presented as a new construction. Both inspected versions of the original construction say that the branch semigroup contains the three-generator semigroup and give two bounds on delta. They do not assert that the upper bound is attained. The added content is uniform equality of the geometric semigroup and hence the exact conductor and delta. The nearby Chebyshev model has a different multiplicity at fixed genus, and the exact catalogue hit is the assigned record itself.

## value

PASS

The specific projection already arises in a finite-field point-count problem, and the infinity branch was the location with only two-sided delta bounds. The valuation equality resolves that gap for every admissible genus and computes the arithmetic-genus contribution and the exact Aubry–Perret deficit when the normalization is maximal. The below-conductor separation of homogeneous degrees is the geometric step that makes the explicit numerical calculation applicable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
