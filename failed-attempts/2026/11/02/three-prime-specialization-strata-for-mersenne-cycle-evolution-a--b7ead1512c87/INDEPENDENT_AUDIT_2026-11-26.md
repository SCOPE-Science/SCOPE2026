# Independent mathematical audit

## correctness

PASS

The structure determinant is ±2, so all odd reductions are perfect. Idempotence yields the zero vector or the successive squares of a scalar a with a^ell=1/2. Independence of the squares makes automorphisms monomial, and the directed cycle permits rotations only. The diagonal kernel is the group of ell-th roots of unity; the first coefficient for a shift s must be an ell-th root of 2^{-(2^s-1)}. The other coefficients then lie in the field by the square recurrences. For 0<s<n the exponent is coprime to ell, so the shift criterion is exactly triviality of the power class of 2. When a root exists, normalization to the unweighted cycle splits the action; taking the inverse of the forward rotation as generator gives exponent 2. Over Q the 2-adic valuation precludes a root and there is no nontrivial rational ell-th root of unity. At p=ell the ell-power map on the finite-field points is a bijection; no smooth group-scheme assertion is needed. Over Q(zeta_ell) the norm of a putative ell-th root would have valuation (ell-1)/ell, impossible. Thus the splitting field has degree ell(ell-1); its faithful affine action on the roots is the full affine group. Away from ramification the first two relevant Frobenius tests are the cyclotomic component and identity in the translation kernel. The three class-union sizes are ell(ell-2), 1 and ell-1, proving the densities. An independent bounded enumeration of the two counts matched 108 finite fields for n=3,5,7; neither that enumeration nor the frozen verify.py proves the group isomorphism or density assertions. The frozen script was inspected, not executed.

## originality

FAIL

An earlier published Resultary finding covers arbitrary weighted directed cycles over every finite field and gives the cycle-power-class classification, rotation-lift criterion, automorphism orders, and idempotent counts. The finite-field part is its direct specialization including the abstract group labels by changing to the unweighted basis in the trivial-class case. The rational case and natural densities are not claims of that earlier record, but follow immediately from the same recurrences, valuation, and the standard Chebotarev calculation for the splitting field of X^ell-2. The comparison is to mathematical implication, not a claim that the earlier record literally writes down these densities.

## value

FAIL

This is a sound illustrative example of the reduction question, but the prior general weighted-cycle result already determines the exceptional finite-field behavior. The additional density computation is a textbook splitting-field count and uses no further distinguishing arithmetic of the family. No independently useful exact remainder not mechanically implied was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
