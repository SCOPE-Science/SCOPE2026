# Review: Skew-gamma rigidity for drifted Brownian diffusion with random proportional resets

## Correctness — PASS

The stationary identity follows from a genuinely contracting random affine perpetuity. The asymmetric bilateral exponential excursion law is derived from the independent exponential inter-reset age. Two-sided gamma-tail asymptotics rule out either target shape below one. Fourier uniqueness identifies the reset term as a gamma difference with shapes reduced by one; its sign must agree with the original gamma difference because the multiplier is positive. The explicit beta-CDF difference identity forces the strict shape-balance relation. Conversely, beta integration proves the target fixed-point identity along that balanced ray, and even-moment determinacy uniquely identifies the contraction distribution. The zero-shape boundary is treated separately. The standalone rational checker passes 3,204 finite tests; infinite claims rely on the complete proof in `RESULT.md`.

## Originality — PASS against inspected sources

Palmowski and Vlasiou (2026, arXiv:2611.14692v1) give the general stochastic fixed-point framework and fixed-coefficient drifted Brownian calculations, not the complete asymmetric inverse target classification. Tal-Friedman et al. (2022, arXiv:2205.03363) and Pierce (2022, arXiv:2204.07215) treat deterministic contractions. The closest accessible published published-finding corpus result classifies the **zero-drift symmetric** variance-gamma target, which does not logically imply the strict, nonzero-drift sign-balance condition or the two unequal shape parameters in this theorem. Targeted searches of equivalent gamma-difference, bilateral-gamma perpetuity, random autoregressive, beta contraction and random Brownian reset terminology did not identify a covering result. These searches do not establish absolute historical priority, particularly against general beta-gamma distributional identities or obscure perpetuity literature.

## Mathematical value — PASS

This exact inverse design criterion is a natural missing link between drifted diffusions, self-similar random resets and two-sided gamma equilibria. It gives both a sharp impossibility principle for unbalanced positive/negative gamma shapes and an explicit one-parameter family of admissible, inherently asymmetric stationary laws, with uniqueness of the entire reset mechanism. It is a classification rather than a renaming of the fixed-point equation or a finite numerical curiosity. It is restricted to natural exponential excursion scales, and does not classify all variance-gamma equilibria.

Self-review: passed. Independent audit: not yet performed.
