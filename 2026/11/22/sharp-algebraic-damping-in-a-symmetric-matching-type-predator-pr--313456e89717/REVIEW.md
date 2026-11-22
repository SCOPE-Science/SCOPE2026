# Self-review

## Correctness — PASS
The exact four-equation reduction matches the published dynamics. The Lyapunov derivative is an exact identity; the LaSalle invariant-set test treats the null directions explicitly. The two-dimensional stable block has strictly negative real spectrum and the difference block has imaginary eigenvalues, so a quadratic center-manifold calculation is needed. Its harmonic transfer is invertible; time averaging of the entropy dissipation yields the complete constant \(1/(2uD)\). The symmetric subspace is the exact strong-stable manifold. SymPy confirms the symbolic identity and the unit-parameter rational value, with additional finite integrations. The proof does not infer an infinite-time statement merely from simulations.

## Originality — PASS (literature-bounded)
The closest full source, Costa–Czuppon–Forien (arXiv:2609.04834, Proposition 2.4 and Appendix A.2), proves coexistence convergence but neither its sharp polynomial contrast clock nor its parameter-explicit coefficient. The earlier Costa–Hauzy–Loeuille–Méléard paper (arXiv:1407.3069, §3) assumes positive-definite prey competition, not satisfied in the singular equal-competition system. Indexed critical-Hopf and four-species analogy records concern different dynamical systems; their rates do not imply this coefficient. Targeted indexed-science searches found no direct duplicate. One related full-text source and some indexed linked full texts could not be inspected, leaving a bounded priority risk.

## Value — PASS
The degeneracy in the very model of interest creates a nontrivial discrepancy between generic and exactly symmetric trajectories: slow universal oscillatory relaxation versus exponential total-population relaxation. The explicit, positive, parameter-dependent amplitude coefficient directly characterizes a natural unexplained timescale and is not supplied by global-attraction theory. This is useful for interpreting deterministic eco-evolutionary transients while making no unsupported stochastic-scale claim.

## Limits and comparison
The deterministic four-population coexistence family is treated with strictly positive populations; arbitrary networked predation, mutation during evolution, stochastic accumulation and uniform finite-population relaxation are not addressed. The general center-manifold principle is standard, but its algebraic transfer coefficient is specific to the modeled interaction. Partial third-party access does not establish absolute historical priority.

Self-review: passed. Independent audit: not yet performed.
