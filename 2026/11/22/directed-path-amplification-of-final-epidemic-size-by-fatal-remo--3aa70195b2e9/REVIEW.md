# Self-review

## Correctness — PASS

The claimed comparison fixes the total infectious exit rates, the transmission matrix and all initial conditions. Integrating the exact SIRD equations gives the source-normalized final-size map with the continuous integral convention for zero fatality fraction. Its positive intercept, boundedness and strict coordinate concavity supply a unique positive fixed point for every nonnegative transmission matrix with a positive entry in each row and strictly positive initial infection in every group. The key nonstandard step is the spectral inequality \(Jh\ll h\), which follows directly from positive-intercept concavity; it makes the Neumann-series inverse legitimate. Differentiating the map gives the stated matrix sensitivity and its sharp graph-support equivalence. The proof covers all finite group counts and the boundaries \(q_i=0\) by one-sided continuity. The checker replays the rational-parameter illustration and finite-difference/sparse graph tests but is not substituted for a proof.

## Originality — PASS, bounded by inspected evidence

The founding active-population SIRD study of Melo and Santos (2026) derives final-size formulas and compares increased transmission, but does not prove fixed-total-removal fatality-split monotonicity or any directed graph reachability criterion. The textbook of Diekmann, Heesterbeek and Britton already presents the **single-group** mortality/survival dependence at fixed reproduction number, so that scalar fact is excluded from the novelty claim. The published work on parameter-unrestricted final-size uniqueness in active-population SIRD networks covers the existence/uniqueness ingredient: that ingredient is credited as prior, not relabeled. The new statement compares source-specific fatal-removal parameters, gives an exact all-group derivative and establishes the iff support characterization over sparse directed networks. Classical heterogeneous-mixing final-size studies were checked for stronger implications; their accessible material did not establish this fixed-exit active-denominator graph criterion. The full Brauer (2008) treatment paper was unavailable; a hidden equivalent formula remains a residual priority risk.

## Value — PASS

The result resolves a motivated comparative-statics question left open by the original two-group construction: whether a severity change in one group has external effects on infections in other groups despite unchanged infectious durations and reproduction thresholds. The answer is a complete graph-theoretic classification, including exact zeros in disconnected/restricted mixing directions, and a formula that attributes the positive spillover to transmission walks. It also distinguishes the active-population model from its fixed-denominator counterpart. These are mathematically interpretable boundaries for structured-epidemic sensitivity, not a routine substitution into the scalar final-size equation.

## Closest literature and limitations

The scalar mortality effect is old; the generic positive-concave fixed-point argument is old; neither is claimed. The theorem assumes every group initially contains infectives, every transmission row is nonzero, and fatality fractions remain below one. The comparative parameter change is not a medical recommendation or stochastic survival result. Full historical priority is subject to possible equivalent content in older heterogeneous-treatment literature, particularly Brauer (2008). The analytical theorem is reviewed only at the same-model level; no external independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
