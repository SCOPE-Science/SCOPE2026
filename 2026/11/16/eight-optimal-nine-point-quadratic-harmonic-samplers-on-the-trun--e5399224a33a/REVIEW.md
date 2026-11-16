# Scientific review: optimal truncated-tetrahedral quadratic sampling

## Correctness — PASS
The dimension, kernel normalization, sample weights, and all quantifiers are explicit. The addition theorem reduces the squared sampling spectrum to a rational principal submatrix. An independent integer evaluation matrix with its complete three-dimensional Gale kernel proves the rank criterion. The thirteen symmetry orbits exhaust all 220 erasure triples; exact determinant signs for twelve orbits and Sylvester's criterion for the remaining orbit separate the optimal eight. The characteristic polynomial and exact real-root intervals identify the sharp eigenvalue. The standalone checker verifies all these algebraic steps from the specified definitions. Real-root isolation and a finite exhaustive orbit classification are used, not extrapolated beyond this geometry.

## Originality — PASS, with residual priority uncertainty
The March 9, 2023 spherical-framelet source discusses structured spherical harmonic sampling but has no fixed twelve-point, nine-sample, three-erasure E-optimal theorem. The published cuboctahedral 128/92 erasure census has analogous graph-matroid rank structure but a different node geometry, and its inspected full account explicitly does not claim stability constants; it cannot imply the present exact optimal lower eigenvalue. Earlier general interpolation conditioning results do not state this fixed-grid eight-set classification. Specialized unpublished or unindexed polyhedral sampling tables could contain the same spectrum; this is a genuine historical-priority risk and warrants independent review. The rank count alone is not asserted to be original.

## Mathematical value — PASS
The nine-dimensional harmonic band makes nine the first possible number of samples for unique determination. Removing three of twelve candidate sites is a natural exact-recovery design problem. All 128 invertible choices have equal determinant, so D-optimality does not distinguish them; an exact E-optimal theorem that selects only eight directed triangle complements resolves a nontrivial conditioning question and identifies the full symmetry class of optimizers. No generalization to freely chosen locations or weighted design is claimed.

## Scientific limitations
The result assumes the fixed truncated-tetrahedral geometry, equally weighted samples with the original \(1/\sqrt{12}\) scale, real harmonics up to degree two, and noiseless mathematical sampling. Independent publication-priority and proof auditing remain outstanding.

Self-review: passed. Independent audit: not yet performed.
