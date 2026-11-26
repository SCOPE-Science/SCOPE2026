# Independent mathematical audit

## correctness

PASS

Writing p=Σ_{i<j}x_i x_j, q=x_1x_2x_3 and b=(1−2p)/3 gives output coordinates b+2r_i with r_i the three pair products. They sum to one, and Σr_i²=p²−2q, so D(Vx)=8p²/3−8q. The next product is b³+2p b²+4qb+8q², and p'=1/3−D(Vx)/2; these reproduce the two-step polynomial. At fixed p its q derivative is −(32/9)(8p²−6p+12q+1); q≥0 suffices for p≤1/4 and Schur 9q≥4p−1 gives the strictly positive bracket for 1/4<p<1/3. The edge minimum q=0 is feasible through p=1/4, and the edge ratio increases to 1/9 (its derivative sign reduces to 18p²−11p+2>0). Above p=1/4 every state is interior; multiplier equations force repeated coordinates at an extremum of q, since pairwise differences of the equations for three distinct coordinates would identify all three with the same multiplier. The branch with repeated a=(1+sqrt(1−3p))/3 gives the smaller product. On it one step multiplies variance by 4a² and maps the repeated coordinate to a'=(1+2a−6a²)/3, so the two-step factor is 16a²(a')². Its derivative has the unique interior maximizing root of 18a²−4a−1=0 on (1/3,1/2); the other quadratic factor 6a²−2a−1 is negative there. At that root a(a+1)=(31+11sqrt(22))/162 and a'=2(a+1)/9, giving exactly the stated radical. Since the other branch and the edge cannot attain it, only its coordinate permutations give noncenter equality. The one-step ratio is increasing to one on the edge, and is 4a²<1 on the interior minimizing branch. Iteration gives the global bound; on the tangent plane the derivative is (2/3)(I+cyclic shift), with squared two-step factor 16/81. The frozen symbolic identities and 285 grid states are corroboration; the continuous maximum and closed-boundary cases were checked analytically.

## originality

PASS

The supported distinct claim is the optimal global two-step Euclidean variance factor and its interior equality orbit, contrasted with the sharp one-step factor. Mamurov's exact same map and qualitative regularity assertions are prior; the inspected proof bounds a different Lyapunov function that loses all variance information on the maximizing two-equal-coordinate branch. The plausible permutation-family comparison is a different map even under relabeling. This is a bounded best-of-knowledge decision, not a historical priority claim.

## value

PASS

Variance around equilibrium is a natural imbalance statistic for this previously studied map. Two generations are the first horizon at which there is strict uniform contraction in this metric, since the one-step maximum is one at edge midpoints. The exact constant is a usable global transient bound, and its interior equality composition identifies an obstruction that neither boundary testing nor the equilibrium linearization captures. Thus this is a motivated sharp finite-horizon result, not a new claim of qualitative regularity or an arbitrary iterate count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
