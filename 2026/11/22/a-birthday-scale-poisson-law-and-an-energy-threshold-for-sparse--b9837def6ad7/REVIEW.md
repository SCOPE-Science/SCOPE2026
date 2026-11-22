# Self-review

## Correctness

**PASS.** The exact factorial form is equation (9) of the cited rank-martingale construction. The proof begins with cell masses of a bounded continuous density, obtains a deterministic normalization error of order \(n^3/K^2\), bounds deviations from pair-collision logarithms by triple occupancies, and checks the exact variance of pair collisions. Its factorial-moment graph argument establishes the nonuniform Poisson law at the birthday scale, while Chebyshev controls the many-collision region. The analytic copula threshold follows from a direct \(L^2\) integral and its exact finite-cell formula. There are no claims at the unscaled cutoff equality.

## Originality

**PASS with historical-priority qualifications.** The source paper establishes the statistic, fixed-grid behavior and sequential validity; no inspected section states the growing-grid Poisson law or nonuniform energy threshold. The known Dirichlet-multinomial formula and birthday problem account for individual ingredients, not the combined three-regime statement. An indexed four-cell finite-horizon calibration concerns a different parameter regime and does not imply this limit. Searches did not identify a dominating theorem, but generic sparse-multinomial Bayes-factor literature remains a priority risk.

## Value

**PASS.** The threshold is motivated by tuning resolution in a published histogram-based independence procedure. The result identifies a non-Gaussian terminal null calibration exactly when grid width reaches the birthday scale, and a sharp \(L^2\)-energy boundary that causes the same evidence to vanish under some fixed positive analytic copula densities yet explode under stronger ones in the independent oracle-copula sampling model. These effects are stronger and more specific than a routine finite-count evaluation.

## Closest literature and limitations

Henzi and Law (arXiv:2305.13818), equation (9), supply the exact evidence statistic and establish fixed-grid power results. Dirichlet Bayesian-birthday formulas appear in the Stanford course notes, and Arratia, Garibaldi and Kilian (2016) establish classical birthday collision asymptotics. The *Book of Statistical Proofs* gives a general finite Dirichlet-multinomial Bayes-factor expression. The main limiting theorem is restricted to the iid histogram input model with \(n/K\to0\); its null case applies exactly to randomized sequential ranks, but its alternative claims do not automatically transfer to dependent sequential ranks. The point \(J(f)=1/\log2\) remains unclassified at unscaled order.

Self-review: passed. Independent audit: not yet performed.
