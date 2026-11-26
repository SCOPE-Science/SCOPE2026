# Independent mathematical audit

## correctness

PASS

For M the dyadic floor of N, the first M characters span cell constants and the r extra orthonormal modes are the next Rademacher times r cell-constant sign characters. The unit jump at relative position q has M-mode residual variance q(1-q)/M; each extra coefficient has magnitude min(q,1-q)/M because whole cells cancel under the Rademacher sign. Thus the squared residual is exactly the stated formula. Its left-half quadratic is (q-(N/M)q²)/M, whose unique maximizer is M/(2N), with its reflection on the right; the maximum is 1/(4N). This includes N=1 and r=0. The derivative-measure representation of real interval BV is a Bochner integral of jumps modulo constants (the jump map is L²-continuous), with total mass in variation equal to TV. Equality for a nonzero signed derivative forces its variation measure onto the finite maximizing set. Triangle equality then requires proportional signed residuals. Distinct maximizing jumps cannot be proportional: every projected function is constant near each maximizer, using the half-cell grid for r>0 and the cell grid for r=0, so any asserted proportionality would leave an uncancelled jump. The sharp equal-cell comparator follows from unit-step cell variance and the same integral bound.

## originality

PASS

The inspected comparisons do not cover the exact non-dyadic correction, sharp all-cutoff bound and rigidity for the Paley-ordered joint residual. The dyadic averaging mechanism and its midpoint case are not credited as new.

## value

PASS

Paley partial sums have natural non-dyadic cutoffs not handled by cell averaging alone. The result gives a worst-case BV approximation benchmark at every rank, identifies how the extra block changes the jump response, and locates all extremizers. Equality with the regular equal-cell error is a useful comparison, not a global optimality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
