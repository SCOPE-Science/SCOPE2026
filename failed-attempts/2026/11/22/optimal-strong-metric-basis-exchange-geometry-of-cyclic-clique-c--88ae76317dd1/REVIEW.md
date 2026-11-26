# Independent mathematical audit

## correctness

PASS

The endpoints of a mutually maximally distant pair are its only possible strong resolvers. Conversely, maximally extend a geodesic through the pair to be resolved at either end as long as a neighbor at greater distance from the other end exists; the resulting MMD pair has at least one endpoint in any cover, which resolves the original pair. In the Cartesian host the distance is cycle distance plus the color mismatch indicator, and a pair is MMD exactly when cycle distance is maximal and colors differ. For even circumference this gives disjoint crowns; a crown with m≥3 has only entire shores as maximum independent sets because a mixed independent set has size at most two, while m=2 gives independent choices in disjoint edges. For odd circumference the steps ±k form the distance-k cycle. If j>0 positions in that cycle contain at least two colors, these positions are independent and force their adjacent positions to be empty. The intervening gaps have at least one missing position each, and one gap has at least two by odd parity; the closed neighborhood of the j positions thus has at least 2j+1 positions. The size bound (m−2)j+2k gives equality for m≥3 only at j=k with full fibers; all singleton positions instead give size at most n with equality only for a monochromatic layer. The case tie is (3,3). In a maximum odd-cycle independent set all gaps have one missing position except one gap of two. Following the two-step progression translates to steps ±1 in the original cycle, yielding precisely k-intervals. For odd n and m=2 the direct product is the single 2n-cycle with two alternating optima. Complementing preserves one-sided equal-size exchange costs. Opposite-block changes cost m (or 1 per separate edge when m=2), cyclic intervals exchange min(delta,n−delta) full fibers, and the two families in 3×3 exchange 2 across families and 3 within. Thresholds follow by retaining the weight-one cube/cycle adjacencies at the first corresponding budget. The only one-vertex exchanges occur across MMD pairs that are not host edges. These are universal arguments; support code was inspected but not used to infer all n,m.

## originality

FAIL

The full optimizer classification is covered by the prior Cartesian strong-resolving product reduction and Zhang's general maximum-independent-set structure theorem for direct products, not just a known dimension formula. The advertised exchange metrics, connectivity thresholds and slide obstruction are immediate coordinate comparisons on the resulting known families. An exact prior statement using batch-exchange terminology is unnecessary for this implication.

## value

FAIL

The compilation is a convenient exposition, but after existing structural optimizer coverage the only residual step is taking intersections of full rows, columns, intervals or disjoint blocks. This gives graph powers and cutoffs by a routine substitution, and the slide observation only asks if exchanged MMD endpoints are adjacent. No distinct substantive gap or useful unknown exact fact remains in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
