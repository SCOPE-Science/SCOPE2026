# Scientific review of two-camera Gaussian coverage

## Correctness — PASS

The conditional at-least-one detection probability integrates exactly over a planar normal activity centre, producing a difference of two Gaussian exponentials in the squared half-spacing. The separation derivative has a monotone exponential ratio and at most one positive crossing. The critical-width optimization reduces to a log-rational equation whose derivative has an exactly factored quartic numerator with a single positive root. The rare-baseline-detection limit is derived from that same unique equation. The standalone `verify.py` and its certificate were replayed from their delivered sources and passed 11,156 tests; no finite sampling is used as a substitute for the analytical global proof.

## Originality — PASS, with provisional priority

Litvak et al. (2008, PDF pp. 89–90) prove an overlap criterion for hard one-dimensional sensor intervals; Rowcliffe et al. (2011) calibrate detector response; Sun et al. (2014) investigate multi-trap estimation performance; Efford and Boulanger (2019) give the general expected-detected-individuals integral. Their mathematical statements do not directly establish the present planar Gaussian symmetric-pair co-location classification, unique peak of the *optimal physical spacing* with detector width, or low-sensitivity scaling. The closest published finite-transect published-finding corpus theorem optimizes geometric decay over uniform discrete sites, not this response and spatial law. The 2019 general integral already subsumes the expectation identity, which is not asserted as new. Relevant facility-location and general probabilistic-coverage literature may contain unnoticed equivalent results. The 2008 report was publicly deposited on 2009-11-09; the original release day was not established.

## Value — PASS

The theorem distinguishes narrow-detector clustering, intermediate-range maximum separation, and wide-detector co-location, which cannot be inferred from a simple always-separate or always-cluster heuristic. It is motivated by distinct-individual coverage and a measurable detection width rather than an arbitrary numeric slice. Its explicit single-root law and rare-detection square-root scaling provide analytic design benchmarks. The result concerns only two symmetrically placed devices under a Gaussian habitat and independent Bernoulli detection; actual camera geometry, animal movement, false positives and abundance-estimator information are outside the model.

## Related work and limits

Primary sources and the checked mathematical theorem are listed in `RESULT.md`, and statement-level comparisons with original source locations appear in `AUDIT.json`. No independent scientific validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
