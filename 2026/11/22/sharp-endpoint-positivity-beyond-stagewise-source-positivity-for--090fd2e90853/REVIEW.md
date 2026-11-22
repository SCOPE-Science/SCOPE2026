# Self-review

## Correctness — PASS
The matrix-polynomial spectral reduction is exact for every real symmetric input with eigenvalues in the closed unit interval. The zero-crossing equations and derivative factorization give the unique least positive crossing at the radical constant. Descartes' rule ensures the fixed critical input is negative for every larger timestep; endpoint and stage source bounds are checked separately. Direct exact arithmetic independently verifies the key identities and a rational negative example. No numerical sample is used as an infinite proof.

## Originality — PASS, with historical priority limits
The 2026 primary source supplies the integrator and the same spectral matrix-cubic nonlinear source, but its positivity argument uses stagewise positive semidefinite forcing. The new assertion is the exact all-input completed-step threshold beyond that hypothesis, not the integrator formula itself. Literature on maximum-bound-preserving Allen–Cahn schemes typically gives stagewise sufficient restrictions or analyzes different stabilized/integrating-factor schemes. Closely related accessible full text was inspected and did not identify this sharp endpoint-only claim. The 2021 Applied Numerical Mathematics paper is a plausible but partly inaccessible prior source: its abstract was compared, but equivalent material could be present in the full text. Lack of a search match is not proof of novelty.

## Value — PASS
A published nonlinear positive-semidefinite experiment uses precisely this matrix-cubic source. Knowing the exact completed-step threshold instead of only the much smaller stagewise sufficient bound changes which timesteps may be justified for a single output, while pinpointing when positivity genuinely fails. The result is a complete natural scalar-spectrum classification, not an arbitrary computed example, and it exposes a practical distinction between intermediate and endpoint constraints.

## Limitations
This theorem does not imply repeated-step positivity, an upper spectral invariant, or safety for nonzero linear terms. The historical-priority search cannot exclude inaccessible or unindexed equivalent work. Exact checks cover the one-step polynomial and threshold, not other numerical schemes.

Self-review: passed. Independent audit: not yet performed.
