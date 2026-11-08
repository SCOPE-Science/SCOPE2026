# Review of radius-order comparison and smooth sharpness

## Correctness — PASS

The ball-constrained exact minimizer satisfies a unique scalar-multiplier KKT equation. Its coordinate solution is increasing in its input and decreasing in the multiplier, while its displacement is increasing in both. Comparison of multipliers proves order preservation at fixed radius and monotonicity in radius, hence trajectory-wise dominance under independently chosen ordered schedules. Full nonterminal ball moves decrease the transformed coordinate \(\ell_1\) norm by at least the radius. For smooth sharpness, a feasible trial point annihilates the stiff coordinates; normalizing its cost by the next stiffness and taking the singular hierarchy limit proves that exactly one further coordinate vanishes at each step, giving \(N_1=d\) for small positive stiffness ratio. The proof establishes infinite-dimensional-family claims without relying on finite numerical checks. The included checker passed 960 trajectory comparisons and the quadratic dimension witnesses from two through seven.

## Originality — PASS, qualified

The nearest same-iteration work is Richtárik–Li (arXiv:2609.35147v1), which proves general convex finite termination and supplies a nonsmooth/polyhedral dimension-sharp family and a general-radius nonmonotonicity example. It does not establish the present coordinatewise radius-order comparison for orthogonally separable objectives or a smooth strongly convex dimension-sharp family. The earlier Gruntkowska–Li–Rane–Richtárik work (arXiv:2502.02002) proves universal convex bounds but not the new comparisons or lower example. Carmon et al. (arXiv:2003.08078) study an accelerated ball-oracle method. Semantic published-claim searches returned related but noncovering methods. Priority risks remain for older isotone resolvent and trust-region literature; absence of a search hit is not proof of novelty.

## Value — PASS

General ball-proximal iteration can exhibit paradoxical radius effects, so a sufficient structural regime in which larger radii can never hurt is relevant to exact trust-region oracle selection. The exact smooth-SPD attainment demonstrates that the dimensional term cannot be blamed on nonsmooth polyhedral geometry alone and clarifies the scope of the generic complexity theory. The contribution is a structural comparison and a natural sharpness boundary; it does not imply a practical oracle-cost improvement.

## Limits

Only exact ball-oracle steps on orthogonally separable strictly convex differentiable objectives are covered. The smooth worst-case family becomes ill-conditioned as the stiffness ratio vanishes. The historical comparison is bounded, and no independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
