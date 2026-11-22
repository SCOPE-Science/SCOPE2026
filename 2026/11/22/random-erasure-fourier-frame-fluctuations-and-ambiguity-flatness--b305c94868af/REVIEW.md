# Scientific review

## Correctness

PASS. Full cyclic time--frequency tightness gives the exact off-diagonal correlation row sum. Sampling edges without replacement produces the explicit covariance factor after coincident-edge/shared-vertex/disjoint-edge enumeration. The fourth coherence dispersion is exactly half the Gabor orbit's centered edge-square sum. The bound and equality cases follow from \(0\leq|\langle g,\pi(z)g\rangle|^2\leq1\), the Weyl orthogonality identity, and isotropic stabilizer character theory. The Alltop special case follows from nondegenerate quadratic Gauss sums in odd prime characteristic. `CHECK.py` passes independent finite enumerations and exact rational combinatorial comparisons. These finite tests supplement, not substitute for, the proof.

## Originality

PASS relative to the inspected full primary texts and available indexed records. Salanevich--Strachan (arXiv:2509.01325, Sections 3--5) calculate deterministic MUB subframe potentials and random-window frame bounds. Their deterministic MUB expression already implies the Alltop occupancy corollary; the original claim is the all-window, fixed-cardinality variance identity and its sharp SIC/stabilizer classification. Haikin--Zamir--Gavish (arXiv:1801.04548, Sections II--IV) treat Bernoulli erasures and expected single spectral moments, not fixed-cardinality two-trace covariance. Nearby indexed research on adversarial Gabor erasures, random-phase Fourier fourth moments and Gaussian log-volume fluctuations concerns different random variables. No equivalence was found in the accessed records, though an older sampling-theoretic identity may exist.

## Value

PASS. The theorem evaluates a natural exact spread statistic for random erasure robustness over every cyclic Gabor window, separates universal cardinality effects from a single window-dependent Fourier ambiguity invariant, and determines both extremal geometries. It gives a dimension-uniform quantitative benchmark between stabilizer, Alltop and possible SIC designs. This is a statement about Frobenius/frame-potential fluctuations and must not be presented as a sharp singular-value or condition-number theorem.

## Scientific limitations

The result does not classify the full distribution or the optimizer of the lower variance when no SIC exists. The fact that the Alltop subframe potential depends on basis occupancies is prior literature, not a separate originality assertion. A potentially unindexed equivalent finite-population U-statistic expression remains an originality risk.

Self-review: passed. Independent audit: not yet performed.
