# Scientific review — sharp drift–noise transition for Bernstein–Stancu BV error

## Correctness: PASS

The operator is defined on canonically right-continuous real BV inputs with one-sided endpoint traces, so point sampling is well-defined modulo constants and no isolated spike has zero derivative seminorm. Signed-derivative decomposition reduces the sharp \(BV\to L^1\) error to step responses. The binomial survival function is the CDF of the appropriate Beta order statistic; integrating on either side of the jump gives its absolute-deviation moment. Piecewise convexity yields the finite formula, including both one-sided knot values and the deterministic edge cases. The order-statistic CLT, exact variance and a subsequence compactness argument prove the Gaussian limiting variational problem at interior and boundary indices. Finally, the strictly increasing positive integral \(R(a)\) proves that the Gaussian objective has no interior maxima and yields the exact threshold and maximizing-site localization. The independent binomial-integral comparisons in `check.py` passed. Finite numerical tests corroborate, but do not prove, the all-degree theorem.

## Originality: PASS (historical-priority qualification)

The inspected 2015 Üster–İbikli primary paper addresses pointwise BV bounds for Bernstein–Stancu sampling and gives its sampling definition and moment estimates; it does not state a sharp integrated \(BV\to L^1\) norm or a degree-dependent square-root parameter transition. The full arXiv text of Gandhi–Mishra (2017) concerns knot sensitivity and continuous-function convergence, not the displayed sharp discontinuous-input asymptotics. The open-access Dong–Yu (2017) paper studies an integral Durrmeyer modification instead. Published-result searches for the formula, its Beta-order-statistic equivalent, and the Gaussian boundary/midpoint crossover returned no statement implying the result; classical Bernstein estimates address only the zero-displacement limit. These searches cannot establish absolute historical uniqueness; the 1983 original Stancu paper and any otherwise unindexed equivalent remain priority risks.

## Value: PASS

The scale \(\beta_n=b\sqrt n\) makes deterministic inward displacement and binomial averaging noise compete at exactly the order of the worst BV approximation error. The result identifies a sharp universal value \(b_*=\sqrt{2/\pi}\) separating boundary-dominated and center-dominated discontinuities, with complete limiting location rigidity, while the finite Beta formula permits exact error calibration at every degree. This is more than a parameter relabeling of the classical Bernstein case, whose leading constant has no such competition. The theorem is deliberately limited to the symmetric Stancu family; it does not purport to settle all two-parameter Stancu sequences or finite-degree equality classification.

## Closest literature and limits

- R. Üster and E. İbikli, *On the rate of convergence of the Stancu type Bernstein operators for functions of bounded variation*, Mathematical Sciences and Applications E-Notes 3 (2015), pp. 126–136, https://doi.org/10.36753/mathenot.421231 (PDF inspected).
- R. B. Gandhi and V. N. Mishra, *Study of sensitivity of parameters of Bernstein-Stancu operators*, arXiv:1707.07424, https://arxiv.org/abs/1707.07424 (full HTML examined).
- L. Dong and D. Yu, *Pointwise approximation by a Durrmeyer variant of Bernstein-Stancu operators*, Journal of Inequalities and Applications (2017), article 28, https://doi.org/10.1186/s13660-016-1291-x (open-access article sections read).
- Residual risks: unknown older exact norms, incompletely indexed preprints, and unavailable full text of D. D. Stancu's 1983 original definition. No external independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
