# Scientific review: Beta blind alternatives for a fitted Gamma U-statistic

## Correctness — PASS

The claim fixes the uncensored scalar discrepancy and the method-of-moments estimators, so there is no ambiguity between fixed-parameter and fitted-parameter limits. The \(\operatorname{Beta}(a,1)\) first two moments, minimum kernel and ratio kernel integrate to the displayed rational formula; its zero at the uniform law is exact. Real analyticity in the two Beta shapes and nonzero \(\partial_b\Delta(1,1)\) justify the local analytic curve by the implicit-function theorem. Under the uniform alternative the fitted influence function is \(3x-3x^2+2x\log x\) and has exact variance \(7/540\). Under the matching \(\Gamma(3,1/6)\) null, exponential-polynomial integration gives \(37/2592\). U-statistic projection and the multivariate delta method then give the two distinct Gaussian limits and the stated limiting two-sided rejection probability. The exact checker independently evaluates critical identities using symbolic algebra; its 19 assertions passed.

## Originality — PASS (qualified)

The original 2021 preprint, arXiv:2108.00503 (Sections 2–4), presents the scalar statistic and its asymptotics, but its accessible formula and discussed alternatives do not state this explicit continuum of fixed non-Gamma zero-discrepancy laws or the specific 3.971% power limit. Betsch and Ebner, arXiv:1806.06028, establish global consistency for an *integrated squared* pointwise discrepancy, which is logically different from a single signed integral and does not imply the scalar result. Search comparisons also considered generic Stein characterizations, Gamma moment-estimator papers and several related published research records; these have different objects or functionals. The 2023 journal page was available only at abstract level. General arguments about non-injectivity of scalar functionals could predict some cancellation, but do not supply this exact Beta law, local zero manifold, the two influence variances or the limiting calibration formula. Residual priority risk persists in older scalar-characterization and Gamma-test literature.

## Value — PASS

The object is a published parametric goodness-of-fit test for lifetime models, not an arbitrary statistic. The exact uniform alternative shares both mean and variance with the fitted Gamma reference, defeats the scalar population discrepancy, and produces an asymptotic rejection probability below the nominal level in the specified two-sided calibration. The result is not just a single accidental parameter: an analytic family of smooth continuous non-Gamma alternatives remains invisible. The sign law also distinguishes behavior of the paper's positive-side rejection prescription from a two-sided test. These are substantive limitations for users who may otherwise infer consistency from the underlying pointwise characterization.

## Scientific limitations and closest literature

The analysis is limited to the uncensored, moment-fitted scalar version and large-sample critical values. It does not challenge the integrated-squared omnibus Gamma test, characterize every invisible distribution, or supply finite-sample error bounds. The same original paper's final published text could not be examined in full; the explicit 2021 arXiv version was examined at the actual equations and test sections. Earlier scalar tests may contain analogous non-identification examples even though targeted searches found no direct implication. Independent auditing remains outstanding.

Self-review: passed. Independent audit: not yet performed.
