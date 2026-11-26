# Independent mathematical audit

## correctness

PASS

Reconstructed the weighted Fourier Gram form and the converse by density: an orthogonal vector gives an absolutely convergent Fourier series vanishing at all angles. The band matrix is positive by a squared-norm factorization, bounded for s<=r and compact for s<r. For omitted diagonal rows the weights are (1+s²)(s/r)^(|n|-1)/(4r); omitted step-two bonds have midpoint absolute index at least N and weight at most (s/r)^N/4. The symmetric row-sum bound gives the claimed compression error. A nonnegative compact top vector and strictly increasing diagonal entries give strict monotonicity, including comparison with the endpoint. At s=0 the matrix has the stated rank one. Near zero the odd block is analytic in s² in operator norm and its isolated maximum has first correction s²/(4r); the even block has norm O_r(s). At equal scales the odd block is the constant Jacobi chain with one strengthened bond. The positive part of this bond perturbation has rank one, so at most one spectral direction lies above the free upper edge; the even block lies below that edge by its row sums. The displayed geometric odd eigenvector is normalized and has eigenvalue (r+r^-1)/2, yielding the stated gap. Its unweighted Fourier sequence is constant on odd indices, so summing the two even-index geometric series gives the Rayleigh deficit (r²-s²)/(r(1-s²)). Applied to this localized vector, the band difference is O_r(r-s) in norm by |1-(s/r)^m|<=m(1-s/r). Order W_(r,s)<=W_(r,r) preserves the complement gap, so eliminating the complement corrects the Rayleigh value by only O_r((r-s)²). Reciprocal expansion gives the claimed coefficient. For s<r, a critical zero Gram vector would force the bounded atomic Fourier sequence to decay by the displayed eigen-equation; Cesàro mean squares rule this out for nonzero coefficients at distinct sites. At equal scales, the simple eigendirection unweights to the coefficients of delta_0-delta_pi, and Fourier uniqueness gives exactly the stated nullspace. The supplementary Python script was read, not run; it does not certify floating-point eigenvalues or replace the proof.

## originality

PASS

Limited to the distinct-scale frontier, its two certified limiting expansions and the critical strictness for s<r. Neither Fourier covariance criteria nor the equal-scale endpoint are claimed as original. The closest catalogued scalar modulations and positive scale-mixture results do not give the stated signed subtraction between different scales; the available statements were compared by their actual harmonic structure. Full-text formula-level overlap remains a named bibliographic risk, not evidence of absence.

## value

PASS

The result gives a usable sharp signed-subtraction boundary with an analytic finite-section error bound, not just a necessary Gram test. The endpoint laws and the strictness change show why distinct scales behave differently despite approaching the same threshold. Those are naturally motivated covariance and spectral questions, independent of priority for the equal-scale endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
