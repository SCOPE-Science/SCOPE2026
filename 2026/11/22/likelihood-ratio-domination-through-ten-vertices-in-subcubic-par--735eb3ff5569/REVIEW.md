# Likelihood-ratio domination through ten vertices in subcubic parking graphs — review

## Correctness
**PASS (self-review).** The quantified claim is restricted to simple connected graphs with maximum degree at most three and at most ten vertices. The finite proof uses a complete vertex-deletion induction, an adjacency-preserving isomorphism backtracker, an exact first-selected-vertex recurrence for the sequential law, and exact enumeration of independent dominating sets for the uniform static law. `verify_census.py` generated all 2,571 isomorphism types and checked every adjacent likelihood-ratio comparison using `fractions.Fraction`; `verify_orders.py` independently checked all arrival permutations for the 49 types through size six. The argument neither extrapolates to eleven vertices nor identifies sampling with exhaustive proof.

## Originality
**PASS under examined sources, with a priority limitation.** Higuita-Diaz, López and Roldán-Correa (arXiv:2611.14718v1, November 10, 2026) prove first-order dominance for paths and cycles, describe all-graph comparability through seven vertices, and conjecture stochastic dominance for subcubic graphs. Their inspected article does not state the stronger likelihood-ratio inequalities for every connected subcubic graph through size ten. The code repository README describes random degree-three checks and general exhaustive searches, not the specific stronger theorem. Published related findings about greedy output uniformity on cycles and clique bouquets concern different comparison claims. A full historical-priority determination is not possible from this bounded literature investigation.

## Value
**PASS.** Degree-three sufficiency is an explicit open structural conjecture about greedy adsorption. The sizes eight through ten are the first three orders beyond the seven-vertex comparison reported in the motivating paper; eight is already the first order at which stochastic comparability fails without the degree restriction. The complete finite census covers 2,458 previously unreported connected subcubic types at these orders and proves the strictly stronger monotone-likelihood-ratio comparison, not merely an incremental recalculation of a mean or a numerical sample. It supplies a concrete finite boundary for future approaches to the all-orders problem.

## Limitations and closest literature
The new result is finite, and no claim is made that ten vertices is a sharp point of failure or that any all-order statement holds. Statistical priority uncertainty includes unindexed computations or a stronger published domination theorem not found in the investigated sources. The standalone proof depends on exact finite code and a completeness argument; the independent arrival-order cross-check covers only orders at most six. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
