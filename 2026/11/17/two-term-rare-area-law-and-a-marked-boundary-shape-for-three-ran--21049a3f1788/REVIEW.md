# Review of the rare-area finding

## Correctness — PASS

The Gram-correlation density, orthant area identities, determinant factorization, Jacobian, uniform sine expansion, and Dirichlet moments are explicitly derived in `RESULT.md`. The exact arithmetic yields \(\mathbb E[g]=4/21\) and \(\mathbb E_h\sum T_i^2=29/55\), hence the relative second coefficient \(-7/330\). The disjointness of near-hemisphere events and the uniform density-ratio bound prove both the extreme tail and the marked total-variation convergence. A standalone checker reproduces rational coefficients and independent geometric/numerical diagnostics.

## Originality — PASS, with historical uncertainty

The full joint angular law is known and is **not** claimed as new. Finch–Jones provides polar-dual and perimeter distributions, and Philip's inspected manuscript provides densities and numeric evaluations, but neither inspected source states the two-term four-cell maximum tail or the full independent rare-area partition law with total-variation rate. Prior published records concerning the balanced area range, a pole-containing zero-cell perimeter, and near-maximal perimeter of random spherical vertex triangles address different regimes. The leading scalar asymptotic follows in principle by boundary analysis of known densities; its isolated evaluation is not the whole contribution. An earlier paper giving an equivalent endpoint expansion or marked limit would supersede the novelty claim; this remains a residual risk.

## Value — PASS

The asymptotic describes an actual extremal transition of a random spherical tessellation: one antipodal pair occupies almost half the sphere while the other three areas jointly vanish. The rare probability, the rational next correction, and the non-Dirichlet limiting partition quantify different aspects of the same geometric mechanism, and the conditional total-variation estimate permits finite-threshold rare-event approximations. This is motivated by cell-area extremes rather than an arbitrary sampled statistic.

## Scope and limits

Only three isotropic independent great circles and a near-hemisphere largest cell are covered. The numerical script does not independently prove the asymptotics. Independent review of proof and priority is outstanding.

Self-review: passed. Independent audit: not yet performed.
