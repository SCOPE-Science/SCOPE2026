# Self-review

## Correctness — PASS

The fixed-season model, normalization, initial redistribution, and stock-recursion agree with the primary full-text equations. The proof reconstructs the complete two-eigenvalue matrix exponential, including the slow projection coefficient. Duhamel differentiation gives strict monotonicity of the survival fraction with harvesting effort. An asymptotic expansion uniform near the interior critical fraction gives a strictly positive first correction, and the smooth reserve-limit function has strictly positive derivative; hence the claimed reciprocal-distance divergence has an explicit, nonzero constant. Both threshold existence directions, equality at the extinction boundary, and the cases of all finite efforts are proved with precise quantifiers. The included standard-library checker passed 435 supplementary calculations against a separately implemented matrix power series and numerical cutoff roots. Computational checks are supportive rather than logically exhaustive.

## Originality — PASS (literature-bounded)

Kumar (arXiv:2601.20563v1) supplies the two-patch model, the exact high-effort survival limit and the persistence criterion. Its Table 1 discusses a large-effort reserve asymptote, but not the joint-limit expansion or the \(1/(R_c-R)\) effort-cap law with the coefficient. Doyen and Béné (2003), including its model and Appendix A viability results, use a spatially implicit uncertain-harvest Beverton–Holt model and a safe-biomass viability threshold; they do not imply the claimed finite-rate dispersal coefficient. The indexed mathematical record on source-specific fishery-threshold calibration does not report this singular effort-gap law, although full repository content could not be opened. Other closely retrieved records concern reserve locations, seasonal quota ordering or metapopulation persistence. Previous accessible claim-ledger entries were searched for the source and the claimed parameter transition and did not contain this result.

Historical priority is **not a formal uniqueness theorem**. The indexed summaries and checked primary full text set the limits of the originality assessment; inaccessible deeper repository text and unindexed literature remain a residual risk. The result does not present the source's persistence condition or Lambert \(W\) rearrangement alone as new.

## Value — PASS

The paper's horizontal asymptote leaves the operational question of how rapidly allowable harvesting effort becomes large as protected-area coverage approaches its limit. The answer is a sharp scale and fully evaluated coefficient for an entire positive-parameter family, not a hand-picked numerical example. It separates the reserve's baseline survival contribution from its finite-effort spillover corrections and gives quantitative sensitivity for effort-constrained planning near the sustainability boundary. The coefficient does not depend on the recruitment-density parameter, a meaningful structural distinction between persistence and abundance.

## Checked sources and limits

- D. Kumar, arXiv:2601.20563v1, Sections 2–4, Table 1, discussion, full HTML: https://arxiv.org/html/2601.20563v1
- L. Doyen and C. Béné (2003), model, viability threshold, Appendix A in accessible posted full text: https://www.researchgate.net/publication/10607113_Sustainability_of_Fisheries_through_Marine_Reserves_A_Robust_Modeling_Analysis
- J. Boncoeur et al. (2002), high-effort reserve spillover discussion: https://doi.org/10.1111/j.1939-7445.2002.tb00095.x

No claim about stochastic fisheries, empirical robustness, or optimal dynamic control follows. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
