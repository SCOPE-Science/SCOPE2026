# Scientific review

## Correctness

PASS. On every interior Fourier shell, the spatial two-site evaluation matrix has determinant proportional to \(\sin(\pi kh/m)\), so exactly \(g-1\) shells lose one direction, where \(g=\gcd(h,m)\). The distinct eigenvalues produce an invertible \((m+1)\)-time Vandermonde matrix and an \(m\)-time Vandermonde kernel with no zero coordinates. Imposing the endpoint and spatially degenerate shell ratios produces an extra nullity of exactly one iff \(h/g\) is even. The finite checks use exact fractions over 120 cases and do not replace the proof.

## Originality

PASS relative to the materially inspected and retrievable literature. General dynamical-frame criteria and earlier path-focused work are broader in setting but do not state the exact arithmetic deficiency at the two critical horizons. An earlier sharp even-cycle minimal-horizon determinant gives only zero versus nonzero, not the nullity or its recoverability by a single additional snapshot; thus it does not imply the present rank classification. The 2011 cycle-observability work has a superficially stronger arithmetic coprimality statement, but an exact six-vertex example and the spectral argument distinguish it from the present half-cycle criterion. The 2026 motivating paper's complete manuscript remained unavailable, and publication priority requires further external review.

## Value

PASS. A single determinant zero cannot tell a sensor designer whether the missed information is permanently invisible or recoverable through one additional time observation. The formula resolves that distinction for every sensor separation and even cycle length, gives the exact number of permanently invisible Fourier directions, and yields the precise number of viable sensor placements and minimum horizons. These are structural, natural rank invariants of the two-site dynamical sampling problem rather than an arbitrary finite computation.

## Boundaries

All claims assume distinct spectral multipliers, full complex signals and two stationary vertex sensors. Neither uniform stability nor condition-number optimization is claimed. A potentially conflicting older observability statement warrants careful independent reconciliation of model conventions.

Self-review: passed. Independent audit: not yet performed.
