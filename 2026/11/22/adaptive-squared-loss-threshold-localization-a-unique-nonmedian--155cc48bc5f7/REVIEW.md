# Scientific review: adaptive noisy threshold localization under squared loss

## Correctness (PASS)

For a uniform target and independent symmetric bit-flip noise, the conditional posterior after a fixed midpoint question is a two-step constant density. Direct moment integration gives the second-query variance-explained expression. The exact positive-factor mirror comparison reduces optimization over every possible second threshold to the half-interval beyond the midpoint. The stationary derivative has the sign of the explicitly displayed cubic. Its Bernstein coefficients have exactly one sign variation; Descartes' rule then proves a unique interior maximum. Evaluation at the posterior median establishes a strictly nonmedian squared-loss optimum. The exact four-response moment formula for a completely arbitrary nonadaptive threshold pair gives a uniform weak-channel expansion; compactness and unique leading optimizer establish the sharp fourth-order comparison. The packaged `verify.py` independently performs 3,743 finite checks. Analytical proof, not finite testing, supports the quantified statements.

## Originality (PASS, with risk)

The closest publicly deposited mathematical result, *Noise-calibrated thresholds for two parallel binary location queries* (2026; see References in RESULT.md), optimizes **simultaneously fixed mirror-symmetric** thresholds and explicitly excludes adaptive designs. Its formula does not imply the feedback-dependent unique nonmedian follow-up or the fourth-order advantage against **all** parallel pairs. Jedynak–Frazier–Sznitman analyze entropy loss, where noisy posterior median sampling is optimal, which is genuinely a different loss function; the demonstrated strict nonmedian inequality precludes transfer of that optimizer to squared loss. Variani et al. develop nonadaptive dyadic policies and asymptotic mean-square rates. Zhou–Hero 2019/2020 derive excess-resolution-probability bounds and finite-blocklength approximations, not the present two-query squared-error optimum. The explicit 2019-09-27 preprint is the motivating dated source. Search cannot conclusively exclude all earlier exact finite-horizon Bayesian experimental-design calculations, so historical priority remains a nontrivial qualification.

## Value (PASS)

Noisy binary search is a natural finite-budget sequential estimation problem. Its standard posterior-median/entropy rule can be strictly inferior for the natural operational objective of mean-square localization error. The theorem identifies the unique risk-optimal second threshold, quantifies the mismatch for every nondegenerate noise level, and proves a sharp adaptivity advantage over every nonadaptive pair despite the first midpoint being fixed. This is a structural boundary between two statistical loss functions plus a quantitative finite-horizon feedback gain, not merely a restatement of an integration formula.

## Limitations and independent verification

The first query is fixed at the midpoint, so global optimality over all adaptive two-question policies is **not** claimed. The adaptive-versus-best-nonadaptive gain is asymptotic as the channel approaches total noise, not an asserted positive gap for every channel contrast. Both bits have identical independent known error rates and the target prior is uniform. The finite verifier cannot prove the infinite parameter-range claims, and a separate independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
