# Independent mathematical audit

## correctness

PASS

Normalization over the closure gives projective lines with no Picard variety and nodes joining every pair. Gluing scalars at nodes modulo scalar changes on components dualizes to the kernel of the oriented incidence map, with the sign on edge reversal; rank is the connected cycle rank (n−1)(n−2)/2. For every distance j between 1 and n/2, excluding endpoints, subtract the oriented chord from the j-step perimeter path. Shortcuts form regular orbit blocks and have a unit triangular projection to the corresponding chord axes, so eliminating them preserves the integral kernel. For odd n the remaining kernel is the trivial perimeter Z. For n=2h, let c be the full perimeter and v_i the path-minus-chord lifts for i=0,…,h−1 of antipodal edges. They form a basis with c and s^h v_0=c−v_0. Hence the residual cyclic annihilator is (s−1)(s^h+1), with the rank and basis ruling out further integral relations. Equivalently, the two rational summands' integral product contains the image f↦(f(1),f mod (s^h+1)) as the index-two subgroup with equal evaluation mod 2. No equivariant map to the trivial Z retracts the perimeter, since c=(s^h+1)v_0 maps to an even integer. A point on a torus over the closure is a homomorphism from its characters into the multiplicative group; rationality means evaluation on sm is the qth power of evaluation on m. Thus the point group is dual to M/(q−s)M; the polynomial modules give the stated groups by evaluation at q. These orders are prime to the characteristic. For point counts, if n divides the extension degree r all lines and nodes are rational, giving n(q^r+1)−binom(n,2). Otherwise no normalization components are fixed, and the only rational points occur for even n=2h and r≡h mod n, exactly h antipodal nodes whose branches are exchanged. The generating zeta functions are as asserted, with the branch-reversal factor 1+t^h. A degree-n element has distinct conjugates and their (1,a,a²) determinants are Vandermonde, so the incidence assumptions are realizable in all characteristics. The supplied verify.py and CHECKS.txt were inspected; the recorded small-n exact checks were not rerun and are supplementary to the uniform derivation.

## originality

PASS

Credit the standard normalization description by a graph cycle lattice, gluing and Frobenius methods, and exact earlier arithmetic arrangements. The distinct result is the uniform integral C_n lattice of the complete dual graph under transitive Frobenius, including the even antipodal index-two gluing and its cyclic rational-point summand. The strongest inspected analogous results have different incidence graphs and Galois actions and do not give this decomposition. This bounded comparison does not establish historical priority over unindexed lattice calculations.

## value

PASS

For a natural unbounded family of reduced nodal curves over every finite field, the result distinguishes the actual torus up to isomorphism from its split-up-to-isogeny factors. The even signed orbit creates a detectable cyclic rather than split rational-point factor and a simultaneous branch-reversal zeta contribution. This evaluated integral structure is more useful than rational rank or order and is not supplied by the general normalization framework alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
