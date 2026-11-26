# Independent mathematical audit

## correctness

PASS

For an invertible generator matrix U, each face pair bounds one coordinate of U^−1x to [−1/2,1/2]. Its maximum possible ball radius is the corresponding half-width, and the centered ball simultaneously attains the smallest half-width. Thus 2R=1/sqrt(max_i (G^−1)_ii)=sqrt(Δ/(1−m)), where G=U^T U and the last equality uses its principal minors. The perpendicular component of each unit generator to the other two is at most one, with all equalities exactly for orthonormal triples. The Gram density has the claimed factor 1/(4π): two independent uniform polar cosines and the azimuthal cosine with its two branches give denominator sqrt((1−a²)(1−b²)−(c−ab)²)=sqrt(Δ), on the positive definite domain. This also verifies the exact integral. On the endpoint event each projection onto the other two generators' span has norm at most 2√ε, so every off-diagonal correlation is at most that large in absolute value. After dividing correlations by 2√ε, the expansion of (1−(2R)²)/(4ε) on the fixed cube is maximum pair-sum of squares plus a uniform O(√ε) error. Its level-one boundary has zero Lebesgue measure, and the Gram density is uniformly bounded there and tends to 1/(4π). Dominated convergence yields the mass and the L1 convergence of normalized conditional densities. In one of 48 signed ordered sectors the third coordinate ranges from 0 to the smaller of the two leading coordinates, giving integral 48·(1/3)·(1−1/√2)=8(2−√2). The Jacobian 8ε^(3/2) yields the coefficient 16(2−√2)/π. The ratio of endpoint tails at tε and ε gives the CDF t^(3/2) for 0≤t≤1 under conditioning. The minimum squared correlation uniquely labels the closest facet pair except on a density-zero tie set; permutation symmetry persists under endpoint conditioning. Degenerate frames have probability zero. The finite quadrature and simulation code was inspected, not run; neither is an asymptotic proof.

## originality

PASS

The strongest inspected catalogue matches share either an inradius, a least altitude, or the tricylinder itself, but not this random-frame small-deficit event. The distinct result is the endpoint coefficient and uniform tricylinder conditional limit, not the separately classical cylinder volume or the general relation between facet altitude and the inverse Gram matrix. This is a bounded, best-knowledge decision with stated archival access risk.

## value

PASS

The inradius measures the weakest of three competing clearances for a natural random frame, and a determinant distribution cannot recover it. The exact coefficient and nonellipsoidal conditional shape distinguish which joint angular perturbations permit a near-maximal inball; the beta deficit law describes the corresponding leading conditional scale. These are meaningful metric conclusions not captured by random volume or by classical Steinmetz geometry alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
