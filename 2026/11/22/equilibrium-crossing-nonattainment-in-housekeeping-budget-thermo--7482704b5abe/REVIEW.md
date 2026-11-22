# Self-review

## Correctness — PASS

The universal inequality is Cauchy–Schwarz combined with the one-dimensional antiderivative/total-variation bound. Equality forces positive monotone velocity proportional to \(\sqrt{\sigma/\zeta}\). At an interior \(C^2\) nonnegative zero, this is bounded above by a constant times distance to equilibrium, so a finite-duration crossing contradicts Grönwall's inequality. Regularization by \(\sigma+\varepsilon^2\) gives admissible finite-time protocols of exactly the prescribed housekeeping budget and with excess energy approaching the lower bound. H¹ compactness after rescaling the time interval proves that every minimizing sequence has divergent duration. The nondegenerate quadratic zero gives a logarithmic divergence. Explicit three-state rate perturbation verifies \(\sigma(\lambda)=\lambda^2+O(\lambda^3)\), \(\zeta(0)=2/27\). The standard-library checker passed. The slow-driving approximation itself is not an exact finite-rate theorem.

## Originality — PASS (qualified)

Sugie, Loutchko and Kobayashi, *Optimal Driving between Nonequilibrium Steady States under a Dissipation Budget*, arXiv:2611.14891v1, establish the positive-housekeeping weighted-length inequality and positivity-dependent entropic-time equality, but their analysed nonzero-budget paths are in positive-housekeeping regions; their equilibrium-only discussion has zero stationary budget. The new boundary case crosses an isolated EPR zero with a strictly positive fixed budget, separating an unattained infimum from the attainable optimal protocol. Kamp and Proesmans, arXiv:2506.14416v1, consider an inequivalent fixed-duration total-EP functional. Semantic searches of published mathematical records and accessible local claims found related results on entropy-optimal flows and dissipative Markov rings, but no covering implication. Literature search cannot rule out an unindexed singular thermodynamic-length or variational-control treatment; novelty therefore has residual priority risk.

## Value — PASS

An equilibrium point embedded inside a driven nonequilibrium control path is physically unavoidable when changing the sign of a cycle affinity, even when end states dissipate. The result identifies the sharp failure of finite-time optimizer existence, an exact attainable versus unattainable threshold in the order of the housekeeping zero, and a logarithmically diverging near-optimal duration. A concrete irreducible three-state continuous-time Markov generator demonstrates that the singularity is physical rather than an artificial metric choice. It clarifies a resource-budget frontier in a new stochastic-thermodynamic geometry.

## Closest literature, scope and risks

- Sugie, Loutchko and Kobayashi (2026, arXiv:2611.14891v1): base functional and positive-rate inequality; no isolated-zero positive-budget crossing theorem in the inspected HTML manuscript.
- Kamp and Proesmans (2025, arXiv:2506.14416v1): finite-duration, total-EP functional, not the asserted free-duration stationary-housekeeping-budget problem.
- Residual risks: mathematical variational optimal-control literature may contain an equivalent general singular-weight theorem; a full independent search/review remains necessary.
- The finding is restricted to a leading-order friction model. No exact master-equation optimum, multidimensional rerouting criterion or independent certification is asserted.

Self-review: passed. Independent audit: not yet performed.
