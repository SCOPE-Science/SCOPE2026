# Self-review

## Correctness — PASS

The definition uses the original leverage-score Bernoulli sketch with \(U=(1,1,1)^{\mathsf T}/\sqrt3\), \(\eta_i=1/3\), and strictly positive diagonal coefficient and control fields. The eight indicator patterns have exact probabilities; the only integer-base levels that contain two patterns are levels two and three. On the two mixed events, the empirical least-squares coefficient is exactly \(1+\sqrt\varepsilon/\varepsilon\), and the corrected errors are exactly \(-1/(3\sqrt\varepsilon)\) and \(-4/(3\sqrt\varepsilon)\). All other fixed-ensemble patterns give bounded error by the finite-state case split. Hence the limit coefficient \((A_\nu+16B_\nu)/9\), the negativity probability \(A_\nu+B_\nu\), and the fixed-weight variance \(2\varepsilon/(9\nu)\) follow without unproved regularity assumptions. Exact-rational enumeration corroborates the finite patterns and constants.

## Originality — PASS, with qualified priority

The motivating 2026 Gram-sketch paper already gives the Bernoulli scheme, uses empirical same-ensemble control-variate coefficients, and warns that the corrected matrix may lose positive definiteness; those general observations are prior work. The narrow new comparison is a sharp \(1/\varepsilon\) finite-ensemble risk law and exact nonpositive-geometry probability while the physical/control diagonals stay uniformly positive and close. Portier–Segers prove OLS control-variate large-sample limits, not this fixed-ensemble triangular parameter limit. Glynn–Szechtman provide broader asymptotic theory; its abstract alone does not establish the narrow result, and the full text was not used to assert otherwise. General regression extrapolation or weak-design literature may contain an equivalent mechanism, so historical priority is not independently established. Literature and published-finding similarity searches did not yield the exact theorem.

## Mathematical value — PASS

The target is a natural performance diagnostic of a proposed variance-reduced projected FEM Gram estimator. The example isolates a finite-ensemble hazard that is invisible to population correlations and oracle variance comparisons, gives an exact probability of leaving the SPD cone, and distinguishes a failure of empirical coefficient estimation from singularity of the original coefficients or sketch average. Its precisely quantified scope informs safeguards such as coefficient regularization or clipping without claiming those safeguards have been analyzed here.

## Scope and limits

This is a scalar, three-row, pre-damping estimator at the minimal expected Bernoulli sampling budget, with a conventional zero-denominator rule and fixed ensemble size. It does not assert instability of a damped inverse estimator or of a pilot-trained/capped alternative. Independent historical and mathematical review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
