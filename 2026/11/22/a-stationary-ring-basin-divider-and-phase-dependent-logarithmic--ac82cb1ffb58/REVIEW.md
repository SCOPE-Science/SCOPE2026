# Scientific review of the stationary-ring theorem

## Correctness — PASS (self-review)

The origin of all equations is fixed explicitly to the published mass-action polynomial system at \(\mu=32\). The critical identities are the exact radial and angular equations in RESULT.md (4), independently recomputed by the accompanying checker. The sign intervals prove the global (but disk-restricted) dynamics with full quantifiers and no finite-simulation inference. Fourier expansion of the exact physical-time angular quadrature yields the two closed periods. The normal variational equation gives the Floquet multipliers without conflating tangential rates. Cancellation of mobility in \(d\theta/ds\), a smooth angular primitive, and uniform reciprocal-speed bounds prove the phase-sensitive logarithmic exit law and its bounded remainder. The checker succeeded with `TWO_CYCLE_BASIN_CHECK_OK`. Remaining limitation: the theorem does not address outside-disk initial conditions, \(\varepsilon=0\), or stochastic trajectories.

## Originality — PASS within the inspected published sources

The originating manuscript [1] has the exact same field and identifies its two concentric cycles at \(\mu=32\); the cycles and their attracting property are prior, not the contribution. Reading its original equations (5.13)–(5.19), Theorem 3 and Lemma 13 established that it does not provide an entire equilibrium-ring census, the exact full-disk basin divider, the evaluated original-time period/multiplier pair, or the uniform angularly dependent first-exit coefficient. An exact-match semantic comparison with nearby mathematical records found a same-system four-oval analysis for \(\mu>337/9\), a high-coupling four-oval limit, and a different completed nested-oval field; none implies the equilibrium-ring clock at \(\mu=32\). Gasull and Giacomini [2] develop general algebraic-curve methods but do not evaluate this ninth-degree original-time flow. The overlap search is not proof of universal novelty; an unindexed equivalent treatment remains a real publication-priority risk.

## Value — PASS

The phase transition between two attracting chemical cycles is governed by a *continuum* of stationary states, and the physical-time delay depends on the initial angular composition even at fixed radial displacement. The explicit coefficient, exact basins, and contrasting cycle periods and spectra characterize a natural symmetry value chosen in the original source, not an arbitrary numerical slice. This provides reproducible quantitative observables not supplied by a mere existence theorem; no downstream theorem or global positive-quadrant phase portrait is claimed.

## Sources and limits

[1] Craciun–Erban (2024), https://arxiv.org/abs/2406.05057, equations (5.13)–(5.19) and Lemma 13(iv).

[2] Gasull–Giacomini (2023), https://doi.org/10.1007/s12346-023-00746-7, algebraic invariant-curve techniques.

Closest indexed counterparts are described explicitly in AUDIT.json; their subject matter is compared by implication, not their titles alone. Findings of independent reviewers are not asserted.

Self-review: passed. Independent audit: not yet performed.
