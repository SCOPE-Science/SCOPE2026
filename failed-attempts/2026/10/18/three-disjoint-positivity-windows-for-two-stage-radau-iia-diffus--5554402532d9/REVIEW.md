# Independent mathematical audit

## correctness

PASS

The stiffly accurate tableau gives scalar numerator 1+z/3 and denominator 1−2z/3+z²/6. On the star the constant vector, the hub-versus-leaf contrast and the zero-sum leaf vectors have Laplacian eigenvalues 0, m+1 and 1 respectively (the last subspace is zero for m=1). The spectral formula gives positive off-diagonals for h>0: the hub-to-leaf numerator is proportional to 1−r((m+1)h), and the leaf-to-leaf numerator is h²[(m+1)h²+(6m+12)h+18]. The two diagonal numerators are the stated quadratic and quartic with positive denominators. Both diagonals are bounded below by [1+m(5−3√3)/2]/(m+1), positive through m=10, including m=1. For m≥11 the hub quadratic is positive at 0 and 2, nonpositive at 1, has distinct roots, and has its vertex below 1. The leaf diagonal is positive on [0,3] since r(h)≥0 there and r((m+1)h)>−1. The quartic value at 8 is −4(160m²−1392m−2593)<0 for m≥11, and its leading term is positive. Descartes' two sign changes force exactly the two simple positive roots located by these signs. The failure intervals are disjoint and their endpoints are included in the safe set. At m=11, the hub roots are 1/2 and 1, and numerical bisection on the frozen reduced quartic gives 6.068411604176 and 11.764257595354, consistent with the stated digits. This proves endpoint preservation for the full orthant, not stage positivity.

## originality

FAIL

Distinct indexed findings substantively cover the complete window classification for m≥2, not merely its general positivity setting or its first counterexample. They give identical polynomials, thresholds, endpoint quantifiers and first failing star, and give further size-asymptotic information. The unused m=1 case is an immediate two-state computation and leaves no material distinct theorem. This is a finding of present equivalent coverage, not a historical priority or authorship judgment inferred from catalogue paths.

## value

FAIL

The exact cutoff and separate hub and leaf obstructions would be a useful benchmark beyond A/L-stability, but these concrete contributions are already supplied by the indexed findings. The only extension of the stated graph domain, K₁,₁, is a routine two-state positivity calculation; no additional substantive benchmark, structural statement or worthwhile repaired remainder is supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
