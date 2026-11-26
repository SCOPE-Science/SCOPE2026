# Independent mathematical audit

## correctness

PASS

For unordered two-token configurations the AA, AB and BB layers have degrees 2n, N-2 and 2m, respectively, and there are only AA–AB and BB–AB off-diagonal blocks. An AA pair couples to each AB pair containing one of its A vertices, giving the unsigned incidence block tensored with the all-ones vector on B, and symmetrically for BB. The incidence Gram matrix on an r-vertex part is (r-2)I+J, giving full rank for r>=3 and singular values sqrt(2r-2) on constants and sqrt(r-2) on the zero-sum subspace. The two outer incidence kernels give eigenvalues 2n and 2m in dimensions m(m-3)/2 and n(n-3)/2; the tensor product of the two zero-sum spaces in AB gives N-2 in dimension (m-1)(n-1). Coupling just the A-zero-sum directions to their AB lifts gives the two-by-two block with trace m+3n-2 and determinant n(m+2n-2), and hence roots n and m+2n-2, each repeated m-1 times. The B-zero-sum block gives m and n+2m-2, each repeated n-1 times. In the remaining three-layer constant block, the off-diagonal magnitudes are sqrt(2n(m-1)) and sqrt(2m(n-1)). Its determinant is zero from the constant token vector, its trace is 3N-2, and its order-two principal minors sum to 2N(N-1); its roots are 0,N,2N-2. These orthogonal pieces exhaust binom(N,2) dimensions. Vanishing kernel dimensions at a side length of three and coincident numerical eigenvalues are handled by the stated multiplicity convention. There is exactly one zero, so the graph is connected; multiplying the positive eigenvalues and dividing by binom(N,2) leaves 4 from the two exceptional nonzero constant-layer roots, as asserted. The bundled numerical and modular checker was inspected, not executed, and is not needed for the infinite claim.

## originality

FAIL

Mendonça's 2013 exclusion-process spin Hamiltonian and tensor spin multiplicities specialize to the full two-token spectrum, not just its extremal values. The tree product is then the direct matrix-tree corollary. In addition, the distinct indexed finding 40156451790b explicitly prints the identical characteristic polynomial and tree product and uses the same incidence-block argument. Its later record date does not establish historical priority; the earlier exclusion-process coverage does not depend on that record. The inaccessible Barik–Verma full text is not a reason for failure.

## value

FAIL

The spectrum and spanning-tree count are natural invariants, and the incidence proof is transparent. But as a new exact-invariant contribution, every spectral factor is already obtained by the two-particle substitution in the earlier biclique exclusion Hamiltonian, and the tree count is its routine Kirchhoff product. The same explicit formulas and block method are also already present in the indexed comparison. No distinct invariant or surviving mathematically substantive result is established in this frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
