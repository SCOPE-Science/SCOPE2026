# Scientific review

## Correctness — PASS
The proof defines both probability measures, derives the exact cubic residual identity, and uses a quadratic discriminant and two interval-length formulas to obtain necessary-and-sufficient exceedance laws for every stated parameter and severity. The formulas include their strict endpoints, square-root asymptotics and sign-switch exclusion. The standalone checker corroborates exact identities and selected numerical probabilities, rather than being taken as a universal proof.

## Originality — PASS, with historical-priority risk
Hofmann's arXiv:2607.04993v1 (§§2.1–2.10) contains the same gradient map, a phase threshold and a state-space envelope. Chen et al.'s arXiv:2310.01687v1 (§2 and Appendix A) contains the equivalent residual map, global convergence and the uniform-residual phase threshold. Chen and Bruna's arXiv:2206.04172v1 (§4 and Appendix F) covers stable period-two behavior for a different parameter range. None of the inspected relevant primary statements supplies the two full relative first-loss exceedance distributions for all thresholds \(t\ge1\). Actual searches of a mathematical research record and external literature for equivalent formulas, spikes, probabilities, arbitrary severity and the same quartic map identified related optimization methods but no directly covering statement. The distinction between knowing that an increase exists and knowing the exact superlevel-set measure at **every** severity is essential. Priority is provisional, and an independently derived short special-case calculation may exist elsewhere.

## Value — PASS
The complete exceedance distribution, not merely a transition threshold, quantifies the severity and frequency of one-step loss spikes among convergent-regime initializations, and gives exact risk quantiles. Contrasting uniform physical weights with uniform residuals demonstrates a substantive sampling-coordinate effect. The independent sign-switch mechanism is proven disjoint, clarifying what loss spikes do and do not indicate. This is a natural exact invariant of the specified random-initialization dynamical model; broader neural-network claims are expressly excluded.

## Closest literature and limitations
Prior cubic map, catapult threshold and sign-boundary ingredients are explicitly credited. The new claim is only the exact all-threshold distribution and its two sampling laws and consequences. Calculations are elementary but go beyond the printed threshold/phase classifications; exhaustive historical priority and independent validation are not asserted.

Self-review: passed. Independent audit: not yet performed.
