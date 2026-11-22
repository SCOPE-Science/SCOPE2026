# Scientific review

## Correctness — PASS

The lower-record joint density reduces to a single exponential factor involving the last record; direct maximization under each candidate fixed shape gives the exact profiled likelihood ratio. Transforming by the true inverse-Weibull tail exponent turns lower records into upper exponential records. Conditional on the last transformed record, earlier values are uniform order statistics, giving an exact integer-shape Gamma sum of logarithms. The finite probabilities are Gamma tails, and sharp Poisson-tail/Stirling estimates establish the asymptotic prefactors and the identity of the two error exponents. The diagnostic code checks rational profile algebra and seeded record simulations; the infinite statements are analytically established.

## Originality — PASS (qualified)

Tripathi, Singh and Singh (2022) define the same lower-record comparison and estimate its operating characteristics by simulation, but do not provide its exact Gamma distribution, finite power formula, or equal-exponent asymptotics. Their Eq. (20) is not the ratio implied by their likelihoods for three or more lower records; this is distinguished from their simulation implementation, which has not been inspected. Al-Duais (2021) treats inverse-Weibull scale estimation, whereas Shorrock (1972) treats the classical record-process structure, neither specifying this two-model profiled test. Targeted research-record and published-literature comparisons found no result that directly states or dominates the combined claim. The component exponential-record representation is classical, and undiscovered earlier applications remain possible; originality has not been independently established.

## Value — PASS

For a published model-discrimination procedure whose correct-selection probabilities were estimated with 30,000 simulated samples, the theorem supplies exact scale-free finite operating characteristics for every lower-record count and every pair of fixed inverse-Weibull shapes. It also gives a sharp shared error exponent and distinct prefactors, making sample-size and asymmetric-error comparisons quantitative. Correcting the printed lower-record likelihood-ratio simplification removes a consequential record-count dependency error. These are specific inferential results, not claims about unrelated record procedures or the reliability of unpublished code.

## Limits and closest literature

The result concerns lower records only, with independent observations, two preassigned shapes, separately fitted positive scales, and a unit decision threshold. It does not cover upper-record likelihoods or prove global minimax optimality. The 2022 article's published equations and simulation table, the relevant full-text sections of Al-Duais (2021), and the available record-process description by Shorrock (1972) were compared. Historical priority remains qualified by possible less discoverable work and unavailable full text of some classic references.

Self-review: passed. Independent audit: not yet performed.
