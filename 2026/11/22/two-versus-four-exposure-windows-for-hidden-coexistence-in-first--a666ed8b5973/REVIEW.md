# Scientific review

## Correctness — PASS

The exact first-arrival law follows from independent equal-rate exponential races conditional on the four latent occupancy states. The unbalanced inversion uses the cause difference to determine the common rate and then two linear equations to reconstruct overlap. The balanced inversion uses a strictly positive two-atom Hankel determinant and two recurrence equations, giving a unique positive decay factor and positive component weights. The strict three-window lower bound is established by two complete rational occupancy distributions with opposite exact covariance signs, not by a parameter count or numerical search. All boundaries are explicitly limited to strictly positive cells and rate. The standalone standard-library checker verified the exact table identities and passed 19,000+ randomized inverse tests.

## Originality — PASS on inspected evidence

The key comparison is by mathematical implication. The 2024 first-arrival ecological paper uses independent latent occupancy assumptions and a time-resolved competing-use likelihood, not a sharp 2/4 fixed-horizon inverse for correlated occupancy. Recurrent-event and confirmatory occupancy methods address different observation designs. Standard Prony/Hankel reconstruction subsumes the algebra of four-window sufficiency but does not by itself establish the two-window unbalanced shortcut or the three-window sign-ambiguous counterexample. Searches of prior indexed research and public literature did not locate the combined claim. Residual risk: general current-status/cure and exponential-mixture identifiability literature is extensive, and some primary mathematical full texts were inaccessible.

## Value — PASS

The result answers a concrete monitoring-design question: how many coarse, cause-labeled exposure deadlines are needed to infer hidden competition/association at ephemeral resources when exact visit times are unavailable. The counterexample shows that three deadlines can give **the wrong sign of inferred ecological association** under two indistinguishable models, whereas four suffice throughout the interior. It also identifies a two-deadline economy when the species' marginal availabilities differ. Both the positive reconstruction and the negative ambiguity are exact, model-specific structural facts; they are not claims of field suitability or finite-sample stability.

## Closest literature and limitations

Closest inspected literature: Nakashima et al. (2024), Ferry et al. (2024), Chambert et al. (2018), Lonsinger (2022), and the Plonka–Tasche (2014) Prony survey. Related current-status competing-risk work by Koley and Dewanji (2021, 2023) was available only by abstracts/search extracts; no conclusion that the full papers lack an equivalent theorem is asserted. Assumptions are restrictive (equal exponential rates, independent clocks conditional on occupancy, two species, exact probabilities), and exact identifiability does not provide robust finite-sample inference. Independent external review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
