# Independent mathematical audit

## correctness

PASS

The circulant, up to transpose, is multiplication by a=(1+X)^n−1 in the odd-order quotient Z₂[X]/(X^n−1). One can verify the Smith conclusion without a splitting field. For n=2^r−1 the factors X−1 and H=(X^n−1)/(X−1) are coprime modulo two since H(1)=n is odd, giving an integral 2-adic product. At X=1 the multiplier is odd. On the H factor, 1+X is a unit; repeated squaring modulo four gives (1+X)^(2^r)≡1+X^(2^r)+2X^(2^(r−1)). As X^(2^r)=X there, (1+X)a≡2X^(2^(r−1)) modulo four. Thus multiplication by a on the rank n−1 summand is twice an invertible integral map. At n=1 that summand is absent. For n=2^r+1, a reduces modulo two to 1+X+X^(−1) in the cyclic quotient (using Frobenius and X^n=1). Its only possible common factor with X^n−1 is X²+X+1, occurring exactly when 3 divides n, i.e. r odd. The cyclic polynomial is squarefree modulo two. In that case split off the integral cubic-root factor X²+X+1; on its rank-two summand a=(−X²)^n−1=−2, and a is a unit on the complement. These integral arguments give the exact elementary divisors, nonzero determinants and their valuations for all exponents. An independent integer resultant/binary gcd replay equated determinant valuation and binary nullity for both families at 1≤r≤6 (orders through 65). The replay is a check of small cases, not the all-exponent proof.

## originality

PASS

The distinct supported contribution is the uniform exact two-primary lattice classification at both power-of-two-neighbor orders. The circulant, the determinant resultant, older parity/factorization relations, and finite determinant entries are not new. Since exact determinant valuations together with the easily recoverable mod-two nullity would imply the Smith factors, the comparison included scalar determinant literature rather than requiring prior work to use Smith terminology. No inspected source establishes the two-family formula or a theorem implying it; access to two relevant determinant papers limits historical priority claims.

## value

PASS

The natural orders next to powers of two give exact lattice information for a classical determinant family. The classification tells not merely whether two divides, but exactly how many independent order-two cokernel summands occur and that no order-four or higher summands survive, uniformly in r and with the parity contrast between the families. The integral proof explains why binary root overlap never lifts to a higher valuation in these cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
