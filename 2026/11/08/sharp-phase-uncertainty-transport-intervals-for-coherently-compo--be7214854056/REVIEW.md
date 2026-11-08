# Scientific review

## Correctness (PASS)
The transport formula is taken verbatim in substance from the motivating source, not reproved as new. The key additional steps are: calibrated-vector fibers are exactly left diagonal phase circles, because \(T_z=1-|b|\) and transverse components fix \(b\overline a\); the free left phase of the **previous** product controls the two-amplitude interference under the next multiplication while preserving its polar angle; this gives the exact angle interval; a continuous map of a connected compact phase torus makes this an exhaustive interval and yields the distance recursion; and taking the norm of the source's vector gives \(F\). The endpoints and degenerate diagonal/antidiagonal coins are explicitly included. The packaged `verify.py` passed 16,593 finite diagnostics, but universal correctness rests on the complete analytic induction.

## Originality (PASS, qualified)
The most relevant source [1] explicitly derives the transport vector, its left-diagonal phase invariance, and geometric Parrondo criteria. These are credited, and the present result does not merely rename them: it gives an all-length *inverse-calibration range*, not the transport of already specified products. Reference [2] supplies established composite-pulse phase steering and is a close method comparison, yet its target-specific robustness sequences do not state this complete closed-interval inverse transport classification. Published indexed claims and available prior local findings were also searched by source, transport-vector aliases, SU(2) phase control, reachability, and product equivalences. No direct coverage was found. This does not establish global uniqueness; a more general spherical-reachability theorem may imply the exact angle recursion.

## Mathematical value (PASS)
Transport-vector calibration is explicitly proposed as a compact geometric descriptor of asymptotic quantum-walk motion in [1]. The finding quantifies precisely what information such complete individual calibration fails to predict under coherent composition. Its computable sharp envelope, feasible full-transport/zero-transport criteria and full-width three-coin example are structural observability boundaries for quantum-walk control, not an arbitrary finite numerical case or an already given formula.

## Scope and residual risks
Only independent hidden phases, one-dimensional two-state homogeneous coin composition, and initial-state-optimized drift are covered. A specified initial coin state, alternating full steps or correlated phase constraints require different analyses. The priority of all related rotation-controllability results remains an open literature risk; no independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
