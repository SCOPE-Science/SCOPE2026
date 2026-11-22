# Scientific assessment

## Correctness — PASS
The capture objective is reconstructed by partitioning uniformly distributed event-start phases into live windows and silent gaps; strictly positive event-duration density implies strict concavity of the gap benefit. Equal gaps and full spending follow by strict Jensen and a positive marginal-improvement integral. The relaxed count envelope has explicit negative second derivative, and the adjacent-count difference is strictly increasing in monitoring slack. Its two endpoint signs prove a single switch for each pair when setup overhead is below mean event duration, and strict count concavity forces ordered transitions and exactly adjacent ties. Mean-overhead equality belongs to the one-window regime because the derivative is *strictly* negative at finite horizons. The included independent-of-packaging Python checker supplies 67,326 supplementary assertions, not an infinite proof.

## Originality — PASS on inspected evidence, with historical limitations
Michel et al. (2024), DOI 10.1121/10.0025545, investigates blue whale listening duty cycles experimentally and does not solve an energy-equivalent per-activation count optimization. **Closest primary:** Yau et al. (2010), DOI 10.1145/1824766.1824774, Theorems 4.2 and 5.2 give a general survival-integral formula for finite-duration event capture, which the new proof acknowledges and does not claim as original. Sections 5–6 optimize multi-location sensor schedules and examine travel overhead, not the single-recorder, fixed-budget universal mean-duration frontier or all consecutive discrete count thresholds. Targeted searches of published mathematical and monitoring literature did not identify a theorem covering these exact statements; unsuccessful searches do not prove novelty, and an unexamined earlier sensing/surveillance optimization theorem could dominate them.

## Value — PASS
The mean-duration boundary distinguishes regimes in which fragmentation of live recording effort can never pay from regimes with a nontrivial, predictable ladder of optimal activation counts. The universal boundary works for all positive continuous finite-mean event-duration laws; the optimal gap and transition locations retain model-dependent details. This is a motivated energetic design result for a first-overlap event-detection objective, and it exposes an explicit parameter whose physical relevance is testable; it is not a mere reparameterization of the existing survival-integral formula. The model is theoretical, not a calibrated prediction for blue whale monitoring, where event detectors may require complete calls.

## Closest comparisons and limitations
- Yau et al. 2010 Theorems 4.2, 5.2: capture formula already known; additional startup-cost constraint and universal count classification are the intended new claims.
- Michel et al. 2024 pp. 2538–2548: empirical duty-cycle data; its full-call detection differs from the idealized overlap rule.
- Teixeira et al. 2024: operational/ecological monitoring context, not the mathematical frontier.
- Historical priority remains provisional across older surveillance, reliability, and renewal scheduling literatures. The finite verifier checks calculations, not novelty or all infinite cases.

Self-review: passed. Independent audit: not yet performed.
