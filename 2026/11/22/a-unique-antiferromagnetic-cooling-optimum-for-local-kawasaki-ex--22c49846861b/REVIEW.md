# Independent mathematical audit

## correctness

PASS

With k positive spins on the star and d=2k-n-1, the energy change from a negative to positive hub is -2Jd. Thus the two directed rates are a and b=1-a, with proposal clocks of rate one per hub–leaf edge; detailed balance gives the positive-hub to negative-hub per-state weight ratio a/b. The two configuration levels are the k- and (k-1)-subsets, not a two-state chain. For their inclusion matrix B, BBᵀ=kI plus Johnson adjacency on k-subsets, or equivalently U_{k-1}D_k in the Boolean up/down notation. The commutator gives eigenvalue (k-j)(n-k+1-j) on the (k-j)-fold raise of level-j harmonics. Norm recursion shows the raised vectors are nonzero for j≤min(k,n-k) and the harmonic dimensions telescope to the full level size. Reversible symmetrization gives a 2-by-2 block on each positive singular pair, with diagonals ka,cb for c=n-k+1 and off-diagonal magnitude sqrt(ab) times the singular value. The trivial pair contributes 0,S. In interacting sectors j=1 is the largest nontrivial singular value, so its lower eigenvalue is the gap; it is strictly below both unpaired diagonals and has determinant nab. In the endpoint sectors the nonconstant eigenvalues on unpaired vectors give a or b instead. At a=1/2 the lower root is 1/2. Its derivative has the sign of F=n(1-2a)-dg; for d>0 it is negative on a≥1/2, and on (0,1/2) it has exactly one positive-to-negative crossing because F(0)=n, F(1/2)=-d/2, and at every zero F'=-2n. The reflection (k,c,a)↔(c,k,1-a) covers d<0. The logistic map gives the claimed antiferromagnetic, ferromagnetic and balanced classifications and the antiferromagnetic endpoint limit/growth rates. Substituting n=4,k=2 gives the stated exact example with g=2n(a-1/2) at stationarity.

## originality

PASS

The configuration graph is exactly an established adjacent-level Boolean graph, and its singular values are known in the precise parameter range needed. The spectral conversion with two constant directional rates is a direct application of those singular values, not a new combinatorial spectrum. The supported distinct result is the sharp temperature classification of local Ising exchange across all star fillings: one strict interior optimum precisely in the interacting unbalanced antiferromagnetic sectors, a flat balanced sector, and different dilute-sector behavior.

## value

PASS

The star is a simple heterogeneous graph in which one hub induces two Gibbs energy levels but relaxation still depends on the nontrivial leaf modes. The complete result distinguishes when cooling improves, optimizes, leaves unchanged, or suppresses the gap, including the difference between genuinely interacting fillings and a single particle or vacancy. This is a useful exact benchmark for local conservative dynamics: the aggregate two-state hub relaxation would miss the leaf-mode bottleneck and its low-temperature slowdown. The mathematical value is the uniform and sharp classification, not the small numerical gain in the example or rediscovery of Boolean spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
