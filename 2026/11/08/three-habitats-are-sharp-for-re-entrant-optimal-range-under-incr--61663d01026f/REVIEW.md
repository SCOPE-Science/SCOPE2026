# Scientific review

## Correctness
The exact Itô log-growth formula follows from a scalar stochastic exponential. Positive definiteness follows from the three principal minors \(2,3,1\), giving a unique optimum. The displayed KKT identities prove each branch on its full interval; the two-habitat clipping formula establishes sharp minimality. The final-branch objective has exactly one positive root, and strict decrease of the optimal value covers the earlier intervals. `verify.py` replayed successfully, including 150 rational active-set checks. Scientific correctness passes for the stated model.

## Originality
Searches for environmental-variance-driven re-entrant habitat allocation, nonnested optimal support, and no-short-sale mean–variance portfolio support found no direct match for the exact minimal-three-habitat theorem, four phases, and persistence window. Comparison to Schreiber (2012) is substantive: it treats density-dependent evolutionary stable habitat selection, not this fixed low-density growth objective. Markowitz (1952) and Bailey–López de Prado (2013) supply the mathematically equivalent general quadratic optimization machinery; none of the inspected pertinent text directly states this sharp ecological support sequence. The method is not original and historical priority is provisional; standard critical-line theory is an important equivalence risk. Within those limits, the specific claim passes the self-review.

## Value
This is a sharp dimension boundary and an exact counterexample to the notion that increasing environmental risk must monotonically expand the support of a growth-maximizing range. The intermediate occupancy and subsequent exclusion occur before regional stochastic extinction, and the same model gives regional growth despite three individually declining habitats. That distinction is motivated by ecological rescue and stochastic habitat selection, not arbitrary rounding or a numerical curiosity. It is a benchmark for a specific abstract model, not an empirical intervention recommendation. Value passes for this scoped theorem.

## Sources and remaining risks
Schreiber (2012), DOI 10.1086/665655, author full text and Appendix C; Markowitz (1952), DOI 10.1111/j.1540-6261.1952.tb01525.x, archival full text pp. 77–91; Bailey and López de Prado (2013), DOI 10.3390/a6010169, openly indexed text. Standard parametric quadratic programming may contain equivalent examples not identified in this search. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
