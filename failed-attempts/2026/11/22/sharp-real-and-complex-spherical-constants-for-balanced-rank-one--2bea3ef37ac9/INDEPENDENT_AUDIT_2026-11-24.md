# Independent mathematical audit

## correctness

PASS

The theorem is true for finite termwise matched-length pairs in real or complex Euclidean d, not arbitrary pairs. Dualizing the multiplier norm and maximizing the phases gives the stated supremum of sums of absolute projection products. Haar averaging one projection gives mu times the vector length; matched lengths and |inner product|<=length then give the desired Bessel quadratic form, and exchanging the families gives the other bound. The real and complex beta laws for the squared coordinate are correct and give the stated gamma ratios; Stirling gives both limits. Haar empirical approximations give uniform convergence of the direction-dependent first moments by a finite net and uniform Lipschitz bounds. The fixed f_j=e_1 then gives B_f=N. Choosing x_j to span and replacing only d-1 of the f_j by independent directions changes U by O(d) and B_f to N-d+1 for large N, preserving sharpness. For strictness a great-circle path out of a generic point perpendicular to one positive-weight x_j has a positive cusp from the parallel terms; every other term is smooth there (also over the complex field). Thus the continuous projection sum is nonconstant and its maximum strictly exceeds its Haar mean when d>=2. At d=1 phase alignment always gives equality. In the planar family, max over signs selects a consecutive half of the 2N roots at any maximizing direction (a zero projection cannot occur for a maximizing signed sum, since flipping that sign would increase its norm). The geometric sum has modulus csc(pi/(2N)); strict increase of sin(x)/x as x decreases gives the limit ratio. The independent replay `python3 /workspace/branches/frozen_review_checks.py` (section 2, passes) integrates both beta moments in four dimensions per field and enumerates planar sign maxima at five lengths. These are checks of normalizations and examples only; the analytical proof covers all d and lengths. The supplied checker was inspected, not executed.

## originality

FAIL

The central claimed sharp constant is not an independent extremal invariant: it is exactly the absolutely 1-summing norm of the Euclidean identity, via an elementary two-way reduction preserving the optimal constant. The classical Pietsch domination theorem gives this Euclidean norm directly by rotation averaging and a beta moment; no prior frame-multiplier paper stating the rewritten inequality is needed. Finite strictness is the standard distinction between a finite absolute-projection sum and its constant sphere average; spanning sharpness is a dense perturbation, and the special planar sequence is ordinary regular-polygon geometry. This is a finding of direct mathematical coverage of the core constant, not a claim that an earlier paper was shown to use the same terminology or to state every ancillary observation verbatim.

## value

FAIL

The motivating frame-bound comparison is natural and the exposition is correct and potentially useful pedagogically, but the frozen claim computes a known operator-ideal invariant in equivalent notation. Its further consequences use a finite projection-sum cusp, dense spanning perturbation and the geometric sum of a regular half-polygon. None supplies an independently useful unknown exact invariant or new sharp parameter problem beyond the classical 1-summing comparison as frozen. No unbalanced, finite-N optimal, or conditioned-optimal refinement is proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
