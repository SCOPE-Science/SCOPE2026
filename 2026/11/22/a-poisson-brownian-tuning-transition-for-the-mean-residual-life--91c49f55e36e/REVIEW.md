# Scientific review: a Poisson–Brownian tuning transition

## Correctness (C): PASS

The identity \(H_n(y)=N_n(y)-ny+\int_0^yN_n(t)dt\) is pathwise, and the factor \(a/n\) after changing variables is checked directly. The two marginal Dirichlet survivor probabilities give both negative covariance of threshold indicators and the explicit finite-sample second moment. These yield the weighted-tail bound needed for all three regimes, including the non-uniform-integrability assertion. The critical regime follows from finite-count point-process convergence; the subcritical regime from the centered local-count functional central limit theorem with random-scale time-change; the supercritical regime from no points in the first \(M/a_n\) segment. The Poisson fourth-cumulant calculation independently gives \(\mathbb E Q_c=1\) and \(\operatorname{Var}(Q_c)=1+c/2\). The standalone checker reports 71 supplementary assertions. Its finite calculations are not substituted for infinite-sample proofs.

## Originality (O): PASS with historical-priority reservations

The motivating open-access arXiv paper (Ebner, arXiv:2209.05153, first public submission 2022-09-12) was inspected at its definition, fixed-parameter null theorem, alternative analysis and conclusion. It does not classify diverging weights. The earlier Baringhaus–Henze (2008) test is the same statistic; its identified abstract and Ebner's detailed historical discussion establish a fixed-weight limiting weighted bridge law, not the moving-weight Poisson window or the non-uniform-integrability effect. The older generic theory of local empirical processes (Einmahl, 1997) already predicts Poisson-versus-Gaussian local *count-process* limits; that generic mechanism is expressly excluded from the originality claim. The self-contained statistic-specific Dirichlet tail estimate, all-regime functional limits, exact moment law and escaping expectation are the claimed mathematical additions. A related older weight-decay/smooth-test article (Baringhaus, Gürtler and Henze, 2000) studies fixed-sample or fixed-weight high-decay mechanisms but is not evidence of this sample-size joint limit. Published research-record searches returned no claim with the same source, statistic and implication. The relevant available in-scope ledger was checked for recoverable claims only, including previous high-weight but mathematically different statistics.

Residual risks: The 1995 Einmahl report was identified as open access but its full text could not be retrieved through the available research interfaces; generic functional limit theorems could imply some weak-convergence components. The older 2008 and 2000 source full texts were also not accessible in this inspection, so historical priority cannot be certified from abstracts. The full conjunction of the scale-fitted statistic, explicit Poisson moments and supercritical mean escape was not found, but absence of a search hit is not proof of novelty.

## Value (V): PASS

This is a concrete calibration boundary in a published one-parameter goodness-of-fit statistic. A tuning rule that takes \(a_n\) of order sample size cannot be justified by the known fixed-weight null law: its null limit is a non-Gaussian compensated-Poisson quadratic functional, with variance exceeding the Brownian limit by \(c/2\). More strikingly, taking the weight still faster produces an apparently vanishing statistic in probability although its normalized expected value persists. The explicit threshold and moment-escape mechanism help delineate when weighted-integral calibration requires a new limiting law, rather than merely giving a small-parameter algebraic variant.

## Limits

No result about optimal power, parameter-adaptive weights, non-exponential alternatives, or simultaneous rates outside the hypotheses is claimed. The critical CDF is not evaluated in closed form. Independent expert assessment and historical-priority certification have not taken place.

Self-review: passed. Independent audit: not yet performed.
