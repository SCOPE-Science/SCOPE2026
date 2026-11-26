# Independent mathematical audit

## correctness

PASS

For each allowed part size, multiplicity m>=1 has m choices of designated copy, so the local generating factor at x=q^j is 1+sum m x^m=(1−x^6)/[(1−x)(1−x^2)(1−x^3)]. Thus F counts designated partitions and F^k counts ordered tuples. All formal products and reductions are coefficientwise. R=F^(-1) is exactly the cited eta quotient since 1+2+3−6=0. The Kassel–Reutenauer coefficient formula is a signed multiple of the two-square representation number in each mod-3 class; hence [q^(4n+3)]R=0. Independently, F(q)^4 and F(q^4) agree mod 2 by two Frobenius steps; repeatedly squaring a congruence mod 2^a gains one power of two because the sum of the two squared bases is even. For s>=2 this gives F(q)^(2^s) congruent to F(q^4)^(2^(s−2)) mod 2^(s−1), also after raising to the odd integer (k+1)/2^s. Multiplication by integral R preserves precision; convolution with a series supported in degrees divisible by four preserves the missing class of R. If s=1 there is no divisibility claim beyond modulus 1. Direct expansion of (1+q+3q²+5q³+...)^k gives 5k+3k(k−1)+binom(k,3)=k(k+1)(k+14)/6. For odd k this gives exactly s−1 at n=0 of the progression, establishing sharpness even for s=1.

## originality

PASS

The new component is the all-index divisibility at the sharp exponent for arbitrary odd orders. The predicted exponent, first-index polynomial witness, reciprocal eta formula and some low-precision cases are prior material and are not credited as new. The complementary indexed even-order finding does not state or cover the odd-order theorem as a new result.

## value

PASS

This proves the odd-order part of an explicit conjecture for a natural partition-tuple enumerator. The exact exponent at every odd order, including unbounded exponents, is an all-index structural result; it is not a single coefficient evaluation. The proof identifies why vanishing of one reciprocal residue class supplies a sharp universal congruence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
