# Independent mathematical audit

## correctness

PASS

The declared interval implies alpha>-1, delta=beta-alpha>0 and c=beta-2delta+1>0. Under x=exp(-s) and multiplication by exp(-(beta+1)s/2), the operator is f(s) mapped to the integral of exp(-cu/2)f(s+u) for u>=0, whose norm is at most 2/c. Monomials are eigenvectors, hence only the low-output/high-input block of the commutator can be nonzero. The adjoint applied to a polynomial p is x^(-delta) times the scalar integral of t^(delta-1)p(t), minus a polynomial of the same degree; x^(-delta) is square integrable precisely here because c>0. In the stated shifted Jacobi basis, Rodrigues integration by parts gives the unnormalized moment of P_k at x^(s-1) as (-1)^k Gamma(s) (beta+1-s)_k/Gamma(k+s+1). For s=delta and s=alpha+1, endpoint terms vanish (order at least x^s at zero and a positive order at one); reinserting the square-root normalization yields both stated factors with the correct signs. Thus after removing basis signs each rate contributes one outer product. The Gamma constants cancel between the two factors. With degree-dependent rescaling n^(-c_j) and n^(c_j), the two Gram entries have limits given by the low partial sum of powers and the high tail sum of inverse powers at d=c_i+c_j>0, both 2/d. The exact limiting matrix 2C follows for each Gram; the exponentials exp(-c_j t) prove C positive definite for distinct rates. Polar decomposition and continuity of the finite matrix square roots and singular values give all m limits, eventual rank m, and positivity, including for complex lambda. The example is Hermitian with trace 1/6 and determinant -1/150 and hence eigenvalues 1/5 and -1/30. Polynomial density and boundedness give strong convergence to zero, while the norm tends to a positive number. The optional checker was inspected but not run; its finite tail cutoff is not the proof.

## originality

PASS

The inspected monomial/Hardy and approximation literature supplies eigenvectors, operator theory and distance tools, but not the joint off-diagonal block limit at these polynomial cutoffs. The closest distinct catalogue singular-system results concern different commutators and different spectral regimes. The supported distinct claim is the complete coupled finite-multirate singular spectrum for this specific weighted space and polynomial flag, not a priority claim for any of those tools.

## value

PASS

For the natural polynomial approximation scheme of a monomial-diagonal operator, the exact off-diagonal leakage is a meaningful obstruction to norm-convergent finite sections. The theorem gives all leakage channels and their interaction, not merely nonconvergence or the one-rate norm. The rate-induced Cauchy matrix explains what can be lost if leakage from distinct averages is treated separately; it remains meaningful for complex coefficients and cancellations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
