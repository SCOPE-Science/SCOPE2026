# Scientific review

## Correctness — PASS

The exact two-class pseudogradient has a strictly convex quadratic potential for all positive slopes. The change of variables \(L_i=S_i\), \(H_i=S_i+2C_i\) turns the potential into two independent Beckmann potentials. The only additional cross-class constraints, \(L_i\leq H_i\), hold automatically because parallel affine Wardrop flows are coordinatewise nondecreasing with total demand. This proves existence, uniqueness and the claimed formulas including empty class, tied-intercept, and road-activation boundaries. The two-road efficiency formula follows by explicit water filling and completing a positive quadratic square. An exact rational checker passed 2,100 multi-road equilibrium instances and 1,344 two-road efficiency instances; the infinite claim rests on the proof, not on these finite tests.

## Originality — PASS on inspected evidence

Toso et al. (arXiv:2408.15742) prove general strong-monotonicity uniqueness and, for parallel networks, monotonicity of total traffic cost with fleet fraction. Their inspected mathematical statements and proofs do not give a two-Wardrop-demand decoupling. Battifarano and Qian (2023, Sections 4–5) give analytical parallel-network results conditional on preserving the user-equilibrium assignment, plus critical fleet-size conditions; they do not provide this unconditional exact assignment formula. Nilsson et al. (2018, Sections II–III) establish the game and a general solver, without this decomposition. Published research-record similarity searches returned different stochastic-road, Braess, network-allocation and exclusion-process claims, none an implication of the new identity. The source model and basic convex-potential machinery are established prior art, not claimed as new. Residual priority risk remains from older general multi-class equilibrium theories and other obscure affine specializations; absence in retrieved sources is not a proof of first discovery.

## Value — PASS

The identity replaces a coupled nonlinear-complementarity calculation by two scalar monotone water-filling problems and gives a complete exact solution for any number of parallel roads. It pinpoints precisely which roads each class uses at every fleet penetration and yields a sharp, nonzero plateau followed by an explicit quadratic efficiency improvement in the two-road model. The result addresses the precise fleet-share threshold question raised by Toso et al. It is more than a numerical instance or restatement of monotonicity: it is a general equilibrium representation that enables exact sensitivity calculations. No claim is made for nonlinear networks, field-realistic road capacities or deployment effects.

## Closest sources and remaining limitations

Toso et al. (2024), https://arxiv.org/abs/2408.15742; Battifarano and Qian (2023), https://doi.org/10.1287/trsc.2022.1189; Nilsson et al. (2018), https://doi.org/10.1109/CDC.2018.8619411. These contain the same game, partial parallel-road theory and generic solution methods, respectively. Broad older priority is not exhaustively excluded. The proof applies only to one OD pair, positive affine slopes and an own-fleet (not social) planner.

Self-review: passed. Independent audit: not yet performed.
