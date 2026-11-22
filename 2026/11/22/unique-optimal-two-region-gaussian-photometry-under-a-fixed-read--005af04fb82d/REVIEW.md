# Scientific review

## Correctness: PASS

For all positive \(R,\sigma,b\) and any two nonnull measurable spatial bins, the two independent Poisson count means give an exact two-by-two Fisher determinant. Under \(F\downarrow0\), it reduces to the squared source-mass-minus-area contrast divided by the two area fractions. Strict radial rearrangement bounds this contrast for every possible nonradial partition, including its equality cases. A derivative numerator with a single curvature sign change admits exactly one interior zero; an explicit midpoint sign makes the maximizing central fraction strictly less than one half. Uniform secant-error control proves the narrow-field limit, while tight rescaling and a unique limiting scalar maximizer prove the large-field limit. The proof is infinite-dimensional only at the rearrangement step and uses a direct signed-integrand argument; finite diagnostics are corroborating rather than a substitute. This assessment does not claim independent verification.

## Originality: PASS relative to inspected evidence

Fischer and Kochanski (1993), Chandra aperture-photometry documentation (2012) and Masci (2008) address aperture signal-to-noise and source/background regions. The Masci 2008 Gaussian large-field \(1.5852\sigma\) radius is fully acknowledged as known, not a new numerical constant. Vicuña et al. (2023) study joint source and background estimation using individual pixel counts; the inspected full paper derives a pixel-level Fisher matrix and compares fitting methods, not optimization of two aggregate bins over all measurable partitions. Indexed portions of Espinosa et al. (2025) examine retained fitting radius, not rearrangement among all two-bin partitions of a fixed field. The exact finite-field global geometric classification under a two-count budget, with unique inner area fraction and asymptotics, was not implied by those inspected sources or the nearest indexed mathematical records. Priority remains provisional against unsurveyed optimal-quantization results and partially accessible primary texts.

## Value: PASS

There is a meaningful instrumentation tradeoff between preserving two cheap photon totals and retaining full pixel-level positions. This classification gives a fixed-field D-optimal partition when source strength and background must both be inferred, where one count cannot identify two parameters. Its global measurable-partition bound rules out irregular masks, not just nearby circular thresholds; its finite-field solution differs nontrivially from both equal-area partition and the already-known infinite-field Gaussian SNR radius. The example at squared field radius parameter \(c=2\) yields approximately 10.99% more Fisher determinant than an equal-area split. This is a benchmark for a particular constrained readout instrument, not a recommendation to discard full imaging data or a claim about estimator behavior at the parameter boundary.

## Closest sources and limits

- Fischer and Kochanski (1993), https://arxiv.org/abs/astro-ph/9310031, abstract/record checked; aperture-image combination, not exact two-count global partition.
- Masci (2008), https://web.ipac.caltech.edu/staff/fmasci/home/mystats/GaussApRadius.pdf, full note reviewed; the asymptotic 1.5852 sigma Gaussian SNR optimum is already published.
- Chandra Source Catalog, https://asc.harvard.edu/csc1/why/ap_vals_errs.html, two-aperture source/background formulas, but not the constrained partition theorem.
- Vicuña et al. (2023), https://arxiv.org/pdf/2311.12142, full relevant Fisher derivation and region-method discussion inspected; the pixel-resolved design is a different experiment.
- Espinosa et al. (2025), https://arxiv.org/abs/2509.20613, indexed sections only; residual risk remains until full manuscript comparison.
- Klepser (2017), https://arxiv.org/abs/1701.04731, published abstract establishes a related single-region detection-SNR radius rather than joint-parameter, two-region partition optimization.

Limitations: positive uniform background; exact known Gaussian width and centroid; local vanishing-flux design; independent Poisson counts; outer radius and number of retained channels fixed. No noise stability or finite-flux optimality and no field data.

Self-review: passed. Independent audit: not yet performed.
