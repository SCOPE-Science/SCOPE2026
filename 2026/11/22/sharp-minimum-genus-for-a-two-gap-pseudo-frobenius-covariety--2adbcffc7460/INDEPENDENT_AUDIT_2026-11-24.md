# Independent mathematical audit

## correctness

PASS

Among semigroups of Frobenius F=2k+1, F-2 is pseudo-Frobenius iff F-2 and 2 are gaps: 1 is already a gap, and every positive nongap above 2 sends F-2 past F. The eligible entries other than 2k form the forbidden-sum path indexed by e_j=2k-2-2j and o_j=3+2j, 0<=j<k-2. The pair e_j,o_j sums to F, and o_j,e_(j+1) sums to F-2; there are no loops, since the forbidden totals are odd. At most one from each pair can occur, and equality prohibits an odd choice followed by an even choice, forcing the unique switch indexed by t. With 2k present, the chosen evens form a terminal interval and all mixed sums exceed F. If odds occur, the smallest odd-plus-odd sum, 4t+6, must be at least 2k-2t; this is also sufficient. If no odds occur the same inequality is automatic. This covers k=2 (empty path) and gives the stated count by summing the allowable indices. The independent replay `python /workspace/branches/independent_replay.py 2` checks 699048 subsets for odd F=5 through 21 using the pseudo-Frobenius definition and additive closure, comparing full minimizer sets. The finite check does not replace the path proof.

## originality

PASS

Credit the prior genus lower bound, fixed-genus enumeration procedure, and specific F=11 count. The minimum is reached by a simple all-even construction, so priority is not assigned to the lower bound or to general enumerability. The supported distinct claim is the uniform switch classification and closed count of the entire minimum stratum, including both exact types, not a restatement of prescribed-PF theory.

## value

PASS

A fixed-genus algorithm need not reveal the shape or exact size of a minimum stratum. For the first nonconsecutive terminal pair in a prescribed-PF covariety, the theorem gives all extremizers uniformly without generating semigroups, including a count growing with F and both exact types when present. This is a natural structural refinement of the prior genus bound, not value claimed for the numerical bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
