# Independent mathematical audit

## correctness

PASS

The cut uses principal blocks with unchanged diagonals. An independent factorization puts the root first and writes B for the direct sum of the cut blocks and v for the coupling from the root. The projected Krylov columns follow y₁=v and yₖ₊₁=Byₖ+v xₖ, where xₖ is the root component. Unit triangular column operations reduce the determinant in absolute value to that of [v,Bv,…,B^{n−2}v]. In block eigenbases the Vandermonde over both cut spectra factors into the two within-block Vandermondes and the cross differences, whose absolute product is the resultant. On each block the product of modal coefficients times its own Vandermonde is the absolute endpoint Krylov determinant: ordering away from the cut makes it triangular by distance, with diagonal entries the coupling to the root times successive path weight products. Multiplication gives precisely Eⱼ, including an empty block and zeros from common eigenvalues. For the full Laplacian the simple Jacobi spectrum gives a Gramian equal in the eigenbasis to its exponential Gram matrix sandwiched by diagonal modal weights. Distinct exponentials on a nonempty interval give a strictly positive common determinant factor after dividing by the squared Vandermonde. The Cauchy formula yields the stated ordered-pair denominator at infinite time for μ>0. For five vertices, the right cut-block polynomial at z=a for root 2 is −a²(a−2b); the center cuts are isospectral, and the endpoint factors are a⁵b⁵. The comparison |a−2b| against a gives precisely the three optimal sets, including all ties at b=a and the nonoptimal singular interior pair at a=2b. Independent symbolic and exact rational checks agree.

## originality

PASS

The supported distinct claim is the all-vertex, all-positive-conductance cross-resultant factor with explicit edge exponents and its weighted five-site switch. The general modal Gramian method, the cofactor resultant in the unfactored form, unit-weight classification and four-site classification are antecedents, not credited as new here.

## value

PASS

The path-specific factorization is a usable algebraic design rule for all locations and all positive conductances: it retains uncontrollable sites, eliminates time integration from optimization, and isolates the role of matching cut spectra and edge magnitudes. The five-site transition exhibits a change in optimal placement that a binary controllability test or the unit-weight result cannot predict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
