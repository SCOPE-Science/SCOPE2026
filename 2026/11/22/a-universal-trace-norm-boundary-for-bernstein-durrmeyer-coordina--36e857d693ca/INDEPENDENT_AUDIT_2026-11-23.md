# Independent mathematical audit

## correctness

PASS

Beta integration against b_{n,j} on a monomial of degree k≤n produces a polynomial in j with leading coefficient (n+1)!/(n+k+1)! after multiplying by n+1. The binomial expectation contributes leading coefficient n!/(n−k)!, and selfadjointness then diagonalizes M_n in shifted orthonormal Legendre polynomials. Modes above n are orthogonal to the polynomial image and vanish. The shifted recurrence has off-diagonal β_k=(k+1)/(2√((2k+1)(2k+3))); the commutator has opposite entries of absolute size β_k(λ_{n,k}−λ_{n,k+1}), including the final edge to degree n+1. Phase conjugation gives the symmetric Jacobi matrix for i√n C_n with weights a_{n,k}. Expanding the λ product for k≤R√n gives log λ=−k(k+1)/n+O_R(n^−1/2). For arbitrary k≤n, each log factor is at most −(j+1)/(n+1), since the ratio is 1−(2j+2)/(n+j+2); thus the stated Gaussian envelope holds and controls the normalized weighted ℓ^p tail for every fixed p>0. Split the compact window into blocks of length ⌊n^(1/4)⌋: the weight-deletion error has o(√n) bounded singular values, and freezing the weights within blocks gives an o(1)-norm error of rank O(√n). More generally the p-tail error is bounded by summing the p-th powers of the edge weights for the two weighted shifts, using the Schatten triangle inequality for p≥1 and trace-power subadditivity in both directions for 0<p<1. These bounds justify both perturbation and removal of the cutoff. Constant-block eigenvalues give the asserted angle-frequency integral, whose factors are the displayed gamma integrals. Substitution gives trace constant 1/π and squared Hilbert–Schmidt constant √π/(16√2). The limsup operator norm is at most twice the limiting maximum edge; a growing principal block of length o(√n) near √(n/2) attains the asymptotic value 1/√(2e). Dividing by its square gives the stable-rank constant. This applies to the classical unweighted interval operator and each fixed p, without uniformity in p or a claim about individual singular values. The supplied exact/finite spectral checker was inspected, not executed.

## originality

PASS

The compact-window arcsine spectral-distribution step is already supplied by a stronger varying-recurrence theorem and is not itself novel. The supported distinct contribution is the full commutator result: exact Legendre-gap reduction and its square-root-frequency profile, integrable tail control at a scale much smaller than the full matrix size, the evaluated all-p constants, and the sharp norm edge. The known compact-window theorem alone neither controls the removed singular-value mass nor bounds the maximum. Nearby exact Durrmeyer records have different spectral observables, and no inspected theorem was found to cover the full law as a special case.

## value

PASS

For a canonical finite-rank smoother and the natural position observable, the result quantifies a sharp failure of trace-class commutation despite operator-norm commutation. The nonzero trace-norm constant, diverging stable rank and entire fixed-p power scale distinguish a population of order √n weak spectral modes from an estimate of just the largest one. The finite degree is inherent to the operator, and the square-root window and critical p=1 are derived rather than arbitrary slices. The exact commutator constants are the value, not a new general Jacobi distribution method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
