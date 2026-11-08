# Scientific review

## Correctness
**PASS.** The orthogonal-column and fixed-noise assumptions imply an exact radial recurrence without probabilistic or asymptotic approximation. At unit relaxation this map is an involution. Above one, normalization yields a strict contraction of the absolute logarithmic radius error, proving global attraction; differentiation and exact algebra give the local rate and its quadratic exception. The midpoint identity gives recovery of the least-squares solution. The symbolic/exact arithmetic verifier and direct vector tests corroborate the proof but are not substituted for it.

## Originality
**PASS, subject to stated historical-priority risk.** Actual searches compared the 2026 extended normal-equation paper, the original consistent-equation surrogate-hyperplane paper, the sparse surrogate-hyperplane update, the extended least-squares method, fixed-noise Kaczmarz and related published research records. The former establish convergence for different algorithms or the consistent case, while this claim identifies all nonoptimal initial trajectories of the specifically defined *unextended* residual map on an entire orthogonal-column family, the global relaxation bifurcation and the special quadratic false attractor. No covering claim was identified in the available material. The complete 2026 and 2023 papers were not accessible, so exact historical priority is not certified.

## Value
**PASS.** This is a natural best-conditioned test family for inconsistent data. It rigorously demonstrates that an unextended surrogate projection can turn fixed residual noise into nonvanishing oscillation, and that a seemingly superior quadratic stabilization rate can attract to the wrong solution. The exact error radius quantifies noise amplification, while adjacent averaging gives a limited, explicit recovery mechanism. It helps explain the mathematical purpose of extended correction schemes without conflating their guarantees.

## Boundaries and risk
The result addresses a defined fixed-data unextended map, not the double/triple extended algorithms. Its complete-dimensional guarantee is restricted to orthogonal columns with a common norm and \(1\le\omega<2\). Earlier unavailable full texts may contain equivalent special-case observations. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
