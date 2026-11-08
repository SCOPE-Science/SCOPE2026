# Self-review

## Correctness
**PASS.** Each nonhub and hub update is derived directly from the relevant open-neighbor count and strict-majority/tie convention. Odd cliques permanently homogenize their nonhubs in one update and their hubs at the next. Even cliques homogenize in a single update except at the two precisely defined critical count states; there the nonhubs flip and the hub copies the other hub. An indefinitely critical pair is possible precisely for two even cliques with opposing hubs. Critical states have only critical predecessors, so no transient feeds a period-two cycle. Case analysis gives sharp 2/4/5 first-entry bounds, with parametric witnesses, and labelled binomial enumeration gives the cycle count. Three distinct executable checks reproduce finite results. **Risk:** all proofs assume each clique has order at least three; order-two cases are not covered.

## Originality
**PASS, qualified by historical-search limitations.** The closest general period-two theory (Goles–Olivos 1980 and Benjamini et al. 2014) establishes eventual periodicity but not this exact graph-specific census. Kaaser–Mallmann-Trenn–Natale 2015 gives broader module-derived upper estimates for majority voting time but not the exact bridge-barbell parity trichotomy, sharp witnesses, exact two-cycle population, or lack of transient two-cycle attraction. The published mathematical findings index contains a zero-forcing polynomial for the same graph but not a synchronous-majority statement. Queries and implication comparisons are listed in the structured review. **Residual risk:** an unindexed equivalent barbell-specific statement may exist, and the historical 1980 full paper was not inspected.

## Mathematical value
**PASS.** Barbell graphs model two dense communities with a single weak edge, a natural test of how topology changes majority-rule stabilization. The theorem separates parity-controlled persistent oscillation from rapid deterministic settlement: the all-configurations first-entry maximum is uniformly at most five, yet even-even instances have a growing number of distinct unstable-in-basin two-cycles. The exact probability \(1/(\pi\sqrt{mn})\) quantifies their rarity. This is an infinite-family dynamical classification, not a restatement of eventual period at most two.

## Limitations
Four fixed-point basins are not separately enumerated. The one-bridge assumption is essential. The stochastic-voter and random-graph literature is not equivalent to deterministic synchronous majority on the present fixed graph. Priority beyond the inspected accessible literature cannot be guaranteed.

Self-review: passed. Independent audit: not yet performed.
