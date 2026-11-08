# Scientific review

## Correctness — PASS
The boundary crosses one or two square cells per column, giving the exact conditional area fractions in the proof. Independence reduces the variance to a one-dimensional rotation average; its rational sum is an exact power-sum identity, and its irrational limit follows from elementary Fourier equidistribution of irrational rotations. Continuity is proved by the decay of the reduced-denominator spike. The arithmetic checker exercises 23,772 exact-rational assertions and an independent clipped-polygon implementation, but the infinite proof is analytical.

## Originality — PASS, with explicit scope qualification
The direct 2021 discrepancy papers establish sharp averaged star discrepancy and general partition comparisons, not a slanted-indicator fixed-direction variance law. The 2012 visibility paper studies line discontinuities and correlations but its inspected analysis does not state an orientation-by-orientation arithmetic coefficient. The simple rational-slope sector is not claimed as independently new: a related restricted-slope/intercept geometric formula can imply that component as a limiting case. The non-implied claim is the complete **irrational** coefficient and the dense rational-discontinuity theorem, which cannot be inferred merely by taking a limit through rational slopes since the grid-refinement limit is not uniform. Residual risk: some specialist literature on polygon indicator sampling and lattice arithmetic might contain an equivalent theorem.

## Value — PASS
Piecewise-constant integration across a moving straight boundary is a canonical model for discontinuous planar cubature. General \(O(n^{-3})\) variance bounds cannot express how the leading sampling risk responds to arbitrarily small rotations. This result supplies exact risk constants, sharp dependence on rational denominator and a dense-discontinuity benchmark; it identifies a genuine noncommutation of refinement and orientation limits rather than merely recalculating a generic sum. The rational jump is only about 7.1 percent at the diagonal and diminishes for large denominators; no general-purpose speedup is claimed.

## Closest comparisons and limitations
Doerr, arXiv:2103.15712 (2021); Kiderlen–Pausinger, DOI 10.1007/s00605-021-01538-4 (2021); Ramamoorthi et al., ACM TOG 31, article 121 (2012). Detailed source inspections and residual risks are recorded in `AUDIT.json`. Restricted to \(0<\alpha\le1\), independent draws and the exact triangular indicator. There is no independent validation.

Self-review: passed. Independent audit: not yet performed.
