# Review: Sharp variance thresholds for flowering-overlap duration and occurrence

## Correctness — PASS
The complete proof is analytic. The Gaussian heat equation turns the triangular overlap function into the exact derivative of expected overlap duration. The strictly convex equation \(\log\cosh(az)-z=0\), with \(a=2d/L\), gives the sharp half-duration threshold and a unique optimum whenever \(d>L/2\). A separate normal-tail derivative gives the full-duration threshold for probability of any co-flowering. The layer-cake argument proves strict ordering of the two optima when \(d>L\), and the endpoint discontinuity when \(d=L\) is handled explicitly. Direct numerical quadrature, independent Gaussian-moment evaluation, finite differences and positive-parameter stress tests passed; these finite checks do not prove the all-parameter results.

## Originality — PASS on inspected evidence, priority provisional
Austin et al. (2024, https://doi.org/10.1111/nph.19994) motivate variable relative phenological shifts and days of overlap but do not provide this Gaussian all-variance phase diagram. Rudolf (2018, https://doi.org/10.1111/1365-2656.12850) already shows nonlinear interaction response to timing variability in another model, so broad nonlinear variability effects are not new. Buckley et al. (2021, https://doi.org/10.1111/1365-2656.13451) quantify different empirical overlap metrics, without exact distributional thresholds. Weis et al. (2014), Stemkovski et al. (2023), and Montes-Perez et al. (2025) provide related schedule-variation or co-occurrence studies with distinct mathematical objectives. Semantic published-record searches and claim implication comparisons found no dominating theorem among the inspected material. Standard Gaussian heat smoothing, the triangular overlap identity, and normal CDF calculus are acknowledged prior tools. Older random-interval probability or Gaussian scale-space literature remains a genuine priority risk.

## Value — PASS
Two biologically motivated overlap summaries can convey contradictory changes under the same perturbation: for \(L/2<d<L\), more Gaussian timing variability raises average shared flowering days over a nonzero interval yet always lowers the fraction of years with any positive overlap. The exact thresholds, ordering and critical onset provide a natural benchmark. The result does not claim biological fitness optimization or calibrated field effects.

## Limits and evidence
The result assumes two equal, fixed flowering durations, independent of onset, a normal relative-year displacement, binary floral presence, and an unbounded real-line calendar. It excludes stochastic widths, seasonal edge effects, abundance weighting and interaction networks. The proof is self-contained in RESULT.md and the numerical checks are reproducible with `python3 verify_overlap.py`. No independent audit or human priority check has been performed.

Self-review: passed. Independent audit: not yet performed.
