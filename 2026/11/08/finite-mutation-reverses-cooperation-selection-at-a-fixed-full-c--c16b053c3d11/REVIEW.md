# Scientific review: finite-mutation public-goods return threshold

## Correctness — PASS

The exact domain is a four-person, two-strategy, three-person-group stochastic game with payoff-independent symmetric strategy flipping, independent with-replacement role-model sampling, and Fermi imitation. The three conditional payoff differences are reconstructed by finite hypergeometric sampling. The resulting five-state birth–death chain is irreducible for every \(0<\mu<1\), with unique detailed-balance stationary weights. Differentiating these weights at neutral selection proves the rational coefficient with numerator proportional to \(r_2-5\). At \(r_2=5\) an exact reflection symmetry forces neutrality for all selection strengths. Two exact fractions at \(\mu=1/2\), \(\delta=9\log2\) are checked by an independently assembled rational stationary chain. The proof distinguishes the rare-mutation limit from the absorbing chain at zero mutation. `CHECK.py` passed 72 exact rational comparisons and both exact witnesses. No finite experiment is used as a replacement for the analytic proof.

## Originality — PASS (qualified)

Wang et al., arXiv:2607.16809, Sections 2.1–2.3 and Appendix B establish a boundary-return invariant in the **rare-mutation, weak-selection** regime, not the positive-mutation sign threshold. Hauert and McAvoy (2024), Sections 2.2–2.3 and 4.2 analyse finite mutation but constrain the return profile to be affine in group composition; at the chosen endpoints they are restricted to the neutral \(r_2=5\). Antal et al. (2008–09) examine pairwise matrix-game mutation-selection abundance, not freely varying three-player middle returns. McAvoy and Hauert (2015) develop general weak-selection structure-coefficient rules for multiplayer games (their Section 4 and Appendix B), but do not compute this concrete positive-mutation Fermi public-goods coefficient or its finite-strength stationary examples. Searches of the scholarly literature identified no explicit prior claim implying the stated exact \(r_2=5\) threshold and opposite-sign same-endpoint examples. Generic Markov-chain perturbation theory is known; the concrete game-specific phase boundary, not that general machinery, is the originality claim. Residual risk: unindexed work may contain an equivalent multiplayer-mutation calculation, and the broader structure-coefficient literature can supply related approaches.

## Mathematical value — PASS

The fixed full-cooperation return \(r_3=9\) produces neutrality in the rare-mutation limit, yet with any fixed positive nonunit mutation rate the sign of weak selection depends on the middle return. This pinpoints a scientifically motivated assumption boundary, with a smallest-size genuinely three-person interaction and two nondecreasing (economies-of-scale) return profiles giving opposite outcomes. Exact finite-strength stationary abundances show the distinction is not merely an artifact of taking a derivative. This prevents extrapolating the motivating boundary-only condition to positive-mutation populations, without claiming that the original restricted theorem is false.

## Closest literature and residual limits

The closest primary texts examined are Wang et al. (2026), arXiv:2607.16809; Hauert–McAvoy (2024), PMC11521596; and McAvoy–Hauert (2015), DOI 10.1007/s00285-015-0882-3. Antal et al. (2008–09) supply broader pairwise mutation background. Multiauthor unindexed multiplayer mutation results are a residual originality risk. The statement does not cover arbitrary population sizes, network structure, mutation rules or all-selection sign monotonicity away from the displayed witnesses.

Self-review: passed. Independent audit: not yet performed.
