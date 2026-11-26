# Independent mathematical audit

## correctness

PASS

The affine recurrence has b_i=(P_{2i−1}−1)/2 for i≥1. The identities P_{2i−1}=B_i−B_{i−1} and P_{2i−1}²=(C_{2i−1}+1)/4 yield the telescoped formula for 32W_k(n). The five exponential modes give the claimed integer recurrence, making the first five starts sufficient. The matrix determinant checks independently by dividing out the five stated column scalars (product 2^14), putting B_n,C_n first (even permutation), and replacing rows 2–4 by the forward row combinations with coefficients (1,−6,1). The resulting diagonal blocks have determinants −1 and (−4)28²(−192), recovering −2^26·3·7². At 3 and 7 the square residue periods are 4 and 3, with period sums 2 and 4 respectively, so divisibility occurs exactly at multiples of 12 and 21. The unit 3+2√2 has orders 4 and 3 there; lifting from B_4=204 and B_3=35 and using 16W_k(0)=5k+B_k(C_k−8) gives exact valuations. At 2, the parity period of b_n/2 proves the odd-k case; repeated squaring of the affine shift makes all even-k windows congruent modulo 2^(v_2(k)+1). The modulo-64 binomial calculation makes 5+(B_k/k)(C_k−8) equal 32 modulo 64, proving the first window has exactly the required valuation. This proves the formula at all primes and includes k=1, whose first zero window is allowed and whose next window is 4.

## originality

FAIL

The exact same all-k GCD with the same initialization and window starts is already covered by the earlier published Resultary record 9c2a2a5070c4. The compact gcd of three entries repackages its prime-power divisors without giving a distinct exact invariant. The result answers the cobalancing-square subquestion, not all four cases of Question 30.

## value

FAIL

An unknown exact solution to this cobalancing-square subquestion would be worthwhile. Here the all-length values and exceptional-prime laws are already given by the exact order-product theorem. The shorter presentation mechanically recovers the same invariant, with no additional case, consequence or separately motivated structural result claimed. Convenience of evaluation alone does not supply a distinct scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
