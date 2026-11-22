# Mathematical review

## Correctness — PASS

The at-most-three bound uses an analytic classification, not a simulation. Each invariant pure-adherence face contains at most one potentially stable equilibrium, since a fixed-adherence SIRS subsystem has exactly one stable epidemiological state (apart from its nonhyperbolic threshold). A disease-free state with mixed adherence has a strictly positive behavioral eigenvalue. On the positive-endemic mixed branch, \(G''<0\) exactly; the previously established Jacobian determinant identity makes \(G'<0\) necessary for stability, which at most one root can satisfy. The witness gives six exact rational biological equilibria, and its three sinks are confirmed by strict rational Routh–Hurwitz inequalities. The standalone checker recalculates these algebraic certificates. Nonstandard steps are proved in RESULT.md; the finite checker is confined to its witness.

## Originality — PASS (bounded literature assessment)

The exact originating model and its published supplement already include the scalar response \(G\), equilibrium formulas, a determinant sign identity, and qualitative bistable outcome diagrams. None of those pieces is claimed as new. The assessed claim is the universal **sharp upper bound of three attracting equilibria** together with a strictly feasible **simultaneous three-sink exact rational realization** under the full conformist, waning-immunity model. The inspected source's main text and supplement do not state this bound or provide this exact realization. The 2023 Saad-Roy–Traulsen model and the 2026 Martin–Castella–Hamelin SIS model differ in infection/behavior mechanisms and do not imply the claim; the latter was accessible only in abstract. The related public mathematical results on no-conformity permanent-immunity global convergence and on finite-horizon Poisson masking bistability address structurally different subclasses. Comparison of these statements and implications supports bounded originality, not exhaustive priority.

## Value — PASS

A maximal attractor-count theorem and a full exact rational witness clarify how several behavioral and epidemiological regimes can be locally robust under identical conditions. The result answers a structural question motivated by the paper's coexistence maps: whether non-adherence, partial adherence and full adherence can all locally attract at once, and what is the maximum number. Its significance lies in a reproducible classification boundary, not in a tiny numerical improvement or an unsupported policy extrapolation.

## Limitations and risks

Only locally exponential stability of equilibria is established, not global convergence, basin sizes, or absence of periodic orbits. The statement depends on the specified linear social-conformity payoff and homogeneous behavioral SIRS equations. The related 2026 SIS article's full text could not be inspected, and other historical literature may contain a broader bound. Independent review and external validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
