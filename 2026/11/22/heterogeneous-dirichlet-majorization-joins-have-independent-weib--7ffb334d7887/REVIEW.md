# Independent mathematical audit

## correctness

PASS

For a fixed proper subset J, Gamma aggregation gives a Beta(a_J,A-a_J) sum; integrating its density from 0 to t yields t^{a_J} Gamma(A)/(Gamma(a_J+1)Gamma(A-a_J)) times 1+O(t) with no integrality restriction. The deficit is the minimum over J of the prescribed size. Distinct equal-size faces overlap only if the union sum is <=2t; that union has shape strictly larger than the least a_J, or is the full coordinate set and the event is impossible. Thus exactly the minimizing subsets contribute the first-order coefficient, including ties. With k<ell and thresholds x_k m^{-1/gamma_k}, x_ell m^{-1/gamma_ell}, any simultaneous witness J,K forces disjoint sums on K and on the nonempty J minus K. Integrating their aggregated joint Dirichlet density on the small rectangle yields O(m^{-a_K/gamma_ell-a_{J minus K}/gamma_k})=o(1/m); if their union is full the event is empty. This bounds all pair overlaps, so multiplying the per-sample complementary union probability over m independent draws gives the product survival function. The same calculation for every subcollection (or with thresholds zero in the other coordinates) gives joint weak convergence. Positive limiting variables imply each successive deficit ratio tends to zero in probability by tightness and boundedness away from zero in probability after rankwise scaling. Consequently successive slopes, asymptotic in probability to 1, Delta_1, ..., Delta_{d-1}, are strictly decreasing with high probability; this also treats d=2 with just the first and last slopes. On that event no concavification changes the join. Independently substituting (1,1,2,4) gives shapes (4,2,1), multiplicities (1,1,2) and constants (35,21,14).

## originality

PASS

The independent rank limit and inactive join correction for uniform simplex samples are prior work. The supported distinct claim gives the heterogeneous shape exponents and tied-face intensities and establishes the joint law and join transfer under the resulting heterogeneous scales.

## value

PASS

Unequal shape parameters are a natural model of heterogeneous compositions. A sharp joint law for all ranks of the least common upper bound quantifies concentration and distinguishes repeated from isolated minimum faces. The rank separation and exact high-probability join simplification explain why the result is stronger than a calculation for one Beta minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
