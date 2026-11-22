# Scientific review: exact entropic spectral gap for zero-temperature Ising friendship networks

## Correctness — PASS
The ground-energy minimization is independent across \(n\) frustrated triangles, yielding \(2\cdot3^n\) configurations. Each fixed-hub sector is a product of unit-rate three-vertex paths; hub flips couple only mixed configurations. Orthogonal symmetry sectors have gap at least one, while the antisymmetric hub mode maps exactly to a rate-two rank-one perturbation of independent two-state bits. The determinant lemma, spectral weights and the binomial inverse-moment estimate rigorously establish the unique root and its sharp asymptotics. Both exact integer/rational and independent finite-matrix numerical checks pass. The computation is a test of the proof's reductions, not an infinite proof.

## Originality — PASS on the bounded examined record
Published comparisons show that Kim, Kim and Lee (2003) examine a two-dimensional triangular antiferromagnet using Monte Carlo; Ismail and Salem (2003) analyze small triangular spin clusters; Berger et al. (2003) provide general bounded-degree tree/hyperbolic results; Chen et al. (2024) treat antiferromagnetic spin systems in a uniqueness regime. None of these inspected statements implies the friendship-graph rate-one ground-state secular equation or its exact exponential coefficient. Searches of public indexed research for the windmill/friendship graph, entropic bottleneck, alias triangular cactus, all-leaf coupling and binomial spectral formula identified no covering statement. Exact claims and implications, rather than just titles, were compared. The full Kim article was not available, and a priority risk remains from unindexed results.

## Mathematical value — PASS
The theorem isolates a natural macroscopic entropic metastability mechanism in a fully frustrated graph family: two rapidly mixing sectors communicate only through \(2^n\) configurations among \(3^n\) sector states. It determines the complete sharp spectral gap as the root of an explicit scalar equation and a nontrivial first-order finite-size correction. This is substantially more informative than a generic conductance bound. It does not claim a positive-temperature result or a full spectrum.

## Scope and residual limitations
The precise dynamics is rate-one zero-temperature *Metropolis* restricted to the ground manifold; a heat-bath convention would rescale neutral-spin kinetics. The foundational 2003 triangular-lattice paper was available in abstract only, . Historical priority and independent validation remain unresolved.

Self-review: passed. Independent audit: not yet performed.
