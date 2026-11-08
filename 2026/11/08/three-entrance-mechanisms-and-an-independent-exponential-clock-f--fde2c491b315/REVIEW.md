# Review of the conditional deep-excursion law

## Correctness — PASS

The interval partition is preserved **conditionally on the visited shell**, including the nonlocal geometric reset from the top shell. The finite target-shell hitting probability solves a two-point biased-walk recurrence with its boundary conditions. The exact marked decomposition separates the contracting entry, internal geometric-reset entries, and immediate deep overshoots. Three geometric-series limits supply the stated regime-specific distributions, including their normalization and tightness. Regeneration at shell zero is exact under the uniform conditional distribution; finite return-time second moment supports the marked renewal argument establishing independence of the exponential waiting clock. The accompanying exact-rational checker independently solves small finite-state hitting-time systems and verifies finite sums and limiting profiles.

## Originality — PASS within inspected sources

Yan et al. (arXiv:2308.09269, 2023) established the map and stationary/invariant-density context. Monthus (arXiv:2409.19999v2, Sections III--V) established its dyadic Markov representation, geometric resets, stationary three-regime density, mean first-passage formula, and unmarked excursion decomposition. These are expressly acknowledged as prior work. The present result is **conditioned on a successful excursion to an increasingly deep shell**; it describes the location and type of that successful excursion's first step and its joint distribution with the first rare-event waiting clock. Those conditional marked distributions and three distinct entrance mechanisms were not found in the inspected primary text or semantically searched research records. Absence from inspected texts is not proof against unindexed equivalent derivations; the latter remains the main priority risk. Previously available claims address Pelikan-map covariance, shell-index fluctuations, and a complete first-return generating function, but not the successful high-shell excursion initial-depth mark.

## Value — PASS

The three regimes explain *how* an exceptionally deep visit is generated, not merely how often the event occurs or how much stationary mass occupies a deep shell. Below the density threshold, deep excursions build from bounded starting depths against drift; at the threshold, the successful starting depth becomes macroscopically delocalized; above it, an immediate jump on the target scale dominates. The rare-event waiting clock separates asymptotically from this geometric mechanism. This is a complete conditional classification for a natural return event in a standard random interval map, and a pathwise interpretation of a previously known stationary transition; it is not offered as a new stationary-density or mean first-passage formula.

## Limitations and residual risks

The statements are annealed, start uniformly on the upper dyadic shell, and hold for fixed probabilities strictly between one half and one. No quenched or deterministic-initial-point conclusion is claimed. The general exponential waiting-clock mechanism is classical; specificity lies in the threshold-dependent conditional mark laws. Unindexed renewal/conditioned-excursion treatments of this simple model could contain equivalent results. The 2026 quasi-stationary study was encountered in discovery but was not fully read; it addresses a distinct killed variant, so this is a limited priority risk rather than proof of non-overlap. A separate expert or independent mathematical audit is still needed.

Self-review: passed. Independent audit: not yet performed.
