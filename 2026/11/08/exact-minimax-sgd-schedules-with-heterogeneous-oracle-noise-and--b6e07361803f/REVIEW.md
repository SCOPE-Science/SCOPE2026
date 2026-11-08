# Scientific assessment

## Correctness — PASS

The sharp performance functional follows by variance-by-variance substitution in the nonnegative interpolation certificate of Grimmer–Shen (arXiv:2610.42048v1, Section 2, especially Lemma 2.2). A separately constructed separable Huber problem attains the bound for every sign realization with the claimed dimensional threshold; the original conditional variance bound remains satisfied. The unique optimum follows from strict convexity/coercivity of quadratic perspectives, the interior derivative conditions and one monotone scalar root. The adjacent-step threshold and high-noise limit are algebraic consequences, with the rational two-step example checked exactly. The packaged standard-library checker passes 6,248 randomized and exact checks. Risk: the inherited nonnegative certificate is a substantive external lemma; its hypotheses and the way its noise term enters were inspected, not independently reproved from first principles.

## Originality — PASS (qualified)

The motivating Grimmer–Shen paper has a shared bound \(\sigma^2\), whereas this theorem resolves separately bounded \(v_i\), gives an exact optimizer recurrence for all horizons, and proves a sharp adjacent-step reversal criterion and arbitrary high-noise ordering. Bai–Zhou optimize two steps in a different strongly convex class and objective metric. The closest indexed mathematical results concern different optimizers, stationary variance or step stability and do not imply these conclusions. Public scholarly keyword and full-text comparisons did not expose an exact equivalent. Risk: the weighted Huber proof is a direct structural extension of the motivating proof, and prior unpublished or unindexed heteroscedastic scheduling calculations may subsume some or all of the new classification. The novelty claim does not include the general convex interpolation method.

## Value — PASS

Knowing that the exact finite-horizon minimax schedule can *increase* after a variance drop (for example when late-stage mini-batches are larger) changes a practically meaningful learning-rate design conclusion. The recurrence is constructive for arbitrary finite horizons, and the local condition is both necessary and sufficient; inverse-variance asymptotics permit arbitrarily many schedule reversals. The distinction is not a renaming or a single numerical example. Risk: the theorem is a fixed-horizon optimization under known deterministic variance ceilings, not a performance guarantee for adaptive procedures or integer-valued batch allocation.

## Closest literature and scope

The indispensable antecedent is Grimmer–Shen (2026), whose uniform-noise minimax result and extremal Huber device are credited explicitly. Bai–Zhou (2026) studies strongly convex two-step squared-distance bounds under common noise; Attia et al. (2025) provide smooth-interpolation last-iterate rates rather than sharp adversarial heteroscedastic finite-horizon optimization. The global minimax statement is conditional on computed steps remaining in the short-step range. Independent validation and historical-priority certification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
