# Scientific review

## Correctness

**PASS.** Strict positive definiteness makes the augmented saddle-point system invertible, and constant reproduction follows exactly. Every data vector is a sum of a constant and adjacent single-jump steps, so the induced variation norm is the maximum of finitely many step-response variations for each scale. As kernel scale increases, the Gram matrix approaches identity, the fitted constant approaches the data mean, and the radial coefficients approach the centered data. Splitting the interval at the Voronoi midpoints controls cross-peak variation by the profile tail, proving the weighted peak-variation formula uniformly over normalized data. Direct evaluation on step data yields the exact sharp coefficient and its center-index maximizers. These implications do not rely on finite numerical tests.

## Originality

**PASS, with historical-priority risk.** The archived Platte–Driscoll technical report and author-hosted journal full text treat Gaussian interpolation, Runge phenomena, potential theory, and uniform-norm Lebesgue stability, rather than the present constant-augmented one-dimensional variation norm. Yarotsky's accessible Gaussian-interpolation paper treats analytic interpolation-error formulas and convergence, not peaked constant-reproducing BV amplification. Specialized geostatistical or BV operator-norm literature remains a possible uninspected route to prior coverage. Searches and comparisons are recorded in the structured review. No originality conclusion is based on merely different terminology; no broader result was identified that implies the exact central-step factor for the stated scheme.

## Mathematical value

**PASS.** Constant augmentation is a natural correction for the failure of unaugmented peaked interpolants to preserve constants. The exact value of its variation-stability cost is not given by conditioning or a Lebesgue constant. The result is a sharp asymptotic operator norm for every site count and every fixed irregular grid, and is universal across monotone decaying strictly positive definite kernels. Its central-step extremizer and linear growth identify a concrete instability mechanism in increasingly localized interpolation.

## Checks and limitations

The analytical proof establishes the infinite-parameter limit; the standalone checker provides finite-scale numerical corroboration for Gaussian and exponential kernels on irregular meshes. The result does not claim a finite-scale closed formula or simultaneous uniformity in mesh size and scale. The historical-priority question is not independently certified and additional full-text specialty literature may be relevant.

Self-review: passed. Independent audit: not yet performed.
