# Mathematical review

## Correctness
**PASS.** The zero-at-start normalization is fixed explicitly. Strict inverse-trace convexity and injectivity of the edge-weight Laplacian give uniqueness over all symmetric stochastic chains, not only invariant chains. The full graph automorphism group reduces the optimizer to three edge classes. The spectrum decomposes into nongateway contrasts, a symmetric quotient and an antisymmetric quotient, yielding the displayed rational Kemeny formula. Both stochastic constraints saturate by strict objective monotonicity, and a one-dimensional positive second derivative gives exactly one optimum. The rescaled objective proves its limits by coercivity and uniform convergence on compact subintervals. `verify.py` independently confirms the spectral formula using exact rational matrix inverses and checks the stated benchmark and asymptotic constants.

## Originality
**PASS on inspected evidence, with residual risks.** Boyd–Diaconis–Xiao (2004) optimize SLEM rather than Kemeny's constant. Patel–Agharkar–Bullo (2015) provide the general convex Kemeny design framework and trace identity, not an explicit analytical equal-clique-barbell optimizer or its limiting bridge allocation. Breen et al. (2019) give barbell formulas for a fixed degree-proportional random walk, not a freely adjustable uniform-stationary one. Durastante–Gnazzo–Meini (2026) discuss reversible Kemeny perturbations and numerical optimization but do not state this graph-family classification in the inspected treatment. Closest indexed graph-family results address different objectives (fastest mixing or leader placement) or graphs. Searches cannot exclude an unindexed equivalent closed form, and the general convex program can derive this after nontrivial specialization.

## Value
**PASS.** A single bridge is the bottleneck in two dense communities. The theorem supplies the complete unrestricted equal-size optimizer for every clique size, proves that the optimal gateway devotes a nonzero constant fraction of probability to the bottleneck even as each clique grows, and quantifies an unbounded (linear-in-clique-size) mean-hitting-time regret for standard maximum-degree weighting. This is a structural benchmark, not a claim that the general optimization algorithm is new or that the result holds for arbitrary unequal communities.

## Limitations
Kemeny's constant uses the convention that the destination contributes zero time when it equals the starting node; an alternative convention adds one. Assumptions require symmetry, uniform stationary distribution, equal clique sizes, one bridge and free self-loops. Numerical testing covers finitely many instances; the all-size result is analytic. Specialized prior tables may remain undiscovered, and independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
