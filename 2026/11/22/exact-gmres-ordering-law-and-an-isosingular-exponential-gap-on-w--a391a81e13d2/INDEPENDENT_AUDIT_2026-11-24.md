# Independent mathematical audit

## correctness

PASS

The kth root-start Krylov space is the first k coordinate directions: the newly reached coordinate in B^j e_1 is (-1)^j times the product of the first j positive weights. The residual lies in the first k+1 coordinates and is perpendicular to each e_j-w_j e_{j+1} for j<=k. The orthogonal complement there has dimension one, and its vector normalized at the first coordinate has entries 1, 1/w_1, and the successive reciprocal products. Projecting the unit e_1 onto this line gives the inverse sum of squared entries, including R_0=1. The full Krylov space and unit triangular invertibility give R_n=0. In a fixed multiset each j-prefix product is bounded by the products of its j smallest and j largest elements; the sorted arrangements realize the appropriate bound in every term. Equality with pairwise distinct weights requires each of the first k prefix sets to be extremal and hence fixes the first k positions only. The two blocks give prefix-square sums (5*4^m-2)/3 and (8-5*4^(-m))/3; their quotient in the stated order and the square root yield the sharp ratio and limit constant. Coordinate reversal of the transpose reverses exactly the subdiagonal sequence, preserving singular values, and the unit diagonal gives the same eigenvalues. The supplied verifier was inspected but not executed; its reported 39,018 finite checks are supplementary. The argument is exact arithmetic, not an estimate of roundoff or a reordering of one fixed linear system.

## originality

PASS

The homogeneous endpoint formula and general residual identities are known, and the weighted residual identity also follows by computing the standard projected direction for this matrix. Novelty credit is for the simultaneous sharp fixed-multiset extremization and its explicit fixed-start, fixed-singular-spectrum exponential witness, not for general GMRES projection or qualitative spectral insufficiency.

## value

PASS

The fixed-multiset optimization is solved sharply at every horizon by one pair of orientations, and the reciprocal two-block case gives a structured witness with identical full singular spectra, coupling multisets and starting vectors yet exponentially separated penultimate residuals. This is useful as a numerical-analysis counterexample and benchmark, rather than merely a rederivation of homogeneous convergence or a prescription for general ILU ordering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
