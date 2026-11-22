# Self-review

## Correctness — PASS
The theorem states the full positive-parameter domain and fixes which kernel mass is evaluated. Periodic variation of constants yields two boundary identities and the exact average formula; the Poincaré contraction ensures uniqueness. The key nonstandard step is the global inequality \(H(x+y)>H(x)+H(y)\), deduced from \(\sinh z>z\), so numerical monotonicity is not substituted for a proof. Taylor expansions and a continuous strict-limit argument give the unique cutoff, while a direct per-period integral produces the negative Floquet exponent. Exact algebra and separate numerical integrations are executed in `checker.py`; finite checks are not infinite proofs.

## Originality — PASS (bounded comparison)
The initiating 2026 study proves an equivalence under stationary waiting-time distributions and does not cover periodically changing removal hazards. The 2023 general time-dependent branching-process paper can represent this kernel, but the inspected introduction, construction and incidence equations do not themselves state the strict two-rate mean-mass monotonicity and unique season-length crossing alongside a fixed negative Floquet exponent. The older periodic-demography literature already supplies background on scalar Floquet thresholds; that background is **not** claimed as new. Search comparisons across terminology for time-varying recovery hazard, integrated infectious survival, average renewal kernel, and switching-period crossover found no exact dominating claim in the checked record. Closest research records address seasonally forced contact, vaccination timing or multi-stage population calendars rather than this survival-kernel assertion. Priority remains limited by unindexed historical sources and a relevant periodic-demography article not fully accessible.

## Value — PASS
A fixed pair of biological recovery conditions with a fixed mean removal rate produces a strictly variable *mean backward kernel mass* as the switching timescale changes. The exact unique crossing demonstrates how an intuitively tempting average-of-index threshold can disagree with the true linear infection growth, without incorrectly challenging a stationary-case equivalence theorem. This is a structural diagnostic for nonstationary renewal interpretation and a reproducible analytic benchmark; it is not an empirical or probabilistic outbreak forecast.

## Closest literature and residual limitations
- Goldwasser, Tibshirani, Bilinski (2026), arXiv:2606.15397, §§2–3: stationary mean-duration equivalence; calendar-changing recovery rate excluded explicitly.
- Pakkanen et al. (2023), DOI:10.1007/s00285-023-01958-w, introduction and §§2–3: general time-varying renewal/branching apparatus; not an exact two-season threshold statement in inspected material.
- Ward, Brown and Oleson (2023), DOI:10.1002/bimj.202100401, §2.3: infectious-duration-dependent reproduction definitions; different question.
- Greenhalgh and Dumas (2023), DOI:10.1016/j.idm.2023.11.007, §2.2: potentially periodic **forward** mean residual waiting time satisfying a different hazard differentiation identity; not the backward infectious-survival age integral or exact two-season monotonicity.
- *The basic reproduction number in epidemic models with periodic demographics*, DOI:10.1080/17513750802304893: potentially relevant earlier periodic theory, full content not read; cannot rule out a historical equivalent.

The backward kernel mass is not assumed to equal either forward case reproduction or a correct nonautonomous spectral invasion number; the example instead exposes why one must not mistake its period average for the latter. Self-review do not establish priority definitively, and do not constitute independent assessment.

Self-review: passed. Independent audit: not yet performed.
