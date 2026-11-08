# Scientific review: divisor-indexed Ramanujan Gram Smith factors

## Correctness — PASS

The integer identity \(C=M D Z^{\mathsf T}\) follows term-by-term from Kluyver's formula, and both incidence matrices are unimodular. The prime-power Gram core has entries \(p^{i+j}(a-\max(i,j)+1)\). Consecutive leading minors of its unweighted kernel have determinant \(a-i+2\); the Schur complement is explicit. A local diagonal unit splits a factor \(p^{2i}\), whereas a divisibility event \(p\mid(a-i+1)\) produces a unit-determinant two-by-two block after extracting \(p^{2i+1}\). All elimination coefficients are integral over \(\mathbb Z_p\) because later index weights carry additional powers of \(p\). Tensor-product localization proves the all-modulus formula. The verifier independently checks Smith factors from all minors in finite cases. Boundary cases \(n=1\) and final singleton/pair indices are covered.

## Originality — PASS, with residual historical uncertainty

Tóth (arXiv:1002.3221v1) develops Ramanujan polynomials and the standard divisor formula, not the integer Gram Smith form. Fowler–Garcia–Karaali (arXiv:1201.1060) establish the supercharacter table, its weighted orthogonality, Kronecker structure and square identity; these do not specify the unweighted Gram cokernel. Schlage-Puchta (DOI:10.1007/s00013-021-01643-8) establishes the determinant of the table, hence only the product of the Gram invariant factors. The new complete invariant-factor profile distinguishes previously undetermined elementary divisors, including nontrivial adjacent-pair transitions. Targeted literature, mathematical alias, and related database searches found no equivalent statement; historical priority cannot be guaranteed by searches alone.

## Mathematical value — PASS

This is a complete classification of an intrinsic integer-lattice invariant associated with a canonical arithmetic Fourier/supercharacter table. It goes beyond determinant and orthogonality to describe the finite abelian cokernel, sharp exponent \(n^2\) (odd \(n\)) or \(n^2/2\) (even \(n\)), and a modular-rank collapse controlled by \(p\mid(a_p+1)\). The exceptional pair substitutions encode a nontrivial arithmetic dependence on the prime-power exponent and are invisible to the already-known determinant. This is a natural all-moduli classification rather than an arbitrary numerical slice.

## Limits

No claim of novelty is made for the Ramanujan sum formula, supercharacter table, weighted orthogonality, tensor decomposition or determinant. The theorem is restricted to the specified unweighted divisor-indexed Gram matrix. Full-text comparison covered the most directly relevant primary articles; undiscovered equivalent integral classifications remain possible. Finite computations are corroborative and do not establish the universal result.

Self-review: passed. Independent audit: not yet performed.
