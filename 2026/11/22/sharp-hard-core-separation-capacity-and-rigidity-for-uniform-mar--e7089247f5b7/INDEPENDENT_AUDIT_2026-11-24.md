# Independent mathematical audit

## correctness

PASS

Sorting the coordinates gives the deterministic bands (j−1)r ≤ V_j ≤ (j−1)r+a, a=1−(n−1)r. In the open critical interval they are disjoint, and the expected occupancy of each band is na by the marginals. The occupancy is exactly one on the separation event, giving the upper bound q=na. A uniform shift of the spacing-r progression, with balanced label probabilities, gives unconditional density one on the bands at mass q. A common uniform draw on the complementary set H on failure gives density one there and attains q. At r≤1/n the shifted 1/n lattice gives probability one; at r=1/(n−1) a successful packing must hit 0 and 1, an event of zero probability by atomlessness, and above it the packing is impossible. At equality, each band's occupancy exhausts its marginal mass on success, so failures lie in H almost surely; consequently each ordered successful V_j is uniform on its band. The offsets after subtracting (j−1)r are ordered and have equal expectations, so they coincide almost surely, establishing the exact progression. For any label i and position j, the conditional probability kernel p_ij(t) satisfies (q/a)p_ij(t)=1 a.e. by uniform marginal mass on each translated Borel subset of band j and zero failure mass there; hence p_ij=1/n. Failure marginals are uniform on H. The converse allows every coupling with those failure marginals because a tuple in H cannot pass the band condition. The optimizer attains S=r on all its successes, so every larger tail is zero, and in particular no pair of distinct critical thresholds has a common optimizer. All these statements were checked analytically; the frozen diagnostic was only read.

## originality

PASS

Exact progression and exact-distance copula capacities are close neighbors. The supported distinct result is the whole all-pairs separation tail and the complete critical equality structure with incompatibility, rather than merely constructing separated samples or maximizing a prescribed progression event. This is a bounded statement comparison, not a priority determination.

## value

PASS

The exact attainable tail for this natural constrained-packing statistic is accompanied by a nontrivial change in all optimizing laws: every band marginal saturates and produces a rigid success pattern with a full description of allowed label couplings. The zero larger tail of every critical optimizer gives a sharp obstruction to a universal stochastic maximizer, not visible from an upper bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
