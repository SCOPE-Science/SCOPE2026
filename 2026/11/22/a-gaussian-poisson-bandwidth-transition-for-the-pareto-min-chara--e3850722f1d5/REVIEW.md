# Scientific review: Pareto minCF bandwidth transition

## Correctness — PASS

The claim is an exact three-regime asymptotic statement for the published MLE-standardized statistic. Equation (1) in RESULT.md follows from an exact change of variables; (2) is a direct Pareto integral. The Gaussian limit uses triangular-array Hilbert-space Lindeberg convergence with an explicit vanishing maximal summand and integrable covariance trace. The critical limit uses a point-process Poisson limit with an explicit \(2\varepsilon\) small-jump \(L^2\) bound. Above the boundary the sample Pareto mean minus \(\log n\) is tight; a quantitative truncation estimate makes the clipped-tail remainder vanish in the weighted norm. The effect of MLE substitution is controlled separately and vanishes under the correct normalization in all three regimes. Gaussian fourth moments and compensated-Poisson fourth cumulants give the exact variance difference. Formula identities and integration were independently checked by the supplied Python checker (68 assertions). Simulation is only supporting evidence. Unproved: empirical test size and power, simultaneous tuning validity, finite-sample fourth-moment convergence for the fitted statistic.

## Originality — PASS (with recorded historical-priority risk)

The source article's sections 2–5 and appendix were read: its MLE equivariance and fixed-positive-weight null theorem are prior results. A fixed-weight theorem does not automatically extend to the triangular family \(\gamma_n\to\infty\), because the integrating weight concentrates at the infinite-mean Pareto endpoint and the truncated empirical minCF undergoes a change of limit. The minCF itself and its empirical-process theory are due to Falk and Stupfler. Existing general soft/hard Pareto truncation literature supports the possibility of Gaussian and non-Gaussian regimes; it does not itself furnish the displayed **fitted integrated quadratic statistic**, the compensated-Poisson critical functional, the exact \(\frac83(1-\log2)\) variance slope, or the arbitrary-rate supercritical normalization. No exact or stronger covering claim was identified in the available own-ledger entries or queried published mathematical records. Search absence does not prove priority. The 2024 repository printing could not be inspected separately in full, and two generic truncation papers were accessible only at abstract level; this is an explicit residual risk rather than an invented NOT_COVERING judgment.

## Value — PASS

The result resolves a motivated question about a published test's tuning parameter: changing the weight rate with sample size produces three qualitatively distinct null calibrations. The exact critical variance law quantifies the non-Gaussian contribution and cannot be recovered by simply rescaling the fixed-weight null asymptotic law. The supercritical result explains why typical scaled statistic values collapse even though the critical family has fixed mean. This is an informative statistical boundary, not an arbitrary numeric invariant or a mere finite-sample recomputation. The theorem does not claim practical power changes without calibrated rejection probabilities.

## Closest literature and limitations

- Meintanis, Milošević and Jiménez-Gamero, arXiv:2310.12348 (2023), and *Computational Statistics & Data Analysis* 197 (2024), 107988: exact statistic, Pareto minCF, MLE equivariance, fixed-weight limit and fixed-alternative consistency; closely inspected source.
- Falk and Stupfler, *Sankhya A* 83 (2021), 254–282: definition, characterizing property and general empirical minCF convergence; available scientific summary.
- Chakrabarty and Samorodnitsky, *Stochastic Models* 28 (2012), 109–143: general soft/hard heavy-tail truncation framework; abstract-level comparison, not a full-text exclusion.
- Tang and Han, *Communications in Statistics – Theory and Methods* 53 (2024), 5168–5185: generic truncated-mean limit classes; abstract-level comparison, not a full-text exclusion.

Residual priorities: other general empirical-process representations, unpublished results and inaccessible full journal papers may contain implications not exposed by indexed abstracts. No independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
